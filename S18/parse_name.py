parse_name=lambda s:str(" ".join(list(map(lambda x: "".join(list(filter(str.isalpha,x))),filter(lambda b: b[0].isupper(),s.split())))[1:]))
