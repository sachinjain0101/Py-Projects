def showCount(str):
    w=str.split(' ')
    d=dict()
    for s in w:
        if d.has_key(s):
            d.update({s:d.get(s)+1})
        else:
            d.update({s:1})
    return d
    

l='sachin jain jain'

print showCount(l)
