def process(line: str) -> str:
    line.upper()
    split1 = line[:2]
    split2 = line[2:]
    #print(split1)
    #print(split2)
    i = int(split2, 16)
    k = 0
    for j in str(i):
        k+= int(j)
    #print(i)
    #print(k)
    l = int(split1, 16)
    if k == l:
        return 'VALID'
    else:
        return 'INVALID'


print(process('BADF00D5'))
print(process('1CC0FfEE'))
