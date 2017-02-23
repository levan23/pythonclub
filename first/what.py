
def say_hello(person_name):
    return ("Hello {}!".format(person_name))

name = "Levan"
#say_hello(name)

resulting_string =say_hello(name)
#print(resulting_string)

persons= ["Levan","Papo","Toko"]
for p in persons:
    hello_message=say_hello(p)
    print(hello_message)

index=0
while len(persons)>index:
    print(persons[index])
    index+=1
