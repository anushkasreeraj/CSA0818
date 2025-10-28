#wap to print area of the circle
p=3.14
r=int(input('radius='))
a=p*r**2
print('area=',a)

#simple int
p=eval(input('principle amt:'))
r=eval(input('rate:'))
t=eval(input('time:'))
si=p*r*t//100
print('si=',si)

#swap two no. without temp
x=int(input('x='))
y=int(input('y='))
x,y=y,x
print(x)
print(y)

#sq and cube of a no.
n=int(input('n='))
print('square of the given no.:',n**2)
print('cube of the given no. :',n**3)

#c to f
c=int(input('temp in c:'))
f=(c*5/9)+32
print('converted temp:',f)

#f to c
f=int(input('temp in f:'))
c=(f-32)*95
print(c)
