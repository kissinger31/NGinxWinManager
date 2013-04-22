# NGinxRemoteThread.py
# (C)2013
# Scott Ernst

from pyaid.ArgsUtils import ArgsUtils

from pyglass.threading.RemoteExecutionThread import RemoteExecutionThread

from nwm.ops.NGinxRunOps import NGinxRunOps
from nwm.ops.NGinxSetupOps import NGinxSetupOps

#___________________________________________________________________________________________________ NGinxRemoteThread
class NGinxRemoteThread(RemoteExecutionThread):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        super(NGinxRemoteThread, self).__init__(parent, **kwargs)
        self._path = ArgsUtils.get('rootPath', None, kwargs)
        if not self._path:
            self._path = NGinxSetupOps.getExePath()

#===================================================================================================
#                                                                                   G E T / S E T

#___________________________________________________________________________________________________ GS: rootPath
    @property
    def rootPath(self):
        return self._path

#===================================================================================================
#                                                                               P R O T E C T E D

#___________________________________________________________________________________________________ _runImpl
    def _runImpl(self):
        """Doc..."""
        self._output = NGinxRunOps.startServer(self._path)
        return self._output['code']
