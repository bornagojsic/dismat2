from math import sqrt

def continued_fraction_sqrt(n: int):
    ## CF(√n) = [a0; (a1, a2, ..., al)], al = 2 * a0
    s = [0]
    t = [1]
    a = [int(sqrt(n))]

    while True:
        s.append(a[-1] * t[-1] - s[-1])
        t.append((n - s[-1] ** 2) // t[-1])

        if len(s) > 2 and t[-1] == t[1] and s[-1] == s[1]:
            break

        a.append((a[0] + s[-1]) // t[-1])

    print("\\begin{tabular}{|c|c|c|c|}")
    print("\\hline")
    print("$i$ & $s_{i}$ & $t_{i}$ & $a_{i}$ \\\\")
    print("\\hline")
    for i in range(len(s)):
        print(f"{i} & {s[i]} & {t[i]} & {a[i] if i != len(a) else ''}\\\\")
    print("\\hline")
    print("\\end{tabular}")


def main():
    n = int(input("Upišite n za računanje CF(sqrt(n)): "))
    continued_fraction_sqrt(n)


if __name__ == "__main__":
    main()