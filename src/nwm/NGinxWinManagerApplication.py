# NGinxWinManagerApplication.py
# (C)2013
# Scott Ernst

from pyglass.app.PyGlassApplication import PyGlassApplication

#___________________________________________________________________________________________________ NGinxWinManagerApplication
class NGinxWinManagerApplication(PyGlassApplication):

#===================================================================================================
#                                                                                   G E T / S E T

#___________________________________________________________________________________________________ GS: debugRootResourcePath
    @property
    def debugRootResourcePath(self):
        return ['..', '..', 'resources']

#___________________________________________________________________________________________________ GS: splashScreenUrl
    @property
    def splashScreenUrl(self):
        return 'splashscreen.png'

#___________________________________________________________________________________________________ GS: appGroupID
    @property
    def appGroupID(self):
        return 'nwm'

#___________________________________________________________________________________________________ GS: appID
    @property
    def appID(self):
        return 'NGinxWinManager'

#___________________________________________________________________________________________________ GS: mainWindowClass
    @property
    def mainWindowClass(self):
        from nwm.views.NGinxWinManagerMainWindow import NGinxWinManagerMainWindow
        return NGinxWinManagerMainWindow

####################################################################################################
####################################################################################################

if __name__ == '__main__':
    NGinxWinManagerApplication().run()


