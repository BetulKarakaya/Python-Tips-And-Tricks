class AutoLoggerMeta(type):
    def __new__(mcs, name, bases, class_dict):
        
        class_dict['logger'] = lambda self, msg: print(f"[{self.__class__.__name__}] {msg}")
        return super().__new__(mcs, name, bases, class_dict)

class User(metaclass=AutoLoggerMeta):
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        self.logger(f"Hi, I'm {self.name}")

class Admin(metaclass=AutoLoggerMeta):
    def __init__(self, admin, attendant):
        self.admin = admin
        self.attendant =  attendant
    
    def give_task(self):
        self.logger(f"Hi, please restart system {self.attendant}")

def main():
    u = User("Alex")
    u.say_hi()  

    a = Admin("John", "Alice")
    a.give_task()

if __name__ == "__main__":
    main()