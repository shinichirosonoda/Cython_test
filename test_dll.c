// C 
#include <stdio.h>
long long sum_c(long long n)
{
	long long i = 0;
	for (long long j = 1; j <= n; j++)
	{
		i = i + j;
	}
	return i;
}