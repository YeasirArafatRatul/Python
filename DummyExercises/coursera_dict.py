def groups_per_user(group_dictionary):
  user_groups = {}
  
  for key in group_dictionary:
    users = group_dictionary[key]
    for user in users:
    
      if user in user_groups:
        data = user_groups[user]
        data.append(key)
        user_groups[user] = data
      else:
        user_groups[user]= [key]
      
  return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
