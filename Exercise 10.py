#Exercise 10 - Is it even?

def odd_or_even(num): #define 'odd_or_even' function
    res = num % 2 #declare variable 'res' which is the remainder of num divided by 2
    return res

def main (): #define 'main' function
    
    num = int(input("Enter number ")) #Variable 'num' is user input
    res = odd_or_even(num) #calls 'odd_or_even' function for 'res' variable
    
    
    if res == 0 : #If res is equal to 0, display following
       print (f"{num} is an even number")
     
    else: #if not, display following
       print (f"{num} is an odd number")
    

main() #call main function
