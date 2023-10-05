#!/usr/bin/python3
"""Distributes an archive to your web servers, using the function do_deploy"""
from fabric.contrib import files
from fabric.api import env, put, run
import os

env.hosts = ['54.236.33.47', '35.175.135.250']


def do_deploy(archive_path):
    """Function for deploy"""
    if not os.path.exists(archive_path):
        return False

    data_path = '/data/web_static/releases/'
    tmp = archive_path.split('.')[0]
    name = tmp.split('/')[1]
    dest = data_path + name
