%module TagLib
%{
#include "audioproperties.h"
#include "tag.h"
#include "fileref.h" 
using namespace TagLib;
%}
%include typemaps.i
%include wchar.i

// Yeah, kill those ugly warnings!
#pragma SWIG nowarn=362,389,402,503,509

namespace TagLib {

    %typemap(typecheck) String = char *;
    %typemap(typecheck) const String & = char *;

    namespace ID3v2 {
        /*
            Assume that Frame** is a pointer to a single Frame*.
            This is okay as long as no functions in TagLib return arrays of Frame*.
            These are intended to match TagLib::List functions.
        */
        %typemap(out) Frame*& {
            Frame* retfrm =  (*$1);
            $result = SWIG_NewPointerObj((void *) retfrm, $descriptor(TagLib::ID3v2::Frame*), 0);
        }
        %typemap(in) Frame*& (Frame* tmp) {
            if ((SWIG_ConvertPtr(
                $input,(void **) &tmp, 
                $descriptor(TagLib::ID3v2::Frame*),
                SWIG_POINTER_EXCEPTION | 0 )) == -1) SWIG_fail;
            $1 = &tmp;
        }
    }
    
    %typemap(out) String {
        $result = PyString_FromString($1.toCString());
    }

    %typemap(in) String & (String temp){
        if (PyString_Check($input)) {
            temp = String(PyString_AsString($input));
            $1 = &temp;
        } else
            SWIG_exception(SWIG_TypeError, "string expected");
    }

    %extend ByteVector {
        PyObject* __repr__() {
            unsigned int len = self->size();
            const char* cstr = self->data();
            return PyString_FromStringAndSize(cstr, len);
        }
    }

    // This is required to check for string (default is checking for ByteVector)
    %typemap(typecheck) (const ByteVector &type, String::Type encoding) {
        $1 = PyString_Check($input) ? 1 : 0;
    }

    %typemap(in) const ByteVector & {
        if (PyString_Check($input)) {
            const char* cstr = PyString_AsString($input);
            unsigned int len = PyString_GET_SIZE($input);
            $1 = new ByteVector(cstr, len);
        } else
            SWIG_exception(SWIG_TypeError, "string expected");
    }

    %typemap(freearg) const ByteVector & {
        if ($1) {
            delete $1;
        }
    }
    
    %extend ID3v2::Frame {
        PyObject* __str__() {
            return PyString_FromString(self->toString().toCString());
        }
        PyObject* __repr__() {
            return PyString_FromString(self->toString().toCString());
        }
    }

    %extend String {
        PyObject* __str__() {
            return PyString_FromStringAndSize(self->toCString(), self->size());
        }
    }
}
// C++ STL wrappers
//%include std_string.i
//%include std_vector.i
//%include std_list.i

// TagLib template wrappers
%include taglib_list.i
%include taglib_map.i

// Get rid of warnings on non-wrappable C++ stuff
//%ignore operator=(
%ignore &operator<<(std::ostream &s, const TagLib::ByteVector &v);

%include taglib.h
%include audioproperties.h
%include fileref.h
%include tbytevector.h
%include tstring.h
%include tag.h

// === StringList ===
namespace TagLib {
    %template(pystringlist) List<String>;
}
%include "tstringlist.h"


%ignore Properties;
%rename ( MPEGFile ) File;
%{
#include "mpegfile.h"
%}
%include mpegproperties.h
%include mpegfile.h

%{
using namespace ID3v2;
%}

// === ID3v2::Frame ===
%{
#include "id3v2frame.h"
%}
%ignore Frame::Header;
%include "id3v2frame.h"

// === ID3v2::Tag ===
%feature("shadow") TagLib::ID3v2::Tag::addFrame (Frame* frame) %{
def addFrame(*args):
    if len(args) > 1:
        self,frame = args[0],args[1]
        if isinstance(frame, Frame):
            # Tag destructor will destroy C++ frame object for us later
            # tell Python Frame class not to destroy it
            frame.thisown = 0 
    return _TagLib.ID3v2Tag_addFrame(*args)
%}
%feature("shadow") TagLib::ID3v2::Tag::removeFrame %{
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
        
%}
%{
#include "id3v2tag.h"
%}
%rename( ID3v2Tag ) Tag;
%include "id3v2tag.h"
namespace TagLib {
    %template(pyframelist) List<ID3v2::Frame*>;
    %template(pyframelistmap) Map<ByteVector, ID3v2::FrameList>;
}

// === ID3v2::TextIdentificationFrame ===
%{
#include "textidentificationframe.h"
%}
%ignore find(Tag *tag, const String &description);
%include "textidentificationframe.h"
namespace TagLib {
    namespace ID3v2 {
        %extend TextIdentificationFrame {
            static TextIdentificationFrame* fromFrame(Frame* frame) {
                return dynamic_cast<TextIdentificationFrame*> (frame);
            }
        }
    }
}
%pythoncode {
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
}

// === ID3v2::CommentsFrame ===
%{
#include "commentsframe.h"
%}
%include "commentsframe.h"
namespace TagLib {
    namespace ID3v2 {
        %extend CommentsFrame {
            static CommentsFrame* fromFrame(Frame* frame) {
                return dynamic_cast<CommentsFrame*> (frame);
            }
        }
    }
}
%pythoncode {
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
}


// === ID3v2::AttachedPictureFrame ===
%{
#include "attachedpictureframe.h"
%}
%include "attachedpictureframe.h"
namespace TagLib {
    namespace ID3v2 {
        %extend AttachedPictureFrame {
            static AttachedPictureFrame* fromFrame(Frame* frame) {
                return dynamic_cast<AttachedPictureFrame*> (frame);
            }
        }
    }
}
%pythoncode {
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
}


// === ID3v1::Tag ===
%rename( ID3v1Tag ) Tag;
%{
#include "id3v1tag.h"
%}
%include "id3v1tag.h"

// === Ogg::File ===
%rename ( OggFile ) File;
%{
#include "oggfile.h"
%}
%include "oggfile.h"

// === Vorbis::File and Vorbis::Ogg::Vorbis::Properties ===
%rename ( VorbisFile ) File;
%{
#include "vorbisfile.h"
%}
%include "vorbisproperties.h"
%include "vorbisfile.h"

// === Ogg::XiphComment ===
%include "xiphcomment.h"
namespace TagLib {
    %template(pyfieldlistmap) Map<String, StringList>;
}

// === Flac::File and Flac::File::Properties
%rename ( FlacFile ) File;
%{
#include "flacfile.h"
%}
%include "flacproperties.h"
%include "flacfile.h"
