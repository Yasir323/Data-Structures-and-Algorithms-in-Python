# Fibonacci using Tabulation
def fibonacci(n):
    # array declaration
    f = [0] * (n + 1)
    # base case assignment
    if n > 0:
        f[1] = 1

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

# Driver program to test the above function


def main():
    n = 3
    print("Fibonacci number is ", fibonacci(n))


if __name__ == "__main__":
    main()
