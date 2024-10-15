n = 100
print(n >= 100)


a = 5 # a = float(input("Введіть число a: "))
b = 10 # b = float(input("Введіть число b: "))

if a > b:
    print(f"Найбільше число a: {a}")
else:
    print(f"Найбільше число b: {b}")


user_word = "Spathiphyllum" # user_word = input("Введіть слово: ")

if user_word == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif user_word == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
elif user_word == "pelargonium":
    print("Spathiphyllum! Not pelargonium!")
else:
    print(f"Spathiphyllum! Not {user_word}!")


income = 100000 # income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + 0.32 * (income - 85528)


if tax < 0:
    tax = 0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")


year = 1895 # year = int(input("Введіть рік: "))

if year < 1582 or year > 2024:
    print("Not within the Gregorian calendar period.")
else:
    if year % 4 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    elif year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")


secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while True:
  n = 777 # n = int(input("Напиши ціле число:"))
  if n != secret_number:
    print("Ха-ха! Ви застрягли у моїй петлі!")
    continue
  else:
    print("Молодець, магле! Тепер ти вільний.")
    break


import time

for i in range(1, 6):
  print(i, "Mississippi")
  time.sleep(1)

print("\nReady or not, here I come!")


while True:
    word = "chupacabra" # word = input("Enter the word: ")
    
    if word == "chupacabra":
        print("You've successfully left the loop.")
        break
    else:
        print("Ha-ha! You're stuck in my noose!")


word = "Gregory" # word = input("Enter the word: ")
word = word.upper()

for i in word:
  if i in ['A', 'E', 'I', 'O', 'U']:
    continue
  else:
    print(i)



word = "Gregory" # word = input("Enter the word: ")
word = word.upper()
word_without_vowels = ""

for i in word:
  if i in ['A', 'E', 'I', 'O', 'U']:
    continue
  else:
    word_without_vowels += i

print(word_without_vowels)


blocks = 20 # blocks = int(input("Enter the number of blocks: "))
height = 0
blocks_used = 0

while True:
  height += 1
  blocks_used += height

  if blocks_used > blocks:
    height -= 1
    break

print("Height of the pyramid:", height)


c0 = 15 # c0 = int(input("Enter the number: "))
steps = 0

while c0 != 1:
    print(c0)
    steps += 1
    
    if c0 % 2 == 0:
        c0 //= 2
    else:
        c0 = 3 * c0 + 1 

print(c0)
print("Steps =", steps)
