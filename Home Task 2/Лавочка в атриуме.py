length,number=(int(i) for i in input().split())
coord=list(map(int,input().split()))
ans=[]
if length%2==0:
    center=length//2
    left=[i for i in coord if i<center]
    right=[i for i in coord if i>=center]
    print(max(left),min(right))
else:
    center = length // 2
    if center in coord:
        print(center)
    else:
        left = [i for i in coord if i < center]
        right = [i for i in coord if i > center]
        print(max(left), min(right))
