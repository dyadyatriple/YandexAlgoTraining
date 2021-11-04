seq=[]
while True:
    inp=int(input())
    if inp==0:
        break
    seq.append(inp)
max=0
for i in range(1,len(seq)):
    if seq[i]>seq[max]:
        max=i
cnt=0
for i in range(len(seq)):
    if seq[i]==seq[max]:
        cnt+=1
print(cnt)