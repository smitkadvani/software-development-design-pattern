class Burger:
    def __init__(self, ingridients):
        self.ingridients = ingridients
        
    def print(self):
        print(self.ingridients)
        
class BurgerFactory:
    def createChickenBurger(self):
        return Burger(['chicken', 'bread'])
    
    def createCheeseBurger(self):
        return Burger(['cheese', 'bread'])
    
    def createVegBurger(self):
        return Burger(['veg', 'bread'])
    
    def createVeganBurger(self):
        return Burger(['vegan', 'bread'])
    
burgerFactory = BurgerFactory()
burgerFactory.createChickenBurger().print()
burgerFactory.createCheeseBurger().print()
burgerFactory.createVegBurger().print()
burgerFactory.createVeganBurger().print()
