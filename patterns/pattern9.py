n=int(input("Enter the number: "))
for i in range(n):
    print(" " * (n - i - 1), end="")
    print("*" * (2 * i + 1))
for j in range(n):
    print(" " * j, end="")
    print("*" * (2*(n-j)-1))
