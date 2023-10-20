#!/usr/bin/python3
"""Distributes an archive to your web servers, using the function do_deploy"""
from fabric.contrib import files
from fabric.api import env, put, run
import os.path import exists

env.hosts = ['54.224.33.148', '54.234.37.54']


def do_deploy(archive_path):
    """Function for deploy"""
    if exists(archive_path) is False:
        return False

    try:
        file = archive_path.split("/")[-1]
        no_ext= file.split(".")[0]
        path = "/data/web_static/releases/"
        put(path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file, path, no_ext))
        run('rm /tmp/{}'.format(file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False
