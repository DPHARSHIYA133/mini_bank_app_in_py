#accessing generic properties by using class.
'''
class Bank():
    bank_name='iob'
    bank_ifsc=1234
    bank_add='anantapur'
girish=Bank()
vishnu=Bank()
print(Bank.bank_add)
print(Bank.bank_ifsc)
print(Bank.bank_name)
'''
#accessing generic properties by using object.
'''
class Bank():
    bank_name='iob'
    bank_ifsc=1234
    bank_add='anantapur'
girish=Bank()
vishnu=Bank()   
print(girish.bank_name)
print(girish.bank_ifsc)
print(girish.bank_add)
print()
print(vishnu.bank_name)
print(vishnu.bank_ifsc)
print(vishnu.bank_add)
'''
#Modifying generic properties by using class.
'''
class Bank():
    bank_name='iob'
    bank_ifsc=1234
    bank_add='anantapur'
girish=Bank()
vishnu=Bank()   
print(Bank.bank_ifsc)
Bank.bank_ifsc=1111
print(Bank.bank_ifsc)
print(girish.bank_ifsc)
print(vishnu.bank_ifsc)
'''
#Modifying generic properties by using object.
class Bank():
    bank_name='iob'
    bank_ifsc=1234
    bank_add='anantapur'
girish=Bank()
vishnu=Bank()
print(girish.bank_ifsc)
girish.bank_ifsc=1111
print(girish.bank_ifsc)
print(vishnu.bank_ifsc)
print(Bank.bank_ifsc)