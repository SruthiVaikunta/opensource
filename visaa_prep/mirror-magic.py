n=int(input())
matrix=[]
for _ in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)
for row in matrix:
    print(' '.join(map(str,row[::-1])))
