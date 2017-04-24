def charswap(s):
    output=""
    # if(type(s) is int):
    #     output+=str(s)
    # else:
    #     output=s
    output += str(s) if type(s) is int s else
    
    if(len(output)==1 or len(output)==0):
        return output
    first = output[0:1]
    last = output[-1:]
    middle = output[1:-1]
    output=last+middle+first
    return output