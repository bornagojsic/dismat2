## a x^n \equiv b (mod m)

def solve_ind_congruence(a, b, n, m):
    sols = []
    for x in range(1, m):
        if (a * x**n - b) % m == 0:
            sols.append(x)
    return sols


def main():
    print("Solving congruence a x^n ≡ b (mod m)")
    a = int(input("Enter a: "))
    n = int(input("Enter n: "))
    b = int(input("Enter b: "))
    m = int(input("Enter m: "))

    sols = solve_ind_congruence(a, b, n, m)
    if sols:
        print("Solutions: ", sols)
    else:
        print("No solutions")


if __name__ == "__main__":
    main()