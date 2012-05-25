# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _TagLib

def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name) or (name == "thisown"):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


TAGLIB_MAJOR_VERSION = _TagLib.TAGLIB_MAJOR_VERSION
TAGLIB_MINOR_VERSION = _TagLib.TAGLIB_MINOR_VERSION
TAGLIB_PATCH_VERSION = _TagLib.TAGLIB_PATCH_VERSION
class RefCounter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RefCounter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RefCounter, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ TagLib::RefCounter instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, RefCounter, 'this', _TagLib.new_RefCounter(*args))
        _swig_setattr(self, RefCounter, 'thisown', 1)
    def ref(*args): return _TagLib.RefCounter_ref(*args)
    def deref(*args): return _TagLib.RefCounter_deref(*args)
    def count(*args): return _TagLib.RefCounter_count(*args)
    def __del__(self, destroy=_TagLib.delete_RefCounter):
        try:
            if self.thisown: destroy(self)
        except: pass


class RefCounterPtr(RefCounter):
    def __init__(self, this):
        _swig_setattr(self, RefCounter, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, RefCounter, 'thisown', 0)
        _swig_setattr(self, RefCounter,self.__class__,RefCounter)
_TagLib.RefCounter_swigregister(RefCounterPtr)

class AudioProperties(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AudioProperties, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AudioProperties, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C++ TagLib::AudioProperties instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    Fast = _TagLib.AudioProperties_Fast
    Average = _TagLib.AudioProperties_Average
    Accurate = _TagLib.AudioProperties_Accurate
    def __del__(self, destroy=_TagLib.delete_AudioProperties):
        try:
            if self.thisown: destroy(self)
        except: pass

    def length(*args): return _TagLib.AudioProperties_length(*args)
    def bitrate(*args): return _TagLib.AudioProperties_bitrate(*args)
    def sampleRate(*args): return _TagLib.AudioProperties_sampleRate(*args)
    def channels(*args): return _TagLib.AudioProperties_channels(*args)

class AudioPropertiesPtr(AudioProperties):
    def __init__(self, this):
        _swig_setattr(self, AudioProperties, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, AudioProperties, 'thisown', 0)
        _swig_setattr(self, AudioProperties,self.__class__,AudioProperties)
_TagLib.AudioProperties_swigregister(AudioPropertiesPtr)

class FileRef(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FileRef, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FileRef, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ TagLib::FileRef instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, FileRef, 'this', _TagLib.new_FileRef(*args))
        _swig_setattr(self, FileRef, 'thisown', 1)
    def __del__(self, destroy=_TagLib.delete_FileRef):
        try:
            if self.thisown: destroy(self)
        except: pass

    def tag(*args): return _TagLib.FileRef_tag(*args)
    def audioProperties(*args): return _TagLib.FileRef_audioProperties(*args)
    def file(*args): return _TagLib.FileRef_file(*args)
    def save(*args): return _TagLib.FileRef_save(*args)
    def isNull(*args): return _TagLib.FileRef_isNull(*args)
    def __eq__(*args): return _TagLib.FileRef___eq__(*args)
    def __ne__(*args): return _TagLib.FileRef___ne__(*args)
    __swig_getmethods__["create"] = lambda x: _TagLib.FileRef_create
    if _newclass:create = staticmethod(_TagLib.FileRef_create)

class FileRefPtr(FileRef):
    def __init__(self, this):
        _swig_setattr(self, FileRef, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, FileRef, 'thisown', 0)
        _swig_setattr(self, FileRef,self.__class__,FileRef)
_TagLib.FileRef_swigregister(FileRefPtr)

FileRef_create = _TagLib.FileRef_create

class ByteVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ByteVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ByteVector, name)
    def __init__(self, *args):
        _swig_setattr(self, ByteVector, 'this', _TagLib.new_ByteVector(*args))
        _swig_setattr(self, ByteVector, 'thisown', 1)
    def __del__(self, destroy=_TagLib.delete_ByteVector):
        try:
            if self.thisown: destroy(self)
        except: pass

    def setData(*args): return _TagLib.ByteVector_setData(*args)
    def data(*args): return _TagLib.ByteVector_data(*args)
    def mid(*args): return _TagLib.ByteVector_mid(*args)
    def at(*args): return _TagLib.ByteVector_at(*args)
    def find(*args): return _TagLib.ByteVector_find(*args)
    def rfind(*args): return _TagLib.ByteVector_rfind(*args)
    def containsAt(*args): return _TagLib.ByteVector_containsAt(*args)
    def startsWith(*args): return _TagLib.ByteVector_startsWith(*args)
    def endsWith(*args): return _TagLib.ByteVector_endsWith(*args)
    def endsWithPartialMatch(*args): return _TagLib.ByteVector_endsWithPartialMatch(*args)
    def append(*args): return _TagLib.ByteVector_append(*args)
    def clear(*args): return _TagLib.ByteVector_clear(*args)
    def size(*args): return _TagLib.ByteVector_size(*args)
    def resize(*args): return _TagLib.ByteVector_resize(*args)
    def begin(*args): return _TagLib.ByteVector_begin(*args)
    def end(*args): return _TagLib.ByteVector_end(*args)
    def isNull(*args): return _TagLib.ByteVector_isNull(*args)
    def isEmpty(*args): return _TagLib.ByteVector_isEmpty(*args)
    def checksum(*args): return _TagLib.ByteVector_checksum(*args)
    def toUInt(*args): return _TagLib.ByteVector_toUInt(*args)
    def toShort(*args): return _TagLib.ByteVector_toShort(*args)
    def toLongLong(*args): return _TagLib.ByteVector_toLongLong(*args)
    __swig_getmethods__["fromUInt"] = lambda x: _TagLib.ByteVector_fromUInt
    if _newclass:fromUInt = staticmethod(_TagLib.ByteVector_fromUInt)
    __swig_getmethods__["fromShort"] = lambda x: _TagLib.ByteVector_fromShort
    if _newclass:fromShort = staticmethod(_TagLib.ByteVector_fromShort)
    __swig_getmethods__["fromLongLong"] = lambda x: _TagLib.ByteVector_fromLongLong
    if _newclass:fromLongLong = staticmethod(_TagLib.ByteVector_fromLongLong)
    __swig_getmethods__["fromCString"] = lambda x: _TagLib.ByteVector_fromCString
    if _newclass:fromCString = staticmethod(_TagLib.ByteVector_fromCString)
    def __eq__(*args): return _TagLib.ByteVector___eq__(*args)
    def __ne__(*args): return _TagLib.ByteVector___ne__(*args)
    def __lt__(*args): return _TagLib.ByteVector___lt__(*args)
    def __gt__(*args): return _TagLib.ByteVector___gt__(*args)
    def __add__(*args): return _TagLib.ByteVector___add__(*args)
    def __repr__(*args): return _TagLib.ByteVector___repr__(*args)

