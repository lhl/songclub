%define python_site %(python -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Python bindings for TagLib
Name: python-taglib
Version: 1.3.3
Release: 1emh
URL: http://namingmuse.berlios.de
Source: http://download.berlios.de/namingmuse/python-taglib-%{version}.tar.gz
Group: tinysofa contrib
License: GPL
BuildRoot: %{_tmppath}/%name-%version-buildroot-%(id -nu)
BuildRequires: python-devel, taglib-devel, swig
Requires: python, taglib

%description
Python bindings for TagLib, the audio meta data library
for mp3/ogg/flac/mpc/ape.

%prep
%setup -q

%build
%configure 
%{__make}

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=%{buildroot} install

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc 
%{_libdir}/libpython_taglib.so
%{_libdir}/libpython_taglib.la
%{python_site}/_TagLib.so
%{python_site}/TagLib.*

%changelog
* Fri Sep 17 2004 Eivind Magnus Hvidevold <emh at hvidevold dot cjb dot net>
- Initial release
