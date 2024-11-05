#1
def is_year_leap(year):
	return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) 

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end=" ")
	result = is_year_leap(yr)
	print(result)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
		
#2
def is_year_leap(year):
  return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

def days_in_month(year, month):
  if month < 1 or month > 12:
    return None
  if year < 1:
    return None
  
  days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  if month == 2:
    if is_year_leap(year):
      return 29
    else:
      return 28
    
  return days_in_months[month - 1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
  yr = test_years[i]
  mo = test_months[i]
  print(yr, mo, "->", end=" ")
  result = days_in_month(yr, mo)
  if result == test_results[i]:
    print("OK")
  else:
    print("Failed")

#3
def is_year_leap(year):
  return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

def days_in_month(year, month):
  if month < 1 or month > 12:
    return None
  if year < 1:
    return None
  
  days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  if month == 2:
    if is_year_leap(year):
      return 29
    else:
      return 28
    
  return days_in_months[month - 1]

def day_of_year(year, month, day):
  if year < 1 or month < 1 or month > 12 or day < 1:
    return None
  
  days_in_this_month = days_in_month(year, month)

  if day > days_in_this_month:
    return None

  day_of_year = 0
  for i in range(1, month):
    day_of_year += days_in_month(year, i)

  day_of_year += day

  return day_of_year
  
print(day_of_year(2000, 12, 31))

#4
def is_prime(num):
  if num < 2:
    return False
  
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  
  return True

for i in range(1, 20):
  if is_prime(i + 1):
    print(i + 1, end=" ")
print()

#5
def liters_100km_to_miles_gallon(liters):
  return ((100 / 1.609344) / (liters / 3.785411784))

def miles_gallon_to_liters_100km(miles):
  return ((100 * 3.785411784) / (miles * 1.609344))

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

#6
def is_a_triangle(a, b, c):
  if a + b > c and a + c > b and b + c > a:
    return True
  else:
    return False

print(is_a_triangle(5, 20, 7))

#7
def is_a_triangle(a, b, c):
  if a + b > c and a + c > b and b + c > a:
    return True
  else:
    return False
  
def is_a_right_triangle(a, b, c):
  if not is_a_triangle(a, b, c):
    return False
  
  s = sorted([a, b, c])
  a1 = s[0]
  b1 = s[1]
  c1 = s[2]

  if c1**2 == a1**2 + b1**2:
    return True
  else:
    return False
  
print(is_a_right_triangle(5, 3, 4))