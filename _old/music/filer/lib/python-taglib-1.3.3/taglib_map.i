//
// SWIG typemaps for TagLib::Map
// based on std::map by
// Luigi Ballabio
// Jan. 2003
//
// Python implementation

%include std_common.i
%include exception.i
%include tmap.h
%include <tmap.tcc>
%module taglib_map
%{
#include <map>
#include <algorithm>
#include <stdexcept>
#include <tmap.h>
%}

%exception TagLib::Map::__getitem__ {
    try {
        $action
    } catch (std::out_of_range& e) {
        PyErr_SetString(PyExc_KeyError,const_cast<char*>(e.what()));
        SWIG_fail;
    }
}

%exception TagLib::Map::__delitem__  {
    try {
        $action
    } catch (std::out_of_range& e) {
        PyErr_SetString(PyExc_KeyError,const_cast<char*>(e.what()));
        SWIG_fail;
    }
}

%exception TagLib::Map::__iter__  {
    try {
        $action
    } catch (std::runtime_error& e) {
        PyErr_SetString(PyExc_RuntimeError,const_cast<char*>(e.what()));
        SWIG_fail;
    }
}

namespace TagLib {


    %typemap(in) Map<Key,T> (TagLib::Map<Key,T>* m) {
        if (PyDict_Check($input)) {
            $1 = TagLib::Map<Key,T >();
            PyObject* items = PyMapping_Items($input);
            unsigned int size = PyList_Size(items);
            for (unsigned int i=0; i<size; i++) {
                Key* k;
                T* x;
                PyObject* pair = PySequence_GetItem(items,i);
                PyObject* key = PySequence_GetItem(pair,0);
                PyObject* o = PySequence_GetItem(pair,1);
                if (SWIG_ConvertPtr(key,(void **) &k,
                            $descriptor(Key *),0) != -1 &&
                        SWIG_ConvertPtr(o,(void **) &x,
                            $descriptor(T *),0) != -1) {
                    (($1_type &)$1)[*k] = *x;
                    Py_DECREF(key);
                    Py_DECREF(o);
                    Py_DECREF(pair);
                } else {
                    Py_DECREF(key);
                    Py_DECREF(o);
                    Py_DECREF(pair);
                    Py_DECREF(items);
                    PyErr_SetString(PyExc_TypeError,
                            "Map<" #Key "," #T "> expected");
                    SWIG_fail;
                }
            }
            Py_DECREF(items);
        } else if (SWIG_ConvertPtr($input,(void **) &m,
                    $&1_descriptor,0) != -1) {
            $1 = *m;
        } else {
            PyErr_SetString(PyExc_TypeError,
                    "Map<" #Key "," #T "> expected");
            SWIG_fail;
        }
    }
    
    %rename(__len__) size;
    %extend Map{
        
        bool __nonzero__() {
            return !(self->isEmpty());
        }
        T& __getitem__(const Key& key) {
            TagLib::Map<Key,T >::Iterator i = self->find(key);
            if (i != self->end()) 
                return i->second;
            else
                throw std::out_of_range("key not found");
        }
        void __setitem__(const Key& key, const T& x) {
            (*self)[key] = x;
        }
        void __delitem__(const Key& key) {
            TagLib::Map<Key,T >::Iterator i = self->find(key);
            if (i != self->end())
                self->erase(i);
            else
                throw std::out_of_range("key not found");
        }
        bool has_key(const Key& key) {
            TagLib::Map<Key,T >::Iterator i = self->find(key);
            return i != self->end();
        }
        PyObject* keys() {
            PyObject* keyList = PyList_New(self->size());
            TagLib::Map<Key,T >::Iterator i;
            unsigned int j;
            for (i=self->begin(), j=0; i!=self->end(); ++i, ++j) {
                Key* ptr = new Key(i->first);
                PyList_SetItem(keyList,j,
                        SWIG_NewPointerObj((void *) ptr,
                            $descriptor(Key *),1));
            }
            return keyList;
        }
        PyObject* values() {
            PyObject* valueList = PyList_New(self->size());
            TagLib::Map<Key,T >::Iterator i;
            unsigned int j;
            for (i=self->begin(), j=0; i!=self->end(); ++i, ++j) {
                T* ptr = new T(i->second);
                PyList_SetItem(valueList,j,
                        SWIG_NewPointerObj((void *) ptr,
                            $descriptor(T *),1));
            }
            return valueList;
        }
        PyObject* items() {
            PyObject* itemList = PyList_New(self->size());
            TagLib::Map<Key,T >::Iterator i;
            unsigned int j;
            for (i=self->begin(), j=0; i!=self->end(); ++i, ++j) {
                Key* k_ptr = new Key(i->first);
                T* t_ptr = new T(i->second);
                PyObject* item = PyTuple_New(2);
                PyTuple_SetItem(item,0,
                        SWIG_NewPointerObj((void *) k_ptr,
                            $descriptor(Key *),1));
                PyTuple_SetItem(item,1,
                        SWIG_NewPointerObj((void *) t_ptr,
                            $descriptor(T *),1));
                PyList_SetItem(itemList,j,item);
            }
            return itemList;
        }
        // Python 2.2 methods
        bool __contains__(const Key& key) {
            TagLib::Map<Key,T >::Iterator i = self->find(key);
            return i != self->end();
        }
        PyObject* __iter__() {
            %#if PY_VERSION_HEX >= 0x02020000
                PyObject* keyList = PyList_New(self->size());
            TagLib::Map<Key,T >::Iterator i;
            unsigned int j;
            for (i=self->begin(), j=0; i!=self->end(); ++i, ++j) {
                Key* ptr = new Key(i->first);
                PyList_SetItem(keyList,j,
                        SWIG_NewPointerObj((void *) ptr,
                            $descriptor(Key *),1));
            }
            PyObject* iter = PyObject_GetIter(keyList);
            Py_DECREF(keyList);
            return iter;
            %#else
                throw std::runtime_error("Python 2.2 or later is needed"
                        " for Iterator support");
            %#endif
        }
        %pythoncode %{
            def __setitem__(a,b,c):
                """ This is not supported, use addFrame and/or removeFrame """
                raise AttributeError
            def __deltem__(a,b,c):
                """ This is not supported, use addFrame and/or removeFrame """
                raise AttributeError
        %}
    }
}
