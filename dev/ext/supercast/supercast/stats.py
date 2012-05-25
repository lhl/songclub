# stats.py:  Miscellaneous functions for formatting server stats
# Copyright 2001 by Matthew W. Campbell.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

def formatKB(kb):
    gb = kb / 1048576.0
    mb = kb / 1024.0

    if gb >= 1.0:
        return "%.1f GB" % gb
    elif mb >= 1.0:
        return "%.1f MB" % mb
    else:
        return "%.1f KB" % kb

def formatTime(sec):
    hr = sec / 3600.0
    min = sec / 60.0

    if hr >= 1.0:
        return "%.1f hr" % hr
    elif min >= 1.0:
        return "%.1f min" % min
    else:
        return "%.1f s" % sec
