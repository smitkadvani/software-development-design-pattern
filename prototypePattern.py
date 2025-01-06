import copy
from factoryPattern import Rectangle, Shape

class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type
    
    def __str__(self):
        return f"Shape  : {self.shape_type}"
    
    def clone(self):
        return copy.deepcopy(self)

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__('Rectangle')
    
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"{super().__str__()}, Width : {self.width} Height : {self.height}"
    

class Circle(Shape):
    def __init__(self, radius):
        super().__init__('Circle')
        self.radius = radius 
    
    def __str__(self):
        return f"{super().__str__()} Radius : {self.radius} "
    
if __name__ == '__main__':
    circle_prototype = Circle(6)
    rectangle_prototype = Rectangle(7, 8)
    
    print("Original Prototype")
    print(circle_prototype)
    print(rectangle_prototype) 
    
    circle_copy = circle_prototype.clone()
    rectangle_copy = rectangle_prototype.clone()
    
    circle_copy.radius = 50
    rectangle_copy.width = 100
    rectangle_copy.height = 200
    
    print("After modification")
    print(circle_prototype)
    print(rectangle_prototype) 
    print(circle_copy)
    print(rectangle_copy)
    
    
    
        