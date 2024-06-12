def caching_fibonacci():
    cash = {}

    def fibonacci(n):
        if n not in cash:
            if n == 0:
                cash[n] = 0
                return cash[n]
            elif n == 1:
                cash[n] = 1
                return cash[n]
            else:
                cash[n] = fibonacci(n - 1) + fibonacci(n - 2)
                return cash[n]
        else:
            return cash[n]

    return fibonacci
