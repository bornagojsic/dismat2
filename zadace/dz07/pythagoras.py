from math import sqrt


def divisors_less_than_eq_sqrt(n: int) -> list:
    divs = [i for i in range(1, int(sqrt(n)) + 1) if n % i == 0]
    
    return divs


def divisors(n: int) -> list:
    divs = divisors_less_than_eq_sqrt(n)
    
    for div in divs[::-1]:
        div_ = n // div
        if div_ not in divs:
            divs.append(div_)
    return divs


def get_triangle(d: int, m: int, n: int) -> tuple:
    x = d * (m ** 2 - n ** 2)
    y = 2 * d * m * n
    z = d * (m ** 2 + n ** 2)
    return (x, y, z)


def pythagoras(side: int) -> list:
    divs = divisors(side)[:-1]

    triangles = set()

    for d in divs:
        side_ = side // d
        if side_ % 2 == 0:
            ## 2 * m * n = side_, m > n
            divs_side_ = divisors_less_than_eq_sqrt(side_ // 2)
            for n in divs_side_:
                m = side_ // 2 // n
                if m == n or m < n:
                    continue
                triangles.add(get_triangle(d, m, n))
        
        if side_ % 4 == 1:
            ## m^2 + n^2 = side_
            for m in range(1, int(sqrt(side_)) + 1):
                if sqrt(side_ - m ** 2).is_integer():
                    n = int(sqrt(side_ - m ** 2))
                    if m <= n:
                        continue
                    triangles.add(get_triangle(d, m, n))

        if side_ % 4 != 2:
            ## m^2 - n^2 = side_
            
            ## m - n = div(side_)
            ## m + n = side_ // div(side_)
            ## m = (div(side_) + side_ // div(side_)) // 2
            ## n = (side_ // div(side_) - div(side_)) // 2

            divs_side_ = divisors_less_than_eq_sqrt(side_)
            for div in divs_side_:
                m = (div + side_ // div) // 2
                n = (side_ // div - div) // 2
                if m == n or m < n:
                    continue
                triangles.add(get_triangle(d, m, n))

    triangles = list(triangles)
    print(triangles)


def main():
    s = int(input("Unesite duljinu stranice Pitagorinog trokuta: "))
    pythagoras(s)
    # l = [(1,4,1),
    #     (1,4,3),
    #     (2,3,2),
    #     (3,2,1),
    #     (4,2,1)]
    
    # for t in l:
    #     print(get_triangle(*t))
    # print(get_triangle(1, 50, 21))
    # print(get_triangle(1, 51, 20))
    # print(get_triangle(1, 51, 22))
    # print(get_triangle(1, 52, 21))
    # print(get_triangle(1, 52, 23))
    # print(get_triangle(1, 52, 25))



if __name__ == "__main__":
    main()