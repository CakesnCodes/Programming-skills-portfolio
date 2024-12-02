#Vending_machine
import time #For adding delay
wares = {"A1":"Ruben's Rookies","A2":"ChipChap","A3":'"Honeyed Snack"',
          "B1":"Cheeselocks","B2":"Kritter Krunch","B3":"Pawpaws",
          "C1":"Water","C2":"Starlight Pop","C3":"Bowline Fizz",
          "D1":"Lenire's Leaves","D2":"Brewed Storm","D3":"Cre8ive Juice"}

price = {"A1":5.50,"A2":3.20,"A3":1.50,
         "B1":3.20,"B2":4.00,"B3":2.20,
         "C1":1.00,"C2":3.00,"C3":3.00,
         "D1":3.50,"D2":3.50,"D3":4.50,}

desc = {"A1":"Cookies with runes inscribed to them",
		"A2":"Lightly Salted Potato chips",
		"A3":"Hexagonal hardware fasteners covered in honey, Dubiously Edible",
        "B1":"Corn curls with cheese dusting",
		"B2":"Biscuits with chocolate insides, and creatures printed on the outside",
		"B3":"Paw-shaped gummies of assorted flavors",
        "C1":"Just your average bottle of water",
        "C2":"Raspberry-flavored Cola [A taste that's out of this world]",
        "C3":"Lemon-Lime soda [Something to float your boat]",
        "D1":"Lemon iced tea [A Miracle in a can]",
        "D2":"An Energy drink [Never strikes once]",
        "D3":"A fruit juice blend that simulates creativity [Art is a part of our heart]",}

quan = {"A1":5,"A2":4,"A3":6,
        "B1":5,"B2":5,"B3":7,
        "C1":7,"C2":6,"C3":8,
        "D1":7,"D2":3,"D3":3}
    
status = {"A1":"","A2":"","A3":"",
           "B1":"","B2":"","B3":"",
           "C1":"","C2":"","C3":"",
           "D1":"","D2":"","D3":""}
"""
^^^
Dictionaries that carry information about the products.

wares are the names of the products

desc are descriptions

quan are Quantities/stocks of products

status are for showing stock atatus

All the products (except water) are fictional
"""

act="" #For actions
skip= "" #For skipping code
inv= {"Allowance":15.00}
#inventory/basket system, Keys are item names, values are amount
#Allowance is set at 15

def what():#For when the user does an action that does nothing
    print("-You continue to stare at the machine-")
    time.sleep(2)
    
def buy(skip,sel): #For buying products
    cont=True #Variable continue set to true
    try:
        if skip != "Y": # if skip is not Y (Yes)
            while True:
                sel= input("What would you like to purchase? ").capitalize() #ask question
                if sel not in wares: #if the item selected is not in wares
                    print("Invalid Input") #print error message
                elif quan[sel]==0:
                    print("Sorry! item out of stock")
                else: #otherwise, continue
                    break
        while cont: #loop
            try:
                amt=int(input("How many would you like? ")) # how many of product
                if amt == 0: #If the amount is 0
                    print("Real funny...")
                elif quan[sel] < amt: #If the amount is more than what is in stock
                    print("You cannot have more than what is in stock")
                else:
                    print(f"This will cost {(price[sel] * amt)} AED")
                    if (price[sel] * amt) > inv["Allowance"]: #If the price is more than your allowance
                        print (f"Sorry! You only have {inv['Allowance']} AED of allowance left")                            
                        break #break loop
                    else:
                        while cont: #While 'cont' is True
                            try:
                                money=float(input("Input the amount you wish to pay with ")) #ask user for amount of money
                                if money < (price[sel] * amt): # if the money is more than the price of selected product time how many they want to buy
                                    print("Insufficient Funds")
                                elif money > inv["Allowance"]: # If money is higher than allowance
                                    print(f"-You only have {inv['Allowance']} AED of allowance-")
                                else: #if not
                                    quan[sel] -= amt #Subtract amount purchased from stock
                                    change (amt,sel,money) #Call change function
                                    cont = False #set 'cont' to false
                                    break #end loop
                            except ValueError:
                                what()                                                  
            except ValueError: #if the code fails, print following
                print("Invalid Input")                   
    except ValueError: #ditto ^
        print("Invalid Input")

def info(sel): #For describing products
    print(f"Item: {wares[sel]} | {desc[sel]}") #Displays name of product and description
    print(" ")    
        
