a=int(input())
b=list(map(int,input().split()))
if a==1:
    print(b[0]-1)
else:
    max=0
    for i in range(1,a):
        if b[i]>b[max]:
            max=i
    s=0
    for i in range(a):
        if i!=max:
            s+=b[i]
    print(s)