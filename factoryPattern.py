from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self):
        print(f'Rectangle is here')

class Square(Shape):
    def draw(self):
        print("Square is here")

class Circle(Shape):
    def draw(self):
        print(f"Circle is here")


class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type == 'Circle':
            return Circle()
        elif shape_type == 'Square':
            return Square()
        elif shape_type == 'Rectangle':
            return Rectangle()

if __name__ == '__main__':
    shape1 = ShapeFactory.get_shape('Circle')
    shape2 = ShapeFactory.get_shape('Rectangle')
    
    shape1.draw()
    shape2.draw()