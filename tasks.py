 # -*- coding: utf-8 -*-
import functools
import os

from invoke import task, run


def _out(name, message):
    print('[\033[1;37m{}\033[0m] {}'.format(name, message))


@task
def compile(verbose=False, **kwargs):
    out = functools.partial(_out, 'development.compile')
    hide = 'out' if not verbose else None
    STATIC_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'avalonstar', 'static')

    # Compile the stylesheets.
    run('autoprefixer -b "> 1%, last 3 versions, ff 17, opera 12.1" {input}'.format(
        input=os.path.join(STATIC_ROOT, 'stylesheets', 'application.css')), hide=hide)
    out('stylesheets/application.css auto-prefixed.')
    run('yuglify {input} --type css --combine {output}'.format(
        input=os.path.join(STATIC_ROOT, 'stylesheets', 'application.css'),
        output=os.path.join(STATIC_ROOT, 'stylesheets', 'production')), hide=hide)
    out('stylesheets/production.min.css created and minified.')
