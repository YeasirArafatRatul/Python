"""Iterative"""
def binary_search(item_list,item):
    lowest = 0
    item_list = item_list.sort()
    highest = len(item_list)- 1 #length [len()] is NoneType
    

    while(lowest<=highest):
        mid = (lowest + highest) // 2
        
        if item_list[mid] == item:
            print("Item found")
        else:
            if item < item_list[mid]:
                highest = mid - 1
            else:
                lowest = mid + 1
    print("not found")

    

if __name__ == "__main__":
    data_list = input().split(" ")
    data_to_find = input()

print(binary_search(data_list,data_to_find))





"""Recursive"""
