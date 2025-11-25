n = int(input("Enter how many numbers you want to enter: "))
sum = 0
for i in range(n):
    num = int(input("Enter the number: "))
    if(num%3==0):
      sum = sum + num
print(sum)