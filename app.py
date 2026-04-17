import streamlit as st
import matplotlib.pyplot as plt

from src.chiral.solver import solve_system
from src.chiral.analysis import instability_condition


st.title("Chiral Effects Playground")

# User-controlled parameters
Gamma_f = st.slider("Chirality flipping rate Γ_f", 0.0, 1.0, 0.1)
C       = st.slider("Anomaly coupling C", 0.0, 2.0, 1.0)
eta     = st.slider("Diffusivity η", 0.0, 1.0, 0.1)
k       = st.slider("Wavenumber k", 0.1, 5.0, 1.0)
xi      = st.slider("Chiral feedback ξ", 0.0, 2.0, 1.0)

# Solve system
t, y = solve_system((Gamma_f, C, eta, k, xi))

mu5, B = y

# Plot results
fig, ax = plt.subplots()
ax.plot(t, mu5, label="μ₅")
ax.plot(t, B, label="B")
ax.legend()

st.pyplot(fig)

# Simple physical interpretation
if instability_condition(mu5[-1], eta, k, xi):
    st.success("Chiral instability active")
else:
    st.warning("Stable regime")