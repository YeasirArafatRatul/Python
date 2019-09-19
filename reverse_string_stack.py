def reverse_stack(string):
    stack = [] #empty


    #make the stack fulled by pushing the characters of the string
    for char in string:
        stack.append(char)

    reverse = ''

    while len(stack) > 0:
        last = stack.pop()

        #here the pop function take the last character first thats why
        #we have to put it as the right operand 
        reverse = reverse + last

    return reverse


string = input("Give Input:")
result = reverse_stack(string)
print(result)
