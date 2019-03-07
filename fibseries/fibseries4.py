def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

print(_fib(0))
print(_fib(1))
print(_fib(2))
print(_fib(10))
print(_fib(30))
print(_fib(60))
print(_fib(100))