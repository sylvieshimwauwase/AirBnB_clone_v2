#!/usr/bin/python3
"""Create and distributes an archive to web servers"""
import os.path
import time
from fabric.api import local
from fabric.operations import env, put, run

env.hosts = ['54.236.33.47', '35.175.135.250']


def do_pack():
    """Generate an tgz archive from web_static folder"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.
                                                    strftime("%Y%m%d%H%M%S")))
