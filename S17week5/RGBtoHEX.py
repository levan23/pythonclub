s={
    0:"0",
    1:"1",
    2:"2",
    3:"3",
    4:"4",
    5:"5",
    6:"6",
    7:"7",
    8:"8",
    9:"9",
    10:"a",
    11:"b",
    12:"c",
    13:"d",
    14:"e",
    15:"f",
}
def rgb_to_hex(rgb):
    if(type(rgb) is not list or len(rgb)!=3):
        return ""
    out=""
    for i in rgb:
        if(type(i) is not int or i>255 or i<0):
            return ""
        out+=dec_to_hex(i)
    return out


def dec_to_hex(inp):
    va=""
    va+= s[(inp//16)]
    return va+s[inp%16]
