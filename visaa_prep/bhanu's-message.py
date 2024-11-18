msg=input().strip()
if msg.startswith("+"):
    parts=msg.split(" ")
    if len(parts)==2 and parts[0][1:].isdigit() and parts[1].isdigit()and len(parts[1])==10 and len(parts[0])==3:
        digits=parts[1]
        if(sum(int(digit) for digit in digits))>0:
            print("Correct")
        else:
            print("Incorrect")
    else:
        print("Incorrect")
else:
    print("Incorrect")
