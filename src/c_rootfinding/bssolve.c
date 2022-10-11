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