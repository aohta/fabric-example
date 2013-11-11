# -*- coding: utf-8 -*-
from fabric.api import env, run, task, roles
from fabric.operations import put
from fabric.context_managers import cd
from fabric.contrib.files import sed

import cuisine

@task
def sync_config():
    """ 設定ファイルを更新する。
    """
    put('../etc/riak/app.config', '/etc/riak/app.config')
    put('../etc/riak/vm.args', '/etc/riak/vm.args')
    put('../etc/riak/key.pem', '/etc/riak/key.pem')
    put('../etc/riak/cert.pem', '/etc/riak/cert.pem')
    sed('/etc/riak/vm.args', 'HOST_IP_ADDRESS', env.host)


@task
def sysctl_update(reboot=False):
    """ sysctl.conf を更新する。 reboot するかはオプション
    """
    put('../etc/sysctl.conf', '/etc/sysctl.conf')
    if reboot:
        run('reboot', timeout=1)

