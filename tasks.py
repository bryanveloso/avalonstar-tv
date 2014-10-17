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

    # Compile the 3rd-party Javascript base.apps.
    invoke.run('yuglify {input} --type js --combine {output}'.format(
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
        output=os.path.join(STATIC_ROOT, 'stylesheets', 'live.min')), hide=hide)
    out('stylesheets/live.min.css created and minified.')
    run('yuglify {input} --type css --combine {output}'.format(
        input=os.path.join(STATIC_ROOT, 'stylesheets', 'site.css'),
        output=os.path.join(STATIC_ROOT, 'stylesheets', 'site.min')), hide=hide)
    out('stylesheets/site.min.css created and minified.')


@task
def server(**kwargs):
    # Use Foreman to start all the development processes.
    run('foreman start -f Procfile.dev', pty=True)
