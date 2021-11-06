def abcheck(x,seq):
    cache=set()
    for elem in seq:
        if x-elem in cache:
            return elem, x-elem
        cache.add(elem)
    return 0,0

x=int(input())
seq=list(map(int,input().split()))
print(abcheck(x,seq))