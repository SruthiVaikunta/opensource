v,c=input().split()
if v==c:
    print("NULL")
elif ((v=='R' and c=='S') or (v=='P' and c=='R') or (v=='S' and c=='P')):
    print("Vignesh")
else:
    print("Charan")
