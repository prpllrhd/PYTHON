#!/Users/samy/anaconda/bin/python
names=['samy','rahul','samy','rakhee']
dict={}
for i in names:
  if dict.has_key(i):
    dict[i]+=1
  else:
    dict[i]=1
print dict
