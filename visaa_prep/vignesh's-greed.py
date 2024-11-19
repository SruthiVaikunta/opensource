n=int(input())
length=list(map(int,input().split()))
length.sort(reverse=True)
for i in range(n-2):
    if length[i]<length[i+1]+length[i+2]:
        print(length[i]+length[i+1]+length[i+2])
        break
else:
    print(-1)
