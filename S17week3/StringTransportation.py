import re
from itertools import zip_longest
def transposition(text=None):
    if(text==None or type(text) is not str):
        return

    list=[]
    list2=[]
    for i in text.split( ):
        crap=re.sub('\W+','',i)
        if crap:
            list.append(crap)
    for i in zip_longest(*list, fillvalue=' '):
        list2.append(" ".join(i))
    return "\n".join(list2)+"\n"

print(transposition("Python CodeClub @ Tallinn"))