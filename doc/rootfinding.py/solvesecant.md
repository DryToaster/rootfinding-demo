# solveSecant
**Function Name:** solvesecant  
**Author:** Nathan Nelson  
**Language:** Python  
**Description/Purpose:** This function finds roots of a given function using the secant method.  
**Input:** This function takes a function `f`, two floats representing starting points for the algorithm `a` and `b`, an error tolerance float `tol`, a maximum integer number of iterations `maxiters`, and a boolean `verbose` representing whether verbose output should be displayed.  
**Output:** An estimate of a root of `f` in the form of a floating point value is the output. If the sequence does not meet tolerance within the iteration limit, the last estimation made is returned instead.  
**Usage/Example:** All inputs are taken as arguments; if we want to store the found solution of function `f`in `x`:  
`x = solvesecant(f, 3.9, 4.1, .000001, 200, false)`  
If verbose output is enabled,  
`x = folvefp(f, 3.9, 4.1, .000001, 200, true)`  
a table similar to the following will be printed to console:  
```
Estimating root using secant method:
| Iter: | Estimate: |  Error:  |
|     0 | 0.1000000 | 0.090970 |
|     1 | 0.0090299 | 0.008949 |
|     2 | 0.0000808 | 0.000081 |
|     3 | 0.0000000 | 0.000000 |
```  
**Implementation/Code:** This is the function implementation in Python:  
```
def solvesecant(f, a, b, tol, maxiters, verbose):

    if verbose:
        print("Estimating root using secant method:")
        print("| Iter: | Estimate: |  Error:  |")

    err = 10*tol
    xk = a
    xk1 = b
    iters = 0
    while(err>tol and iters<maxiters):
        xk2 = xk1-f(xk1)*(xk1-xk)/(f(xk1)-f(xk))
        xk = xk1
        xk1 = xk2
        err = np.abs(xk1-xk)
        if verbose:
            print("|","%5.0f" % (iters), "|" , "%9.7f" % (xk) , "|" , "%8.6f" % (err), "|")
        
        iters = iters+1

    
    return xk1 
```
**Last Modified:** 9/24/22