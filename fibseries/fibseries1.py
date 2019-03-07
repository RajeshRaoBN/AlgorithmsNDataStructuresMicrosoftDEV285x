def fibonacci(n):
    current = 0
    after = 1
    for i in range(0, n):
        current, after = after, current + after
    return current

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(10))
print(fibonacci(33))
print(fibonacci(36))
print(fibonacci(60))