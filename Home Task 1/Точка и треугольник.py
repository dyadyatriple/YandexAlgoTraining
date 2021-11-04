d=int(input())
x,y=(int(i) for i in input().split())

if x>=0 and y>=0 and d-x>=y:
    print(0)
else:
    r1=(x**2+y**2)**(1/2)
    min=1
    r2 = ((x-d) ** 2 + y ** 2) ** (1 / 2)
    if r2<r1:
        min=2
    r3 = (x ** 2 + (y-d) ** 2) ** (1 / 2)
    if r3<r1 and r3<r2:
        min=3
    print(min)