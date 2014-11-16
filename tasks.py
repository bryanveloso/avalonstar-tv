 # -*- coding: utf-8 -*-
import functools
import os

from invoke import task, run


def _out(name, message):
    print('[\033[1;37m{}\033[0m] {}'.format(name, message))


@task
def collect(verbose=False, **kwargs):
    out = functools.partial(_out, 'project.collect')
    hide = 'out' if not verbose else None

    # Build and send it off.
    out('Using `buildstatic` to concatenate assets.')
    run('python manage.py buildstatic --configuration=Production', hide=hide)
    out('Uploading and post-processing all of the assets.')
    run('python manage.py collectstatic --configuration=Production --noinput', hide=hide)


@task
def compile(verbose=False, **kwargs):
    out = functools.partial(_out, 'development.compile')
    hide = 'out' if not verbose else None
    STATIC_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'avalonstar', 'static')

    # Pre-compile all of our assets.
    out('Compiling stylesheets using production environment settings.')
    run('compass compile -e production --force', hide=hide)

    # Compile the 3rd-party Javascript base.apps.
    run('yuglify {input} --type js --combine {output}'.format(
        input=os.path.join(STATIC_ROOT, 'javascripts', 'components', '*.js'),
        output=os.path.join(STATIC_ROOT, 'javascripts', 'components')), hide=hide)
    out('javascripts/components.min.js created and minified.')

    # Autoprefix the stylesheets.
    run('autoprefixer -b "> 1%, last 3 versions, ff 17, opera 12.1" {input}'.format(
        input=os.path.join(STATIC_ROOT, 'stylesheets', 'site.css')), hide=hide)
    out('stylesheets/site.css auto-prefixed.')
    run('autoprefixer -b "> 1%, last 3 versions, ff 17, opera 12.1" {input}'.format(
        input=os.path.join(STATIC_ROOT, 'stylesheets', 'live.css')), hide=hide)
    out('stylesheets/live.css auto-prefixed.')

    # Compile and minify the stylesheets.
    run('yuglify {input} --type css --combine {output}'.format(
        input=os.path.join(STATIC_ROOT, 'stylesheets', 'live.css'),
        output=os.path.join(STATIC_ROOT, 'stylesheets', 'live')), hide=hide)
    out('stylesheets/live.min.css created and minified.')
    run('yuglify {input} --type css --combine {output}'.format(
        input=os.path.join(STATIC_ROOT, 'stylesheets', 'site.css'),
        output=os.path.join(STATIC_ROOT, 'stylesheets', 'site')), hide=hide)
    out('stylesheets/site.min.css created and minified.')


@task
def dbsync(verbose=False, database='avalonstar-tv', **kwargs):
    out = functools.partial(_out, 'heroku.pull')
    hide = 'out' if not verbose else None

    # Take a snapshot.
    out('Snapshotting the production database.')
    run('heroku pgbackups:capture --expire', hide=hide)

    # Fetch the latest database dump.
    run('curl -o latest.dump `heroku pgbackups:url`', hide=hide)
    out('Latest database dump (latest.dump) grabbed via curl.')

    # Restore it.
    run('pg_restore --verbose --clean --no-acl --no-owner -h localhost -d %s latest.dump' % database, hide=hide)
    run('rm latest.dump', hide=hide)
    out('Restored latest production dump to local database.')


@task
def deploy(verbose=False, migrate=False, **kwargs):
    out = functools.partial(_out, 'project.deploy')
    hide = 'out' if not verbose else None

    # Ready? Let's go.
    out('Pushing project to GitHub.')
    run('git push origin')
    out('Deploying to Heroku.')
    run('git push heroku')

    # Done!
    out('All done~!')


@task
def server(**kwargs):
    # Use Foreman to start all the development processes.
    run('foreman start -f Procfile.dev', pty=True)


@task
def migrate(app='', **kwargs):
    run('heroku run python manage.py migrate %s' % app)
