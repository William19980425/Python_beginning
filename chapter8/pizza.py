#形参名*toppings中的星号让Python创建一个名为topings的元组，该元组包含收到的所有值
def make_pizza(size,*toppings):
    # """打印顾客点的所有配料"""
    # print(toppings)
    """概述要制作的披萨"""
    print(f"\nMaking a {size}-inch pizza with the following topppings:")
    for topping in toppings:
        print(f"-{topping}")
# make_pizza('pepperoni')
# make_pizza('mushroom','green peppers','extra cheese')
