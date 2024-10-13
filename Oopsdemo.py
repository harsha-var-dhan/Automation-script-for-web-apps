class calculator:
    num= 100
    #default constructor

    def __init__(self, a, b):
        self.firstNumber= a
        self.secondNumber= b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def summation(self):
        return self.firstNumber + self.secondNumber + self.num


obj = calculator(2, 3)
obj.getData()
print(obj.summation())

obj1 = calculator(4, 5)
obj1.getData()
print(obj1.summation())
