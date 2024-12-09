#crearing generic property by using class.
'''
class Bank():
    bank_name='iob'
    bank_ifsc='1234'
    bank_add='anantapur'
girish=Bank()
vishnu=Bank()
Bank.bank_code=9398646161
print(Bank.bank_code)
print(girish.bank_code)
print(vishnu.bank_code)
'''
#creating generic property by using object.
class Bank():
    bank_name='iob'
    bank_ifsc='1234'
    bank_add='anantapur'
    def func(self):
        print('hai')
girish=Bank()
vishnu=Bank()
#girish.bank_code=9398646161
#print(girish.bank_code)
#print(vishnu.bank_code)
#print(Bank.bank_code)
girish.func()

#deleting generic properties by using class.
'''
class Bank():
    bank_name='iob'
    bank_ifsc='1234'
    bank_add='anantapur'
girish=Bank()
vishnu=Bank()
print(Bank.bank_add)
del(Bank.bank_add)
'''

