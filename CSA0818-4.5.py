#fibonacci series

n=int(input('enter no. of terms:'))
a,b=0,1
c=0
l=[0,1]
for i in range(n-2):
    c=a+b
    l.append(c)
    a=b
    b=c
print('fibonacci series for the given number is:')
for j in l:
    print(j)
