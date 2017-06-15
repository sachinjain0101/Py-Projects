from multiprocessing.pool  import ThreadPool


global x
x=10

def foo():
    x=100
    print x

def bar():
    print x

print x
foo()
bar()