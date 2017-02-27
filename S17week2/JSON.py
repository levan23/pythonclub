import json
def total_score(j):
    sum=0
    parsed=json.loads(j)
    for key, value in parsed.items():
        sum+=value
    data={}
    data["total_score"]=sum
    return json.dumps(data)
    #return data    ? why not?


print(total_score('{"john": 10, "steve": 31}'))
