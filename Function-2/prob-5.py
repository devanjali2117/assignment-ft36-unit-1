def calculateFactorial(n):
    if n < 0:
        raise ValueError
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculateFactorial(n - 1)
