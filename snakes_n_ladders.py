from random import randint

class Player:
    def __init__(self, name, current=0):
        self.current = current
        self.name = name
    
    def take_turn(self):
        dice_roll = randint(1, 6)
        if self.current < 94:
            self.current += dice_roll
        elif self.current + dice_roll > 100:
            pass
        else:
            self.current += dice_roll
        # print(f"{self.name} rolled a {dice_roll} and is now on field {self.current}")


class Snake:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

class Ladder:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top 

list_of_snakes = [
    Snake(98, 34), 
    Snake(93, 74), 
    Snake(83, 39), 
    Snake(73, 1), 
    Snake(69, 33), 
    Snake(49, 11),
    Snake(48, 9),
    Snake(46, 5),
    Snake(44, 22),
    Snake(24, 2)
]

list_of_ladders = [
    Ladder(8, 26),
    Ladder(12, 31),
    Ladder(17, 25),
    Ladder(21, 82),
    Ladder(28, 66),
    Ladder(36, 57),
    Ladder(43, 77),
    Ladder(52, 91),
    Ladder(75, 86),
    Ladder(80, 99)
]

