#waf max of 2 no.
def maxno(a,b):
    if a>b:
        return a
    else:
        return b
x=int(input('x='))
y=int(input('y='))
a=maxno(x,y)
print('max no.:',a)
