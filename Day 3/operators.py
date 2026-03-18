age = 10
height = 45.45
complex_num = 4 + 89j

triangle_base, triangle_height = int(input("Triangle Base: ")), int(input("Triangle Height: ")) # remember to cast user input to int or float
triangle_area = 0.5*triangle_base*triangle_height 
print("Triangle Area: ", triangle_area)

a_side = int(input("Triangle Side A: ")) # initially, i tried casting a string to a float, which does not work, so cast to int instead
b_side = int(input("Triangle Side B: "))
c_side = int(input("Triangle Side C: "))
perimeter = a_side + b_side + c_side
print("Triangle's Perimeter = ", perimeter)

# Perimeter of a Rectangle
length_rectangle = int(input("Rectangle Length: "))
width_rectangle = int(input("Rectangle Width: "))
area_rectangle = length_rectangle * width_rectangle
perimeter_rectangle = 2 * (length_rectangle + width_rectangle)
print("Rectangle Area: ,", area_rectangle, "Rectangle Perimeter: .", perimeter_rectangle)


# Area of A Circle & Circumference of a Circle
pi = 3.14
circle_radius = float(input("What is The Circle's Radius? > "))

circle_circumference = 2 * pi * circle_radius
circle_area = pi * circle_radius**2

print("Circle Area: ", circle_area, "Circumference: ", circle_circumference)

# No 9. Slope and Euclidean Distance 
x1 = 2
x2 = 6
y1 = x1
y2 = 10

slope_of_coords = (y2 - y1) / (x2 - x1)
print("Slope of Coords: ", slope_of_coords)

x3 = (x2 - x1) ** 2 # Adjacent side 
y3 = (y2 - y1) ** 2 # Opposite side

euclidean_distance = (x3 + y3) ** 0.5 # Hypotenuse 
print("Euclidean Distance: ", euclidean_distance)

# No 11. 
x = [0, 1 , 2, 3, 4, 5]

for nums in x:
  y = (nums**2) + (6*nums) + 9
  print(y)
  
# No. 12 Find the length of ‘python’ and ‘dragon’ and make a falsy comparison statement.
first_animal = "python"
second_animal = "dragon"

len_animal_one = len(first_animal)
len_animal_two = len(second_animal)

result = not len_animal_two == len_animal_two
print(result)

# No. 13 Use and operator to check if ‘on’ is found in both ‘python’ and ‘dragon’

on_in_animals = "on" in first_animal and "on" in second_animal # take note that this is split into 2 statements, one firsts evaluates then moves to the next then compares
print(on_in_animals)

# No. 14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

sentence = "I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence."

check_for_jargon = "jargon" in sentence

# No. 15 There is no ‘on’ in both dragon and python

no_on_in_both = "on" not in first_animal and "on" not in second_animal
print(no_on_in_both)

# No. 16 Find the length of the text python and convert the value to float and convert it to string

len_python = len(first_animal)
python_to_float = float(len_python)
py_float_to_string = str(python_to_float)
print(py_float_to_string)
print(type(py_float_to_string))

# No. 17 Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

number = 7373
print(number % 2 == 0) # Here's where the check happens, on evaluation, if the result is False "number = odd", if True "number = even"

# No. 18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

floor_div = 7 // 3 
float_to_int = int(2.7)
print(floor_div == float_to_int) # on evaluation, the float 2.7 will be converted to just 2 and the floor division of 7 and 3 is 2, so they are equal

# No. 19 Check if type of ‘10’ is equal to type of 10

print(type(10) == type("10")) # False

# No. 20 Check if int(‘9.8’) is equal to 10

print(int('9.8') == 10) #ValueError: invalid literal for int() with base 10: '9.8'

# No. 21 Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours_of_work = int(input("How Many Hours Do You Work?: "))
rate_per_hour = int(input("What You Like To Be Your Pay Rate?: "))

print("Your Weekly Earnings = ", hours_of_work * rate_per_hour)

# No. 22 Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

one_year_to_seconds = 31557600
user_age = int(input("How Old Are You In Years?: "))
print("You Have Lived For:" , one_year_to_seconds * user_age, "seconds")

"""
No. 23 Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
# Now it's comming to me! its a powers table, i'll come back much later, because i dont know if they want us to use loops 🙃
