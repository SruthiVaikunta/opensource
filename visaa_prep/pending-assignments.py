x,y,z=map(int,input().split())
total_time= z*24*60
required_time=x*y
if(required_time<=total_time):
    print("YES")
else:
    print("NO")
