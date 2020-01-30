class Car:
    def __init__(self,color,brand):
        self.color = color
        self.brand = brand
    def __repr__(self):
        return f"{self.__class__.__name__}is{self.color}of{self.brand} brand"
