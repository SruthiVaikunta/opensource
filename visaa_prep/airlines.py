import math
x,n=map(int,input().split())# 1 x=100
possible=x*100
extra_people=n-possible
extra_planes=math.ceil((extra_people)/100)
print(extra_planes)
