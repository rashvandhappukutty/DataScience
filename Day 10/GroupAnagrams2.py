from collections import defaultdict 
a=defaultdict()
words=["apple","banana","rat","orange","tiger","dog","eat","tea","ate","tan",]
anagram_groups = defaultdict(list)
for word in words:
    anagram_groups[''.join(sorted(word))].append(word)
print(dict(anagram_groups))