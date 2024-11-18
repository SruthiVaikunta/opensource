t=int(input())
needed=[]
for _ in range(t):
    x,y=map(int,input().split())
    needed.append((x-y)+1)
for need in needed:
    print(need)
