def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def quadratic_residues(p: int) -> list:
    if not is_prime(p):
        raise ValueError("p must be prime")
    if p == 2:
        return [1]
    
    return [x**2 % p for x in range(1, (p-1)//2 + 1)]

def main():
    p = int(input("Enter a prime number: "))
    try:
        residues = quadratic_residues(p)
        print("Quadratic residues mod", p, "are", residues)
        print(sorted(residues))
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()