def fib(n):
    if(n <= 1):
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(10))
print(fib(30))
print(fib(60))