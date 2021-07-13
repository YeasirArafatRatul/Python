string =list(map(int,input()))


output = ''

cache = string[0]
count = 0

for i in range(len(string)):

    if cache == string[i]:
        count += 1
      
    else:
        output += '('+ str(count) + ',' + " " + str(cache) + ')' + " "
        cache = string[i]
        count = 1
        
output += '('+ str(count) + ',' + " " + str(cache) + ')'

print(output)
