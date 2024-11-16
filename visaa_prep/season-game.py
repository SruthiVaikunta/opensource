n=int(input())
if(1<=n<=12):
    if(n==4 or n==5 or n==3):
        print("Spring")
    elif(n==6 or n==7 or n==8):
        print("Summer")
    elif(n==9 or n==10 or n==11):
        print("Autumn")
    else:
        print("Winter")
  
else:
    print("Invalid")
