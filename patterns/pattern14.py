n=int(input("Enter the number: "))
alpha = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for i in range(n):
    for j in range(i+1):
        print(alpha[j], end="")
    print()