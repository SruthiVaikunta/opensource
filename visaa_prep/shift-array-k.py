def rot(n,arr,k):
    k=k%n
    return arr[-k:]+arr[:-k]
n=int(input())
arr=list(map(int,input().split()))
k=int(input())
rot=rot(n,arr,k)
print(*rot)
