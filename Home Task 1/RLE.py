string = input()
ans = []
letter = string[0]
s = 1
for i in range(1, len(string)):
    if string[i] != letter:
        ans.append(letter)
        if s > 1:
            ans.append(str(s))
        s = 1
        letter = string[i]
    else:
        s += 1
ans.append(letter)
if s > 1:
    ans.append(str(s))
print(''.join(ans))
