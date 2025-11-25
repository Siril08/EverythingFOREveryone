n = int(input("Enter a number: "))
sum = 0
while(len(str(n)) > 1):
    digit = n % 10
    sum = sum + digit
    n = n//10

print(sum)