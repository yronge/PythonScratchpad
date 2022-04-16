# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class MyGen():
    FibNum1 = 0
    FibNum2 = 1
    def __init__(self, EndFibNumber):
        self.EndFibNumber = EndFibNumber

    def __iter__(self):
        return(self)

    def __next__(self):
        if MyGen.FibNum1 < self.EndFibNumber:
            ReturnNum = MyGen.FibNum1
            MyGen.FibNum1 = MyGen.FibNum2
            MyGen.FibNum2 = MyGen.FibNum2 + ReturnNum
            return ReturnNum
        raise StopIteration


gen = MyGen(7000)
for i in gen:
    print(i)

