n=int(input())
sign=-1 if n<0 else 1
reversed_n= int(str(abs(n))[::-1])  * sign
if reversed_n < -2**31 or reversed_n > 2**31 -1:
    print(0)
else:
    print(reversed_n)
