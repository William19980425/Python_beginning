class Car:

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 89
    
    def get_descriptive_name(self):

        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):

        print(f"This car has {self.odometer_reading} miles on it")
    
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")    

    def increment_odometer(self,miles):
        self.odometer_reading += miles

    def fill_gas_tank(self,gas):
        if self.gas_tank >= 100:
            print("油是满的不用加")
        else:
            self.gas_tank += gas
            print(f"现在的油箱里有{self.gas_tank}L油")
        
# my_new_car = Car('audi','a4','2024')
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 25
# my_new_car.read_odometer()

# my_new_car.update_odometer(27)
# my_new_car.read_odometer()

# my_used_car = Car('subaru','outback',2019)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()                
# my_new_car.fill_gas_tank(50)
