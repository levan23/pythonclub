import math
from decimal import *
from datetime import datetime

def is_prime(value):
    if value <= 1:
        return False
    elif value <= 3:
        return True
    else:
        sqrt = Decimal(str(math.sqrt(value)))
        sqrt_int = int(sqrt)

        checklist = [x for x in range(2, max(2, sqrt_int) + 1)]

        for i in range(2, max(2, sqrt_int) + 1):
            if i in checklist:
                if value % i == 0:
                    return False

                checklist = [x for x in checklist if not x % i == 0]

        return True

def prime_factors(value):
    list = []
    if(type(value) is not int):
        raise TypeError("wtf")
    if(value==1 or value==0):
        return list
    counter = 2

    while(counter<= value):

        if(value%counter==0):
            value /= counter
            list.append(counter)
        else:
            counter+=1

    return list