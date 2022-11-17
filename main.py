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

def main(text, f):
    print(text)
    print("Sigma(1 to n) = {}".format(f(n)))

def main_cy():
    main("cython", sum_cy)

def main_py():
    main("python", sum_py)

def main_np():
    main("numpy", sum_np)

def main_dll():
    main("ctypes", dll.sum_c)

if __name__ == '__main__':
    import cProfile

    cProfile.run('main_cy()', sort='time')
    cProfile.run('main_py()', sort='time')
    cProfile.run('main_np()', sort='time')
    cProfile.run('main_dll()', sort='time')