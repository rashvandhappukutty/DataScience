from collections import defaultdict 
a=defaultdict()
words=["apple","banana","rat","orange","tiger","dog"]

for word in words:
    a[len(word)].append(word)
print(list(a.values()))