class ByteVectorPtr(ByteVector):
    def __init__(self, this):
        _swig_setattr(self, ByteVector, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, ByteVector, 'thisown', 0)
        _swig_setattr(self, ByteVector,self.__class__,ByteVector)
_TagLib.ByteVector_swigregister(ByteVectorPtr)

ByteVector_fromUInt = _TagLib.ByteVector_fromUInt

ByteVector_fromShort = _TagLib.ByteVector_fromShort

ByteVector_fromLongLong = _TagLib.ByteVector_fromLongLong

ByteVector_fromCString = _TagLib.ByteVector_fromCString
cvar = _TagLib.cvar

class String(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, String, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, String, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ TagLib::String instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    Latin1 = _TagLib.String_Latin1
    UTF16 = _TagLib.String_UTF16
    UTF16BE = _TagLib.String_UTF16BE
    UTF8 = _TagLib.String_UTF8
    def __init__(self, *args):
        _swig_setattr(self, String, 'this', _TagLib.new_String(*args))
        _swig_setattr(self, String, 'thisown', 1)
    def __del__(self, destroy=_TagLib.delete_String):
        try:
            if self.thisown: destroy(self)
        except: pass

    def to8Bit(*args): return _TagLib.String_to8Bit(*args)
    def toCString(*args): return _TagLib.String_toCString(*args)
    def begin(*args): return _TagLib.String_begin(*args)
    def end(*args): return _TagLib.String_end(*args)
    def find(*args): return _TagLib.String_find(*args)
    def substr(*args): return _TagLib.String_substr(*args)
    def append(*args): return _TagLib.String_append(*args)
    def upper(*args): return _TagLib.String_upper(*args)
    def size(*args): return _TagLib.String_size(*args)
    def isEmpty(*args): return _TagLib.String_isEmpty(*args)
    def isNull(*args): return _TagLib.String_isNull(*args)
    def data(*args): return _TagLib.String_data(*args)
    def toInt(*args): return _TagLib.String_toInt(*args)
    def stripWhiteSpace(*args): return _TagLib.String_stripWhiteSpace(*args)
    __swig_getmethods__["number"] = lambda x: _TagLib.String_number
    if _newclass:number = staticmethod(_TagLib.String_number)
    def __eq__(*args): return _TagLib.String___eq__(*args)
    def __iadd__(*args): return _TagLib.String___iadd__(*args)
    def __lt__(*args): return _TagLib.String___lt__(*args)
    def __str__(*args): return _TagLib.String___str__(*args)

class StringPtr(String):
    def __init__(self, this):
        _swig_setattr(self, String, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, String, 'thisown', 0)
        _swig_setattr(self, String,self.__class__,String)
_TagLib.String_swigregister(StringPtr)

String_number = _TagLib.String_number

class Tag(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Tag, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Tag, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C++ TagLib::Tag instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __del__(self, destroy=_TagLib.delete_Tag):
        try:
            if self.thisown: destroy(self)
        except: pass

    def title(*args): return _TagLib.Tag_title(*args)
    def artist(*args): return _TagLib.Tag_artist(*args)
    def album(*args): return _TagLib.Tag_album(*args)
    def comment(*args): return _TagLib.Tag_comment(*args)
    def genre(*args): return _TagLib.Tag_genre(*args)
    def year(*args): return _TagLib.Tag_year(*args)
    def track(*args): return _TagLib.Tag_track(*args)
    def setTitle(*args): return _TagLib.Tag_setTitle(*args)
    def setArtist(*args): return _TagLib.Tag_setArtist(*args)
    def setAlbum(*args): return _TagLib.Tag_setAlbum(*args)
    def setComment(*args): return _TagLib.Tag_setComment(*args)
    def setGenre(*args): return _TagLib.Tag_setGenre(*args)
    def setYear(*args): return _TagLib.Tag_setYear(*args)
    def setTrack(*args): return _TagLib.Tag_setTrack(*args)
    def isEmpty(*args): return _TagLib.Tag_isEmpty(*args)
    __swig_getmethods__["duplicate"] = lambda x: _TagLib.Tag_duplicate
    if _newclass:duplicate = staticmethod(_TagLib.Tag_duplicate)

class TagPtr(Tag):
    def __init__(self, this):
        _swig_setattr(self, Tag, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Tag, 'thisown', 0)
        _swig_setattr(self, Tag,self.__class__,Tag)
_TagLib.Tag_swigregister(TagPtr)

Tag_duplicate = _TagLib.Tag_duplicate

class pystringlist(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pystringlist, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pystringlist, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ TagLib::List<TagLib::String > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, pystringlist, 'this', _TagLib.new_pystringlist(*args))
        _swig_setattr(self, pystringlist, 'thisown', 1)
    def __del__(self, destroy=_TagLib.delete_pystringlist):
        try:
            if self.thisown: destroy(self)
        except: pass

    def begin(*args): return _TagLib.pystringlist_begin(*args)
    def end(*args): return _TagLib.pystringlist_end(*args)
    def insert(*args): return _TagLib.pystringlist_insert(*args)
    def sortedInsert(*args): return _TagLib.pystringlist_sortedInsert(*args)
    def append(*args): return _TagLib.pystringlist_append(*args)
    def clear(*args): return _TagLib.pystringlist_clear(*args)
    def size(*args): return _TagLib.pystringlist_size(*args)
    def isEmpty(*args): return _TagLib.pystringlist_isEmpty(*args)
    def find(*args): return _TagLib.pystringlist_find(*args)
    def contains(*args): return _TagLib.pystringlist_contains(*args)
    def erase(*args): return _TagLib.pystringlist_erase(*args)
    def front(*args): return _TagLib.pystringlist_front(*args)
    def back(*args): return _TagLib.pystringlist_back(*args)
    def setAutoDelete(*args): return _TagLib.pystringlist_setAutoDelete(*args)
    def __eq__(*args): return _TagLib.pystringlist___eq__(*args)
    def __getitem__(*args): return _TagLib.pystringlist___getitem__(*args)
    def __setitem__(*args): return _TagLib.pystringlist___setitem__(*args)
    def __delitem__(*args): return _TagLib.pystringlist___delitem__(*args)
    def __getslice__(*args): return _TagLib.pystringlist___getslice__(*args)
    def __delslice__(*args): return _TagLib.pystringlist___delslice__(*args)
    def __setslice__(*args): return _TagLib.pystringlist___setslice__(*args)
    def __len__(*args): return _TagLib.pystringlist___len__(*args)
    def __nonzero__(*args): return _TagLib.pystringlist___nonzero__(*args)
    def __setitem__(a,b,c):
        """ This is not supported, use addFrame and/or removeFrame """
        raise AttributeError
    def __delitem__(a,b,c):
        """ This is not supported, use addFrame and/or removeFrame """
        raise AttributeError
    def __setslice__(a,b,c):
        """ This is not supported, use addFrame and/or removeFrame """
        raise AttributeError


class pystringlistPtr(pystringlist):
    def __init__(self, this):
        _swig_setattr(self, pystringlist, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, pystringlist, 'thisown', 0)
        _swig_setattr(self, pystringlist,self.__class__,pystringlist)
_TagLib.pystringlist_swigregister(pystringlistPtr)

class StringList(pystringlist):
    __swig_setmethods__ = {}
    for _s in [pystringlist]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringList, name, value)
    __swig_getmethods__ = {}
    for _s in [pystringlist]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, StringList, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ TagLib::StringList instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, StringList, 'this', _TagLib.new_StringList(*args))
        _swig_setattr(self, StringList, 'thisown', 1)
    def __del__(self, destroy=_TagLib.delete_StringList):
        try:
            if self.thisown: destroy(self)
        except: pass

    def toString(*args): return _TagLib.StringList_toString(*args)
    def append(*args): return _TagLib.StringList_append(*args)
    __swig_getmethods__["split"] = lambda x: _TagLib.StringList_split
    if _newclass:split = staticmethod(_TagLib.StringList_split)

