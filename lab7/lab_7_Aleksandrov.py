#1
numbers = [10, 4, 43, 2, 11, 19, 7, 6, 32]

numbers_tuple = tuple(numbers)

n = 15 # n = int(input("Введіть число n: "))

rslt = [num for num in numbers_tuple if num < n]

print("Числа з кортежу, які менші за", n, ':', rslt)

#2
names = ("Alice", "John", "Tom")
print(names)

rslt = ", ".join(names)

print(rslt)

#3
book = {
    "name": "1984",
    "author": "George Orwell",
    "number_of_pages": 328,
    "year_of_publication": 1949
}

print(f"Назва: {book['name']}")
print(f"Автор: {book['author']}")
print(f"Кількість сторінок: {book['number_of_pages']}")
print(f"Рік видання: {book['year_of_publication']}")

#4
students = {
  "Іванов": ("Іван", 19, 4.1),
  "Шевченко":("Ольга, 20, 4.8"),
  "Кондра":("Олександр", 20, 5.0)
}

surname = "Кондра" # surname = input("Введіть прізвище: ")

name, age, average_grade = students[surname]

if surname in students:
  name, age, average_grade = students[surname]

  print(f"Ім'я: {name}")
  print(f"Вік: {age}")
  print(f"Середній бал: {average_grade}")
else:
  print("Такого студента немає.")

#5
def add_phone_number(name, number):
  if name in phone_book:
    phone_book[name].append(number)
    print(f"Номер {number} додано до контакту {name}.")
  else:
    print(f"Контакт {name} не знайдено в телефонній книзі.")

phone_book = {
    "Іван": ["123-4567", "234-5678"],
    "Ольга": ["340-6780"],
    "Петро": ["446-7890", "567-0901", "678-9002"],
}

print("Телефонна книга:")
for i, j in phone_book.items():
  print(f"Контакт: {i}, Номери: {', '.join(j)}")

print('')
add_phone_number("Ольга", "444-8888")
add_phone_number("Ольга", "912-4545")
add_phone_number("Іван", "777-7777")
add_phone_number("Олександр", "666-6666")

print("\nТелефонна книга:")
for i, j in phone_book.items():
  print(f"Контакт: {i}, Номери: {', '.join(j)}")
