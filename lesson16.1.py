class Cashbox:
    money = 10000

    def __init__(self, money):
        self.money = money
 
    def top_up(self,):
        self.money += 1000
    
 
    def count_1000(self):
        return self.money // 1000
 
    def take_away(self):
        if 1000 <= self.money:
            self.money -= 1000
        else:
            return ('Недостаточно денег')
        

cashes = Cashbox(1000)
cashes.top_up()
print(cashes.money)
cashes.count_1000()
print(cashes.money)
cashes.take_away()
print(cashes.money)