class StringListPtr(StringList):
    def __init__(self, this):
        _swig_setattr(self, StringList, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, StringList, 'thisown', 0)
        _swig_setattr(self, StringList,self.__class__,StringList)
_TagLib.StringList_swigregister(StringListPtr)

StringList_split = _TagLib.StringList_split

class MPEGFile(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MPEGFile, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MPEGFile, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ TagLib::MPEG::File instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    NoTags = _TagLib.MPEGFile_NoTags
    ID3v1 = _TagLib.MPEGFile_ID3v1
    ID3v2 = _TagLib.MPEGFile_ID3v2
    APE = _TagLib.MPEGFile_APE
    AllTags = _TagLib.MPEGFile_AllTags
    def __init__(self, *args):
        _swig_setattr(self, MPEGFile, 'this', _TagLib.new_MPEGFile(*args))
        _swig_setattr(self, MPEGFile, 'thisown', 1)
    def __del__(self, destroy=_TagLib.delete_MPEGFile):
        try:
            if self.thisown: destroy(self)
        except: pass

    def tag(*args): return _TagLib.MPEGFile_tag(*args)
    def audioProperties(*args): return _TagLib.MPEGFile_audioProperties(*args)
    def save(*args): return _TagLib.MPEGFile_save(*args)
    def ID3v2Tag(*args): return _TagLib.MPEGFile_ID3v2Tag(*args)
    def ID3v1Tag(*args): return _TagLib.MPEGFile_ID3v1Tag(*args)
    def APETag(*args): return _TagLib.MPEGFile_APETag(*args)
    def strip(*args): return _TagLib.MPEGFile_strip(*args)
    def setID3v2FrameFactory(*args): return _TagLib.MPEGFile_setID3v2FrameFactory(*args)
    def firstFrameOffset(*args): return _TagLib.MPEGFile_firstFrameOffset(*args)
    def nextFrameOffset(*args): return _TagLib.MPEGFile_nextFrameOffset(*args)
    def previousFrameOffset(*args): return _TagLib.MPEGFile_previousFrameOffset(*args)
    def lastFrameOffset(*args): return _TagLib.MPEGFile_lastFrameOffset(*args)

class MPEGFilePtr(MPEGFile):
    def __init__(self, this):
        _swig_setattr(self, MPEGFile, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, MPEGFile, 'thisown', 0)
        _swig_setattr(self, MPEGFile,self.__class__,MPEGFile)
_TagLib.MPEGFile_swigregister(MPEGFilePtr)

class Frame(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Frame, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Frame, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __del__(self, destroy=_TagLib.delete_Frame):
        try:
            if self.thisown: destroy(self)
        except: pass

    def frameID(*args): return _TagLib.Frame_frameID(*args)
    def size(*args): return _TagLib.Frame_size(*args)
    __swig_getmethods__["headerSize"] = lambda x: _TagLib.Frame_headerSize
    if _newclass:headerSize = staticmethod(_TagLib.Frame_headerSize)
    def setData(*args): return _TagLib.Frame_setData(*args)
    def setText(*args): return _TagLib.Frame_setText(*args)
    def toString(*args): return _TagLib.Frame_toString(*args)
    def render(*args): return _TagLib.Frame_render(*args)
    __swig_getmethods__["textDelimiter"] = lambda x: _TagLib.Frame_textDelimiter
    if _newclass:textDelimiter = staticmethod(_TagLib.Frame_textDelimiter)
    def __str__(*args): return _TagLib.Frame___str__(*args)
    def __repr__(*args): return _TagLib.Frame___repr__(*args)

class FramePtr(Frame):
    def __init__(self, this):
        _swig_setattr(self, Frame, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Frame, 'thisown', 0)
        _swig_setattr(self, Frame,self.__class__,Frame)
_TagLib.Frame_swigregister(FramePtr)

Frame_headerSize = _TagLib.Frame_headerSize

Frame_textDelimiter = _TagLib.Frame_textDelimiter

class ID3v2Tag(Tag):
    __swig_setmethods__ = {}
    for _s in [Tag]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, ID3v2Tag, name, value)
    __swig_getmethods__ = {}
    for _s in [Tag]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, ID3v2Tag, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ TagLib::ID3v2::Tag instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, ID3v2Tag, 'this', _TagLib.new_ID3v2Tag(*args))
        _swig_setattr(self, ID3v2Tag, 'thisown', 1)
    def __del__(self, destroy=_TagLib.delete_ID3v2Tag):
        try:
            if self.thisown: destroy(self)
        except: pass

    def title(*args): return _TagLib.ID3v2Tag_title(*args)
    def artist(*args): return _TagLib.ID3v2Tag_artist(*args)
    def album(*args): return _TagLib.ID3v2Tag_album(*args)
    def comment(*args): return _TagLib.ID3v2Tag_comment(*args)
    def genre(*args): return _TagLib.ID3v2Tag_genre(*args)
    def year(*args): return _TagLib.ID3v2Tag_year(*args)
    def track(*args): return _TagLib.ID3v2Tag_track(*args)
    def setTitle(*args): return _TagLib.ID3v2Tag_setTitle(*args)
    def setArtist(*args): return _TagLib.ID3v2Tag_setArtist(*args)
    def setAlbum(*args): return _TagLib.ID3v2Tag_setAlbum(*args)
    def setComment(*args): return _TagLib.ID3v2Tag_setComment(*args)
    def setGenre(*args): return _TagLib.ID3v2Tag_setGenre(*args)
    def setYear(*args): return _TagLib.ID3v2Tag_setYear(*args)
    def setTrack(*args): return _TagLib.ID3v2Tag_setTrack(*args)
    def isEmpty(*args): return _TagLib.ID3v2Tag_isEmpty(*args)
    def header(*args): return _TagLib.ID3v2Tag_header(*args)
    def extendedHeader(*args): return _TagLib.ID3v2Tag_extendedHeader(*args)
    def footer(*args): return _TagLib.ID3v2Tag_footer(*args)
    def frameListMap(*args): return _TagLib.ID3v2Tag_frameListMap(*args)
    def frameList(*args): return _TagLib.ID3v2Tag_frameList(*args)
    def addFrame(*args):
        if len(args) > 1:
            self,frame = args[0],args[1]
            if isinstance(frame, Frame):
                # Tag destructor will destroy C++ frame object for us later
                # tell Python Frame class not to destroy it
                frame.thisown = 0 
        return _TagLib.ID3v2Tag_addFrame(*args)


    def removeFrame(*args):
        if len(args) > 1:
            self,frame = args[0],args[1]
            memfree = False
            #if isinstance(frame, Frame):
                # Tag destructor will destroy C++ frame object for us later
                # tell Python Frame class not to destroy it
                # frame.thisown = 1 
            return _TagLib.ID3v2Tag_removeFrame(self, frame, memfree)
        else:
            # let swig handle the error
            return _TagLib.ID3v2Tag_removeFrame(*args)
            


    def removeFrames(*args): return _TagLib.ID3v2Tag_removeFrames(*args)
    def render(*args): return _TagLib.ID3v2Tag_render(*args)

