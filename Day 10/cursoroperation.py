with open('Day 10/file.txt','r') as f:
    print(f.read())
    print(f.tell())
    f.seek(0)
    print(f.read())