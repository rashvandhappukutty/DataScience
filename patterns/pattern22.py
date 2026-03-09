n= int(input("Enter the number: "))
for i in range(2*n - 1):
    for j in range(2*n - 1):
        top = i
        left = j
        bottom = (2*n - 2) - i
        right = (2*n - 2) - j
        mindist = min(top, left, bottom, right)
        print(n - mindist, end=" ")
    print()