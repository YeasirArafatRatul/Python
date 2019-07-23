#a functin that returns the strings which start with the given prefix
def function(a_list,prefix):
    n = len(a_list)
    output_list = []
    for i in range(0,n):
        if a_list[i].startswith(prefix):
            output_list.append(a_list[i])
    return output_list

List = ['abcd','safj','aue','adfa']
pre = 'a'
print(function(List,pre))
