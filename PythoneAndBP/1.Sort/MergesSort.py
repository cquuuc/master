a=[1,2,3,4]
b=[5,6,7,8]
i=0
j=0
res=[]

while i<len(a) and j<len(b):
  if a[i]==b[j]:
    res.append(a[i])
    res.append(b[j])
    i+=1
    j+=1
  elif a[i]<b[j]:
    res.append(a[i])
    i+=1
  else:
    res.append(b[j])
    j+=1
if i<len(a):
  res+=a[i:]
if j<len(b):
  res+=b[j:]

print(res)
  