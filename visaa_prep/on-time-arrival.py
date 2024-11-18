n=int(input())
output=[]
for _ in range(n):
    time=int(input())
    if(time>=30):
        output.append("YES")
    else:
        output.append("NO")
for i in output:
    print(i)
    
