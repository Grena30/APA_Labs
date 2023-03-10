
f = [0] * 500000


def fib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        f[n] = 1
        return f[n]

    if f[n]:
        return f[n]

    if n & 1:
        k = (n + 1) // 2
    else:
        k = n // 2

    # Applying above formula: value n&1 is 1
    # if n is odd, else 0.
    if n & 1:
        f[n] = (fib(k) * fib(k) + fib(k - 1) * fib(k - 1))
    else:
        f[n] = (2 * fib(k - 1) + fib(k)) * fib(k)

    return f[n]
