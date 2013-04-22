# NGinxWinManagerMainWindow.py
# (C)2013
# Scott Ernst

from PySide import QtGui

from nwm.views.BaseWindow import BaseWindow
from nwm.views.home.NwmHomeWidget import NwmHomeWidget

#___________________________________________________________________________________________________ NGinxWinManagerMainWindow
class NGinxWinManagerMainWindow(BaseWindow):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, **kwargs):
        super(NGinxWinManagerMainWindow, self).__init__(
            title=u'NGinx Windows Manager',
            widgets={
                'home':NwmHomeWidget
            },
            **kwargs
        )

        self._projectData = None

        mainLayout = self.layout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)

        w = QtGui.QWidget(self)
        self.setCentralWidget(w)
        self._centerWidget = self.centralWidget()
        self.setActiveWidget('home')

        self.setMinimumSize(480, 180)

#===================================================================================================
#                                                                               P R O T E C T E D

#___________________________________________________________________________________________________ postShow
    def postShow(self, **kwargs):
        self._widgets['home'].stopActiveServer()
