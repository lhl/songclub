
AUTOMAKE_OPTIONS = foreign

EXTRA_DIST = taglib.i taglib_list.i taglib_map.i \
	     taglib_wrap.cxx TagLib.py \
	     python-taglib.spec autogen.sh

CLEANFILES = *_wrap.cxx TagLib.py

lib_LTLIBRARIES = libpython_taglib.la

nodist_python_PYTHON = TagLib.py

# XXX: this is probably autoconf material
TAGLIBFLAGS = $(shell taglib-config --cflags)
TAGLIB = $(shell taglib-config --libs)

nodist_libpython_taglib_la_SOURCES = taglib_wrap.cxx
libpython_taglib_la_LDFLAGS = -avoid-version -module 
libpython_taglib_la_LDFLAGS += $(TAGLIB)
libpython_taglib_la_CPPFLAGS = $(SWIG_PYTHON_CPPFLAGS) $(TAGLIBFLAGS)

TagLib.py: taglib_wrap.cxx

%.py: %_wrap.cxx

%_wrap.cxx: %.i
	$(SWIG) $(TAGLIBFLAGS) $(SWIG_PYTHON_OPT) -I$(top_srcdir) -o $@ $<

install-exec-hook:
	$(mkinstalldirs) "$(DESTDIR)$(pythondir)"
	cd "$(DESTDIR)$(pythondir)" && rm -f _TagLib.so && $(LN_S) $(libdir)/libpython_taglib.so _TagLib.so

uninstall-local:
	rm -f "$(DESTDIR)$(pythondir)/_TagLib.so"
