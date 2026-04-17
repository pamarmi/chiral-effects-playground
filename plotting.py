import matplotlib.pyplot as plt


def plot_solution(t, mu5, B):
    """
    Plots the time evolution of mu5 and B.

    Parameters
    ----------
    t : array
        Time points
    mu5 : array
        Chiral chemical potential evolution
    B : array
        Magnetic field evolution

    Returns
    -------
    fig : matplotlib.figure.Figure
        Figure object for display or saving
    """

    fig, ax = plt.subplots()

    ax.plot(t, mu5, label=r"$\mu_5$")
    ax.plot(t, B, label="B")

    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")
    ax.set_title("Chiral Evolution Dynamics")
    ax.legend()

    return fig