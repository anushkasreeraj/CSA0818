#waf to calculate square of a number
def sqno(n):
    s=n**2
    return s
n=int(input('number='))
x=sqno(n)
print('sq.no:',x)

#waf that converts celsius to fahrenheit
def cvertf(c):
    f=(c*5/9)+32
    return f
a=int(input('temp in celsius:'))
x=cvertf(a)
print('temp in f:',x)

#waf area of circle
def area(r):
    a=3.14*r**2
    return a
r=int(input('radius:'))
x=area(r)
print('area:',x)

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
    
    

