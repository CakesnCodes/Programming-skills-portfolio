#Exercise 8 - Simple search, Advanced requirements

search= input("Enter name ").capitalize()
#Requests user input, Input it converted into proper capitalization
names = ["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"] 
#Create list called 'names'

if search in names: #If the user input is found within the list
    print(f"{search} found")
    
else: # If not
    print (f"Sorry! {search} Not found")
    