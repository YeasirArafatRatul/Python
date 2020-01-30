# print(2**3) #for_power
# print(4/2) #floating result
# print(4//2) #integer output

# print(2**3/2*6-4*3-(3/2)) #precedence rule
# #exponents
# print(2**3**2)
# print(2**9)


# VARIABLE
# number1 =2
# name = "Ratul"
# int name = 23

# name,age = "Ratul", 23
# name,age = "Ratul", "23"
# x = y = z = 1

# user_one_name = "arafat" #snake case writing (recomended by python)
# userOneName = "Yeasir" #camel case writing


# STRING CONCATANATION

# full_name = first_name + " " +second_name
#  print(first_name + 3 ) #error
#  print(first_name + "3") #no error
#  print(first_name*3) #no error


# USER_INPUT
# name = input ("Type Your Age: ")
# print("Hello"+ name ) #(Takes inputs as string)

# number_one = int (input("Enter first number:"))
# number_two = int (input("Enter second number:"))
# total = number_one + number_two
# print(int (total))

# name,age = input("Enter your name and age ").split()   # this can be also used .spliot(",")
# print(name)
# print(age)


# STRING FORMATTING
# print("Hello {}  your age is {}", format(name.age)) #python 3

# print(f"Hello {name} your age is {age}") #python 3.6

# print(f"Hello {name} your age is {age + 2}")


# STRING INDEXING

# language = "PYTHON PROGRAMMING"

# print(language[4])
# print(language[0])
# print(language[6])
# print(language[2])

# print(language[-1])
# print(language[-2])


# SLICING       sytax [start argument : stop argument-1]
# print(language[0:4])


# STRING METHODS
# name = "    Ratul Arafat"
# name2 = "R a t u l Ar af at"


# # length = len(name)
# # print(length)
# # print(name.lower())
# # print(name.upper())

# # print(name.title())

# # print(name.count("a"))


# #STRIP and REPLACE METHOD

# dots = " ........."
# print(name + dots)
# print(name.lstrip() + dots)
# print(name.rstrip() + dots)
# print(name.strip() + dots)
# print(name2.replace(" ","") + dots)

# print(name.find("F"))


# CENTRE Method

# name = input(" Enter Your Name:")

# print(name.center(len(name)+ 8, "~*"))


# CHECK EMPTY OR NOT

# name = "abc"
# if name:
#     print("name is not empty")
# else:
#     print("is empty")


# LOOPS
# While loop

i = 1
while i <= 10:
    print(f"loop{i}")
    i = i+1
