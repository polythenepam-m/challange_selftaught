
#challange1
class Apple:
    def __init__(self,w,c,s,f):
        self.weight=w
        self.color=c
        self.size=s
        self.flavor=f
        print("Created!")
        
ap1=Apple(5,"red",55,"sweet")
print(ap1.flavor)

    
#challange2
import math

class Circle:
    def __init__(self,hankei,radian):
        self.area=hankei*hankei*radian

cc1=Circle(4,3.14)
print(cc1.area)    


#challange3
class Triangle():
    def __init__(self,teihen,takasa):
        self.area=teihen*takasa/2

tr1=Triangle(3,4)
print(tr1.area)


#challange4
class Hexagon():
    def __init__(self,s1,s2,s3,s4,s5,s6):
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.s4=s4
        self.s5=s5
        self.s6=s6

    def calculate_perimeter(self):
        return self.s1+self.s2+self.s3+self.s4+self.s5+self.s6

hexagon=Hexagon(3,3,4,4,5,5,)
print(hexagon.calculate_perimeter())
