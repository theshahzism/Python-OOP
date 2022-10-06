#Q1
    class Circle:
        def __init__(self,radius,colour):
            self.radius=radius
            self.colour=colour
        def set_radius(self,r):
            self.radius=r
        def get_radius(self):
            return self.radius
        def set_colour(self,c):
            self.colour=c
        def circumference(self):
            return 2*(22/7)*self.radius
        def get_area(self):
            return (22/7)*self.radius**2

    Object1=Circle(2,"Blue")
    print(Object1.get_radius())
    Object1.set_radius(3)
    print(Object1.get_radius())
    print(Object1.colour)
    Object1.set_colour("Gray")
    print(Object1.colour)
    print(Object1.circumference())
    print(Object1.get_area())

#Q2
class BankAccount:
    def __init__(self):
        self.balance=0

    def deposit(self,added):
        self.balance=self.balance+added
        print(self.balance)
    def withdraw(self,deducted):
        self.balance-=deducted
        print(self.balance)
    def balance(self):
        return self.balance
Shahzain=BankAccount()
Shahzain.deposit(1000)
Shahzain.withdraw(700)
print(Shahzain.balance())

#Q3

class BankAccount:
    def __init__(self):
        self.__balance=0

    def deposit(self,added):
        self.__balance=self.__balance+added
        #print(self.__balance)
    def withdraw(self,deducted):
        self.__balance-=deducted
        #print(self.__balance)
    def balance(self):
        print(self.__balance)
Shahzain=BankAccount()
Shahzain.deposit(1000)
Shahzain.withdraw(250)
Shahzain.balance()

#Q4

class Worker:
    def __init__(self):
        self.__wagerate=0
        self.__hoursworked=0
    def sethoursworked(self,h):
        self.__hoursworked = h
    def changerate(self,r):
        self.__wagerate = r
    def pay(self):
        return (self.__hoursworked*self.__wagerate)
labour=Worker()
labour.sethoursworked(200)
labour.changerate(3)
print(labour.pay())

#Isse pahly tak variables class k bnany thy mene instance k bnaye hn so for onwards, I will make them as required!

#Q5

class Worker:
    def __init__(self,w=0,h=0):
        self.__wagerate=w
        self.__hoursworked=h
    def sethoursworked(self,h):
        self.__hoursworked = h
    def changerate(self,r):
        self.__wagerate = r
    def pay(self):
        return (self.__hoursworked*self.__wagerate)
labour=Worker()
print(labour.pay())

labour1=Worker(500,3)
labour1.sethoursworked()
labour1.changerate()
print(labour1.pay())

#Q6

class Vehicles:
    def __init__(self,a,b,c):
        self.__noOfwheels=a
        self.__modelno=b
        self.__colour=c
    def getter(self):
        print(self.__colour,self.__modelno,self.__noOfwheels)
    def setter(self,d,e,f):
        self.__noOfwheels = d
        self.__modelno = e
        self.__colour = f
Toyota=Vehicles(4,2019,"black")
Toyota.getter()
Toyota.setter(4,2021,"Gray")
Toyota.getter()

#Q7

class Engine:
    def __init__(self,a,b):
        self.__engineno=a
        self.__menufactureno=b
    def setter(self,c,d):
        self.__engineno=c
        self.__menufactureno=d
    def getter(self):
        return (self.__engineno)
Toyota=Engine(201,200)
print(Toyota.getter())

#Q9

class tollbooth:

    passingcar=0
    moneycount=0
    payingcar=0
    nonpayingcar=0
    @classmethod
    def payingcars(cls):
        cls.passingcar+=1
        cls.moneycount+=50
        cls.payingcar+=1
    @classmethod
    def nopaycar(cls):
        cls.passingcar+=1
        cls.nonpayingcar=1
    @classmethod
    def display(cls):
        print("Car count is",cls.passingcar)
        print("Total money collected is",cls.moneycount)
    @classmethod
    def pc(cls):
        print(cls.payingcar,cls.nonpayingcar)
    def pc2(self):
       print
vehicle1=tollbooth()
vehicle1.payingcars()
vehicle2=tollbooth()
vehicle2.payingcars()
vehicle3=tollbooth()
vehicle3.payingcars()
vehicle4=tollbooth()
vehicle4.nopaycar()
tollbooth.display()
tollbooth.pc()

#Q10

class time:
    def __init__(self,h=0,m=0,s=0):
        self.hours=h
        self.minutes=m
        self.seconds=s
    def display(self):
        print(self.hours,":",self.minutes,":",self.seconds)
    def addtime(self,t):
        self.hours+=t.hours
        self.minutes+=t.minutes
        self.seconds+=t.seconds
        if self.seconds>60:
            self.minutes+=1
       if self.minutes>60:
            self.minutes-=60
            self.hours+=1
        if self.hours>24:
            self.hours-=24
time1=time(21,22,23)
time1.display()
time2=time(1,40,50)
time2.display()
time1.addtime(time2)
time1.display()

#Q12

class tracker:
    count=0
    def __init__(self):
        tracker.count+=1
        self.serialno=tracker.count
    def report(self):
        print(self.serialno)
a=tracker()
b=tracker()
c=tracker()
a.report()
b.report()
c.report()

#Q8
class Int:
    def __init__(self,i=0):
        self.Int=i
    def setter(self,a):
        self.Int=a
    def display(self):
        print(self.Int)
    def adder(self,b):
        self.Int+=b.Int
a=Int(1)
b=Int(2)
a.adder(b)
a.display()
c=Int()
c.display()
c.adder(a)
c.display()
#ismn ap adder mn a.value+b.value krogy do objects as an argument deke!

#Q11 or Q13 bht easy hn sjhny hn srf code koi mushkil nhi!