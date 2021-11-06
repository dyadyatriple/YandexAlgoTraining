seq=list(map(int,input().split()))
cache=set()
for elem in seq:
    if elem not in cache:
        print("NO")
        cache.add(elem)
    else:
        print('YES')