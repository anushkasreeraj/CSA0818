#repeated
def repeated(l):
  d={}
  for i in l:
    if i in d:
      d[i]+=1
    else:
      d[i]=1
  for k in d:
    if d[k]==2:
      return k
    else:
      continue
l=eval(input())
a=repeated(l)
print(a)

