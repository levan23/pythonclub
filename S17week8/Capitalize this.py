def capitalizing_this(input_string):
    if (type(input_string) is not str):
        return
    return ' '.join(w[0].upper() + w[1:].lower() for w in input_string.split())