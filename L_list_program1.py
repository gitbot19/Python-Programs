# this is example of list

lucky_numbers = [4,8,16,33,47,77]
friends = ["lisa", "Jimmy", "Kevin", "Lulu", "Hulio", "Jimmy"]
friends.sort()

print(friends)
print(friends[1:3])
print(friends[1:])
print(friends[:3])

# count item in list
print(friends.count("Jimmy"))

# extend list 
friends.extend(lucky_numbers)
print(friends)

# add element to list
friends.append("Maria")
print(friends)

# insert element to list
friends.insert(1,"Kelly")
print(friends)

# remove element to list
friends.remove("Jimmy")
print(friends)

# removes last element in the list
friends.pop()
print(friends)

# Get index of item in list
print(friends.index("Kevin"))

# clear list
friends.clear()
print(friends)

# reverse list
lucky_numbers.reverse()
print(lucky_numbers)

# copy list
friends2 = friends.copy()
print(friends2)

