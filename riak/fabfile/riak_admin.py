# -*- coding: utf-8 -*-
from fabric.api import env, run, task, roles
from fabric.operations import put
from fabric.context_managers import cd
from fabric.contrib.files import sed


@task
def aae_status():
    """ aae_status を確認する。
    """
    run('riak-admin aae-status')


