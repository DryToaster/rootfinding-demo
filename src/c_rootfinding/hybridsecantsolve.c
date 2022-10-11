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