#导入某个模块后的使用模块内函数的方法 module_name.function_name()

#import pizza

# pizza.make_pizza(16,'pepperoni')
# pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')

#---------------------------------------------------------------------------------------------------

#还可以只导入特定函数 from module_name import function_name
#导入任意数量的函数 from module_name import function_0,function_1,function_2

# from pizza import make_pizza

# make_pizza(16,'pepperoni')
# make_pizza(12,'mushrooms','green peppers','extra cheese')

#---------------------------------------------------------------------------------------------------

#使用as给需要使用的函数指定别名
# from mudule_name import function_name as fn
# fn(index1,index2)

# from pizza import make_pizza as mp

# mp(16,'pepperoni')
# mp(12,'mushrooms','green peppers','extra cheese')

#---------------------------------------------------------------------------------------------------

#使用as给模块指定别名 import module_name as mn
import pizza as p
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushrooms','green peppers','extra cheese')

#---------------------------------------------------------------------------------------------------

#使用星号(*)让Python将模块中的每个函数复制到当前文件中 from module_name import *

from pizza import *
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

