from abc import abstractmethod, ABC

class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass
    @abstractmethod
    def description(self):
        pass 

class SimpleCoffee(Coffee):
    def cost(self):
        return 5
    def description(self):
        return (f"Simple coffee")

class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee
    
    def cost(self):
        return self._coffee.cost()

    def description(self):
        return (f'{self._coffee.description()}')

class MilkDecoration(CoffeeDecorator):
    def cost(self):
        return super().cost() + 2 
    
    def description(self):
        return (f"{super().description() } Milk ")

class SugarDecoration(CoffeeDecorator):
    def cost(self):
        return super().cost() + 5
    
    def description(self):
        return (f"{super().description()} Sugar")
        

if __name__ == '__main__':
    print("-----Simple Coffee")
    coffee = SimpleCoffee()
    print(coffee.description())
    
    print("-----Milk Coffee")

    coffee = MilkDecoration(coffee)
    print(coffee.description())

    print("------Sugar Coffee")
    
    coffee = SugarDecoration(coffee)
    print(coffee.description())
    

        
        