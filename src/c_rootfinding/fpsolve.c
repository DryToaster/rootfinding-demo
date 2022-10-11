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