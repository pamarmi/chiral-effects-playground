import numpy as np

def rhs(t, y, Gamma_f, C, eta, k, xi):
    """
    Right-hand side of the coupled chiral evolution system.

    This function defines the dynamical system:
        - mu5: chiral chemical potential
        - B : magnetic field amplitude (toy model)

    The equations include:
        - chirality flipping term (Γ_f)
        - anomaly-induced coupling term (C, eta)
        - magnetic diffusion term (proportional to eta k**2)
        - chiral feedback term(xi mu5 B)

    Parameters
    ----------
    t : float
        Time variable (required by solver, not explicitly used here)
    y : array-like
        State vector [mu5, B]
    Gamma_f : float
        Chirality flipping rate
    C : float
        Coupling strength for anomaly source term
    eta : float
        Diffusivity / damping parameter
    k : float
        Wavenumber of magnetic mode
    xi : float
        Chiral magnetic feedback strength

    Returns
    -------
    dydt : np.array
        Time derivatives [dmu5dt, dBdt]
    """

    mu5, B = y

    # Chiral asymmetry evolution
    dmu5 = -Gamma_f * mu5 - C * eta * B**2

    # Magnetic field evolution with damping + feedback
    dB = -eta * k**2 * B + xi * mu5 * B

    return np.array([dmu5, dB])