def print_pine_tree(N):
    for i in range(1, N + 1):
        for j in range(N - i):
            print(" ", end="")
        for k in range(2 * i - 1):
            print("*", end="")

        print()

    for _ in range(N - 1):
        print(" ", end="")
    print("|")


N = 5
print_pine_tree(N)