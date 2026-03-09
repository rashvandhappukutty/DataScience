n=int(input("Enter the number: "))
alpha =("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

for i in range(n):
    print(" " * (n - i - 1), end="")
    for j in range(i + 1):
        print(alpha[j], end="")
    
    for j in range(i - 1, -1, -1):
        print(alpha[j], end="")
    print()