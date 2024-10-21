# Exercise 3- Biography, advanced requirements

D={'name': [input ("What is your first name?").capitalize(), input("What is your last name? ").capitalize()],
   'hometown': input ("What's your hometown? ").capitalize(),
   'age': int(input ("How old are you? (Input as number) "))}

"""
Create a dictonary with the strings "name", "hometown", and "age" as keys
and user inputs as the values
"""

#Once all values are inputted, display the following:
print("-------------------------------")
print(f"Name: {D["name"]}")
print(f"Hometown: {D["hometown"]}")
print(f"Age: {D["age"]}")