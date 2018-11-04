from libcpp.list cimport list

cdef extern from "buckets.h":
    void bucket(list[float] &, list[float] &)

def bucket_test(list[float] a, list[float] b):
    bucket(a,b)