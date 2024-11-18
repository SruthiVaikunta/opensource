n=int(input())
arr=list(map(int,input().split()))
new=[]
for i in range(0,len(arr)):
    if(arr[i] not in new):
        new.append(arr[i])
print(*new)
