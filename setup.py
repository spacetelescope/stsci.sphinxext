#!/usr/bin/env python
from __future__ import division # confidence high

try :
    import stsci.tools.stsci_distutils_hack as H
except ImportError :
    H=None

if H :
    H.run()
else :
    import distutils
    from distutils.core import setup
    from defsetup import setupargs, pkg
    import glob

    # copied from stsci_distutils_hack
    l = [ ]
    for f in setupargs['data_files'] :
        ( dest_dir, files ) = f
        fl = [ ]
        for ff in files :
            ff = distutils.util.convert_path(ff)
            ff = glob.glob(ff)
            fl.extend(ff)
        dest_dir = distutils.util.convert_path(dest_dir)
        l.append( ( dest_dir, fl ) )
    setupargs['data_files'] = l


    setup( name=pkg[0], packages = pkg, **setupargs )
