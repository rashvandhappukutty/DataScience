n=int(input("Enter the number: "))
for i in range(n):
    print(" " * i, end="")
    print("*" * (2*(n-i)-1))
