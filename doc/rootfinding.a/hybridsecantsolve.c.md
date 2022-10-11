# hybridSecantSolve
**Function Name:** hybridsecantsolve   
**Author:** Nathan Nelson  
**Language:** C  
**Description/Purpose:** This function approximates a root of a given function using bisection and then Newton's method. Assumes root can be found by bisection on interval.  
**Input:** This function takes a function pointer `f`, the interval of interest as floats 'x_0' and `x_1`, an error tolerance float `tol`, and a maximum integer number of iterations `maxiters`  
**Output:** An estimate of a root of `f` in the form of a floating point value is the output. If the sequence does not meet tolerance within the iteration limit, the last estimation made is returned instead.  
**Usage/Example:** All inputs are taken as arguments; if we want to store the found solution of function `f`in `x`:  
`double x = hybridsecantsolve(f, 3.5, 4.5, .000001, 200);`  


**Implementation/Code:** This is the function implementation in C:  
```
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double hybridsecantsolve(double (*f)(), double x_0, double x_1, double tol, int maxiters)
{
	int k = 5;
	double a = x_0;
	double b = x_1;
	int iters = 0;

	while (iters < k) {
		double c = (a + b) / 2.0;
		if (f(c) == 0.0) { break; }
		if (f(b) * (f(c)) < 0.0) {
			a = c;
		}
		else {
			b = c;
		}
	}

	double err = 10.0 * tol;
	iters = 0;

	double xk = a;
	double xk1 = b;

	while (err > tol && iters < maxiters) {
		double xk2 = xk1 - f(xk1) * (xk1 - xk) / (f(xk1) - f(xk));
		err = fabs(xk1 - xk2);
		xk = xk1;
		xk1 = xk2;
		iters++;
	}

	return xk1;
}
```
**Last Modified:** 10/6/22