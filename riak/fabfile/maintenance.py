# -*- coding: utf-8 -*-
from fabric.api import env, run, task, roles
from fabric.operations import put
from fabric.context_managers import cd
from fabric.contrib.files import sed


@task
@roles('riak')
def check_compaction():
    """ leveldb のコンパクションが起きた日付を確認する。
    """
    run('find %s/leveldb -name LOG | xargs grep Compac' % env.data_dir)


@task
def check_datetime():
    """ 時刻を確認する。
    """
    run('date')

