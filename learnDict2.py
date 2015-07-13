#!/usr/bin/python
dict1={}
list1=['english','maths','economics','sanskrit','geography']
marks=(45,55,65,34,56)
for i in list1:
  if i not in list1:
    dict1[i.key]=[]
    dict1.setdefault(list1,[])
    dict1[list1].append(marks)
for key,value in dict1.items():
  print key