def change (amt,sel,money): #For producing change and changing status
    inv["Allowance"] -= (price[sel] * amt) #Lowers allowance by item cost times the amount
    change = money - (price[sel] * amt) #Change is the money minus the item cost times the amount
    change = round(change,2) #rounds the change by 2 decimal points
    print("Processing payment...")
    time.sleep(2) #pause for effect
    print(f"-The Vending machine dispenses x{amt} {wares[sel]} and {change} aed of change-")
    if wares[sel] in inv: # if the selceted ware is in inventory
        inv[wares[sel]] += amt #updates amount of item
    else: #If not
        inv[wares[sel]] = amt #adds item and amount
    if quan[sel] <= 3 and quan[sel] != 0: #If the quantity is less or equal to 3 and not equal to 0
        status[sel] = "Low in Stock" #Set status as following
    elif quan[sel] == 0: # if quantity is 0
        status[sel] = "Out of Stock" #Set status as following
    print(f'-You have {inv["Allowance"]} left in your allowance-') #prints remaining allowance
  
def display (): #Prints vending machine display
    print(f"""
          =================Driscoll Vendors=================
          ~~~~~~~~~~~~~~~~~~~~~~Snacks~~~~~~~~~~~~~~~~~~~~~~
                                 
     [A1] Reuben's Rookies       amt:x{quan["A1"]}   cost:{price["A1"]}  {status["A1"]}
     [A2] ChipChaps              amt:x{quan["A2"]}   cost:{price["A2"]}  {status["A2"]}
     [A3] "Honeyed Snack"        amt:x{quan["A3"]}   cost:{price["A3"]}  {status["A3"]}
     [B1] Cheeselocks            amt:x{quan["B1"]}   cost:{price["B1"]}  {status["B1"]}
     [B2] Kritter Krunch         amt:x{quan["B2"]}   cost:{price["B2"]}  {status["B2"]}
     [B3] PawPaws                amt:x{quan["B3"]}   cost:{price["B3"]}  {status["B3"]}
            
          ~~~~~~~~~~~~~~~~~~~~~~Drinks~~~~~~~~~~~~~~~~~~~~~~
                          
     [C1] Water                  amt:x{quan["C1"]}   cost:{price["C1"]}  {status["C1"]}
     [C2] Starlight Pop          amt:x{quan["C2"]}   cost:{price["C2"]}  {status["C2"]}
     [C3] Bowline Fizz           amt:x{quan["C3"]}   cost:{price["C3"]}  {status["C3"]} 
     [D1] Lenire's Leaves        amt:x{quan["D1"]}   cost:{price["D1"]}  {status["D1"]}
     [D2] Brewed Storm           amt:x{quan["D2"]}   cost:{price["D2"]}  {status["D2"]} 
     [D3] Creative juice         amt:x{quan["D3"]}   cost:{price["D3"]}  {status["D3"]}  
        
     
        """)
    time.sleep(2)
    
print("-You come across a vending machine near the school-")   
while act !=4: #Loop when act does not equal to 4
    try:
        act=input("Would you like to approach it? [Y/N] ").capitalize()
        if act == "Y": #If user chooses yes
            print("-You decided to approach the machine-")
            cont=input("Press enter to continue ")
            display() #prints vending machine display
            while act != 4:
                try:
                    act=int(input("""
     What would you like to do?
                          
         [1] Purchase products
         [2] Examine products closely
         [3] Check inventory
         [4] Leave Machine
                          
                                 """)) #provides selection of actions
                            
                    if act == 1: #User chooses to purchase
                        if skip != "Y":   
                            buy("N","")
                        while True:
                            add = input("Would you like to purchase another product? [Y/N] ").capitalize()
                            if add == "Y":
                                display()
                                buy("N","")
                            elif add == "N":
                                display()
                                break
                            else:
                                what()
                    elif act == 2: #User chooses to examine
                        while act == 2:
                            ndesc = "" # For additional descriptions
                            sel= input("What would you like to examine? ").capitalize()
                            if sel in wares:
                                info(sel) #display info of product
                                while act == 2: # while act is 2
                                    skip= input("Would you like to purchase this option? [Y/N] ").capitalize()
                                    if skip == "Y": # If yes
                                        buy(skip,sel) #call buy function
                                        act = 1
                                        break
                                    elif skip == "N": #if not
                                        while ndesc != "N":
                                            ndesc = input("Would you like to examine another item? [Y/N] ").capitalize()
                                            if ndesc == "Y": #if yes
                                                skip=" "
                                                display()
                                                sel= input("What else would you like to examine? ").capitalize()
                                                if sel in wares:    
                                                    info(sel) #call info function
                                                    break
                                                else:
                                                    what()
                                            elif ndesc == "N": #if not
                                                skip=" " #
                                                act=" "
                                            else: #if other option
                                                what()
                                    else: #any other input
                                        what()                                                    
                            else:
                                what()
                    elif act == 3: #User chooses to check Inventory
                        for x, y in inv.items():
                            print(f"{x} x{y}")
                    elif act == 4: #User chooses to leave machine
                        print("Have a good day!")
                        print("-You walk away from the machine-")
                        break
                    else: #Users inputs something outside of selection
                        what()
                except ValueError:
                    what()
        elif act == "N": #If user chooses no
            print("-You decided to walk away from the machine-")
            break
        else: #If user inputs anything else
            what()
    except ValueError():#For when user encounters an error
        what()