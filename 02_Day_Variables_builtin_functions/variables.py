#   Dylan Rossi
#   1.25.21
#   Day 2 of 30 Days of Python Programming

#   Day 2 Exercises Part 1:

#   Declaring and assigning values to variables
first_name = "Dylan"
last_name = "Rossi"
full_name = "Dylan J Rossi"
country = 'USA'
city = 'Laguna Niguel'
age = 32
year = 2021
is_married = False
is_true = True
is_light_on = False

#   example of a list
skills = ['Java', 'Python', 'C++', 'JavaScript']

# example of a dict / (dictionary?)
personal_info = {
    'full name': full_name,
    'country': country,
    'city': city,
    'age': age,
    'married?': is_married,
}

#   declare multiple variables in one line
dog_name, dog_age, dog_color, dog_gender = 'Juju', 2, 'black', 'Male'

#   print it all out
print('Name: ', full_name)
print("Country and City: ", country, city)
print("Age and Year: ", age, year)
print("Married?: ", is_married)
print("Leave the light on? ", is_light_on)
print("Personal Info: ", personal_info, "\nSkills: ", skills)
print("Dog's name: ", dog_name, '\nAge, Color, Gender: ', dog_age, dog_color, dog_gender)

#   Day 2 Exercises Part 2:
#   check the data types of variables:
print("Full name: ", type(full_name))
print("Country: ", type(country))
print("Year: ", type(year))
print("Is Married?: ", type(is_married))
print('age: ', type(age))
print("Personal Info: ", type(personal_info))
print("Skills: ", type(skills))

#   length function len()
print("Length of last name: ", len(last_name))
#   woooOOOOOooooo look at me go- interesting way of doing loops i guess
if len(last_name) > len(first_name):
    print("Last name is longer than first name")
if len(first_name) < len(last_name):
    print("First name is longer than last name")
else:
    print("The first and last names are the same length")

# Math part
num_one, num_two = 5, 4
variable_total = num_one + num_two
variable_diff = num_two - num_one
variable_product = num_two * num_one
variable_division = num_one / num_two
variable_remainder = num_two % num_one
variable_exp = num_one ** num_two
variable_floor_division = num_one // num_two
print(variable_total, variable_diff, variable_product,
      variable_division, variable_remainder, variable_exp, variable_floor_division)

#   radius of a circle
radius = 30
area_of_circle = 3.14159 * radius ** 2
circum_of_circle = 2 * 3.14159 * radius
print("The area of the circle is: ", area_of_circle)

#   taking user input (string) have to cast to float (or int) to perform math!!!
second_radius = float(input("Enter new radius: "))
new_area_of_circle = 3.14159 * second_radius ** 2
print("The area of the circle is: ", new_area_of_circle)

# user input of strings and storing in variables and printing
guest_first = input("Enter first name: ")
guest_last = input("Enter last name: ")
guest_country = input("Enter country: ")
guest_age = input("Enter your age: ")

print("First:", guest_first, "Last:", guest_last, "Country:", guest_country,
      "Age:", guest_age)