class ID3v2TagPtr(ID3v2Tag):
    def __init__(self, this):
        _swig_setattr(self, ID3v2Tag, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, ID3v2Tag, 'thisown', 0)
        _swig_setattr(self, ID3v2Tag,self.__class__,ID3v2Tag)
_TagLib.ID3v2Tag_swigregister(ID3v2TagPtr)

class pyframelist(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pyframelist, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pyframelist, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ TagLib::List<TagLib::ID3v2::Frame * > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, pyframelist, 'this', _TagLib.new_pyframelist(*args))
        _swig_setattr(self, pyframelist, 'thisown', 1)
    def __del__(self, destroy=_TagLib.delete_pyframelist):
        try:
            if self.thisown: destroy(self)
        except: pass

    def begin(*args): return _TagLib.pyframelist_begin(*args)
    def end(*args): return _TagLib.pyframelist_end(*args)
    def insert(*args): return _TagLib.pyframelist_insert(*args)
    def sortedInsert(*args): return _TagLib.pyframelist_sortedInsert(*args)
    def append(*args): return _TagLib.pyframelist_append(*args)
    def clear(*args): return _TagLib.pyframelist_clear(*args)
    def size(*args): return _TagLib.pyframelist_size(*args)
    def isEmpty(*args): return _TagLib.pyframelist_isEmpty(*args)
    def find(*args): return _TagLib.pyframelist_find(*args)
    def contains(*args): return _TagLib.pyframelist_contains(*args)
    def erase(*args): return _TagLib.pyframelist_erase(*args)
    def front(*args): return _TagLib.pyframelist_front(*args)
    def back(*args): return _TagLib.pyframelist_back(*args)
    def setAutoDelete(*args): return _TagLib.pyframelist_setAutoDelete(*args)
    def __eq__(*args): return _TagLib.pyframelist___eq__(*args)
    def __getitem__(*args): return _TagLib.pyframelist___getitem__(*args)
    def __setitem__(*args): return _TagLib.pyframelist___setitem__(*args)
    def __delitem__(*args): return _TagLib.pyframelist___delitem__(*args)
    def __getslice__(*args): return _TagLib.pyframelist___getslice__(*args)
    def __delslice__(*args): return _TagLib.pyframelist___delslice__(*args)
    def __setslice__(*args): return _TagLib.pyframelist___setslice__(*args)
    def __len__(*args): return _TagLib.pyframelist___len__(*args)
    def __nonzero__(*args): return _TagLib.pyframelist___nonzero__(*args)
    def __setitem__(a,b,c):
        """ This is not supported, use addFrame and/or removeFrame """
        raise AttributeError
    def __delitem__(a,b,c):
        """ This is not supported, use addFrame and/or removeFrame """
        raise AttributeError
    def __setslice__(a,b,c):
        """ This is not supported, use addFrame and/or removeFrame """
        raise AttributeError


class pyframelistPtr(pyframelist):
    def __init__(self, this):
        _swig_setattr(self, pyframelist, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, pyframelist, 'thisown', 0)
        _swig_setattr(self, pyframelist,self.__class__,pyframelist)
_TagLib.pyframelist_swigregister(pyframelistPtr)

