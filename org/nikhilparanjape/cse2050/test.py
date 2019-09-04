print("test")

tuple1 = (1, 2, 3, 4, 5, 6)
print(tuple1)
tuple2 = list(tuple1)
print(tuple2)
list2 = tuple(tuple2)
print(list2)

d1 = {"1": "mark", "2": "joe", "3": "smith"}

print(d1.get('2'))

d1.replace('1', "john")

print(d1)
