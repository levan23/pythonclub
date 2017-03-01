def evaluator(students=None, grades=None):
    if(grades is None or students is None or len(students)>30 or len(students)==0 or len(grades)==0 or len(students)!=len(grades)):
        return
    tupl=()
    dicti={}
    all=0
    index = 0

    for s in students:
        counter = 0
        if(type(s) is not str):
            return
        sum=0
        if(type(grades[index]) is not list):
            return
        for i in grades[index]:

            if(type(i) is not int or i<0 or i>20):
                return
            sum+=i
            counter+=1
        if(counter<4 or counter>50):
            return
        all+=sum/len(grades[index])
        dicti[s]=round((sum/len(grades[index])),2)
        index += 1
    tupl=(round(all/len(students),2),dicti)
    return tupl
