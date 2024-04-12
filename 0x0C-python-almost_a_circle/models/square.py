#!/usr/bin/python3
""" Model Square that inherits from Base """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class that defines a Square Object """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def __str__(self):
        """ Print Method """
        sq = "[Square] ({:d}) {:d}/{:d} - {:d}"
        sq = sq.format(self.id, self.x, self.y, self.width)
        return sq

    def update(self, *args, **kwargs):
        """ Functions to update arguments of each attr """
        arg_list = ["id", "size", "x", "y"]
        nop = 0
        if args and len(args) != 0:
            for arg in args:
                if nop == 0:
                    super().update(arg)
                elif nop < len(arg_list):
                    setattr(self, arg_list[nop], arg)
                nop += 1

        else:
            for key, value in kwargs.items():
                if key == "id":
                    super().update(id=value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns dicitionary representation of Square """
        return_sq_dic = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return return_sq_dic
