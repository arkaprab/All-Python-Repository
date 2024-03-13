lucky_numbers=[4,6,8,10,12,14,44]
friends = ["Kevin" ,"Karen" ,"Jim" ,"Jia","Mike"]
print(friends)
print(lucky_numbers)

#friends.extend(lucky_numbers)
#print(friends)
#friends.append("Soviet Union")
#print(friends)

friends.insert(2,"United States of America")
print(friends)
friends.remove("United States of America")
friends.remove("Karen")
print(friends)

friends.pop()
print(friends)
print(friends.index("Jim"))
#print(friends.index("Samurai")) # will throw error

friends.append(12)
friends.append(12)
friends.append(12)
friends.append(23)
friends.append(87)
print(friends.count(12))

lucky_numbers.append(23)
lucky_numbers.append(34)
lucky_numbers.append(23)
lucky_numbers.append(11)
print(lucky_numbers)

lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print("Reverse of lucky numbers:" , lucky_numbers)

copied=lucky_numbers.copy()
print(copied)