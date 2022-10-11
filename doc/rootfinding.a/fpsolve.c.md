# FPsolve
**Function Name:** fpsolve  
**Author:** Nathan Nelson  
**Language:** C  
**Description/Purpose:** This function approximates a root of a given function using the fixed-point method. It will automatically use up to 3 different g(x) functions if the first or second fail to converge.  
**Input:** This function takes a function pointer `f`, an initial guess/estimate float 'x_0', an error tolerance float `tol`, and a maximum integer number of iterations `maxiters`  
**Output:** An estimate of a root of `f` in the form of a floating point value is the output. If the sequence does not meet tolerance within the iteration limit or a float error is encountered, the last produced estimate is returned. 
**Usage/Example:** All inputs are taken as arguments; if we want to store the found solution of function `f` in `x`:  
`double x = fpsolve(f, 4.0, .00001, 200);`

**Implementation/Code:** This is the function implementation in C:  
```
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double g1(double x, double(*f)()){return (x-0.1*f(x));}
double g2(double x, double(*f)()){return (x+0.1*f(x));}
double g3(double x, double(*f)()){return (x-.00001*f(x));}

double fpsolve(double (*f)(), double x_0, double tol, int maxiters) {

	int iters = 0;
	double err = 10 * tol;
	double x_k = x_0;

	while (err > tol && iters < maxiters) {
		double x_k1 = g1(x_k, f);
		err = fabs(x_k - x_k1);
		iters++;
		x_k = x_k1;
	}
	if (err <= tol) { return x_k; }

	iters = 0;
	err = 10 * tol;
	x_k = x_0;
	printf("G2");

	while (err > tol && iters < maxiters) {
		double x_k1 = g2(x_k, f);
		err = fabs(x_k - x_k1);
		iters++;
		x_k = x_k1;
	}
	if (err <= tol) { return x_k; }

	iters = 0;
	err = 10 * tol;
	x_k = x_0;
	printf("G3");

	while (err > tol && iters < maxiters) {
		double x_k1 = g3(x_k, f);
		err = fabs(x_k - x_k1);
		iters++;
		x_k = x_k1;
	}
	if (err <= tol) { return x_k; }

	return x_k; 
}
```
**Last Modified:** 10/6/22