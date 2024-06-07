def listMultiples(n, limit):
    multiples = [limit * i for i in range(1, n + 1)]
    print(", ".join(map(str, multiples)))

