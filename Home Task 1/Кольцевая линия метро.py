total,live,work=(int(i) for i in input().split())
print(min(abs(work-live)-1,total-max(work,live)+min(work,live)-1))