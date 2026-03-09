n=int(input("Enter the number: "))
alpha = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for i in range(n):
    for j in range(n-i):
        print(chr(65+j), end="" )
    print()