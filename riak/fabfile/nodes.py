# -*- coding: utf-8 -*-
from fabric.api import env, task

@task
def member():
    env.hosts = [
        '10.0.0.1',
        '10.0.0.2',
        '10.0.0.3',
        '10.0.0.4',
    ]
    env.user = 'root'
    env.key_filename = 'id_rsa_test'
    env.roledefs = {
        'riak': [
            '10.0.0.1',
            '10.0.0.2',
            '10.0.0.3',
            '10.0.0.4',
        ],
    }
