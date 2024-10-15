import math

x = 0
u = 0
sigma = 1

result = (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(- (math.pow(x - u, 2) / 2 * sigma ** 2))
print(result)

john = 3
mary = 5
adam = 6


print(john, mary, adam, sep=', ')
total_apples = john + mary + adam
print(total_apples)

print("Загальна кількість яблук:", total_apples)

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# x = float(input("Enter number x: "))
x = 1

y = 3 * x ** 3 - 2 * x ** 2 + 3 ** x - 1

print("y =", y)

# this program computes the number of seconds in a given number of hours

a = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Hours: ", a) # printing the number of hours
print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours

a = 5 # a = float(input("Введіть значення a: "))
b = 5 # b = float(input("Введіть значення b: "))

addition_result = a + b
print("Результат додавання:", addition_result)

subtraction_result = a - b
print("Результат віднімання:", subtraction_result)

multiplication_result = a * b
print("Результат множення:", multiplication_result)

division_result = a / b
print("Результат ділення:", division_result)

print("\nThat's all, folks!")

x = 1 # x = float(input("Enter value for x: "))

y = 1 / (x + 1 / (x + 1 / (x + 1 / (x + 1 / x))))

print("y =", y)

hour = 12 # hour = int(input("Starting time (hours): "))
mins = 17 # mins = int(input("Starting time (minutes): "))
dura = 59 # dura = int(input("Event duration (minutes): "))

t_mins = mins + dura
r_hour = hour + t_mins // 60
r_mins = t_mins % 60

r_hour = r_hour % 24

print(f"Час закінчення: {r_hour:02}:{r_mins:02}")