class pyframelistmap(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pyframelistmap, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pyframelistmap, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ TagLib::Map<TagLib::ByteVector,TagLib::ID3v2::FrameList > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, pyframelistmap, 'this', _TagLib.new_pyframelistmap(*args))
        _swig_setattr(self, pyframelistmap, 'thisown', 1)
    def __del__(self, destroy=_TagLib.delete_pyframelistmap):
        try:
            if self.thisown: destroy(self)
        except: pass

    def begin(*args): return _TagLib.pyframelistmap_begin(*args)
    def end(*args): return _TagLib.pyframelistmap_end(*args)
    def insert(*args): return _TagLib.pyframelistmap_insert(*args)
    def clear(*args): return _TagLib.pyframelistmap_clear(*args)
    def size(*args): return _TagLib.pyframelistmap_size(*args)
    def isEmpty(*args): return _TagLib.pyframelistmap_isEmpty(*args)
    def find(*args): return _TagLib.pyframelistmap_find(*args)
    def contains(*args): return _TagLib.pyframelistmap_contains(*args)
    def erase(*args): return _TagLib.pyframelistmap_erase(*args)
    def __nonzero__(*args): return _TagLib.pyframelistmap___nonzero__(*args)
    def __getitem__(*args): return _TagLib.pyframelistmap___getitem__(*args)
    def __setitem__(*args): return _TagLib.pyframelistmap___setitem__(*args)
    def __delitem__(*args): return _TagLib.pyframelistmap___delitem__(*args)
    def has_key(*args): return _TagLib.pyframelistmap_has_key(*args)
    def keys(*args): return _TagLib.pyframelistmap_keys(*args)
    def values(*args): return _TagLib.pyframelistmap_values(*args)
    def items(*args): return _TagLib.pyframelistmap_items(*args)
    def __contains__(*args): return _TagLib.pyframelistmap___contains__(*args)
    def __iter__(*args): return _TagLib.pyframelistmap___iter__(*args)
    def __setitem__(a,b,c):
        """ This is not supported, use addFrame and/or removeFrame """
        raise AttributeError
    def __deltem__(a,b,c):
        """ This is not supported, use addFrame and/or removeFrame """
        raise AttributeError


class pyframelistmapPtr(pyframelistmap):
    def __init__(self, this):
        _swig_setattr(self, pyframelistmap, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, pyframelistmap, 'thisown', 0)
        _swig_setattr(self, pyframelistmap,self.__class__,pyframelistmap)
_TagLib.pyframelistmap_swigregister(pyframelistmapPtr)

class TextIdentificationFrame(Frame):
    __swig_setmethods__ = {}
    for _s in [Frame]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, TextIdentificationFrame, name, value)
    __swig_getmethods__ = {}
    for _s in [Frame]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, TextIdentificationFrame, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ TagLib::ID3v2::TextIdentificationFrame instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, TextIdentificationFrame, 'this', _TagLib.new_TextIdentificationFrame(*args))
        _swig_setattr(self, TextIdentificationFrame, 'thisown', 1)
    def __del__(self, destroy=_TagLib.delete_TextIdentificationFrame):
        try:
            if self.thisown: destroy(self)
        except: pass

    def setText(*args): return _TagLib.TextIdentificationFrame_setText(*args)
    def toString(*args): return _TagLib.TextIdentificationFrame_toString(*args)
    def textEncoding(*args): return _TagLib.TextIdentificationFrame_textEncoding(*args)
    def setTextEncoding(*args): return _TagLib.TextIdentificationFrame_setTextEncoding(*args)
    def fieldList(*args): return _TagLib.TextIdentificationFrame_fieldList(*args)
    __swig_getmethods__["fromFrame"] = lambda x: _TagLib.TextIdentificationFrame_fromFrame
    if _newclass:fromFrame = staticmethod(_TagLib.TextIdentificationFrame_fromFrame)

class TextIdentificationFramePtr(TextIdentificationFrame):
    def __init__(self, this):
        _swig_setattr(self, TextIdentificationFrame, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, TextIdentificationFrame, 'thisown', 0)
        _swig_setattr(self, TextIdentificationFrame,self.__class__,TextIdentificationFrame)
_TagLib.TextIdentificationFrame_swigregister(TextIdentificationFramePtr)

TextIdentificationFrame_fromFrame = _TagLib.TextIdentificationFrame_fromFrame

class UserTextIdentificationFrame(TextIdentificationFrame):
    __swig_setmethods__ = {}
    for _s in [TextIdentificationFrame]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, UserTextIdentificationFrame, name, value)
    __swig_getmethods__ = {}
    for _s in [TextIdentificationFrame]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, UserTextIdentificationFrame, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ TagLib::ID3v2::UserTextIdentificationFrame instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, UserTextIdentificationFrame, 'this', _TagLib.new_UserTextIdentificationFrame(*args))
        _swig_setattr(self, UserTextIdentificationFrame, 'thisown', 1)
    def toString(*args): return _TagLib.UserTextIdentificationFrame_toString(*args)
    def description(*args): return _TagLib.UserTextIdentificationFrame_description(*args)
    def setDescription(*args): return _TagLib.UserTextIdentificationFrame_setDescription(*args)
    def fieldList(*args): return _TagLib.UserTextIdentificationFrame_fieldList(*args)
    def setText(*args): return _TagLib.UserTextIdentificationFrame_setText(*args)
    def __del__(self, destroy=_TagLib.delete_UserTextIdentificationFrame):
        try:
            if self.thisown: destroy(self)
        except: pass


class UserTextIdentificationFramePtr(UserTextIdentificationFrame):
    def __init__(self, this):
        _swig_setattr(self, UserTextIdentificationFrame, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, UserTextIdentificationFrame, 'thisown', 0)
        _swig_setattr(self, UserTextIdentificationFrame,self.__class__,UserTextIdentificationFrame)
_TagLib.UserTextIdentificationFrame_swigregister(UserTextIdentificationFramePtr)

oldTextIdentificationFrameInit = TextIdentificationFrame.__init__
def newTextIdentificationFrameInit(*args):
    self = args[0]
    if len(args) > 1 and isinstance(args[1], Frame):
        frame = args[1]
        if not str(frame.frameID()).startswith("T"): #XXX: inaccurate
            raise TypeError("this frame type is not a TextIdentificationFrame: " + str(frame.frameID()))
        _swig_setattr(self, TextIdentificationFrame, 'this', self.fromFrame(frame))
        _swig_setattr(self, TextIdentificationFrame, 'thisown', 0)
    else:
        oldTextIdentificationFrameInit(*args)
TextIdentificationFrame.__init__ = newTextIdentificationFrameInit

