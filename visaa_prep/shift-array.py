n=int(input())
arr=list(map(int,input().split()))
new=arr[1:]+arr[:1]
print(*new)
