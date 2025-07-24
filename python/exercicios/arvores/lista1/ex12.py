def catalan_fatorial(n):
    def fatorial(x):
        res = 1
        for i in range(2, x+1):
            res *= i
        return res
    return fatorial(2*n) // (fatorial(n+1) * fatorial(n))