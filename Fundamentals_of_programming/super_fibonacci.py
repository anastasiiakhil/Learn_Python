def super_fibonacci(n, m):
    if type(n) == type(m) == int:
        if (0 < n <= 35) & (0 < m <= 35):
            fibonacci = [0 for i in range(36)]
            for k in range(len(fibonacci)):
                if k <= m:
                    fibonacci[k] = 1
                else:
                    fibonacci[k] = sum(fibonacci[k-m:k])
            return fibonacci[n]
