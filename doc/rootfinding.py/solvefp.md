# solveFP
**Function Name:** solvefp  
**Author:** Nathan Nelson  
**Language:** Python  
**Description/Purpose:** This function finds roots of a given function using the fixed-point method. It will automatically use up to 3 different g(x) functions if the first or second fail to converge.  
**Input:** This function takes a function `f`, an initial guess/estimate float 'x_0', an error tolerance float `tol`, a maximum integer number of iterations `maxiters`, and a boolean `verbose` representing whether verbose output should be displayed.  
**Output:** An estimate of a root of `f` in the form of a floating point value is the output. If the sequence does not meet tolerance within the iteration limit or a float error is encountered, `None` is returned instead.  
**Usage/Example:** All inputs are taken as arguments; if we want to store the found solution of function `f` in `x`:  
`x = solvefp(f, 4.0, .000001, 200, false)`  
If verbose output is enabled,  
`x = solvefp(f, 4.0, .000001, 200, true)`  
the cli will print a table such as:  
```
Estimating root of F(x) using G_1:
| Iter: | Estimate: |  Error:  |
|     0 | 0.1000000 | 0.090970 |
|     1 | 0.0090299 | 0.008949 |
|     2 | 0.0000808 | 0.000081 |
|     3 | 0.0000000 | 0.000000 |
```  
**Implementation/Code:** This is the function implementation in Python:  
```
def solvefp(f, x_0, tol, maxiters, verbose):
    np.seterr(all='raise')
    if verbose:
        print("Estimating root of F(x) using G_1:")
        print("| Iter: | Estimate: |  Error:  |")
    iters = 0
    err = 10*tol
    x_k=x_0
    
    
    # Trying g_1 for convergence
    while(err>tol and iters<maxiters):
        try:
            if verbose:
                print("|","%5.0f" % iters, "|" , "%9.7f" % x_k , "|" , "%8.6f" % err, "|")
            x_k1 = x_k - f(x_k)
            err = np.abs(x_k-x_k1)
            iters = iters+1
            x_k = x_k1
        except FloatingPointError:
            iters=maxiters
    if verbose:
        print("|","%5.0f" % iters, "|" , "%9.7f" % x_k , "|" , "%8.6f" % err, "|")

    if(err<=tol):
        if verbose:
            print("G_1 estimate reached tolerance:")
        return x_k1
    elif verbose:
        print("G_1 failed to converge, restarting estimation using G_2:")

    # Trying g_2 for convergence
    iters=0
    err = 10*tol
    x_k=x_0
    while(err>tol and iters<maxiters):
        try:
            if verbose:
                print("|","%5.0f" % iters, "|" , "%9.7f" % x_k , "|" , "%8.6f" % err, "|")
            x_k1 = x_k + f(x_k)
            err = np.abs(x_k-x_k1)
            iters = iters+1
            x_k = x_k1
        except FloatingPointError:
            iters=maxiters

    if(err<tol):
        if verbose:
            print("G_2 estimate reached tolerance:")
        return x_k1
    elif verbose:
        print("G_2 failed to converge within ", maxiters, " iterations, stopping.")

    # Trying g_3 for convergence
    iters=0
    err = 10*tol
    x_k=x_0
    while(err>tol and iters<maxiters):
        try:
            if verbose:
                print("|","%5.0f" % iters, "|" , "%9.7f" % x_k , "|" , "%8.6f" % err, "|")
            x_k1 = x_k - .0000001*f(x_k)
            err = np.abs(x_k-x_k1)
            iters = iters+1
            x_k = x_k1
        except FloatingPointError:
            iters=maxiters

    if(err<tol):
        if verbose:
            print("G_3 estimate reached tolerance: ",x_k1)
        return x_k1
    elif verbose:
        print("G_3 failed to converge within ", maxiters, " iterations, stopping.")

```
**Last Modified:** 9/24/22