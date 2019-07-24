def function(string):
    n = len(string)
    new_string =''
    for i in range(0,n):
        substring = string[i]
        count = string.count(substring)
        new_string = new_string + str(count)
        print(string[i]+new_string,sep='',end='')
   

string = 'ahaghfhakffaAAAsjd'
function(string)
