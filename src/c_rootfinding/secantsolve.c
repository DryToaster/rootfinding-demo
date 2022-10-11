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