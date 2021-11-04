seq=list(map(int,input().split()))
shop=-15
dist=[]
for i in range(len(seq)):
    if seq[i]==1:
        dist.append(i-shop)
    elif seq[i]==2:
        shop=i
shop=15
h=len(dist)-1
for i in range(len(seq)-1,-1,-1):
    if seq[i]==1:
        d=shop-i
        if dist[h]>d:
            dist[h]=d
        h-=1
    if seq[i]==2:
        shop=i

print(max(dist))