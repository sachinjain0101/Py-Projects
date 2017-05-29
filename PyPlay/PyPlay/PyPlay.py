
def displayList(lst):
    print '*'*60
    for a in lst:
        print a
    print '*'*60

lst = [1,2,'a']

print lst

displayList(lst)
    
name = 'my name is sachin jain'
lst = list(name)
displayList(lst)

lst=name.split()
displayList(lst)

print len(name)

name='sachin'

for char in name:
    print char

i=len(name)
while i>0:
    print name[i-1]
    i-=1


print name[1:4]
print name[1:]

print 