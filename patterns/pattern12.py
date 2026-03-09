n = int(input("Enter the number: "))
spaces = 2 * (n-1)
for i in range(1, n + 1):
    for j in range(1,i+1):
        print(j, end="")
    for j in range(1, spaces + 1):
        print(" ", end="")
    for j in range(i,0,-1):
        print(j, end="")
    print()
    spaces -= 2