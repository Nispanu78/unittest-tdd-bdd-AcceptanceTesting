class Calculate(object):
    def add(self, x, y):
        """Takes two integers and adds them together to produce
        the result.

        >>> c = Calculate()
        >>> c.add(1, 1)
        2
        >>> c.add(25, 125)
        150
        """
        
        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))

if __name__ == '__main__':
    # calc = Calculate()
    # result = calc.add("Hello", "World!")
    # print (result)
    import doctest
    doctest.testmod()
