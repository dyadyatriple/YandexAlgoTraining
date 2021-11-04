string=input()
sum=0
if len(string)%2==0:
    left=string[:len(string)//2]
    right=string[len(string)//2:]
    for i in range(len(left)):
        if left[i]!=right[len(right)-1-i]:
            sum+=1
else:
    left = string[:len(string) // 2]
    right = string[len(string) // 2+1:]
    for i in range(len(left)):
        if left[i]!=right[len(right)-1-i]:
            sum+=1
print(sum)