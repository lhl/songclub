#!/bin/sh
swigm=http://ac-archive.sourceforge.net/Installed_Packages/ac_pkg_swig.m4
pythonm=http://ac-archive.sourceforge.net/Installed_Packages/ac_python_devel.m4
wget -q $swigm -O acinclude.m4
wget -q $pythonm -O- >> acinclude.m4
autoreconf -vi
