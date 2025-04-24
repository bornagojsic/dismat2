def solve_congruence(a, b, m):
    for x in range(m):
        if (a * x) % m == b:
            return x
        if (a * x) % m + b == 0:
            return m - x

def main():
    print("Rješavanje a * x ≡ b (mod m)")
    a = int(input("Unesite a: "))
    b = int(input("Unesite b: "))
    m = int(input("Unesite m: "))
    print(f"Rješenje je x = {solve_congruence(a, b, m)}")

if __name__ == "__main__":
    main()