class CommentsFrame(Frame):
    __swig_setmethods__ = {}
    for _s in [Frame]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, CommentsFrame, name, value)
    __swig_getmethods__ = {}
    for _s in [Frame]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, CommentsFrame, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ TagLib::ID3v2::CommentsFrame instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, CommentsFrame, 'this', _TagLib.new_CommentsFrame(*args))
        _swig_setattr(self, CommentsFrame, 'thisown', 1)
    def __del__(self, destroy=_TagLib.delete_CommentsFrame):
        try:
            if self.thisown: destroy(self)
        except: pass

    def toString(*args): return _TagLib.CommentsFrame_toString(*args)
    def language(*args): return _TagLib.CommentsFrame_language(*args)
    def description(*args): return _TagLib.CommentsFrame_description(*args)
    def text(*args): return _TagLib.CommentsFrame_text(*args)
    def setLanguage(*args): return _TagLib.CommentsFrame_setLanguage(*args)
    def setDescription(*args): return _TagLib.CommentsFrame_setDescription(*args)
    def setText(*args): return _TagLib.CommentsFrame_setText(*args)
    def textEncoding(*args): return _TagLib.CommentsFrame_textEncoding(*args)
    def setTextEncoding(*args): return _TagLib.CommentsFrame_setTextEncoding(*args)
    __swig_getmethods__["fromFrame"] = lambda x: _TagLib.CommentsFrame_fromFrame
    if _newclass:fromFrame = staticmethod(_TagLib.CommentsFrame_fromFrame)

class CommentsFramePtr(CommentsFrame):
    def __init__(self, this):
        _swig_setattr(self, CommentsFrame, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, CommentsFrame, 'thisown', 0)
        _swig_setattr(self, CommentsFrame,self.__class__,CommentsFrame)
_TagLib.CommentsFrame_swigregister(CommentsFramePtr)

CommentsFrame_fromFrame = _TagLib.CommentsFrame_fromFrame

oldCommentsFrameInit = CommentsFrame.__init__
def newCommentsFrameInit(*args):
    self = args[0]
    if len(args) > 1 and isinstance(args[1], Frame):
        frame = args[1]
        if frame.frameID() != "COMM":
            raise TypeError("this frame type is not a CommentsFrame: " + str(frame.frameID()))
        _swig_setattr(self, CommentsFrame, 'this', self.fromFrame(frame))
        _swig_setattr(self, CommentsFrame, 'thisown', 0)
    else:
        oldCommentsFrameInit(*args)
CommentsFrame.__init__ = newCommentsFrameInit

class AttachedPictureFrame(Frame):
    __swig_setmethods__ = {}
    for _s in [Frame]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, AttachedPictureFrame, name, value)
    __swig_getmethods__ = {}
    for _s in [Frame]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, AttachedPictureFrame, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ TagLib::ID3v2::AttachedPictureFrame instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    Other = _TagLib.AttachedPictureFrame_Other
    FileIcon = _TagLib.AttachedPictureFrame_FileIcon
    OtherFileIcon = _TagLib.AttachedPictureFrame_OtherFileIcon
    FrontCover = _TagLib.AttachedPictureFrame_FrontCover
    BackCover = _TagLib.AttachedPictureFrame_BackCover
    LeafletPage = _TagLib.AttachedPictureFrame_LeafletPage
    Media = _TagLib.AttachedPictureFrame_Media
    LeadArtist = _TagLib.AttachedPictureFrame_LeadArtist
    Artist = _TagLib.AttachedPictureFrame_Artist
    Conductor = _TagLib.AttachedPictureFrame_Conductor
    Band = _TagLib.AttachedPictureFrame_Band
    Composer = _TagLib.AttachedPictureFrame_Composer
    Lyricist = _TagLib.AttachedPictureFrame_Lyricist
    RecordingLocation = _TagLib.AttachedPictureFrame_RecordingLocation
    DuringRecording = _TagLib.AttachedPictureFrame_DuringRecording
    DuringPerformance = _TagLib.AttachedPictureFrame_DuringPerformance
    MovieScreenCapture = _TagLib.AttachedPictureFrame_MovieScreenCapture
    ColouredFish = _TagLib.AttachedPictureFrame_ColouredFish
    Illustration = _TagLib.AttachedPictureFrame_Illustration
    BandLogo = _TagLib.AttachedPictureFrame_BandLogo
    PublisherLogo = _TagLib.AttachedPictureFrame_PublisherLogo
    def __init__(self, *args):
        _swig_setattr(self, AttachedPictureFrame, 'this', _TagLib.new_AttachedPictureFrame(*args))
        _swig_setattr(self, AttachedPictureFrame, 'thisown', 1)
    def __del__(self, destroy=_TagLib.delete_AttachedPictureFrame):
        try:
            if self.thisown: destroy(self)
        except: pass

    def toString(*args): return _TagLib.AttachedPictureFrame_toString(*args)
    def textEncoding(*args): return _TagLib.AttachedPictureFrame_textEncoding(*args)
    def setTextEncoding(*args): return _TagLib.AttachedPictureFrame_setTextEncoding(*args)
    def mimeType(*args): return _TagLib.AttachedPictureFrame_mimeType(*args)
    def setMimeType(*args): return _TagLib.AttachedPictureFrame_setMimeType(*args)
    def type(*args): return _TagLib.AttachedPictureFrame_type(*args)
    def setType(*args): return _TagLib.AttachedPictureFrame_setType(*args)
    def picture(*args): return _TagLib.AttachedPictureFrame_picture(*args)
    def setPicture(*args): return _TagLib.AttachedPictureFrame_setPicture(*args)
    __swig_getmethods__["fromFrame"] = lambda x: _TagLib.AttachedPictureFrame_fromFrame
    if _newclass:fromFrame = staticmethod(_TagLib.AttachedPictureFrame_fromFrame)

class AttachedPictureFramePtr(AttachedPictureFrame):
    def __init__(self, this):
        _swig_setattr(self, AttachedPictureFrame, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, AttachedPictureFrame, 'thisown', 0)
        _swig_setattr(self, AttachedPictureFrame,self.__class__,AttachedPictureFrame)
_TagLib.AttachedPictureFrame_swigregister(AttachedPictureFramePtr)

AttachedPictureFrame_fromFrame = _TagLib.AttachedPictureFrame_fromFrame

