def integrate_newton(x,f,alg):
    """
    inputs 
    ______
    x: array like the independent variable 
    f: array like the dependent variable
    alg: string trap or simp to indicate the use of trapazoid rule or Simpson's rule  
    outputs
    _______
    estamate: float

    raises
    ______
    ValueError: if alg is not simp or trap
    ValueError: if x and f are to many dimensions or different lengths
    TypeError: if str-like 
    """

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
