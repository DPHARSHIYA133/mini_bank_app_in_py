class Bank():
    bank_name='sbi'
    bank_roi=3
    bank_branch='kizikistan'
    def __init__(self,cn,ca,cb,cac):
        self.cname=cn
        self.cage=ca
        self.cbal=cb
        self.caccount=cac
    def bank_details(cls):
        print(f'bank name is {cls.bank_name}')
        print(f'bank roi is {cls.bank_roi}')
        print(f'bank branch is {cls.bank_branch}')
    def customer_details(self):
        print(f'customer name is {self.cname}')
        print(f'customer age is {self.cage}')
        print(f'customer bal is {self.cbal}')
        print(f'customer account number is {self.caccount}')
    #@staticmethod
    def get_int_val():
        iv=int(input('enter value:'))
        return iv
    @staticmethod
    def get_str_val():
        sv=input()
        return sv
    def withdrawl(self):
        amount=self.get_int_val()
        if amount <= self.cbal:
            self.cbal-=amount
            print('withdrawl is successfull....balance in ur account is',self.cbal)
        else:
            print('insufficient bal')
    def deposite(self):
        amount=self.get_int_val()
        if amount > 0:
            self.cbal+=amount
            print('ur money deposited successfully....balance in ur account is',self.cbal)
        else:
            print('plz enter amount >0')
    #@classmethod
    def change_roi(cls):
        new_roi=cls.get_int_val()
        cls.bank_roi=new_roi
        print('roi is changed to',cls.bank_roi)
    #@classmethod
    def change_branch(cls):
        new_branch=cls.get_str_val()
        cls.bank_branch=new_branch
        print('bank branch is changed to',cls.bank_branch)
harsha=Bank('harsha',20,200000,2345)
harsha.change_roi()
'''
class Bank():
    bank_name='iob'
    bank_ifsc=1234
    bank_add='kizikistan'
    def __init__(self,cn,cac,cb):
        self.cn=cn
        self.cac=cac
        self.cb=cb
    def customer_details(self):
        print(f'customer name is {self.cn}') 
        print(f'customer account no is {self.cac}')
        print(f'customer bal is {self.cb}')      
    def withdrawl(self):
        amount=int(input('enter withdrawl amount'))
        if self.cb>=amount:
            self.cb=self.cb-amount
            print('withdrawl successfull',self.cb)
        else:
            print('insufficient balance')
    def deposite(self):
        amount=int(input('enter deposite amount'))
        if amount>0:
            self.cb=self.cb+amount
            print('deposite successfull',self.cb)
        else:
            print('plz deposite amount greater than 1 rupee')
girish=Bank('girish',1234,10000)
girish.customer_details()
girish.withdrawl()
girish.deposite()
'''
'''
class Employee:
    company_name='deloitee'
    def __init__(self,ename,eposition):
        self.ename=ename
        self.eposition=eposition
    def display_employee_details(self):
        print(f'name of the employee is {self.ename}')
        print(f'position of employee is {self.eposition}')
        print(f'company in which employee is working is {self.company_name}')
    @staticmethod
    def get_str_value():
        sv=input('enter new company name:')
        return sv
    def modify_company_name(self):
        new_company=self.get_str_value()
        Employee.company_name=new_company
        print(f'ur company name is changed to {Employee.company_name}')
employee_obj=Employee('harsha','fullstack developer')
employee_obj2=Employee('maaa','frontend developer')
employee_obj.modify_company_name()
employee_obj.display_employee_details()
employee_obj2.display_employee_details()
'''

    