def is_person_code_valid(string):
    first=[1,2,3,4,5,6,7,8,9,1]
    second=[3,4,5,6,7,8,9,1,2,3]
    sum2=0
    sum1=0
    ind=0;
    if(len(string)!=11):
        return False
    elif((int(string[:1]))<1 or (int(string[:1]))>6):
        return False
    elif((int(string[1:3]))<0):
        return False
    elif((int(string[3:5]))>12 or (int(string[3:5])<1)):
        return False
    elif((int(string[5:7]))>31 or (int(string[5:7])<1)):
        return False
    elif((int(string[7:10]))<1):
        return False
    else:
        for a in string[:10]:
            sum1+=int(a)*(first[ind])
            sum2 += int(a) * (second[ind])
            ind+=1
        if((sum1%11)!=10):
            return True
        else:
            if((sum2%11)!=10):
                return True
        return False


