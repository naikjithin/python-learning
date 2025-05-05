fruits = ["apple", "orange", "banana"]
print(fruits)

print(fruits[0]) # gives first item

print(fruits[-1]) # gives last item

print(len(fruits)) # gives length of list

fruits.append("grapes")
print(fruits)

fruits.remove("grapes")
print(fruits)

fruits[2] = "strawberry"
print(fruits)

# output
# ['apple', 'orange', 'banana']
# apple
# banana
# 3
# ['apple', 'orange', 'banana', 'grapes']
# ['apple', 'orange', 'banana']
# ['apple', 'orange', 'strawberry']