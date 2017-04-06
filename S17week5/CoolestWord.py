def coolest_word(words):
    return max(words,key=lambda a:len(set(a))) if len(words)!=0 else None
