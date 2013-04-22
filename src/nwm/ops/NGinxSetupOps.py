# NGinxSetupOps.py
# (C)2013
# Scott Ernst

import os

from pyaid.system.SystemUtils import SystemUtils

#___________________________________________________________________________________________________ NGinxSetupOps
class NGinxSetupOps(object):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ commandExists
    @classmethod
    def commandExists(cls):
        """ DOES THE NGINX COMMAND EXIST?
            NGinx must be a recognized command on the user or system path to be accessible. If the
            command is not found the process is aborted.
        """
        result = SystemUtils.executeCommand('where nginx')
        if result['code']:
            print 'ERROR: Unable to find the nginx command. Is it on your system path?'
            print result['error'].strip()
            return False

        return True

#___________________________________________________________________________________________________ getExePath
    @classmethod
    def getExePath(cls):
        result = SystemUtils.executeCommand('where nginx')
        if result['code']:
            return None
        nginxExePath   = result['out'].strip()
        return os.path.dirname(nginxExePath)
