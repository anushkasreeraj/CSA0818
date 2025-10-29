#check if given no. prime or not
n=int(input('enter the number whichn is to be checked:'))
for i in range(2,n//2+1):
    if n%i==0:
        print('the given number is not prime')
        break
else:
    print('the given number is a prime number')
