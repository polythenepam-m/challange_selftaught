#challange1
class Square:
    square_list = []

    def __init__(self,r1):
        self.r1=r1
        self.square_list.append(self.r1)

list1=Square(10)
list2=Square("abc")
list3=Square(10.54)
list4=Square("こんにちは！")

print(Square.square_list)


#challange2
class Square:
    square_list = []

    def __init__(self,r1):
        self.r1=r1
        self.square_list.append(self.r1)

    def hen(self):
        print("{} by {} by {} by {}".format(self.r1,self.r1,self.r1,self.r1))

awnser=Square(29)
awnser.hen()


#challange3
class School:
    def __init__(self):
        self.name = 'gosho'
        #self.city = city

gosho = School()
rokusho = gosho
print(gosho is rokusho)

tamasho = School()
print(gosho is tamasho)


class Shape():
    def what_am_i(self):
        print("I am a shape.")


class Square(Shape):
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)

a_square = Square(29)
print(a_square)
print(Square.calculate_perimeter)
