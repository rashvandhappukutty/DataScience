n=int(input("Enter the number: "))
num = 0
for i in range(n):
    print("*" * (n - i ), end="")
    print(" " * num, end="")
    print("*" * (n - i))
    num += 2
num = 2 * n - 2

for i in range(1 , n + 1):
    print("*" * i, end="")
    print(" " * num, end="")
    print("*" * i)
    num -= 2