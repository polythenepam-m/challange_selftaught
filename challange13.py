#challange1
"""
class Rectangle:
    def __init__(self,t,w):
        self.tall= t
        self.width = w

    def calculate_perimeter(self):
        return self.tall*2 + self.width*2

class Square:
    def __init__(self,h):
        self.hen = h

    def calculate_perimeter(self):
        return self.hen * 4

rect=Rectangle(3,4)
print(rect.calculate_perimeter())
squa=Square(5)
print(squa.calculate_perimeter())
"""

#challange2
"""
class Rectangle:
    def __init__(self,t,w):
        self.tall= t
        self.width = w

    def calculate_perimeter(self):
        return self.tall*2 + self.width*2

class Square:
    def __init__(self,h):
        self.hen = h

    def calculate_perimeter(self):
        return self.hen * 4

    def change_size(self,c):
        self.hen += c
    

rect=Rectangle(3,4)
print(rect.calculate_perimeter())
squa=Square(5)
print(squa.calculate_perimeter())
squa.change_size(200)
print(squa.hen)
"""


#challange3
class Shape():
    def what_am_i(self):
        print("I am a shape")
    
class Rectangle(Shape):
    def __init__(self,t,w):
        self.tall= t
        self.width = w

    def calculate_perimeter(self):
        return self.tall*2 + self.width*2

class Square(Shape):
    def __init__(self,h):
        self.hen = h

    def calculate_perimeter(self):
        return self.hen * 4

    def change_size(self,c):
        self.hen += c
    


rect=Rectangle(3,4)
print(rect.calculate_perimeter())
squa=Square(5)
print(squa.calculate_perimeter())
squa.change_size(200)
print(squa.hen)

rect.what_am_i()
squa.what_am_i()

#challange4
class Horse:
    def __init__(self,name,rider,color):
        self.name=name
        self.rider=rider
        self.color=color

class Rider:
    def __init__(self,name):
        self.name=name

yutaka= Rider("Take Yutaka")
uma= Horse("Deepimpact",yutaka,"brown")
print(uma.rider.name)
print(uma.color)
print(uma.name)    
