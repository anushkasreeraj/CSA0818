#perfect number
n=int(input('enter a number:'))
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
    else:
        continue
if s==n:
    print('the given number is a perfect number')
else:
    print('the given number is not a perfect number')
