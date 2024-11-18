n=int(input())
arr=list(map(int,input().split()))
max_count=0
current=0

for i in arr:
    if i==0:
        current+=1
        max_count=max(max_count,current)
    else:
        current=0
print(max_count)
