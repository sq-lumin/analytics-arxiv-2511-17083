# Analytical expressions for the steady-state density matrix of coupled quantum emitters

Supplementary material to the paper [https://arxiv.org/abs/2511.17083v1]().

The analytical expressions are provided as text files in [src/analytics_arxiv_2511_17083/resources]().

- `sympy_*.txt` files are in SymPy srepr format, and can be loaded with the function `sympify`
- `matematica_*.txt` files can be loaded using Wolfram Mathematica.

For an example, see the jupyter notebook [notebooks/example_excitation_spectrum.ipynb]().

> [!IMPORTANT]
> since `gamma^*` is not a valid python variable name, the dephasing rate was renamed to `gamma_d`. All other notation is identical to the paper.

> [!IMPORTANT]
> since `_` cannot be used in mathematica variable variable names, all underscores were removed from those files. For instance: `Omega_R` => `OmegaR`
