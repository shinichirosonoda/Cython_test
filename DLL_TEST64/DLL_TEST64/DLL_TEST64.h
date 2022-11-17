#pragma once
#ifdef DLL_TEST64_EXPORTS
#define DLL_TEST64_API __declspec(dllexport)
#else
#define DLL_TEST64_API __declspec(dllimport)
#endif

extern "C" DLL_TEST64_API void DLL_TEST1();
extern "C" DLL_TEST64_API double ADD(double a, double b);
extern "C" DLL_TEST64_API long long sum_c(long long n);