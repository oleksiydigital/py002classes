# classes, f-string

class My_class:
    def __init__(self, name):
        self.__name = name
        return

    #f-string
    def tell(self):
        print(f"hello, I am {self.__name}")
