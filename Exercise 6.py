# Exercise 6 - Brute Force Attack

code = "12345" #declare code variable with the value "12345"
guess = input("Input password ") #request input from user
attempts = 5 #declare attempts variable with value of 5

while guess != code and attempts != 0:
    #While the input doesn't match the code, and the attempts don't equal to 0
    
    attempts = attempts - 1 #subtract 1 from attempts and declare as new value
    #Print the following message
    print(f"Oops! Incorrect Code, You have {attempts} attempts left")
    
    
    if attempts == 0: #If the attempts equal to 0, Print the following
        print("Sorry! You've inputted the wrong code 5 times")
        print("Security has been alerted")
        
    
    else:#if not
        guess = input("Input password ")
        
        
if code == guess: #if the code matches the guess
    print("Code accepted, Welcome")