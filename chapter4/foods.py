#复制列表 [:]  同时省略起始索引和终止索引
my_foods = ['披萨','薯片','可乐']
friends_foods = my_foods[:]

print("我最喜欢的食物是:")
print(my_foods)

print("\n我的朋友最喜欢的食物是:")
print(friends_foods)

my_foods.append('油饼')
friends_foods.append('炉面')

print(my_foods)
print(friends_foods)

