class Burger:
    def __init__(self):
        self.bun = None
        self.patty = None
        self.cheese = None
        
    def setBun(self, bun):
        self.bun = bun
    
    def setPatty(self, patty):
        self.patty = patty
    
    def setCheese(self, cheese):
        self.cheese = cheese
    
    def print(self):
        print('Burger: ', self.bun, self.patty, self.cheese)
        
class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()
        
    def addBun(self, bun):
        self.burger.setBun(bun)
        return self
        
    def addPatty(self, patty):
        self.burger.setPatty(patty)
        return self
    
    def addCheese(self, cheese):
        self.burger.setCheese(cheese)
        return self
        
    def build(self):
        return self.burger

burger = BurgerBuilder()\
                .addBun('bread')\
                .addPatty('chicken')\
                .addCheese('cheese')\
                .build().print()