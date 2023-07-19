requested_topping = 'mushrooms'
if requested_topping !='anchovies':
    print("Hold the anchovies")

a = 3
b = 3.0
type_a = type(a)
type_b = type(b)
if type_a == type_b :
    print("a=b")
else:
    print("a!=b")

requested_toppings = ['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'peperoni' in requested_toppings:
    print("Adding peperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")        
print("\nFinished making your pizza")

#如果只想运行一个代码块，就使用if-elif-else语句
#如果要运行多个代码块，就使用一系列独立的if语句