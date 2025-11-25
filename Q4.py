def is_Perfect(n):
    sum = 0
    for i in range(1,n):
        if (n%i==0):
            sum+=i
    return sum==n
num = int(input("Enter a number: "))
print(is_Perfect(num))