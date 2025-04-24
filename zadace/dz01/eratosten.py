from math import ceil

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def latex_eratosten(n: int, rows: int = 10) -> str:
    latex_string = "\\begin{tabular}{|" + "c|" * (rows) + "}\n\\hline\n& & & & & & & & & & & & \\\\[-1em]\n"

    for i in range(ceil(n/rows)):
        latex_string += " & ".join(["$\\mathcircled{" + str(j) + "}$" if is_prime(j) else "\\cancel{" + str(j) + "}" for j in range(i * rows + 1, min(n + 1, (i + 1) * rows + 1))])
        latex_string += "\\\\\n\\hline\n"

    missing_cells = ceil(n/rows) * rows - n + 1
    if missing_cells > 0:
        latex_string = latex_string[:-len("\\\\\n\\hline\n")]
        latex_string += " & ".join(["" for _ in range(missing_cells)])
        latex_string += "\\\\\n\\hline\n"

    latex_string += "\\end{tabular}\n"

    return latex_string

print(latex_eratosten(200, 12))