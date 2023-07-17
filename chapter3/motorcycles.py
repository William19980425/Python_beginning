#3.2修改、添加和删除元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

print("====================================分割线====================================")
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('ducati') #.append() 追加元素到列表末尾
print(motorcycles)

print("====================================分割线====================================")
motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

print("====================================分割线====================================")
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati') # .insert(index,'string')方法可以在列表的任意位置添加新元素
print(motorcycles)

del(motorcycles[0])
print(motorcycles)

del motorcycles[0]
print(motorcycles)

print("====================================分割线====================================")
print(motorcycles)
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop() #pop()方法可以删除列表末尾的元素，并能够使你接着使用它
print(popped_motorcycles)

print("====================================分割线====================================")
last_owned = motorcycles.pop()
print(f'The last motorcycle I owned was a "{last_owned.title()}"')

motorcycles = ['honda','ducati','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati') #如果只知道要删除的元素的值，可使用remove方法.remove()方法只删除第一个指定的值，
                             #如果要删除的值可能在列表中多次出现，就需要使用循环
print(motorcycles)

print("====================================分割线====================================")
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive) #使用remove()方法删除元素后，也可继续使用它的值
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")




