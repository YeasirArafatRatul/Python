"""Iterative"""
def binary_search(item_list,item):
    item_list.sort()
    lowest = 0
    highest = len(item_list) - 1  # length [len()] is NoneType


    while (lowest <= highest):
        mid = (lowest + highest) // 2
        
        if item_list[mid] == item:
            print(f"Item found  in position: {mid} after sorting" )
            break
        
            
        else:
            if item < item_list[mid]:
                highest = mid - 1
                
            else:
                lowest = mid + 1
                
        
    

data_list = [1,2,4,5,7,3,8]
item = 3
call = binary_search(data_list,item)
