def instability_condition(mu5, eta, k, xi):
    """
    Checks whether the system is in the chiral instability regime.

    Physical interpretation:
    The magnetic field grows when chiral feedback dominates diffusion.

    Condition:
        xi mu5 > eta k**2

    Returns
    -------
    bool
        True if instability is active
    """

    return xi * mu5 > eta * k**2