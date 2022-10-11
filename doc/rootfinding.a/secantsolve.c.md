# secantSolve
**Function Name:** secantsolve   
**Author:** Nathan Nelson  
**Language:** C  
**Description/Purpose:** This function approximates a root of a given function using the secant method.  
**Input:** This function takes a function pointer `f`, two initial guess/estimate floats 'x_0' and `x_1`, an error tolerance float `tol`, and a maximum integer number of iterations `maxiters`  
**Output:** An estimate of a root of `f` in the form of a floating point value is the output. If the sequence does not meet tolerance within the iteration limit, the last estimation made is returned instead.  
**Usage/Example:** All inputs are taken as arguments; if we want to store the found solution of function `f`in `x`:  
`double x = secantsolve(f, 3.5, 4.5, .000001, 200);`  


**Implementation/Code:** This is the function implementation in C:  
```
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double secantsolve(double (*f)(), double a, double b, double tol, int maxiters)
{
	/* Setup of basic parameters */
	double err = 10*tol;
	double xk = a;
	double xk1 = b;
	int iters = 0;

	/* Looping through secant method until tolerances are met or failure */
	while(err>tol && iters<maxiters){
		double xk2 = xk1-f(xk1)*(xk1-xk)/(f(xk1)-f(xk));
		err = fabs(xk1-xk2);
		xk = xk1;
		xk1 = xk2;
		iters++;
	}
	
	return xk1;
}
```
**Last Modified:** 10/6/22