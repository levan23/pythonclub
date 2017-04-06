def find_factors(upper_limit):
    lst=[]
    sum=0
    if(upper_limit>=2):
        sum+=2
    if(upper_limit>=3):
        sum+=3
    if(upper_limit>3):
        for i in range(4,upper_limit):
            if(i%2!=0):
                #lst.append(i)
                sum+=i
    for i in range(1,sum+1):
        if(sum%i==0):
            lst.append(i)

    return lst