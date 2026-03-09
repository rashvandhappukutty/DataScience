n=int(input("Enter the number:"))
alpha = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for i in range(n):
    start = n - i - 1
    for j in range (start, n):
        print(alpha[j], end="")
    print()