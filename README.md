# Cython Python Numpy C の性能比較  

```bash
python main.py  
```
を実行してください。  


```bash
n = 100000000  

cython  
Sigma(1 to n) = 5000000050000000  
         9 function calls in 0.032 seconds  

   Ordered by: internal time  
  
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)  
        1    0.031    0.031    0.031    0.031 {test_c.sum_cy}  
        2    0.001    0.000    0.001    0.000 {built-in method builtins.print}  
        1    0.000    0.000    0.032    0.032 {built-in method builtins.exec}  
        1    0.000    0.000    0.032    0.032 main.py:16(main)  
        1    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}  
        1    0.000    0.000    0.032    0.032 main.py:20(main_cy)  
        1    0.000    0.000    0.032    0.032 <string>:1(<module>)  
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}  


python  
Sigma(1 to n) = 5000000050000000  
         9 function calls in 4.871 seconds  

   Ordered by: internal time  

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)  
        1    4.871    4.871    4.871    4.871 test_py.py:2(sum_py)  
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}  
        1    0.000    0.000    4.871    4.871 {built-in method builtins.exec}  
        1    0.000    0.000    4.871    4.871 main.py:16(main)  
        1    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}  
        1    0.000    0.000    4.871    4.871 main.py:23(main_py)  
        1    0.000    0.000    4.871    4.871 <string>:1(<module>)  
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}  


numpy  
Sigma(1 to n) = 5000000050000000  
         19 function calls in 0.229 seconds  

   Ordered by: internal time  

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)  
        1    0.152    0.152    0.152    0.152 {built-in method numpy.arange}  
        1    0.050    0.050    0.050    0.050 {method 'reduce' of 'numpy.ufunc' objects}  
        1    0.027    0.027    0.229    0.229 test_np.py:4(sum_np)  
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}  
        1    0.000    0.000    0.229    0.229 {built-in method builtins.exec}  
        1    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}  
        1    0.000    0.000    0.229    0.229 main.py:16(main)  
        1    0.000    0.000    0.050    0.050 fromnumeric.py:70(_wrapreduction)  
        1    0.000    0.000    0.050    0.050 fromnumeric.py:2111(sum)  
        1    0.000    0.000    0.050    0.050 <__array_function__ internals>:2(sum)  
        1    0.000    0.000    0.050    0.050 {built-in method numpy.core._multiarray_umath.implement_array_function}  
        1    0.000    0.000    0.229    0.229 main.py:26(main_np)  
        1    0.000    0.000    0.229    0.229 <string>:1(<module>)  
        1    0.000    0.000    0.000    0.000 fromnumeric.py:71(<dictcomp>)  
        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}  
        1    0.000    0.000    0.000    0.000 fromnumeric.py:2106(_sum_dispatcher)  
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}  
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}  


ctypes  
Sigma(1 to n) = 5000000050000000  
         8 function calls in 0.033 seconds  

   Ordered by: internal time  

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)  
        1    0.032    0.032    0.033    0.033 main.py:16(main)  
        2    0.001    0.000    0.001    0.000 {built-in method builtins.print}  
        1    0.000    0.000    0.033    0.033 {built-in method builtins.exec}  
        1    0.000    0.000    0.033    0.033 main.py:29(main_dll)  
        1    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}  
        1    0.000    0.000    0.033    0.033 <string>:1(<module>)  
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects} 
        
```
        
