#to check if the given number is armstrong or not
r=d=0
n=int(input('enter a number:'))
m=n
while m:
    d=m%10
    r+=d**3
    m//=10
if r==n:
    print('the given no. is armstrong number')
else:
    print('the given no. is not an armstrong number')
