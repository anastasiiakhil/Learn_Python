import sys

n = int(sys.argv[1])


def fib(n):
    if n < 0:
        return 'error'
    else:
        a = 0
        b = 1
        for __ in range(n):
            a, b = b, a + b
        return a


print(fib(n))
