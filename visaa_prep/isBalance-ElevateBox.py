n=int(input())
arr=list(map(int,input().split()))

b=[0]*n
pre_sum=[0]*(n+1)
for i in range(1,n+1):
    pre_sum[i]=pre_sum[i-1]+arr[i-1]
for i in range(n):
    left_sum=pre_sum[i]
    right_sum=pre_sum[n]-pre_sum[i+1]
    b[i]=abs(left_sum-right_sum)
for i in range(n):
    print(b[i], end=" ")
