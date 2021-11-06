seq=list(map(int,input().split()))
cnt={}
for elem in seq:
    if elem not in cnt:
        cnt[elem]=1
    else:
        cnt[elem]+=1
for elem in cnt.keys():
    if cnt[elem]==1:
        print(elem,end=' ')