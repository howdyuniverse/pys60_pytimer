import os
import sys
import e32

PACKAGE_LOC = "E:\\Data\\python"
if PACKAGE_LOC not in sys.path:
    sys.path.append(PACKAGE_LOC)

try:
    from pytimer import pytimerapp
    pytimerapp.PyTimerApp().run()
except Exception, e:
      import appuifw
      appuifw.note(u"Exception: %s" % (e))
