cars = ['bmw','audi','toyota','subaru']
cars.sort() #sort()方法能永久修改列表元素中的排列顺序
print(cars)

print("====================================分割线====================================")
cars = ['bmw','audi','toyota','subaru']
print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars)) #sorted()方法能够按照特定顺序显示列表元素，且不影响它们在列表中的排列顺序

print("\nHere is the original list again: ")
print(cars)

print("====================================分割线====================================")
#反向打印列表
cars = ['bmw','audi','toyota','subaru']
print(cars)

cars.reverse() #reverse()方法会永久的修改列表元素的排列顺序
print(cars)

(cars.reverse())
print(cars)

cars = ['bmw','audi','toyota','subaru']
len(cars)
