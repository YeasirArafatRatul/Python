# dictionary Comprehension

#Dictionary and set is unordered


square = {f"Square of {num} is ": num ** 2 for num in range(1, 11)}
for k, v in square.items():
    print(f"{k} : {v}")

string = "Arafat"
word_count = {char: string.count(char) for char in string}
print(word_count)

odd_even = {i: ('even' if i % 2 == 0 else 'odd') for in range(1, 11)}

print(odd_even)

# set_comprehension

s = {k**2 for k in range(1, 11)}
print(s)
