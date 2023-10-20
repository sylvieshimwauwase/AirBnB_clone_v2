#!/usr/bin/python3
"""Fabric script to generate .tgz archive"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """generates .tgz archive from the contents of the web_static folder"""

    time = datetime.now()
    archive = 'we_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local("mkdir -p versions")
    path = local("tar -cvzf versions/{} web_static".format(archive))

    if path is not None:
        return archive
    else:
        return None
