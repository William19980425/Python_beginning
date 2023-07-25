from car import Car

class Battery:

    def __init__(self,battery_size=40):
        self.battery_size = battery_size
        self.battery_range = 0

    def describe_battery(self):
        print(f"This car has a {self.battery_size}kwh battery")    

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range}miles on a full charge.")

#定义子类时，必须在括号内指定父类的名称
class ElectricCar(Car):
    
    def __init__(self,make,model,year):
        super().__init__(make,model,year)   #super()能够让你调用父类的方法
        self.battery = Battery()
    
    # def describe_battery(self):
    #     print(f"This car has a {self.battery_size}kwh battery.")

    #重写父类中的方法
    # def fill_gas_tank(self):
    #     print("This car does't have a gas tank")



my_leaf = ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
# my_leaf.describe_battery()
# my_leaf.fill_gas_tank()
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
