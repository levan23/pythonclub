def can_i_spell_this(cards,word):
    count=0
    #word=word.upper()
    flag=False
    for i in word:
        for c in cards:
            for b in c:
                if i==b:
                    count+=1
                    cards=[i for i in cards if i!=c]
                    print(cards)
                    flag=True
                    break
            if flag:break
    return count==len(word)
#

cards=(('A','B'),('C','D'),('C','L'),('G','C'))
word="CDL"
print(can_i_spell_this(cards, word))