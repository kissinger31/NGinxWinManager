# NGinxRunOps.py
# (C)2013
# Scott Ernst

import os
import shutil

from pyaid.file.FileUtils import FileUtils
from pyaid.system.SystemUtils import SystemUtils

from nwm.ops.NGinxSetupOps import NGinxSetupOps

#___________________________________________________________________________________________________ NGinxRunOps
class NGinxRunOps(object):

#===================================================================================================
#                                                                                       C L A S S

    _NGINX_FOLDERS = [
        ['conf'],
        ['logs'],
        ['temp'],
        ['temp', 'client_body_temp'],
        ['temp', 'proxy_temp'],
        ['temp', 'fastcgi_temp'],
        ['temp', 'uwsgi_temp'],
        ['temp', 'scgi_temp']
    ]

    _NGINX_FILES = [
        ['logs', 'error.log'],
        ['logs', 'access.log']
    ]

#___________________________________________________________________________________________________ isRunning
    @classmethod
    def isRunning(cls):
        """ NGINX ALREADY RUNNING?
            Only one NGinx server should be running at a time.
        """
        result = SystemUtils.executeCommand('tasklist')
        if result['code']:
            print 'ERROR: Unable to access active process list.'
            print result['error']
            return True

        for task in result['out'].strip().replace('\r', '').split('\n'):
            if task.startswith('nginx.exe'):
                return True
        return False


#___________________________________________________________________________________________________
    @classmethod
    def initializeEnvironment(cls, path):
        """ CREATE MISSING FILES AND FOLDERS
            Due to the limited file creation privileges while running NGinx as a normal user,
            certain files and folders must exist prior to starting the server.
        """

        for folderParts in cls._NGINX_FOLDERS:
            p = FileUtils.createPath(path, *folderParts, isDir=True)
            if not os.path.exists(p):
                os.makedirs(p)

        for fileParts in cls._NGINX_FILES:
            p = FileUtils.createPath(path, *fileParts, isFile=True)
            if not os.path.exists(p):
                f = open(p, 'w+')
                f.close()

        #-------------------------------------------------------------------------------------------
        # COPY CONF FILES
        #       NGinx requires a number of conf files to be present and comes with a default set of
        #       files, which must be cloned to the target location if they do not already exist.
        nginxExeConfFolder = FileUtils.createPath(NGinxSetupOps.getExePath(), 'conf', isDir=True)
        for item in os.listdir(nginxExeConfFolder):
            itemPath = FileUtils.createPath(nginxExeConfFolder, item)
            if not os.path.isfile(itemPath):
                continue
            targetPath = FileUtils.createPath(path, 'conf', item, isFile=True)
            if os.path.exists(targetPath):
                continue
            shutil.copy(itemPath, targetPath)

#___________________________________________________________________________________________________ startServer
    @classmethod
    def startServer(cls, path):
        """ RUN NGINX
            NGinx is started as an active process.
        """

        cls.initializeEnvironment(path)
        os.chdir(path)
        print 'STARTING SERVER AT:', path
        return SystemUtils.executeCommand('nginx')

#___________________________________________________________________________________________________ stopServer
    @classmethod
    def stopServer(cls, path, force =False):
        os.chdir(path)
        if force:
            return SystemUtils.executeCommand('nginx -s stop')
        return SystemUtils.executeCommand('nginx -s quit')

#___________________________________________________________________________________________________ reloadServer
    @classmethod
    def reloadServer(cls, path):
        os.chdir(path)
        return SystemUtils.executeCommand('nginx -s reload')

#___________________________________________________________________________________________________ reopenServer
    @classmethod
    def reopenServer(cls, path):
        os.chdir(path)
        return SystemUtils.executeCommand('nginx -s reopen')
