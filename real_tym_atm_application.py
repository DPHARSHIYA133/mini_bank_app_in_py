class Atm:
    bank_name='iob'
    bank_add='ashok nagar'
    bank_ifsc=1234567
    def __init__(self,cname,caccount,cbal,cpin):
        self.customer_name=cname
        self.customer_account=caccount
        self.customer_bal=cbal
        self.customer_pin=cpin
    def display_customer_details(self):
        print(f'customer name is {self.customer_name}') 
        print(f'customer account no is {self.customer_account}')
        print(f'customer bal is {self.customer_bal}')   
        print(f'customer pin is {self.customer_pin}')
    @classmethod
    def display_bank_details(cls):
        print(f'bank name is {cls.bank_name}') 
        print(f'bank address  is {cls.bank_add}')
        print(f'bank ifsc code is {cls.bank_ifsc}') 
    def deposite(self):
        pin=self.get_int_value()
        if pin==self.customer_pin:
            amount=self.get_int_value()
            if amount>0:
                self.customer_bal+=amount
                print(f'amount is deposited successfully...ur current bal is {self.customer_bal}')
            else:
                print('plz enter amount > 0 ')
        else:
            print('pin entered incorrectly')
            
    def withdrawl(self):
        pin=self.get_int_value()
        if pin==self.customer_pin:
            amount=self.get_int_value()
            if amount<=self.customer_bal:
                self.customer_bal-=amount
                print(f'withdrawl is successfull...ur current bal is {self.customer_bal}')
            else:
                print('insufficient bal')
        else:
            print('pin entered incorrectly')
    def generate_pin(self):
        import random
        a=random.randint(1000,9999)
        self.customer_pin = a
        print(f'ur pin is {a}')
        return a
    def check_balance(self):
        pin=self.get_int_value()
        if pin==self.customer_pin:
            print(f'ur current balance in ur account is {self.customer_bal}')
    @staticmethod
    def get_int_value():
        int_val=int(input('enter amount/pin:'))
        return int_val
    def exit(self):
        print()
harsha_obj=Atm('harsha',123456,1500000,3333)
#maa_obj=Atm('maa',7890,60000,4444)
n=int(input('enter 1.for deposite 2.for withdrawl 3.for check bank balance 4.generate pin'))
if n==1:
    harsha_obj.deposite()
elif n==2:
    harsha_obj.withdrawl()
elif n==3:
    harsha_obj.check_balance()
else:
    harsha_obj.generate_pin()