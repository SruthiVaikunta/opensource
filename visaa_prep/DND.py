n,m=map(int,input().split())
arr=list(map(int,input().split()))
num1=[]
num2=[]
for i in range(0,len(arr)):
    if arr[i]%m==0:
        num1.append(arr[i])
    else:
        num2.append(arr[i])
print((sum(num1) - sum(num2)))
