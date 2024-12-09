'''
class Harsha:
    a=10
    def printHai(self):
        print('hai')
        print(Harsha.a)
ob=Harsha()
ob.printHai()
'''
'''
class Person:
    species='human'
    planet='earth'
    def printDetails(self):
        print(Person.species)
        print(Person.planet)
person=Person()
person.printDetails()
'''
'''
class Animal():
    kingdom='animal'
    def printKingdom(self):
        print(Animal.kingdom)
animal=Animal()
animal.printKingdom()
Animal.kingdom='Mammalia'
animal.printKingdom()
'''
#generic properties of a class
'''
class Car():
    make='harsha'
    model=123
    year=2024 
car_obj=Car()#obj creation
print(Car.make)#accessing generic property
'''
'''
#specific properties of a class.
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def start_engine(self):
        print('the engine is now running')
    @staticmethod
    def check_warranty(purchase_year,current_year):
        warranty_year=5
        if (current_year-purchase_year)<=warranty_year:
            print('car is under warranty')
        else:
            print('car warranty expired')
car_obj=Car('harsha',123,2024)
#car_obj=Car('harsha',123,2024)
#car_obj.start_engine()
#print(car_obj.make,car_obj.year,car_obj.model)
print(Car.check_warranty(2022,2024))
'''
'''
class Student:
    def __init__(self,sname,sage,smajor):
        self.sname=sname
        self.sage=sage
        self.smajor=smajor
student_obj=Student('harsha',20,'major')
print(student_obj.sname,student_obj.sage,student_obj.smajor)
'''
'''
class Book:
    title='harshabook'
    author='maa'
    year_of_published=2022
book_obj=Book
print(book_obj.title,book_obj.author,book_obj.year_of_published)
'''
'''
class Rectangle:
    def __init__(self,len,wid):
        self.len=len
        self.wid=wid
    def area_of_rectangle(self):
        area=self.len*self.wid
        print(area)
    def perimeter_of_rectangle(self):
        perimeter=2*(self.len+self.wid)
        print(perimeter)
rectangle_obj=Rectangle(2,3)
rectangle_obj.area_of_rectangle()
rectangle_obj.perimeter_of_rectangle()
'''
'''
class Person:
    def __init__(self,pname,page):
        self.pname=pname
        self.page=page
    def person_details(self):
        print(f'person name is {self.pname}')
        print(f'person age is {self.page}')
person_obj=Person('harsha',20)
person_obj.person_details()
'''
class KabadiTeam:
    pass
class Player:
    def __init__(self,pn,pa,pp,pe):
        self.pn=pn
        self.pa=pa
        self.pp=pp
        self.pe=pe
    def display_players_details(self):
        print(f'player name is {self.pn}')
        print(f'player age is {self.pa}')
        print(f'player points are {self.pp}')
        print(f'palyer experience is {self.pe}')
players=[]
for i in range(1,3):
    print(f'enter details of playerno {i}')
    pn=input('enter name:')
    pa=input('enter age')
    pp=int(input('enter points:'))
    pe=int(input('enter experience in years:'))
    player_obj=Player(pn,pa,pp,pe)
    players.append(player_obj)
for player in players:#display
    player.display_players_details()
    print()
for max in player.pp:
    max_points=max(players.pp)
    print(max_points)