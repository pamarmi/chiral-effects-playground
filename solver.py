from scipy.integrate import solve_ivp
import numpy as np
from .model import rhs


def solve_system(params):
    """
    Solves the coupled chiral evolution system.

    This is a wrapper around scipy.integrate.solve_ivp
    that integrates the system defined in model.py.

    Parameters
    ----------
    params : tuple
        (Gamma_f, C, eta, k, xi)

    Returns
    -------
    t : np.array
        Time grid
    y : np.array
        Solution array with shape (2, N):
        y[0] = μ5(t)
        y[1] = B(t)
    """

    # Time grid for evaluation
    t_eval = np.linspace(0, 20, 500)

    # Initial conditions: small asymmetry + seed field
    y0 = [1.0, 0.1]

    # Unpack parameters
    Gamma_f, C, eta, k, xi = params

    # Solve ODE system
    sol = solve_ivp(
        lambda t, y: rhs(t, y, Gamma_f, C, eta, k, xi),
        [0, 20],
        y0,
        t_eval=t_eval
    )

    return sol.t, sol.y