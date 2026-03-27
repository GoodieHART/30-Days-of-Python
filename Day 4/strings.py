# Challenge 1
str1, str2, str3, str4 = "Thirty", "Days", "of", "Python"
print(str1 + str2 + str3 + str4) # this will give us combined string with no space

challenge_words = ["Thirty", "Days", "of", "Python"]
print(' '.join(challenge_words)) # here we are using the join method to add a space inbetween each array elements

# No. 2 
coding_words = ["Coding", "For", "All"]
print(' '.join(coding_words))

# No. 3-11
company = "Coding For All"
print(company + '; ' + "Length = " + str(len(company)))

print(company.upper() + ' ' + company.lower())

print(company.capitalize().title().swapcase()) # first iterates through the first capitalize, then title, finally swapcase

print(company[0:6]) # to print only "Coding"
print(company[-7:]) # to print only "For All"

print(company.find("Coding"))
print(company.index("Coding"))
print(company.rindex("Coding"))

# No. 11
print(company.replace("Coding", "Python"))

# No. 12
python_words = "Python For Everyone"
print(python_words.replace("Everyone", "All"))

# No. 13
print(company.split(" ")) # will work if the used character is present in the string

# No. 14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))

# No. 15, 16, 17  
print(company[0])
print(company[-1])
print(company[10])

# No. 18
print(python_words.find("P"), python_words.find("F"), python_words.find("E")) # 0, 7, 11
print('.'.join(python_words[0] + python_words[7] + python_words[11]), "-" , python_words)

# No. 19
print('.'.join(company[0] + company[7] + company[11]), "-", company)

# No. 20, 21, 22
print(company.index("C"))
print(company.index("F"))
print(company.rfind("l"))

# No. 23, 24, 25
because_conj = "You cannot end a sentence with because because because is a conjunction"
print(because_conj.index("because"))
print(because_conj.rindex("because"))
print(because_conj.replace("because", ""))

# No. 28
print(company.startswith("Coding"))

# No. 29
print(company.endswith("Coding"))

# No. 30
print(" Coding For All ".strip(" "))

# No. 31
print("30DaysofPython".isidentifier(), "thirty_days_of_python".isidentifier())

# No. 32
print('# '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

# No. 33
print("I am enjoying this challenge.\nI just wonder what is next.")

# No. 34
print('Name\tAge\tCountry\tCity')
print('Goodie\t999\tNigeria\tnul')

# No. 35
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {:.1f} meters square".format(radius, area))

# No. 36
num1 = 8 
num2 = 6 

print("{} + {} = {}".format(num1, num2, num1+num2)
)
print("{} - {} = {}".format(num1, num2, num1-num2))
print(f"{num1} * {num2} = {num1*num2}")
print(f"{num1} / {num2} = {num1/num2:.2f}")
print(f"{num1} % {num2} = {num1%num2}")
print(f"{num1} // {num2} = {num1//num2}")
print(f"{num1} ** {num2} = {num1**num2}")