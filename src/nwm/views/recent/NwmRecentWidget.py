# NwmRecentWidget.py
# (C)2013
# Scott Ernst

from PySide import QtGui

from pyglass.widgets.PyGlassWidget import PyGlassWidget

from nwm.enum.AppConfigEnum import AppConfigEnum
from nwm.ops.NGinxRunOps import NGinxRunOps
from nwm.ops.NGinxSetupOps import NGinxSetupOps
from nwm.threads.NGinxRemoteThread import NGinxRemoteThread

#___________________________________________________________________________________________________ NwmRecentWidget
class NwmRecentWidget(PyGlassWidget):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

    _HEADER_STYLE = "QLabel { font-size:12px; } "

    _serverThread = None

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of NwmRecentWidget."""
        super(NwmRecentWidget, self).__init__(parent, widgetFile=False, id='recent', **kwargs)

        mainLayout = self._getLayout(self, QtGui.QVBoxLayout)
        mainLayout.setContentsMargins(6, 6, 6, 6)
        mainLayout.setSpacing(6)

        recentPaths = self.mainWindow.appConfig.get(
            AppConfigEnum.RECENT_PATHS, []
        )

        mainLayout.addStretch()

#===================================================================================================
#                                                                                   G E T / S E T

#___________________________________________________________________________________________________ GS: rootPath
    @property
    def rootPath(self):
        path = self._pathLineEdit.text()
        if path:
            return path
        return NGinxSetupOps.getExePath()

#===================================================================================================
#                                                                                     P U B L I C

#___________________________________________________________________________________________________ stopActiveServer
    def stopActiveServer(self):
        if not NGinxRunOps.isRunning() or self._serverThread is None:
            return
        NGinxRunOps.stopServer(self._serverThread.rootPath)

#===================================================================================================
#                                                                               P R O T E C T E D

#___________________________________________________________________________________________________ _updateDisplay
    def _updateDisplay(self):
        self._startBtn.setEnabled(self._serverThread is None)
        self._stopBtn.setEnabled(self._serverThread is not None)
        self._reloadBtn.setEnabled(self._serverThread is not None)
        self._pathLineEdit.setEnabled(self._serverThread is None)

#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _handleStartServer
    def _handleStartServer(self):
        if not NGinxSetupOps.commandExists():
            self.mainWindow.updateStatusBar(u'ERROR: No NGinx command available')
            print 'NO COMMAND'
            return

        if NGinxRunOps.isRunning():
            self.mainWindow.updateStatusBar(u'ERROR: An NGinx process is already active')
            print 'ALREADY RUNNING'
            return

        thread = NGinxRemoteThread(self, rootPath=self.rootPath)
        self._serverThread = thread
        thread.start()
        self.mainWindow.updateStatusBar(u'NGinx server now active')
        self._updateDisplay()

#___________________________________________________________________________________________________ _handleStopServer
    def _handleStopServer(self):
        if not self._serverThread:
            self.mainWindow.updateStatusBar(u'ERROR: Server is not currently active')
            print 'NO ACTIVE SERVER THREAD'
            return

        if not NGinxRunOps.isRunning():
            self.mainWindow.updateStatusBar(u'ERROR: No active NGinx server found')
            print 'NOT RUNNING'
            return

        NGinxRunOps.stopServer(self._serverThread.rootPath)
        self._serverThread = None
        self._updateDisplay()

#___________________________________________________________________________________________________ _handleReloadServer
    def _handleReloadServer(self):
        if not NGinxRunOps.isRunning() or not self._serverThread:
            return
        NGinxRunOps.reloadServer(self._serverThread.rootPath)
        self._updateDisplay()

#___________________________________________________________________________________________________ _handleLocatePath
    def _handleLocatePath(self):
        self.refreshGui()
        path = QtGui.QFileDialog.getExistingDirectory(
            self,
            caption=u'Specify Root NGinx Path',
            dir=self.rootPath
        )

        if path:
            self._pathLineEdit.setText(path)
            self.mainWindow.appConfig.set(AppConfigEnum.ROOT_PATH, path)

#___________________________________________________________________________________________________ _handleRecentLocations
    def _handleRecentLocations(self):
        pass
