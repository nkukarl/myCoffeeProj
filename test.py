def fibo(n):
    """

    Args:
        n: positive integer
    Returns:
        nth fibo number

    """
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    while n - 2:
        a, b = b, a + b
        n -= 1

    return b


if __name__ == "__main__":
    for i in range(1, 10):
        print i, fibo(i)