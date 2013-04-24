# NwmCompiler.py
# (C)2013
# Scott Ernst

from pyglass.compile.PyGlassApplicationCompiler import PyGlassApplicationCompiler
from pyglass.compile.SiteLibraryEnum import SiteLibraryEnum

from nwm.NGinxWinManagerApplication import NGinxWinManagerApplication

#___________________________________________________________________________________________________ NwmCompiler
class NwmCompiler(PyGlassApplicationCompiler):
    """A class for..."""

#===================================================================================================
#                                                                                   G E T / S E T

#___________________________________________________________________________________________________ GS: siteLibraries
    @property
    def siteLibraries(self):
        return [SiteLibraryEnum.PYSIDE]

#___________________________________________________________________________________________________ GS: binPath
    @property
    def binPath(self):
        return ['..', '..', 'bin']

#___________________________________________________________________________________________________ GS: appFilename
    @property
    def appFilename(self):
        return 'NGinxWinManager'

#___________________________________________________________________________________________________ GS: appDisplayName
    @property
    def appDisplayName(self):
        return 'NGinxWinManager'

#___________________________________________________________________________________________________ GS: applicationClass
    @property
    def applicationClass(self):
        return NGinxWinManagerApplication

#___________________________________________________________________________________________________ GS: iconPath
    @property
    def iconPath(self):
        return ['apps', 'NGinxWinManager', 'icons']

####################################################################################################
####################################################################################################

if __name__ == '__main__':
    NwmCompiler().run()
