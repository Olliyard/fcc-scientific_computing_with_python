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
        return (self.width * self.height)
    
    def get_perimeter(self):
        return (2*self.width + 2*self.height)
    
    def get_diagonal(self):
        return ((self.width**2 + self.height**2)** .5)

    def get_picture(self):
        shape_str = ""
        if self.width > 50 or self.height > 50:
            shape_str = f"Too big for picture."
        else:
            for i in range(self.height):
                shape_str += f"{self.width*'*'}\n"
        return shape_str
    
    def get_amount_inside(self, shape):
        max_width = self.width // shape.width
        max_height = self.height // shape.height
        return max_width * max_height
        
class Square(Rectangle):
    def __init__(self, length):
        self.width = length
        self.height = length
    
    def __str__(self):
        return f"Square(side={self.width})"
    
    def set_side(self, length):
        self.set_width(length)
        self.set_height(length)