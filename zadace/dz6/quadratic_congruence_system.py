import functools


def solve_quadratic_congruence_system():
    n = int(input("Upiši broj kongruencija oblika x^2 ≡ a (mod m): "))
    
    A = []
    M = []
    for i in range(n):
        a = int(input("a = "))
        m = int(input("m = "))
        A.append(a)
        M.append(m)

    m = functools.reduce(lambda x, y: x* y, M)

    for x in range(m):
        for i in range(n):
            if (x % M[i])**2 % M[i] != A[i]:
                break
        else:
            print(f"x = {x} (mod {m})")


if __name__ == "__main__":
    solve_quadratic_congruence_system()