#LIST

lis = ["csda","aids","aiml","mscds"]
print(lis)
lis.append("ca") #it appends at the last
print(lis)
lis.insert(0,"csa") #insert the element using index value
print(lis)
lis.pop(0)
print(lis)
lis.pop()
print(lis)

#SET

se = set()
se.add("csda")
se.add("aids")
se.add("aids")
print(se)
se1 = {1,7,"aids"}
se2 = se1 | se #this will give error as set does not support concatenation
print(se2)
se3 = se1 & se
print(se3)

#DICT

dict1 = dict()
dict1 = {"name":"Rashvandh","course":"aiml","duration":"3 years"}
print(dict1)
dict1["course"] = "csda"
print(dict1)
dict1["level"] = 1
print(dict1)

#TUPLE

tup = tuple()
print(tup)
tup1 = tup + ("csda","aids","aiml")
print(tup1)
print(tup1.index("aiml"))

#Collection

from collections import Counter
cnt = Counter(tup1)
print(cnt)
print(cnt.most_common(2))
print(cnt.clear())
print(cnt.most_common(2))