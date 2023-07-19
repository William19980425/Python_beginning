dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
# dimension[0] = 100  tuple的值是不能被修改的，会报错
for dimension in dimensions:
    print(dimension)

#虽然不能修改元祖的元素，但是可以重新定义整个元祖，给表示元祖的变量赋值 来达到修改的目的
print("初始")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("修改后")   
for dimension in dimensions:
    print(dimension) 