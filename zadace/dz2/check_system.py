def check_congruence(a, b, m, x):
    return (a * x - b) % m == 0

def check_system(n, x_0):
    for i in range(n):
        a = int(input(f"Upišite a_{i + 1}: "))
        b = int(input(f"Upišite b_{i + 1}: "))
        m = int(input(f"Upišite m_{i + 1}: "))
        print()
        if not check_congruence(a, b, m, x_0):
            return False
    return True

def main():
    n = int(input("Upišite broj kongruencija: "))
    x_0 = int(input("Upišite x_0: "))
    if check_system(n, x_0):
        print("Sustav je točno riješen.")
    else:
        print("Sustav nije točno riješen.")

if __name__ == "__main__":
    main()