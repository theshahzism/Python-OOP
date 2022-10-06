#q2

class publication:
        title=input("Enter title")
        price=int(input("Enter price"))
class book(publication):
    def getdata(self):
        self.pagecount=int(input("Enter pagecount"))
    def putdata(self):
        print(f'Page count is {self.pagecount}')
        print(self.price)
class tape(publication):
    def getdata(self):
        self.playingtime=float(input("Enter playing time"))
    def putdata(self):
        print(f'Playing time is {self.playingtime}')

a=publication()
print(a.title)

b=book()
b.getdata()
b.putdata()

c=tape()
c.getdata()
c.putdata()

#q3

class sales:
    l=[]
    @classmethod
    def getdata(cls):
        for i in range(1,4):
            n=int(input(f'Enter sales of month{i}'))
            cls.l.append(n)
    @classmethod
    def putdata(cls):
        for i in cls.l:
            print(f'sale is {i}')

class publication:
    title = ""
    price = 0

    def getdata(self):
        self.title =input("Enter Title")
        self.price=int(input("Enter price"))

    def putdata(self):
        print(f'Title is {self.title} and price is {self.price}')


class book(sales,publication):
    def getdata(self):
        super().getdata()
        self.pagecount = int(input("Enter pagecount"))

    def putdata(self):
        super().putdata()
        print(f'Page count is {self.pagecount}')


class tape(sales,publication):
    def getdata(self):
        super().getdata()
        self.playingtime = float(input("Enter playing time"))

    def putdata(self):
        super().putdata()
        print(f'Playing time is {self.playingtime}')


b = book()
b.getdata()
b.putdata()

c = tape()
c.getdata()
c.putdata()


#q4

class sales:
    l=[]
    @classmethod
    def getdata(cls):
        for i in range(1,4):
            n=int(input(f'Enter sales of month{i}'))
            cls.l.append(n)
    @classmethod
    def putdata(cls):
        for i in cls.l:
            print(f'sale is {i}')

class publication:
    title = ""
    price = 0

    def getdata(self):
        self.title =input("Enter Title")
        self.price=int(input("Enter price"))

    def putdata(self):
        print(f'Title is {self.title} and price is {self.price}')


class book(sales,publication):
    def getdata(self):
        super().getdata()
        self.pagecount = int(input("Enter pagecount"))

    def putdata(self):
        super().putdata()
        print(f'Page count is {self.pagecount}')


class tape(sales,publication):
    def getdata(self):
        super().getdata()
        self.playingtime = float(input("Enter playing time"))

    def putdata(self):
        super().putdata()
        print(f'Playing time is {self.playingtime}')

class disk(sales,publication):
    disktype=""
    d={"c":"CD","d":"DVD"}

    def getdata(self,):
        super().getdata()
        n = input("Enter c for CD and d for DVD")
        if n == "c":
            self.disktype = disk.d["c"]
        if n == "d":
            self.disktype = disk.d["d"]

    def putdata(self):
        super().putdata()
        print(self.disktype)




Disk=disk()
Disk.getdata()
Disk.putdata()

#q6

class date:
    def setter(self):
        self.a=int(input("Enter day"))
        self.b=int(input("Enter month"))
        self.c=int(input("Enter year"))
    def __str__(self):
        print(f'{self.a}-{self.b}-{self.c}')
Date=date()
Date.setter()
Date.__str__()

#q7

class date:
    format=int(input("Enter format"))
    def setter(self):
        self.a=int(input("Enter day"))
        self.b=int(input("Enter month"))
        self.c=int(input("Enter year"))
    def __str__(self):
        if date.format==1:
            print(f'{self.a}-{self.b}-{self.c}')
        elif date.format==2:
            print(f'{self.c}-{self.a}-{self.c}')
Date=date()
Date.setter()
Date.__str__()s

#Q9

class sales:
    l=[]
    @classmethod
    def getdata(cls):
        for i in range(1,4):
            n=int(input(f'Enter sales of month{i}'))
            cls.l.append(n)
    @classmethod
    def putdata(cls):
        for i in cls.l:
            print(f'sale is {i}')

class publication:
    title = ""
    price = 0

    def getdata(self):
        self.title =input("Enter Title")
        self.price=int(input("Enter price"))

    def putdata(self):
        print(f'Title is {self.title} and price is {self.price}')


class book(sales,publication):
    count=0
    def __init__(self):
        book.count+=1

    def getdata(self):
        super().getdata()
        self.pagecount = int(input("Enter pagecount"))

    def putdata(self):
        super().putdata()
        print(f'Page count is {self.pagecount}')


class tape(sales,publication):
    count=0
    def __init__(self):
        tape.count+=1
    def getdata(self):
        super().getdata()
        self.playingtime = float(input("Enter playing time"))

    def putdata(self):
        super().putdata()
        print(f'Playing time is {self.playingtime}')

class disk(sales,publication):
    disktype=""
    d={"c":"CD","d":"DVD"}
    count=0
    def __init__(self):
        disk.count+=1
    def getdata(self,):
        super().getdata()
        n = input("Enter c for CD and d for DVD")
        if n == "c":
            self.disktype = disk.d["c"]
        if n == "d":
            self.disktype = disk.d["d"]

    def putdata(self):
        super().putdata()
        print(self.disktype)




Disk=disk()
Disk.getdata()
Disk.putdata()
print(Disk.count)

#Q11

class vehicle:
    def __init__(self,a,b):
        self.__wheels=a
        self.__colour=b
    def getter(self):
        print(self.__wheels,self.__colour)
    def setter(self,c,d):
        self.__wheels=c
        self.__colour=d
a=vehicle(2,"blue")
a.setter(4,"Black")
a.getter()

#Q27

class object:
    def __init__(self):
        print("object")
class Physical_object(object):
    def __init__(self):
        print("Physical object")
        super().__init__()
class vehicle(Physical_object):
    def __init__(self):
        print("Vehicle")
        super().__init__()
class ground(vehicle):
    def __init__(self):
        print("ground")
        super().__init__()
class flying(vehicle):
    def __init__(self):
        print("Flying")
        super().__init__()
class fuel(ground):
    def __init__(self):
        print("fuel")
        super().__init__()
class aircraft(ground,flying):
    def __init__(self):
        print("Aircraft")
        super().__init__()
class commercial(aircraft):
    def __init__(self):
        print("Commercial")
        super().__init__()
class boeing(commercial):
    def __init__(self):
        print("Boeng")
        super().__init__()
a=boeing()
