from math import sqrt


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return sqrt(self.width ** 2 + self.height ** 2)

    def get_picture(self):
        if self.width>50 or self.height>50:
            return "Too big for picture."
        s=''
        l=''
        for x in range(self.width):
            s+='*'
        for y in range(self.height):
            l+=s+'\n'
        
        return l
    
    def get_amount_inside(self,shape):
        return (self.height//shape.height)*(self.width//shape.width)
            
class Square(Rectangle):
    def __init__(self, side):
        self.height=side
        self.width=side
    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side

