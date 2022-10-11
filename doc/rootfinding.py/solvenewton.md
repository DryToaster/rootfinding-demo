# solveNewton
**Function Name:** solvenewton   
**Author:** Nathan Nelson  
**Language:** Python  
**Description/Purpose:** This function finds roots of a given function using Newton's method.  
**Input:** This function takes a function `f`, the derivative function of `f`, `fprime`, an initial guess/estimate float 'x_0', an error tolerance float `tol`, a maximum integer number of iterations `maxiters`, and a boolean `verbose` representing whether verbose output should be displayed.  
**Output:** An estimate of a root of `f` in the form of a floating point value is the output. If the sequence does not meet tolerance within the iteration limit, the last estimation made is returned instead.  
**Usage/Example:** All inputs are taken as arguments; if we want to store the found solution of function `f`in `x`:  
`x = solvenewton(f, fprime, 4.0, .000001, 200, false)`  
If verbose output is enabled,  
`x = solvenewton(f, fprime, 4.0, .000001, 200, true)`  
a similar table to the following will be printed to console:  
```
Estimating root using Newton's method:
| Iter: | Estimate: |  Error:  |
|     0 | 0.1000000 | 0.090970 |
|     1 | 0.0090299 | 0.008949 |
|     2 | 0.0000808 | 0.000081 |
|     3 | 0.0000000 | 0.000000 |
```  
**Implementation/Code:** This is the function implementation in Python:  
```
def solvenewton(f, fprime, x0, tol, maxiters, verbose):

    err = 10*tol
    xk = x0
    iters = 0

    if verbose:
        print("Estimating root using Newton's method:")
        print("| Iter: | Estimate: |  Error:  |")
        
    while(err>tol and iters<maxiters):
        xk1 = xk - (f(xk)/fprime(xk))
        err = np.abs(xk-xk1)
        if verbose:
            print("|","%5.0f" % (iters), "|" , "%9.7f" % (xk) , "|" , "%8.6f" % (err), "|")
        
        xk = xk1
        iters = iters+1
    
    return xk
```
**Last Modified:** 9/24/22