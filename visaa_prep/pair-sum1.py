n=int(input())
arr=list(map(int,input().split()))
k=int(input())
seen=set()
found=False
for num in arr:
    if k-num in seen:
        found=True
        break
    seen.add(num)
print("true" if found else "false")
