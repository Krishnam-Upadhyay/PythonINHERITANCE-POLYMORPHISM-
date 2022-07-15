


class Dog:
    def __init__(self,name,age,friendLiness):
        self.name = name
        self.age = age
        self.friednLiness = friendLiness

    def likes_walks(self):
        return True

    def bark(self):
        return "WOof!"



class Samoyed(Dog):
    def __init__(self,name,age,friendLiness):
        super().__init__(name,age,friendLiness)


class Poddle(Dog):
    def __init__(self,name,age,friendLiness):
        super().__init__(name,age,friendLiness)

class GoldenRetriever(Dog):
    def __init__(self,name,age,friendLiness):
        super().__init__(name,age,friendLiness)

    def fetch_ability(self):
        if self.age<2:
            return 8

        elif self.age<10:
            return  10

        else:
            return 7



class GoldenDoddle(Poddle,GoldenRetriever):
    def __init__(self,name,age,friendLiness):
        super().__init__(name,age,friendLiness)

    def bark(self):
        return "aoooooow"    



sammy  = Samoyed("Sammpy",15,10)
print(sammy.name,sammy.age,sammy.friednLiness)
print(sammy.bark())

goldie = GoldenDoddle("Goldie",1,10)
print(goldie.bark())




            
