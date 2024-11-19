n,x=map(int,input().split())
arr=list(map(int,input().split()))
left,right=0,n-1
pos=0
while left<=right:
    mid=(left+right) //2
    if arr[mid]==x:
        pos=mid
        break
    elif arr[mid]<x:
        left=mid+1
    else:
        right=mid-1
if pos==0:
    pos=left
print(pos)
