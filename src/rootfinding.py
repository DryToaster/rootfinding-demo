import numpy as np, sys

"""
# Defining our test functions
def f(x):
    return x*np.exp(-1*x)
def fprime(x):
    return ((1-x)/np.exp(-1*x))
def f_2(x):
    return 10.14*(np.e)**(x**2)*np.cos(np.pi/x)

"""
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Defining solving algorithm
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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def isbsAble(f, a, b):
    #Ensures that the interval (a,b) on F(x) contains a root if continuous
        #-Does not check continuity of F on (a,b)
        #-If float error is raised, this is treated as either div/0 or otherwise incontinuous
        #   and will return false, or as not known to contain a root.
    try:
        return (f(a)*f(b)<0)
    except FloatingPointError:
        return False

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
    return (1.0/2)*(a+b)
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def hybridnewton(f, fprime, x_0, x_1, tol, maxiters, verbose):
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
    x = solvenewton(f, fprime, ((a+b)/2), tol, maxiters, verbose)
    return x

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
#Test main
if __name__=='__main__':
    np.seterr(all='raise')
    

    print("TASKS 1 AND 2:")
    
    # Establishes tolerances between iterations and maximum iterations, plus verbosity
    
    verbose = False
    if (len(sys.argv)==2):      
        if sys.argv[1]=="-v":
            verbose = True
    tol = 0.000001
    maxiters = 200
    

    # Loops through fixed point algorithm until bounds are met using solvefp function
    estimate = solvefp(f, 2.0, tol, maxiters, verbose)
    print("%.6f" % estimate)

    # FuncIter part 2:
    print()
    print("TASK 3")
    
    #creating list of test x_0
    x0_f2 = []
    current = -3.0
    while(current<7):
        if current!=0.0:
            x0_f2.append(current)
        current = current+0.01
    
    f2_roots = []
    for i in x0_f2:
        x = solvefp(f_2, i, .000001, 200, (verbose))
        if x!=None:
            f2_roots.append(x)
    print("Some roots of f(x):")
    for i in f2_roots:
        print("%0.7f" % i)
    
    #Bisection time
    print()
    print("TASK 4")
    aIndex = 0
    f2_roots_bs = []
    while (aIndex< len(x0_f2) -1):
        x = solvebs(f_2, x0_f2[aIndex], x0_f2[aIndex+1], .000001, verbose)
        if x!=None:
            f2_roots_bs.append(x)
        aIndex=aIndex+1
        
    print("Some roots of f(x):")
    for i in f2_roots_bs:
        print("%0.7f" % i)
    
    #hybridNewton's method
    print()
    print("TASK ??")
    nsolution = hybridnewton(f, fprime, -1, 2, tol, maxiters, verbose)
    print(nsolution)


    #hybridSecant method
    print()
    print("TASK ???")
    ssolution = hybridsecant(f, -1, 2, tol, maxiters, verbose)
    print(ssolution)
"""        
            
    
          
        
    

    
    





    
    


