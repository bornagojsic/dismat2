## a^x \equiv b (mod m)

def solve_exp_congruence(a, b, m):
    sols = []
    for x in range(1, m):
        if (a**x - b) % m == 0:
            sols.append(x)
    return sols

def main():
    print("Solving congruence a^x ≡ b (mod m)")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    m = int(input("Enter m: "))

    sols = solve_exp_congruence(a, b, m)
    if sols:
        print("Solutions:", sols)
    else:
        print("No solutions")


if __name__ == "__main__":
    main()