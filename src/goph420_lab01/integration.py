import numpy as np 
def integrate_newton(x,f,alg):
    """
    inputs 
    ______
    x: array like the independent variable 
    f: array like the dependent variable
    alg: string trap or simp to indicate the use of trapazoid rule or Simpson's rule  
    outputs
    _______
    s: float

    raises
    ______
    ValueError: if alg is not simp or trap
    ValueError: if x and f are to many dimensions or different lengths
    ValueError: if x is not in acending order
    TypeError: if alg is str-like 
    """
    if alg != 'simp' | 'trap':
        raise ValueError(f"alg {alg} is not simp or trap")
    if np.shape(x) != np.shape(f):
        raise ValueError(f"x and f have different lengths or shape {np.shape(f)} != {np.shape(x)}")
    n = len(x)
    for i in range (n-1):
        if x[i+1] < x[i]: raise ValueError("x arrary not in acending order")
    if alg == 'trap':
        s = np.zeros((n))
        for k in range(n-1):
            s[k] = s[k-1] + (x[k]-x[k-1])*(f[k]+f[k-1])/2

    return s


def integrate_gauss(f,lims,npts:int=3):
    """
    inputs 
    ______
    f: function callable
    lims: object of len 2 containing the lower and upper bound of integration
    npts: possitive non zero int 1-5 default 3 
    outputs
    _______
    estimate: float 
    raises
    ______
    TypeError: if f is not callable
    ValueError: if lims does not have len == 2 
    ValueError if lims [0] or lims [1] are not float like
    ValueError if npts is not in [1,2,3,4,5]
    """
    pass
