# BSsolve
**Function Name:** bssolve  
**Author:** Nathan Nelson  
**Language:** C  
**Description/Purpose:** This function approximates a root of a given function using the bisection and assumes bisection can find the root.   
**Input:** This function takes a function pointer `f`, the interval of interest defined by two floats `x_0` and `x_1`, and an error tolerance float `tol`  
**Output:** An estimate of a root of `f` in the form of a floating point value is the output. If the sequence does not meet tolerance within the iteration limit or a float error is encountered, the last produced estimate is returned. 
**Usage/Example:** All inputs are taken as arguments; if we want to store the found solution of function `f` in `x`:  
`double x = bssolve(f, 3.0, 4.0, .000001);`  

**Implementation/Code:** This is the function implementation in C:  
```
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double bssolve(double (*f)(), double x_0, double x_1, double tol) {
	double a = x_0;
	double b = x_1;
	int k = (int)(ceil(1.0 + (log10(tol) / log10(b - a)) / log10(2.0)));
	
	int iters = 0;
	while (iters < k) {
		double c = (a + b) / 2.0;
		if (f(c) == 0.0) { return c; }
		if (f(b) * f(c) < 0.0) {
			a = c;
		}
		else
		{
			printf("Gode?");
			b = c;
		}
		iters++;
	}
	return (a + b) / 2.0;
}
```
**Last Modified:** 10/6/22