# using the add method
def fib(n):         
    f = []
    a, b = 0, 1
    while a < n:
        f.append(a)
        a, b = b, a + b
    return f
print(fib(10))
        
# using a generator
def fib(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
print(list(fib(10)))
# add first string
# 789
