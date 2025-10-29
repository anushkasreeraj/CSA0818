#factors of the giiven number
l=[]
n=int(input('enter a number for which factors are to be found:'))
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
    else:
        continue
print('the given number has',len(l),'factors')
print('factors of the given number are:')
for j in l:
    print(j)
