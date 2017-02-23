symbols = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M": 1000
}

def roman_to_int(string):
    sum=0;
    previous=0;
    for i in string[::-1]:
        if(symbols[i]>=previous):
            sum+=symbols[i]
            previous=symbols[i]
        else:
            sum-=symbols[i]
            previous=0


    return sum

