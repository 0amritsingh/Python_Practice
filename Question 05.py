# Problem 5: Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

x = str(input("Enter a elements by spliting them with a comma ','\n>>> "))
y = list(x.split(",")) # converting user string into list and spliting their element as per the comma 
z = tuple(x.split(",")) # split() function is used to manuplulate string and convert it into list or tuple
print(f"Sring {x} is converted into:\nList: {y}\nTuple: {z}")
