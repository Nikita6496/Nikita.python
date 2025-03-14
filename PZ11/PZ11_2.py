numbers = [10, 11, 12, 13, 14, 15, -16]
count = len(numbers)
new_s = []
for i in range(1, count -1):
    new_e = (numbers[i - 1] + numbers[i + 1]) ** 2
    new_s.append(new_e)
print(new_s)