def fibnacci(n):
    if n <= 1:
        return n
    else:
        return fibnacci(n-1) + fibnacci(n-2)

n = int(input("Enter the number of terms: "))
for i in range(n):
    print(fibnacci(i))
