#Exercise 7 - Some Counting

print("loop 0-50")
for i in range(51): #Create loop with a range of 51
    print (i) #Print current iteration
    
print(" ")    
print("loop 50-0")   
a=50 #create variable 'a' with value of 50
for i in range(51): #Create loop with a range of 51
    print(a) #display the value of a
    a -= 1 #subtract 1 from a
    
print (" ")    
print("loop 30-50")
for i in range (30,51): #Create loop with a range of 51, starting at 30
    print (i)  #Print current iteration
    
print (" ")
print ("loop 50-10")
b=50 #create variable 'b' with value of 50
for i in range(21): #Create loop with a range of 21
    print(b) #display the value of b
    b -= 2 #subtract 2 from b
    
print(" ")   
print("loop 100-200")    
for i in range (100,201,5): #Create loop with a range of 51, starting from 100, and increase by 5
    print(i)  #Print current iteration
