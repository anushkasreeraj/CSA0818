#factorial
n=int(input('enter the numb er for which the facorial is to be obtained'))
f=1
for i in range(1,n+1):
    f*=i
print('factorial of the given number is:',f)
