from pathlib import Path

from sympy import Symbol, lambdify

from .load import load_file

RSC_DIR = Path(__file__).parent.resolve() / "resources"

SHORT_PARAMETER_NAMES = (
    "omega",
    "omega_0",
    "Gamma_0",
    "Omega_R",
    "gamma_d",
    "Omega_12",
    "gamma_12",
)
PARAMETER_NAMES = (
    "excitation_frequency",
    "center_frequency",
    "radiative_decay_rate",
    "rabi_frequency",
    "dephasing_rate",
    "coupling_strength",
    "dissipative_coupling_rate",
)
EXPRESSION_NAMES = (
    "excitation_number",
    "eeee",
    "egeg",
    "gggg",
    "geeg",
    "re_ggee",
    "im_ggee",
    "re_ggeg",
    "im_ggeg",
    "re_egee",
    "im_egee",
)

PREFIX = "sympy_density_matrix"

expressions = {
    name: load_file(RSC_DIR / f"{PREFIX}_{name}.txt") for name in EXPRESSION_NAMES[1:]
}
expressions[EXPRESSION_NAMES[0]] = load_file(
    RSC_DIR / f"sympy_{EXPRESSION_NAMES[0]}.txt"
)

parameters = {
    name: tuple(
        symbol
        for symbol in tuple(expressions.values())[0].free_symbols
        if isinstance(symbol, Symbol) and symbol.name == name
    )[0]
    for name in SHORT_PARAMETER_NAMES
}
for name, short_name in zip(PARAMETER_NAMES, SHORT_PARAMETER_NAMES):
    parameters[name] = parameters[short_name]

functions = {
    expr_name: lambdify(
        tuple(parameters[name] for name in PARAMETER_NAMES),
        expressions[expr_name].args[0],
    )
    for expr_name in EXPRESSION_NAMES
}
