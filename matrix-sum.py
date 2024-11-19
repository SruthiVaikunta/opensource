n=int(input())
matrix=[list(map(int,input().split())) for _ in range(n)]
r=[0]*n
c=[0]*n

for i in range(n):
    for j in range(n):
        r[i]+=matrix[i][j]
        c[j]+=matrix[i][j]
res=[r[i] + c[i] for i in range(n)]
print(' '.join(map(str,res)))
