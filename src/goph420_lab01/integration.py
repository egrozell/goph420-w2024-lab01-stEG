import numpy as np


def integrate_newton(x, f, alg):
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

    # check imputs are float like and array like
    x = np.array(x, dtype=float)
    f = np.array(f, dtype=float)

    # check shape of arrays are equal
    if np.shape(x) != np.shape(f):
        raise ValueError(f"x and f have different lengths or shape {np.shape(f)} != {np.shape(x)}")
    n = len(x)
    s = 0.0

    # check that x is in accending order
    for i in range(n - 1):
        if x[i + 1] < x[i]:
            raise ValueError("x arrary not in acending order")

    if alg == "trap":
        for k in range(n - 1):
            s += (x[k + 1] - x[k]) * (f[k + 1] + f[k]) / 2
    elif alg == "simp":
        if n % 2 != 0:
            for k in range(0, n - 1, 2):
                s += (x[k + 2] - x[k]) * (f[k] + 4 * f[k + 1] + f[k + 2]) / 6
        else:
            for k in range(0, n - 4, 2):
                s += (x[k + 2] - x[k]) * (f[k] + 4 * f[k + 1] + f[k + 2]) / 6
            s += (x[n - 1] - x[n - 4]) * (f[n - 4] + 3 * f[n - 3] + 3 * f[n - 2] + f[n - 1]) / 8
    else:
        raise ValueError(f"alg {alg} is not simp or trap")
    return s


def integrate_gauss(f, lims, npts: int = 3):
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
    if len(lims) != 2:
        raise ValueError(f"dim of limit {len(lims)} is not 2")
    a = float(lims[0])
    b = float(lims[1])
    # n = 2 * npts - 1

    if npts == 3:
        pts = np.array([-np.sqrt(3 / 5), 0, np.sqrt(3 / 5)])
        wts = np.array([5 / 9, 8 / 9, 5 / 9])
    elif npts == 1:
        pts = np.array([0])
        wts = np.array([2.0])
    elif npts == 2:
        pts = np.array([-1 / np.sqrt(3), 1 / np.sqrt(3)])
        wts = np.array([1.0, 1.0])
    elif npts == 4:
        pts = np.array([-np.sqrt(525 + 70 * np.sqrt(30)) / 35,
                        -np.sqrt(525 - 70 * np.sqrt(30)) / 35,
                        np.sqrt(525 - 70 * np.sqrt(30)) / 35,
                        np.sqrt(525 + 70 * np.sqrt(30)) / 35])
        wts = np.array([(18 - np.sqrt(30)) / 36,
                        (18 + np.sqrt(30)) / 36,
                        (18 + np.sqrt(30)) / 36,
                        (18 - np.sqrt(30)) / 36])
    elif npts == 5:
        pts = np.array([- np.sqrt(245 + 14 * np.sqrt(70)) / 21,
                        -np.sqrt(245 - 14 * np.sqrt(70)) / 21,
                        0,
                        np.sqrt(245 - 14 * np.sqrt(70)) / 21,
                        np.sqrt(245 + 14 * np.sqrt(70)) / 21])
        wts = np.array([(322 - 13 * np.sqrt(70)) / 900,
                        (322 + 13 * np.sqrt(70)) / 900,
                        128 / 225,
                        (322 + 13 * np.sqrt(70)) / 900,
                        (322 - 13 * np.sqrt(70)) / 900])
    else:
        raise ValueError("npts must be 1,2,3,4,or 5")
    # pfit = .5*(a+b)+.5*(b-a)*pts
    # wfit = .5*(b-a)*wts
    i = 0.5 * (b - a) * sum(wts * f(0.5 * (b - a) * pts + 0.5 * (b + a)))

    return i
