#leap year or nott

yr=int(input('enter the year which is to be checked:'))
if yr%4==0 and yr%400==0:
    print('the given year is a leap year')
else:
    print('the given year is not a leap year')
