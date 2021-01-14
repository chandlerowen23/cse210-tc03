import random

class Thrower:
    def __init__(self):
        self.dice = []
        self.cnt_throw = 0
        

    def throw_dice(self):
        self.dice.clear()
        for die in range(5):
            die = random.randint(1,6)
            self.dice.append(die)
        self.cnt_throw += 1
        

    def can_throw(self):
        if (self.dice.count(5) > 0 or self.dice.count(1) > 0 or self.cnt_throw == 0):
            return True
        else:
            return False
        
    def get_points(self):
        points = 0
        points += self.dice.count(5) * 50
        points += self.dice.count(1) * 100
        return points

