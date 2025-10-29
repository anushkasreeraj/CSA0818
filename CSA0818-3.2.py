#sum of digits of 2numbers

s=0
n=int(input('enter a number:'))
m=n
while m:
    d=m%10
    s+=d
    m//=10
print('sum of digits =',s)
