
class Vehicle: 
    def __init__(self, name, model) :
        self.name = name 
        self.model = model 

    def get_name(self) :
        print(f"This car is {self.name}")

# This is example of single inheritance
class FuelCar(Vehicle) :
    def __init__(self, name, model, combust_type) :
        self.combust_type = combust_type
        Vehicle.__init__(self, name, model )
    
    def get_fuel_car(self) :
        super().get_name()
        print(f'combust type is {self.combust_type}')
    

# FuelCar and ElectricCar class together is example of Hierarchical inheritance
class ElectricCar(Vehicle) :
    def __init__(self, name, model, battery_type) :
        self.battery_type = battery_type 
        Vehicle.__init__(self, name, model)
    
    def get_electric_car(self) :
        super().get_name()
        print(f'battery type is {self.battery_type}')

class GasolineCar(FuelCar) :
    def __init__(self, name, model, combust_type, gas_capacity) :
        self.gas_capacity = gas_capacity
        FuelCar.__init__(self, name, model, combust_type)

    def get_gasoline_car(self) :
        print(f'Capacity = {self.gas_capacity}')
        super().get_fuel_car()

# Multiple inheritance
class HybridCar(GasolineCar, ElectricCar):
    def __init__(self, name, model, battery_type, comnust_type) :
        FuelCar.__init__(self, name, model, combust_type)
        ElectricCar.__init__(self, name, model, battery_type )


def main() :
    print('Single inheritance')
    fuelCar = FuelCar("HONDA", 'ACCORD', 'PETROL')
    fuelCar.get_fuel_car()
main()




