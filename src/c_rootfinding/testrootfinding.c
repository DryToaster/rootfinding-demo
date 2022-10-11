#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "newtonsolve.c"
#include "secantsolve.c"
#include "fpsolve.c"
#include "bssolve.c"
#include "hybridnewtonsolve.c"
#include "hybridsecantsolve.c"

double f(double x){return (exp(-1*x)*x);}
double fprime(double x){return (1-x)/exp(-1*x);}

int main()
{
    double (*y)(double);
    y=f;
    double (*dy)(double);
    dy=fprime;

    printf("Newton\'s method:\n");
    double soln = newtonsolve(y, dy, 0.1, 0.00001, 200);
    printf("%f\n", soln);
    
    printf("Secant method:\n");
    soln = secantsolve(y, 0.1, 0.2, 0.00001, 200);
    printf("%f\n", soln);

    printf("Fixed point method:\n");
    soln = fpsolve(y, 0.1, .000001, 200);
    printf("%f\n", soln);

    printf("Bisection method:\n");
    soln = bssolve(y, -0.1, 0.1, .00001);
    printf("%f\n", soln);

    printf("Hybrid Newton's method:\n");
    soln = hybridnewtonsolve(y, dy, -1.0, 1.0, .00001, 200);
    printf("%f\n", soln);

    printf("Hybrid secant method:\n");
    soln = hybridsecantsolve(y, -1.0, 1.0, .00001, 200);
    printf("%f\n", soln);
    
    
}