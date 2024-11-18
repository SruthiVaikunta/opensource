t=int(input())
cannots=[]
for _ in range(t):
    n,m=map(int,input().split())
    
    if(n>m):
        cannots.append(n-m)
    else:
        cannots.append(0)
for i in cannots:
    print(i)
