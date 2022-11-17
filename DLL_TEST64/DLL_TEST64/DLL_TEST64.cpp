#include "pch.h" 
#include "DLL_TEST64.h"
#include "stdio.h"

void DLL_TEST1()
{
	MessageBox(NULL, TEXT("DLLåƒÇ—èoÇµê¨å˜ÅI"), TEXT("test"), MB_OK);
	Beep(523, 200);
}

double ADD(double a, double b)
{
	return a + b;
}

long long sum_c(long long n)
{
	long long i = 0;
	for (long long j = 1; j <= n; j++)
	{
		i = i + j;
	}
	return i;
}