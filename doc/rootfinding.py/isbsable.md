# isBsAble
**Function Name:** isbsable  
**Author:** Nathan Nelson  
**Language:** Python  
**Description/Purpose:** This is a sub-function of solvebs that, given two x-values on a function, determines if there is a known root, assuming continuity of the function.  
**Input:** This function accepts a function `f` (that accepts float `x`), an x-value `a`, and second x-value `b`.  
**Output:** A boolean is returned; `True` signifying there is a root on the interval, and `false` if there is not a confirmed root.  
**Usage/Example:** All inputs are taken as arguments:  
`isroot = isbsable(f, 3.0, 3.5)`  
**Implementation/Code:** This is the function implementation in Python:  
```
def isbsAble(f, a, b):
    #Ensures that the interval (a,b) on F(x) contains a root if continuous
        #-Does not check continuity of F on (a,b)
        #-If float error is raised, this is treated as either div/0 or otherwise incontinuous
        #   and will return false, or as not known to contain a root.
    try:
        return (f(a)*f(b)<0)
    except FloatingPointError:
        return False

```
**Last Modified:** 9/24/22