# Day 2: 30 Days of Python Training

first_name = "Ace"
last_name = "Potatoe" # Im a Potatoe
full_name = "Ace Potatoe Sauce"
country = "Potatoe Island"
city = "Irish Springs"
age = 9000 # Old Potatoe
year = 1895
is_married = True # of course I am! I've got multiple wives too!
is_true = False
is_light_on = False

fastest_cpu, chopping_board, art_period = "Potaoe Grater F9", "Wood", "Renaissance"

# print(type(first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on, fastest_cpu, chopping_board, art_period)) # This will produce the error: TypeError: type() takes 1 or 3 arguments

print(len(first_name))
print("First Name Length: ", len(first_name), "Last Name Length: ", len(last_name))
print(first_name == last_name)

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exponent = num_one ** num_two
floor_division = num_one // num_two

print("Sum of Num1 & Num2: ", total)
print("\n")
print("Difference of Num1 & Num2: ", diff)
print("\n") # Print a new line after the output of the previous
print("Product: ", product , "Division: ", division, "Remainder: ", remainder, "Exponent: ", exponent, "Floor Division: ", floor_division)

static_radius = 30
pi = 3.14
area_of_circle = pi * (static_radius**2)
circum_of_circle = 2 * pi * static_radius
print("Area of Circle: ", area_of_circle, "Circumference of Circle: ", circum_of_circle)

user_radius = int(input("Radius of Circle > "))
area_of_circle_input = pi * (user_radius**2) # First run without casting user input will give this error - TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int', so we firstly cast the user input to an integer 
print("User Supplied Circle Area:" , area_of_circle_input)

first_name , last_name , country , age = input("First Name: "), input("Last Name: "), input("Country: "), input("Age: ")
print("\n")
print("First Name: ", first_name, "Last Name: ", last_name, "Country: ", country, "Age: ", age)

