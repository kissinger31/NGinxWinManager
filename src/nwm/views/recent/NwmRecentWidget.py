# NwmRecentWidget.py
# (C)2013
# Scott Ernst

from PySide import QtGui

from pyglass.elements.buttons.PyGlassPushButton import PyGlassPushButton
from pyglass.elements.icons.IconSheetMap import IconSheetMap
from pyglass.enum.SizeEnum import SizeEnum
from pyglass.themes.ColorSchemes import ColorSchemes
from pyglass.widgets.PyGlassWidget import PyGlassWidget

from nwm.enum.AppConfigEnum import AppConfigEnum

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

        topWidget, topLayout = self._createWidget(self, QtGui.QHBoxLayout, True)

        label = QtGui.QLabel(topWidget)
        label.setText(u'Select Recent Container Path:')
        label.setStyleSheet("QLabel { color:#333; font-size:14px; }")
        topLayout.addWidget(label)
        topLayout.addStretch()

        btn = PyGlassPushButton(
            topWidget,
            text='Cancel',
            icon=IconSheetMap.CANCEL,
            size=SizeEnum.MEDIUM,
            colorScheme=ColorSchemes.BLUE
        )
        btn.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        btn.clicked.connect(self._handleCancel)
        topLayout.addWidget(btn)

        mainLayout.addStretch()

#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _handleCancel
    def _handleCancel(self):
        self.mainWindow.setActiveWidget('home')
