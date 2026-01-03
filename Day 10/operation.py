#Read
f=open('Day 10/file.txt','r')
readOperation = f.read()
print(readOperation)
f.close()

#Read line
f=open('Day 10/file.txt','r')
readOperation = f.readline()
print(readOperation)
f.close()

#Read lines
f=open('Day 10/file.txt','r')
readOperation = f.readlines()
print(readOperation)
f.close()