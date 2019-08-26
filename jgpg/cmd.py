#!/usr/bin/env python
# coding: utf-8

import sys, os
import click

@click.command()
@click.option('--version', is_flag=True, default=False)
@click.argument('action', default='sign', type=click.Choice(['sign']))
def run(action, version):
    print('hiya')
    if version:
        try:
            from jgpg.version import version as vstr
        except ModuleNotFoundError:
            if os.path.isfile('./setup.py') and sys.argv[0] == './lrun.py' and os.path.isdir('jgpg'):
                # this is relatively unsafe to inflict on unsuspecting users,
                # but I'm relatively careful to make sure it's probably just me
                # running ./lrun.py in my dev dir
                os.execvp('./setup.py', ['./setup.py', '--version'])
                from jgpg.version import version as vstr
            else:
                raise
        print(f'{vstr} {sys.argv}')
        sys.exit(0)