oldAttachedPictureFrameInit = AttachedPictureFrame.__init__
def newAttachedPictureFrameInit(*args):
    self = args[0]
    if len(args) > 1 and isinstance(args[1], Frame):
        frame = args[1]
        if frame.frameID() != "APIC":
            raise TypeError("this frame type is not an AttachedPictureFrame: " + str(frame.frameID()))
        _swig_setattr(self, AttachedPictureFrame, 'this', self.fromFrame(frame))
        _swig_setattr(self, AttachedPictureFrame, 'thisown', 0)
    else:
        oldAttachedPictureFrameInit(*args)
AttachedPictureFrame.__init__ = newAttachedPictureFrameInit

class StringHandler(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringHandler, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringHandler, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ TagLib::ID3v1::StringHandler instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def parse(*args): return _TagLib.StringHandler_parse(*args)
    def render(*args): return _TagLib.StringHandler_render(*args)
    def __init__(self, *args):
        _swig_setattr(self, StringHandler, 'this', _TagLib.new_StringHandler(*args))
        _swig_setattr(self, StringHandler, 'thisown', 1)
    def __del__(self, destroy=_TagLib.delete_StringHandler):
        try:
            if self.thisown: destroy(self)
        except: pass


class StringHandlerPtr(StringHandler):
    def __init__(self, this):
        _swig_setattr(self, StringHandler, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, StringHandler, 'thisown', 0)
        _swig_setattr(self, StringHandler,self.__class__,StringHandler)
_TagLib.StringHandler_swigregister(StringHandlerPtr)

class ID3v1Tag(Tag):
    __swig_setmethods__ = {}
    for _s in [Tag]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, ID3v1Tag, name, value)
    __swig_getmethods__ = {}
    for _s in [Tag]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, ID3v1Tag, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ TagLib::ID3v1::Tag instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, ID3v1Tag, 'this', _TagLib.new_ID3v1Tag(*args))
        _swig_setattr(self, ID3v1Tag, 'thisown', 1)
    def __del__(self, destroy=_TagLib.delete_ID3v1Tag):
        try:
            if self.thisown: destroy(self)
        except: pass

    def render(*args): return _TagLib.ID3v1Tag_render(*args)
    __swig_getmethods__["fileIdentifier"] = lambda x: _TagLib.ID3v1Tag_fileIdentifier
    if _newclass:fileIdentifier = staticmethod(_TagLib.ID3v1Tag_fileIdentifier)
    def title(*args): return _TagLib.ID3v1Tag_title(*args)
    def artist(*args): return _TagLib.ID3v1Tag_artist(*args)
    def album(*args): return _TagLib.ID3v1Tag_album(*args)
    def comment(*args): return _TagLib.ID3v1Tag_comment(*args)
    def genre(*args): return _TagLib.ID3v1Tag_genre(*args)
    def year(*args): return _TagLib.ID3v1Tag_year(*args)
    def track(*args): return _TagLib.ID3v1Tag_track(*args)
    def setTitle(*args): return _TagLib.ID3v1Tag_setTitle(*args)
    def setArtist(*args): return _TagLib.ID3v1Tag_setArtist(*args)
    def setAlbum(*args): return _TagLib.ID3v1Tag_setAlbum(*args)
    def setComment(*args): return _TagLib.ID3v1Tag_setComment(*args)
    def setGenre(*args): return _TagLib.ID3v1Tag_setGenre(*args)
    def setYear(*args): return _TagLib.ID3v1Tag_setYear(*args)
    def setTrack(*args): return _TagLib.ID3v1Tag_setTrack(*args)
    __swig_getmethods__["setStringHandler"] = lambda x: _TagLib.ID3v1Tag_setStringHandler
    if _newclass:setStringHandler = staticmethod(_TagLib.ID3v1Tag_setStringHandler)

class ID3v1TagPtr(ID3v1Tag):
    def __init__(self, this):
        _swig_setattr(self, ID3v1Tag, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, ID3v1Tag, 'thisown', 0)
        _swig_setattr(self, ID3v1Tag,self.__class__,ID3v1Tag)
_TagLib.ID3v1Tag_swigregister(ID3v1TagPtr)

ID3v1Tag_fileIdentifier = _TagLib.ID3v1Tag_fileIdentifier

ID3v1Tag_setStringHandler = _TagLib.ID3v1Tag_setStringHandler

class OggFile(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OggFile, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OggFile, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C++ TagLib::Ogg::File instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __del__(self, destroy=_TagLib.delete_OggFile):
        try:
            if self.thisown: destroy(self)
        except: pass

    def packet(*args): return _TagLib.OggFile_packet(*args)
    def setPacket(*args): return _TagLib.OggFile_setPacket(*args)
    def firstPageHeader(*args): return _TagLib.OggFile_firstPageHeader(*args)
    def lastPageHeader(*args): return _TagLib.OggFile_lastPageHeader(*args)
    def save(*args): return _TagLib.OggFile_save(*args)

class OggFilePtr(OggFile):
    def __init__(self, this):
        _swig_setattr(self, OggFile, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, OggFile, 'thisown', 0)
        _swig_setattr(self, OggFile,self.__class__,OggFile)
_TagLib.OggFile_swigregister(OggFilePtr)

class VorbisFile(OggFile):
    __swig_setmethods__ = {}
    for _s in [OggFile]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, VorbisFile, name, value)
    __swig_getmethods__ = {}
    for _s in [OggFile]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, VorbisFile, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ TagLib::Vorbis::File instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, VorbisFile, 'this', _TagLib.new_VorbisFile(*args))
        _swig_setattr(self, VorbisFile, 'thisown', 1)
    def __del__(self, destroy=_TagLib.delete_VorbisFile):
        try:
            if self.thisown: destroy(self)
        except: pass

    def tag(*args): return _TagLib.VorbisFile_tag(*args)
    def audioProperties(*args): return _TagLib.VorbisFile_audioProperties(*args)
    def save(*args): return _TagLib.VorbisFile_save(*args)

class VorbisFilePtr(VorbisFile):
    def __init__(self, this):
        _swig_setattr(self, VorbisFile, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, VorbisFile, 'thisown', 0)
        _swig_setattr(self, VorbisFile,self.__class__,VorbisFile)
_TagLib.VorbisFile_swigregister(VorbisFilePtr)

