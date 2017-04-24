 def sonic_how_many_rings_did_you_get(a):    s=0
    for i in a: s+= 1 if(i in "oPO096bRepDdag") else 2 if(i in "B8") else 0
    return s