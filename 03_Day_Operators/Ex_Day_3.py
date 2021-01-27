#   Dylan Rossi
#   1.26.21
#   Day 3 Exercises of 30 Day Python Challenge

#   Boolean and operators

myAge = 32
myHeight = 72.0
complexNum = (6 + 3j)

#   calculate area of triangle with user input
base = float(input("Enter base: "))
height = float(input("Enter height: "))
print("\nThe area of the triangle is ", (.5 * base * height))

#   calculate perimeter of triangle with user input
sideA = float(input("\nEnter side a: "))
sideB = float(input("Enter side b: "))
sideC = float(input("Enter side c: "))
print("\nThe perimeter of the triangle is ", (sideA + sideB + sideC))

#   area and perimeter of rectangle
length = float(input("\nEnter the length: "))
width = float(input("Enter the width: "))
print("\nThe area of the rectangle is ", (length * width),
      " and the perimeter is: ", (2 * (length + width)))

#   area and circumference of a circle
radius = float(input("\nEnter the radius: "))
print("\nThe area of the circle is", (radius * radius * 3.14),
      " and the circumference is", (6.28 * radius))

#   Calculate the slope, x-intercept and y-intercept of y = 2x -2
yInt = 2 * 0 - 2
xInt = -2
slope = (0 - 2) / (1.5 + 2)
print("\nSlope: ", slope)

#   Slope is (m = y2-y1/x2-x1). Find the slope between point (2, 2) and point (6,10)
#   Compare the slopes in tasks 8 and 9.
slope = (10 - 2) / (6 - 2)
print("\nNow slope is: ", slope)

#   Calculate the value of y (y = x^2 + 6x + 9).
x = 0
y = (x ** 2) + (6 * x) + 9
print("\nx is 0, y = ", y)
x = 1
y = (x ** 2) + (6 * x) + 9
print("\nx is 1, y = ", y)

#   Find the length of 'python' and 'jargon' and make a falsy comparison statement
print(len('python') == len('jargon'))
#   Use and operator to check if 'on' is found in both 'python' and 'jargon'
print("\n'on' in jargon and python? ", ('on' in 'jargon' and 'on' in 'python'))
#   Use in operator to check if jargon is in the sentence
print("\n'in' in the sentence? ", 'in' in 'I hope this course is not full of jargon')
#   There is no 'on' in both dragon and python
print("\n 'on' in dragon and python? ", 'on' in 'dragon' and 'on' in 'python')
#   Find the length of the text python and convert the value to float and convert it to string
strLen = float(len('python'))
print("\nString length = ", strLen)
strLen: str = str(strLen)
print("\nString length is now a string = ", strLen)
print("\nIs type '10' == 10? ", type('10') == 10)

#   Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person
hours = float(input("\nEnter hours: "))
rate = float(input("Enter rate per hour: "))
print("\nYour weekly earning is ", hours * rate)

#   Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live.
#   Assume someone lives up to hundred years
years = (int(input("\nEnter number of years you have lived ")))
print("You have lived for ", (years * 365 * 24 * 60 * 60), " seconds")
#   Display table
print("\n1\t1\t1\t1\t1")
print("2\t1\t2\t4\t8")
print("3\t1\t3\t9\t27")
print("4\t1\t4\t16\t64")
print("5\t1\t5\t25\t125")
