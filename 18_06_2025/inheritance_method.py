#single level inheritance
class Vechicle:                         #parent class
    def __init__(self):
        print("I'm the vechicle class constructor")
    @staticmethod                       #@staticmethod means this method does not need access to class or instance data (no self or cls).
    def Start():
        print("vehiclwe is started!")
class Car(Vechicle):                    #Subclass
    def __init__(self):
        super().__init__()
        print("i am car  class constructor")
    @staticmethod
    def Start():
        print("car is started!")
c1=Car()
c1.Start()


#single inheritance
class Father:
    def __init__(self):
        pass
    @staticmethod
    def work():
        print("hardorking father!")
class son(Father):
    def __init__(self):
        super().__init__()
    @staticmethod
    def work():
        print("Enjoying son")
Father.work()
son.work()