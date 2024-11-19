n,m=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(n)]
rows=set()
col=set()
for i in range(n):
    for j in range(m):
        if matrix[i][j]==0:
            rows.add(i)
            col.add(j)
for i in range(n):
    for j in range(m):
        if i in rows or j in col:
            matrix[i][j]=0
for row in matrix:
    print(' '.join(map(str,row)))
