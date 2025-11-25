n = int(input("Enter n: "))

list = []
print("Enter the numbers:")
for i in range(n):
    list.append(int(input()))

print("Original List:", list)

even_sum = 0
for x in list:
    if x % 2 == 0:
        even_sum += x

list.append(even_sum)
print("List after appending sum of even numbers:", list)

odd_count = 0
for x in list:
    if x % 2 != 0:
        odd_count += 1

list.insert(1, odd_count)
print("List after inserting count of odd numbers at index 1:", list)

list.pop()
print("List after removing last element:", list)

print("First 3 elements:", list[:3])

total = sum(list)
print("total is:", total)

average = total / len(list)
print("Average:", average)
