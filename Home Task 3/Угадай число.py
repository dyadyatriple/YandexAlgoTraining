n=int(input())
sett=set(range(1,n+1))
while True:
    k=input()
    if k=='HELP':
        print(*sorted(sett))
        break
    else:
        k=set(map(int,k.split()))
        ans=input()
        if ans=="YES":
            sett.intersection_update(k)
        else:
            sett -=  (k)

