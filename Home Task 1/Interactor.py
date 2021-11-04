system = int(input())
inter = int(input())
check = int(input())
res = None

if inter == 0:
    if system != 0:
        res = 3
    else:
        res = check
elif inter == 1:
    res = check
elif inter == 4:
    if system != 0:
        res = 3
    else:
        res = 4
elif inter == 6:
    res = 0
elif inter == 7:
    res = 1
else:
    res = inter
print(inter)