class XiphComment(Tag):
    __swig_setmethods__ = {}
    for _s in [Tag]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, XiphComment, name, value)
    __swig_getmethods__ = {}
    for _s in [Tag]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, XiphComment, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ TagLib::Ogg::XiphComment instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, XiphComment, 'this', _TagLib.new_XiphComment(*args))
        _swig_setattr(self, XiphComment, 'thisown', 1)
    def __del__(self, destroy=_TagLib.delete_XiphComment):
        try:
            if self.thisown: destroy(self)
        except: pass

    def title(*args): return _TagLib.XiphComment_title(*args)
    def artist(*args): return _TagLib.XiphComment_artist(*args)
    def album(*args): return _TagLib.XiphComment_album(*args)
    def comment(*args): return _TagLib.XiphComment_comment(*args)
    def genre(*args): return _TagLib.XiphComment_genre(*args)
    def year(*args): return _TagLib.XiphComment_year(*args)
    def track(*args): return _TagLib.XiphComment_track(*args)
    def setTitle(*args): return _TagLib.XiphComment_setTitle(*args)
    def setArtist(*args): return _TagLib.XiphComment_setArtist(*args)
    def setAlbum(*args): return _TagLib.XiphComment_setAlbum(*args)
    def setComment(*args): return _TagLib.XiphComment_setComment(*args)
    def setGenre(*args): return _TagLib.XiphComment_setGenre(*args)
    def setYear(*args): return _TagLib.XiphComment_setYear(*args)
    def setTrack(*args): return _TagLib.XiphComment_setTrack(*args)
    def isEmpty(*args): return _TagLib.XiphComment_isEmpty(*args)
    def fieldCount(*args): return _TagLib.XiphComment_fieldCount(*args)
    def fieldListMap(*args): return _TagLib.XiphComment_fieldListMap(*args)
    def vendorID(*args): return _TagLib.XiphComment_vendorID(*args)
    def addField(*args): return _TagLib.XiphComment_addField(*args)
    def removeField(*args): return _TagLib.XiphComment_removeField(*args)
    def render(*args): return _TagLib.XiphComment_render(*args)

class XiphCommentPtr(XiphComment):
    def __init__(self, this):
        _swig_setattr(self, XiphComment, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, XiphComment, 'thisown', 0)
        _swig_setattr(self, XiphComment,self.__class__,XiphComment)
_TagLib.XiphComment_swigregister(XiphCommentPtr)

class pyfieldlistmap(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pyfieldlistmap, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pyfieldlistmap, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ TagLib::Map<TagLib::String,TagLib::StringList > instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, pyfieldlistmap, 'this', _TagLib.new_pyfieldlistmap(*args))
        _swig_setattr(self, pyfieldlistmap, 'thisown', 1)
    def __del__(self, destroy=_TagLib.delete_pyfieldlistmap):
        try:
            if self.thisown: destroy(self)
        except: pass

    def begin(*args): return _TagLib.pyfieldlistmap_begin(*args)
    def end(*args): return _TagLib.pyfieldlistmap_end(*args)
    def insert(*args): return _TagLib.pyfieldlistmap_insert(*args)
    def clear(*args): return _TagLib.pyfieldlistmap_clear(*args)
    def size(*args): return _TagLib.pyfieldlistmap_size(*args)
    def isEmpty(*args): return _TagLib.pyfieldlistmap_isEmpty(*args)
    def find(*args): return _TagLib.pyfieldlistmap_find(*args)
    def contains(*args): return _TagLib.pyfieldlistmap_contains(*args)
    def erase(*args): return _TagLib.pyfieldlistmap_erase(*args)
    def __nonzero__(*args): return _TagLib.pyfieldlistmap___nonzero__(*args)
    def __getitem__(*args): return _TagLib.pyfieldlistmap___getitem__(*args)
    def __setitem__(*args): return _TagLib.pyfieldlistmap___setitem__(*args)
    def __delitem__(*args): return _TagLib.pyfieldlistmap___delitem__(*args)
    def has_key(*args): return _TagLib.pyfieldlistmap_has_key(*args)
    def keys(*args): return _TagLib.pyfieldlistmap_keys(*args)
    def values(*args): return _TagLib.pyfieldlistmap_values(*args)
    def items(*args): return _TagLib.pyfieldlistmap_items(*args)
    def __contains__(*args): return _TagLib.pyfieldlistmap___contains__(*args)
    def __iter__(*args): return _TagLib.pyfieldlistmap___iter__(*args)
    def __setitem__(a,b,c):
        """ This is not supported, use addFrame and/or removeFrame """
        raise AttributeError
    def __deltem__(a,b,c):
        """ This is not supported, use addFrame and/or removeFrame """
        raise AttributeError


class pyfieldlistmapPtr(pyfieldlistmap):
    def __init__(self, this):
        _swig_setattr(self, pyfieldlistmap, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, pyfieldlistmap, 'thisown', 0)
        _swig_setattr(self, pyfieldlistmap,self.__class__,pyfieldlistmap)
_TagLib.pyfieldlistmap_swigregister(pyfieldlistmapPtr)

class FlacFile(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FlacFile, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FlacFile, name)
    def __repr__(self):
        return "<%s.%s; proxy of C++ TagLib::FLAC::File instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def __init__(self, *args):
        _swig_setattr(self, FlacFile, 'this', _TagLib.new_FlacFile(*args))
        _swig_setattr(self, FlacFile, 'thisown', 1)
    def __del__(self, destroy=_TagLib.delete_FlacFile):
        try:
            if self.thisown: destroy(self)
        except: pass

    def tag(*args): return _TagLib.FlacFile_tag(*args)
    def audioProperties(*args): return _TagLib.FlacFile_audioProperties(*args)
    def save(*args): return _TagLib.FlacFile_save(*args)
    def ID3v2Tag(*args): return _TagLib.FlacFile_ID3v2Tag(*args)
    def ID3v1Tag(*args): return _TagLib.FlacFile_ID3v1Tag(*args)
    def xiphComment(*args): return _TagLib.FlacFile_xiphComment(*args)
    def setID3v2FrameFactory(*args): return _TagLib.FlacFile_setID3v2FrameFactory(*args)
    def streamInfoData(*args): return _TagLib.FlacFile_streamInfoData(*args)
    def streamLength(*args): return _TagLib.FlacFile_streamLength(*args)

class FlacFilePtr(FlacFile):
    def __init__(self, this):
        _swig_setattr(self, FlacFile, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, FlacFile, 'thisown', 0)
        _swig_setattr(self, FlacFile,self.__class__,FlacFile)
_TagLib.FlacFile_swigregister(FlacFilePtr)


