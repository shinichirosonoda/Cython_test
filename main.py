import pyximport; pyximport.install()

from test_c import sum_cy
from test_py import sum_py
from test_np import sum_np

from ctypes import *

dll = WinDLL("./DLL_TEST64/x64/Release/DLL_TEST64.dll")
dll.sum_c.restype = c_longlong

n = 100000000
print("n = {}".format(n))
print("")


def main_cy():
    print("cython")
    print("Sigma(1 to n) = {}".format(sum_cy(n)))

def main_py():
    print("python")
    print("Sigma(1 to n) = {}".format(sum_py(n)))

def main_np():
    print("numpy")
    print("Sigma(1 to n) = {}".format(sum_np(n)))

def main_dll():
    print("ctypes")
    print("Sigma(1 to n) = {}".format(dll.sum_c(n)))


if __name__ == '__main__':
    import cProfile

    cProfile.run('main_cy()', sort='time')
    cProfile.run('main_py()', sort='time')
    cProfile.run('main_np()', sort='time')
    cProfile.run('main_dll()', sort='time')