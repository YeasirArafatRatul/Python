user_info = {
    'name': [],
    'age': [],
    'user_id': [],
}

user_items = user_info.items()  # item method
print(user_items)
print(type(user_items))

for i in user_info.items():
    print(f"key is{i}")


# how too add data

user_info['email'] = []

# pop method (delete method)

popped_item = user_info.pop('user_id')
print(f"popped item is (popped_item)")
print(user_info)

# popitem method

popped_item = user_info.popitem()  # for removing random number
print(user_info)


# update method
more_info = {'phone': 326763, 'name': 'gfafksfhh'}
user_info.update(more_info)
