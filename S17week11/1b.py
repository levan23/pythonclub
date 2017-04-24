adder=lambda a,b:(bin(int(a,2)+int(b,2)))[2:].zfill(len(a))

print(adder("0001","0101"))