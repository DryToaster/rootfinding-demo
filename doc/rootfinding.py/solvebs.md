# solveBs
**Function Name:** solvebs  
**Author:** Nathan Nelson  
**Language:** Python  
**Description/Purpose:** This function is usedto solve for roots of a function using bisection.  
**Input:** This function accepts a function `f` (that accepts float `x`), an x-value `a`, and second x-value `b` (to define interval of interest), a float for error tolerance, and a boolean indicating verbose status.  
**Output:** A float is returned representing an approximated root of the function.  
**Usage/Example:** All inputs are taken as arguments:  
`root = solvebs(f, 3.0, 3.5, .0001, false)`  
If verbose output is enabled, a table similar to the following will be printed to console:  
```
Estimating root of f(x) using bisection on interval ( 0.39999999999998054 , 0.40999999999998055 )
| Iter: | Estimate: |  Error:  |
|     0 | 0.4050000 | -0.010000 |
|     1 | 0.4025000 | -0.005000 |
|     2 | 0.4012500 | -0.002500 |
|     3 | 0.4006250 | -0.001250 |
|     4 | 0.4003125 | -0.000625 |
|     5 | 0.4001562 | -0.000312 |
|     6 | 0.4000781 | -0.000156 |
|     7 | 0.4000391 | -0.000078 |
|     8 | 0.4000195 | -0.000039 |
```
**Implementation/Code:** This is the function implementation in Python:  
```
def solvebs(f, a, b, tol, verbose):
    if  not isbsAble(f, a, b):
        return None
    k = int(1+(np.log10(tol)/np.log10(b-a))/np.log10(2))
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
    return c

```
**Last Modified:** 9/24/22