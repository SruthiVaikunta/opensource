t=int(input())
news=[]
for _ in range(t):
    x=int(input())
    if x>=67 and x<=45000:
        news.append("YES")
    else:
        news.append("NO")
for new in news:
    print(new)
