#Exercise 4 - Primitive quiz, advanced requirements

points = 10

#Declare points variable as 10

capitals= {0:"Paris",
         1:"Madrid",
         2:"Moscow",
         3:"Stockholm",
         4:"Havana",
         5:"Amsterdam",
         6:"London",
         7:"Budapest",
         8:"Athens",
         9:"Berlin"}

#Declare "capitals" dictonary that containins the answers

countries= {0:"France",
         1:"Spain",
         2:"Russia",
         3:"Sweden",
         4:"Cuba",
         5:"The Netherlands",
         6:"The United Kingdom",
         7:"Hungary",
         8:"Greece",
         9:"Germany"}

#Declare "countries" dictonary that contains the countries matching the capitals

hint= {0:'"This place is also known as the city of lights"',
         1:"This is the second largest city in Europe",
         2:"A popular german song sang about this capital",
         3:"This Capital is the home of the Nobel Prize",
         4:"One of Camila Cabello's most popular songs is named after this place",
         5:"This place is known for its numerous canals",
         6:"This is one of the world's major global cities",
         7:"Hawkeye and Black Widow mention this location as a one-off joke",
         8:"This capital is named after the greek goddess of wisdom",
         9:'"MR. GORBACHEV, TEAR DOWN THIS WALL"'}
#Declare "hints: dictonary that contains hints to capitals


for i in range(10): #loop the following 10 times

    answer = capitals[i] 
    #The answer is a value within the dictonary (the key is the current iteration)
    useranswer = input("What is the capital of " + countries[i] + "? ").capitalize()
    #requests input from uses and converts the first letter into uppercase and the rest lowercase
    #the input is then declared as value to the variable "useranswer"
    
    while useranswer != answer: #loops while the input matches the answer
            print(" ")    
            print("*EXTREMELY INCORRECT BUZZER SOUND*") #Display humerous message
            print("Hint:" + hint[i]) #Provide corresponding hint to the question
            hint[i] = "Hint given" #replace current hint with string
            useranswer = input("What is the capital of " + countries[i] + "? ").capitalize()
            #ask the question again
            
    #once the Loop is finished, display the following        
    print(" ")
    print("Correct!")
    
    if hint[i] == "Hint given": # if the hint is replaced
        points -= 1 #deduct 1 from points
        
#Once the loop is finished

print("TEST COMPLETE") #print string
print("Correct answers:", points) #print string and point total
