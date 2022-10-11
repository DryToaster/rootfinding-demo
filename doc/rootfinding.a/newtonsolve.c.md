# newtonSolve
**Function Name:** newtonsolve   
**Author:** Nathan Nelson  
**Language:** C  
**Description/Purpose:** This function approximates a root of a given function using Newton's method.  
**Input:** This function takes a function pointer `f`, the derivative function pointer of `f`, `fprime`, an initial guess/estimate float 'x_0', an error tolerance float `tol`, and a maximum integer number of iterations `maxiters`  
**Output:** An estimate of a root of `f` in the form of a floating point value is the output. If the sequence does not meet tolerance within the iteration limit, the last estimation made is returned instead.  
**Usage/Example:** All inputs are taken as arguments; if we want to store the found solution of function `f`in `x`:  
`double x = newtonsolve(f, fprime, 4.0, .000001, 200);`  


**Implementation/Code:** This is the function implementation in C:  
```
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
```
**Last Modified:** 10/6/22