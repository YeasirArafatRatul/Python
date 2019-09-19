def reverse_string(string):
    reverse = "" #empty
    for character in string:
        """
        when we concate two strings the right string
        just join in the left string's end.
        """
        reverse = character + reverse
    return reverse

string = input("Enter a string:")
result = reverse_string(string)
print(result)
