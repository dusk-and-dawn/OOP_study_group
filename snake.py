import pygame
from random import randint

class Snake():
    def __init__(self, head, length):
        self.length = length 
        self.head = head
    
    

class Gamebackground():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def spawn_food(self):
        location = randint(range(self.width*self.height))
        print(f"food is at {location}")


first_snake = Snake()