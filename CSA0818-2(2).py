#waf that converts celsius to fahrenheit
def cvertf(c):
    f=(c*5/9)+32
    return f
a=int(input('temp in celsius:'))
x=cvertf(a)
print('temp in f:',x)
