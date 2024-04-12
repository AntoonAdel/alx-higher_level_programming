#!/usr/bin/python3
""" Model Rectangle that inherits from Base """


from models.base import Base


class Rectangle(Base):
    """ Class that defines a Rectangle model """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if isinstance(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if isinstance(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if isinstance(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if isinstance(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns area value of Rectangle instance """
        return self.width * self.height

    def display(self):
        """ Function to print Rectangle """
        symb = '#'
        if self.width == 0 or self.height == 0:
            return
        for a in range(self.y):
            print()
        for t in range(self.height):
            print(' ' * self.x, end='')
            print(symb * self.width)

    def __str__(self):
        """ Print Method """
        sl = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        sl = sl.format(self.id, self.x, self.y, self.width, self.height)
        return sl

    def update(self, *args, **kwargs):
        """ Function to update arguments of each attr """
        arlist = ["id", "width", "height", 'x', 'y']
        nop = 0
        if args and len(args) != 0:
            for ar in args:
                if nop == 0:
                    super().__init__(ar)
                elif nop < len(arlist):
                    setattr(self, arlist[nop], ar)
                nop += 1

        else:
            for key, value in kwargs.items():
                if key == "id":
                    super().__init__(value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns dictionary representation of a Rectangle """
        return_rec_dic = {"id": self.id, "width": self.width, "height": self.height,
                  "x": self.x, "y": self.y}
        return return_rec_dic
