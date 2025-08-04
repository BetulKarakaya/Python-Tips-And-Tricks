class CapitalizeNameMeta(type):
    def __new__(mcs, name, bases, class_dict):
        # Make Class Name Uppercase
        name = name.capitalize()
        return super().__new__(mcs, name, bases, class_dict)

class myclass(metaclass=CapitalizeNameMeta):
    pass

print(type(myclass))     # <class '__main__.Myclass'>
