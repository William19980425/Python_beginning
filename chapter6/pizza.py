#每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表
pizza = {
    'crust':'thick',
    'toppings':['mushroom','extra cheese'],
}

print(f"You orderd a {pizza['crust']}-crust pizza" "with the following toppings:")
for topping in pizza['toppings']:
    print(f"{topping}")
