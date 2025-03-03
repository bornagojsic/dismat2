from congruence import solve_congruence
from functools import reduce


def solve_crt():
    print("Rješavanje sustava kongruencija a * x ≡ b (mod m)")
    n = int(input("Unesite broj kongruencija: "))
    a = []
    b = []
    m = []

    for i in range(n):
        a.append(int(input(f"Unesite a_{i+1}: ")))
        b.append(int(input(f"Unesite b_{i+1}: ")))
        m.append(int(input(f"Unesite m_{i+1}: ")))
    
    M = reduce(lambda x, y: x * y, m)
    
    for i in range(n):
        if a[i] != 1:
            b[i] = (b[i] * solve_congruence(a[i], 1, m[i])) % m[i]
    
    ## Sada su svi a_i = 1

    m_j = [M // m_i for m_i in m]
    print(f"m_j = {m_j}")
    x_j = [solve_congruence(m_j[i], b[i], m[i]) for i in range(n)]
    print(f"x_j = {x_j}")
    y = [m_j[i] * x_j[i] for i in range(n)]
    print(f"y = {y}")

    x = sum([a[i] * m_j[i] * y[i] for i in range(n)]) % M

    print(f"Rješenje je x = {x}")


def main():
    solve_crt()


if __name__ == "__main__":
    main()

    ## x ≡ 7 (mod 17), x ≡ 18 (mod 31), x ≡ 33 (mod 37)