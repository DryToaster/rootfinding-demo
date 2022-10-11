# hybridSecant
**Function Name:** hybridsecant   
**Author:** Nathan Nelson  
**Language:** Python  
**Description/Purpose:** This function finds roots of a given function using five iterations of bisection and remaining iterations by secant method.  
**Input:** This function takes a function `f`, float endpoints of an interval of interest `x_0` and `x_1`, an error tolerance float `tol`, a maximum integer number of iterations `maxiters`, and a boolean `verbose` representing whether verbose output should be displayed.  
**Output:** An estimate of a root of `f` in the form of a floating point value is the output. If the sequence does not meet tolerance within the iteration limit, the last estimation made is returned instead. If bisection cannot confirm a root between the provided endpoints of interest, `None` will be returned.  
**Usage/Example:** All inputs are taken as arguments; if we want to store the found solution of function `f`in `x`:  
`x = hybridsecant(f, -0.1, 0,1, .000001, 200, false)`  

**Implementation/Code:** This is the function implementation in Python:  
```
def hybridsecant(f, x_0, x_1, tol, maxiters, verbose):
    a = x_0
    b = x_1
    if  not isbsAble(f, a, b):
        return None
    k = 5
    if verbose:
        print("Estimating root of f(x) using bisection on interval (",a,",",b,")")
        print("| Iter: | Estimate: |  Error:  |")
        
    for i in range(1,k):
        if verbose:
            print("|","%5.0f" % (i-1), "|" , "%9.7f" % ((a+b)/2) , "|" , "%8.6f" % (a-b), "|")
        c = (a+b)/2
        if f(b)*f(c)<0:
            a=c
        else:
            b=c
            
    x = solvesecant(f, a, b, tol, maxiters, verbose)
    return x
```
**Last Modified:** 9/25/22