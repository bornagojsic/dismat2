def parse_latex_table_cells(table: list):
    table = table[1:-1]
    table = [line.strip() for line in table]
    table = [line.replace("\\hline", "") for line in table]
    table = [line.split("&") for line in table]
    table = [[cell.strip() for cell in line] for line in table]
    table = [[cell.replace("\\", "") for cell in line] for line in table]
    table = [[cell for cell in line if cell] for line in table]
    table = [line for line in table if line]
    return table


def rotate_latex_table(table: list):
    table = parse_latex_table_cells(table)

    cols = len(table)
    rows = len(table[0])

    rotated_table = []
    for i in range(rows):
        rotated_table.append([table[j][i] for j in range(cols)])

    return rotated_table


def main():
    with open(f"table", "r") as f:
        table = f.readlines()

    rotated_table = rotate_latex_table(table)

    print("Rotated table:")
    print(rotated_table)

    with open(f"rotated_table", "w") as f:
        f.write("\\begin{tabular}{|" + "c|" * len(rotated_table[0]) + "}\n")
        f.write("\\hline\n")
        for row in rotated_table:
            f.write(" & ".join(row) + " \\\\\n")
            f.write("\\hline\n")
        f.write("\\end{tabular}")



if __name__ == "__main__":
    main()