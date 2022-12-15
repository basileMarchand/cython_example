from libcpp.vector cimport vector
cimport numpy as np 

cdef extern from "cpp_sort.h":
    void cpp_sort(vector[double]&)


cpdef cppSorter(vector[double]& v):
    cpp_sort(v)
    return v

