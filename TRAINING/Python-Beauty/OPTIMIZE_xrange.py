"""
Profiling: timeit module use to measure running time of a fun
Since the fun accepts arg, need to develop a wrapper @decorator and timeit on decorator
"""
import timeit


def doubles(n):
    """
    result = []
    for i in range(n):
        result.append(n*2)
    return result
    """
    """
    xrange better then range()
    xrange iterator [] format yields over each ele in list
    """
    return [i for i in xrange(n)]


def wrapper(fun, *args, **kwargs):
    def wrapped():
        return fun(*args, **kwargs)
    return wrapped


if __name__ == "__main__":
    n = 10*1000
    w = wrapper(doubles, n)
    print timeit.timeit(w, number=1000)
