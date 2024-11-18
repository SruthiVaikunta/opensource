N=int(input())
matrix=[list(map(int,input().split())) for _ in range(N)]

transpose=[[matrix[j][i] for j in range(N)] for i in range(N)]
for row in transpose:
    print(" ".join(map(str, row)))
