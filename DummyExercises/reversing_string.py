def reverse_elemnts(l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements


words = ['sfkshj', 'sdfsg', 'srehg']
print(reverse_elemnts(words))
