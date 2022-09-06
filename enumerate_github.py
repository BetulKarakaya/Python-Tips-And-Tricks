
fruits = ["apple","banana","cherry","strawberry","pineapple"]


# you access array elements via loop and increase index manually.
index = 0
for item in fruits:
	print(index,item)
	index = index +1

print()

# you access array elements one by one via index of loop .
for index in range(len(fruits)):
	print(index, fruits[index])

print()

#CLEAR CODE VERSION
#you may use enumerate() method that return both index and value. enumerate() method return tuple type value (index,value).  
for index,item in enumerate(fruits):
	print(index,item)
