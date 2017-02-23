def charswap(s):
    output=""
    if (type(s) is int):
        output+=s
    if(len(output)==0):
        print(len(output))
        return ""
    if(len(output)==1):
        return output

    first = output[0:1]
    last = output[-1:]
    middle = output[1:-1]
    output=last+middle+first
    return output

print(charswap("Levan"))