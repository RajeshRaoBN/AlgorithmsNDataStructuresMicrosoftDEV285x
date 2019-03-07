def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a % b)

print(gcd(3918848, 1653264))
print(gcd(357,234))