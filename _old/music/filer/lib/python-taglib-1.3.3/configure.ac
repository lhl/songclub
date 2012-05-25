#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.59)
AC_INIT(python-taglib, 1.3.3, namingmuse-devel@lists.berlios.de)
AM_INIT_AUTOMAKE
AC_CONFIG_SRCDIR([taglib.i])
AC_CONFIG_HEADER([config.h])

AC_DISABLE_STATIC

# Checks for programs.
AC_PROG_CXX
AC_PROG_INSTALL
AC_PROG_LIBTOOL

# Sets default prefix to same as python
AC_PREFIX_PROGRAM([python])

AC_PROG_SWIG([1.3.24])
SWIG_ENABLE_CXX
SWIG_PYTHON
AC_PROG_LN_S

AC_CHECK_PROG(TAGLIBCONFIG, taglib-config, taglib-config)

SWIGBIN=$(echo $SWIG | cut -f1 -d " ")
if test ! -x "$SWIGBIN"; then
    AC_MSG_WARN([swig is missing. will not recompile bindings from \
interface definition])
    AM_PATH_PYTHON
else
    rm -f taglib_wrap.cxx TagLib.py
fi

if test -z "$TAGLIBCONFIG"; then
    AC_MSG_ERROR([taglib-config is missing. install taglib-devel])
fi

# Checks for libraries.

# Checks for header files.
AC_HEADER_STDC
AC_CHECK_HEADERS([string.h])

# Checks for typedefs, structures, and compiler characteristics.
AC_HEADER_STDBOOL
AC_C_CONST

# Checks for library functions.
AC_FUNC_MALLOC

AC_CONFIG_FILES([Makefile])
AC_OUTPUT
