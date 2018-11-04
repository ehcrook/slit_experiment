from libcpp.list cimport list

cdef extern from "buckets.h":
    list[list[float]] bucket(list[float] &, list[float] &)

def bucket_run(list[float] a, list[float] b):
    return bucket(a,b)