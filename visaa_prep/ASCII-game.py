s=input()
new=''.join([char.upper() if char.islower() else char.lower() for char in s])
print(new)
