from collections import defaultdict

# Initialize defaultdict with list as the default factory
a = defaultdict(list)  # This will create a new list for each new key

words = ["apple", "banana", "rat", "orange", "tiger", "dog"]

for word in words:
    a[len(word)].append(word)

print(dict(a))  # Convert to dict for better readability