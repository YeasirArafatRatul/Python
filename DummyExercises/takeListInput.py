
#Uing map()

# number of elements 
n = int(input("Enter number of elements : ")) 
  
#Below line read inputs from user using map() function
#list comprehension
#give space seperated inputs
a = list(map(int,input("\nEnter the numbers : ").strip().split(",")))[:n]
print("\nList is - ", a) 




#List of lists as input


newlist = [ ] 
n = int(input("Enter number of elements : ")) 
  
for i in range(0, n): 
    element = [input(),input(),int(input())] 
    newlist.append(element) 
      
print(newlist) 
