#Exercise 5 - Months of the day

Days= {"1":"31", "2":"?", "3":"31", "4":"30", "5":"31", "6":"30",
      "7":"31", "8":"31", "9":"30", "10":"31", "11":"30", "12":"31"}
#Create a Dictionary named "Days". The keys are the Months, and Values are Days

Months= input("Please input the number of a month ")

#Request an User input and assign it to "Months" Variable

if Months in Days: #If the input is a key in the days dictionary
    if Months == "2":# If the input is 2 for Febuary
        leap = input("Is it a leap year? (y/n) ").lower()
        #Requests user input asking if the Year is a leap year
        if leap == ("y"): #if yes
            print("This month has 29 days")
        else: #if not
            print("This month has 28 days")
    else:# if the user input is asking for another month instead:
        print(f"This month has {Days[Months]} Days")
        
else: # if not
    print ("Sorry! You have to input a number associated with the month")