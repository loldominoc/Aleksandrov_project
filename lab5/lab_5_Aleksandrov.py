hat_list = [1, 2, 3, 4, 5]
print(hat_list) 

index = 1 # index = int(input("Введіть індекс (0-4) для заміни числа: "))
value = 20 # value = int(input("Введіть нове число: "))
hat_list[index] = value
print(hat_list)

hat_list.pop()
print(hat_list)

print(len(hat_list))
print(hat_list)

numbers = [423, 12, 542, 31, 2, 6, 97, 121, 102, 10]

for i in range(len(numbers)):
  for j in range(len(numbers) - 1):
    if numbers[j] > numbers[j + 1]:
      numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print(my_list)

my_list = list(set(my_list))

print("The list with unique elements only:")
print(my_list)

chessboard = [['_'] * 8 for _ in range(8)]

chessboard[0][0] = "R"
chessboard[0][7] = "R"
chessboard[7][0] = "R"
chessboard[7][7] = "R"

for row in chessboard:
  print(" ".join(row))