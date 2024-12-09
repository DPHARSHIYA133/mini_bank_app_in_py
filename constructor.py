
class Bank():
    bank_name='iob'
    bank_ifsc='1234'
    bank_add='anantapur'
    def details(self):
        print('this is obj method')
    @classmethod
    def clsmethod(cls):
        print('this is class method')
girish=Bank()
# Bank.details(girish)
# girish.details()
Bank.clsmethod()
girish.clsmethod()


#calling by object reference
'''
class Calc():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b)
    def sub(self):
        print(self.a-self.b)
    def mul(self):
        print(self.a*self.b)
obj=Calc(200,100)
obj.add()
obj.sub()
obj.mul()
'''
#calling by class reference
#note:it doesnt required defining of init method and self argument
'''
class Calc():
    def add(a,b):
        print(a+b)
    def sub(a,b):
        print(a-b)
    def mul(a,b):
        print(a*b)
obj=Calc()
Calc.add(2,3)
Calc.sub(3,2)
Calc.mul(2,3)
'''