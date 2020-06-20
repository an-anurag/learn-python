class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length


# single inheritance

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


# multiple inheritance

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area


class A:
    pass


class C:
    def __init__(self):
        pass


class B(A):
    def __init__(self):
        # C.__init__()
        print("child")


b = B()


# Raymond Hettinger - Super considered super! - PyCon 2015

class Adam(object): pass


class Eve(object): pass


class Ramon(Adam, Eve): pass


class Gayle(Adam, Eve): pass


class Raymond(Ramon, Gayle): pass

######################################

class Dennis(Adam, Eve): pass


class Sharon(Adam, Eve): pass


class Rachel(Dennis, Sharon): pass


class Matthew(Raymond, Rachel): pass


help(Matthew)
