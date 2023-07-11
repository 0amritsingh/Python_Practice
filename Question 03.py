# Problem 3: Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

radius_of_circle = float(input("Enter radius of the Circle: "))
area_of_circle = ((22/7) * (radius_of_circle**2)) # formula a = pi r^2
print(f"The area of circle of radius {radius_of_circle} is {area_of_circle}")
