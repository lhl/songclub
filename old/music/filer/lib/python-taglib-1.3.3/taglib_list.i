//
// SWIG typemaps for TagLib::List types
// based on std_list.i by:
// Jing Cao
// Aug 1st, 2002
//
// Python implementation

%module taglib_list
%{
#include <list>
#include <stdexcept>
#include <tlist.h>
%}

%include "exception.i"

%include <tlist.h>

namespace TagLib {
    %exception List::__getitem__ {
        try {
            $action
        } catch (std::out_of_range& e) {
            PyErr_SetString(PyExc_IndexError, const_cast<char*>(e.what()));
            return NULL;
        }
    }

    %exception List::__setitem__ {
        try {
            $action
        } catch (std::out_of_range& e) {
            PyErr_SetString(PyExc_IndexError, const_cast<char*>(e.what()));
            return NULL;
        }
    }

    %exception List::__delitem__  {
        try {
            $action
        } catch (std::out_of_range& e) {
            PyErr_SetString(PyExc_IndexError, const_cast<char*>(e.what()));
            return NULL;
        }
    }

    %extend List
    {
        const T& __getitem__(int i) 
        {
            int size = int(self->size());
            if (i<0) i += size;
            if (i>=0 && i<size)
                return (*self)[i];
            else
                throw std::out_of_range("list index out of range");
        }

        void __setitem__(int i, const T& x) 
        {
            List<T>::Iterator first = self->begin(); 
            int size = int(self->size());
            if (i<0) i += size;
            if (i>=0 && i<size)
                (*self)[i] = x;
            else
                throw std::out_of_range("list index out of range");
        }

        void __delitem__(int i) 
        {
            List<T>::Iterator first = self->begin(); 
            int size = int(self->size());
            if (i<0) i += size;
            if (i>=0 && i<size)
            {
                for (int k=0;k<i;k++)
                {
                    first++;
                }
                self->erase(first);
            }
            else throw std::out_of_range("list index out of range");
        }	     
        List<T> __getslice__(int i,int j) 
        {
            List<T>::ConstIterator it = self->begin();

            int size = int(self->size());
            if (i<0) i += size;
            if (j<0) j += size;
            if (i<0) i = 0;
            if (j>size) j = size;
            if (i>=j) i=j;
            if (i>=0 && i<size && j>=0)
            {
                List<T> tmp;
                for (int k = 0; k < j && k < size; k++) {
                    if (k >= i) tmp.append((*it));
                    it++;
                }
                return tmp;
            }
            else throw std::out_of_range("list index out of range");
        }
        void __delslice__(int i,int j) 
        {
            List<T>::Iterator first = self->begin();
            List<T>::Iterator end = self->end();

            int size = int(self->size());
            if (i<0) i += size;
            if (j<0) j += size;
            if (i<0) i = 0;
            if (j>size) j = size;

            for (int k=0;k<i;k++)
            {
                first++;
            }
            for (int m=0;m<=j;m++)
            {
                end++;
            }
            //erase from first to end
            List<T>::Iterator it = first;
            List<T>::Iterator next = first;
            for (it = first; it != end; it = next) {
                next = it;       //it is valid
                next++;          //next is valid
                self->erase(it); //it is invalid
            }
        }
        void __setslice__(int i,int j, const List<T>& v) 
        {
            List<T>::Iterator first = self->begin();
            List<T>::Iterator end = self->end();

            int size = int(self->size());
            if (i<0) i += size;
            if (j<0) j += size;
            if (i<0) i = 0;
            if (j>size) j = size;

            for (int k=0;k<i;k++)
            {
                first++;
            }
            for (int m=0;m<=j;m++)
            {
                end++;
            }
            if (int(v.size()) == j-i) 
            {
                std::copy(v.begin(),v.end(),first);
            }
            else {
                //erase from first to end
                List<T>::Iterator it = first;
                List<T>::Iterator next = first;
                List<T>::ConstIterator vit;
                for (it = first; it != end; it = next) {
                    next = it;       //it is valid
                    next++;          //next is valid
                    self->erase(it); //it is invalid
                }
                if (i+1 <= int(self->size())) 
                {
                    first = self->begin();
                    for (int k=0;k<i;k++)
                    {
                        first++;
                    }
                    for (vit = v.begin(); vit != v.end(); vit++) {
                        self->insert(first, *vit);
                    }
                    //self->insert(first,v.begin(),v.end());
                }
                else {
                    for (vit = v.begin(); vit != v.end(); vit++) {
                        self->insert(self->end(), *vit);
                    }
                    //self->insert(self->end(),v.begin(),v.end());
                }
            }

        }
        unsigned int __len__() 
        {
            return self->size();
        }	
        bool __nonzero__()
        {
            return !(self->isEmpty());
        }
        %pythoncode %{
            def __setitem__(a,b,c):
                """ This is not supported, use addFrame and/or removeFrame """
                raise AttributeError
            def __delitem__(a,b,c):
                """ This is not supported, use addFrame and/or removeFrame """
                raise AttributeError
            def __setslice__(a,b,c):
                """ This is not supported, use addFrame and/or removeFrame """
                raise AttributeError
        %}
    };   
}
