#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double newtonsolve(double (*f)(), double (*fprime)(), double x0, double tol, int maxiters)
{
    /* Setup of basic parameters */
    double err = 10.0*tol;
    double xk = x0;
    int iters = 0;
	
    /* Looping through steps of Newton's method until tolerances are met or failure*/
    while(err>tol && iters<maxiters){
        double xk1 =xk - (f(xk)/fprime(xk));
        err = fabs(xk-xk1);
        xk = xk1;
        iters++;
    }

    return xk;
}