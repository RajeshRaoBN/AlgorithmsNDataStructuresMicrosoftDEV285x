def fib(n):
    fiblist = [0, 1]
    for i in range(2, n):
        fiblist.append(fiblist[i - 1] + fiblist[i - 2])
    return fiblist

for i in fib(15):
    print(i)