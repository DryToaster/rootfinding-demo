#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double hybridnewtonsolve(double (*f)(), double (*fprime)(), double x_0, double x_1, double tol, int maxiters)
{
    int k = 5;
    int a = x_0;
    int b = x_1;
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

    double err = 10.0*tol;
    double x_k = (a+b)/2.0;
    iters = 0;
	
    while(err>tol && iters<maxiters){
        double x_k1 =x_k - (f(x_k)/fprime(x_k));
        err = fabs(x_k-x_k1);
        x_k = x_k1;
        iters++;
    }

    return x_k;
}