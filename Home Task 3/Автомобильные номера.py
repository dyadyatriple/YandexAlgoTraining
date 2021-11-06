m=int(input())
testimonies=[]
for _ in range(m):
    testimonies.append(set(input()))

n=int(input())
votes={-1:''}
max=-1
for _ in range(n):
    vote=0
    number=input()
    for testi in testimonies:
        if len(testi.intersection(set(number)))==len(testi):
            vote+=1
    if vote>max:
        votes.clear()
        votes[vote]=[number]
        max=vote
    elif vote==max:
        votes[vote].append(number)

print(*votes[max],sep='\n')
