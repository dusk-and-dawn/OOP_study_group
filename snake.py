import pygame
from random import randint

class Snake():
    def __init__(self, spawn=(5, 5), head, length=3):
        self.spawn = spawn
        self.length = length 
        self.head = head
        self.grow_size = 0
    
    def movement(self):
        # up = (x=x, y+=1)
        # down = (x=x, y-=1)
        #left = (x-=1, y=y)
        #right = (x+=1, y=y)

    def grow(self):
        self.grow_size += 1

    def colision(self):
        pass
    
    

class Gamebackground():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def spawn_food(self):
        location = randint(range(self.width*self.height))
        print(f"food is at {location}")


first_snake = Snake()