import traceback
import random
import math

def sep():
    print '*' * 60

def displayList(lst,msg='Default'):
    print '*' * 60
    print msg+' - '+str(lst)
    print '*' * 60

def factorial(num):
    #print num
    if(num == 0):
        return 1
    else:
        return num * factorial(num - 1)

def cummSum(lst):
    x=0
    l=list()
    for i in lst:
        x = x+i
        l.append(x)    
    return l

def oddPos(lst):
    l=list()
    count=0
    for i in lst:
        if count % 2 != 0 :
            l.append(i)
        count+=1
    return l

def numToList(num):
    return list(str(num))

lst1 = [1,2,3,4,5]
lst2 = ['a','b']
lst3 = lst1 + lst2
displayList(lst3)
    
displayList(lst1,'Input List')
displayList(cummSum(lst1),'Cummulative Sum')
displayList(oddPos(lst1),'Odd Position')
displayList(factorial(4),'Factorial')
displayList(factorial(5),'Factorial')
displayList(numToList(5123456789),'Num to List')
displayList(math.fabs(random.random()*100))

name = 'my name is sachin jain'
lst = list(name)
displayList(lst)

lst = name.split(' ')
displayList(lst)

sep()
i = len(lst)
while i > 0:
    print lst[i - 1]
    i-=1

sep()

print name[1:4]
print name[10:]

sep()

lst = [1,2]
lst.append(3)
displayList(lst)

x=(1,2)
displayList(x)
print x.index(2)

d={11:'a',20:'b',30:'c'}
print d
print d.keys()
print d.values()
try:
    d.pop(1)
except:
    traceback.print_stack()

print d
print type(d)
print type(x)

i=0
while(i<=10):
    d.update({i:i*10})
    i+=1

print d

y=list()
y.append(1)
print y

y=tuple((1,2))
print y

y=dict()
y.update({1:1})
print y

