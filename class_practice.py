class Car:
    def __init__(self, color, speed = 0):
        self.color = color
        self.speed = speed
        
    def speedUp(self):
        self.speed = self.speed + 10
        
    def speedDown(self):
        self.speed -= 10
        
class Bag:
    def __init__(self, item):
        self.item = item
    
    def contains(self):
        print(self.item)
    
    def insert(self, item):
        self.item.append(item)
    def remove(self, item):
        self.item.remove(item)
        
    def count(self):
        return len(self)
    
    def __str__(self):
        return "Bag contains: " + str(self.item)
    
mybag = Bag([])
mybag.insert('cellphone')
print(mybag)
mybag.contains()
mybag.insert('protein')
print(mybag)
mybag.insert('protein')
print(mybag)
mybag.remove('protein')
print(mybag)

#from class_practice import Car
class SuperCar(Car):
    def __init__(self, color, speed=0, bTurbo = True):
        super().__init__(color, speed)
        self.bTurbo = bTurbo
        
    def setTurbo(self, bTurbo):
        self.bTurbo = bTurbo
        
    def speedUp(self):
        if self.bTurbo:self.speed += 50
        else: super().speedUp()
        
    def __str__(self):
        if self.bTurbo :
            return "[%s] [speed = %d] turbo mode" % (self.color, self.speed)
        else:
            return "[%s] [speed = %d] eco mode" % (self.color, self.speed)
        
s1 = SuperCar("gold", 0, True)
s2 = SuperCar("White", 0, False)

s1.speedUp()
s2.speedUp()

print(s1)