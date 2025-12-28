import pygame
from random import randint, randrange
from pathlib import Path

pygame.init()

class Gamebackground():
    def __init__(self, width, height, color, food_location = (randint(0, 450), randint(0, 450))):
        self.width = width
        self.height = height
        self.color = color
        self.food_location = food_location
        pygame.display.init()
        self.surface = pygame.display.set_mode([self.width, self.height])
        self.surface.fill(self.color)
        pygame.display.set_caption("Experimental Snake")

    def show_splash(self):
        pygame.display.flip()
        # background.update_food()
        self.show_food()

    def spawn_food(self):
        self.surface.fill(self.color)
        #(f"food is at {self.food_location}")
        self.surface.blit(food, self.food_location)

    def show_food(self):
        # self.surface.fill(self.color)
        #print(f"food is at {self.food_location}")
        self.surface.blit(food, self.food_location)
    
    def update_food(self):
        self.food_location = (randrange(0, 450, 20), randrange(0, 450, 20))
        # self.surface.fill(self.color)
        #print(f"food is at {self.food_location}")
        self.surface.blit(food, self.food_location)

    def check_snake(self, snake):
        #print(f"self.foodlocation: {self.food_location} background.head: {snake.head}")
        if self.food_location == snake.head:
            background.update_food()
            snake.grow()


class Snake(Gamebackground):
    def __init__(self , length=3, spawn=(5, 5)):
        self.spawn = spawn
        self.length = length 
        self.head = (int(260), int(260))
        self.grow_size = 1
        self.prior_head = self.head
    
    def spawn_worm(self):
        location = (260, 260)
        background.surface.blit(head, location)

    def update_snake(self):
        counter = 1
        if self.grow_size > 0:
            for i in range(self.grow_size):
                if i == 0:
                    background.surface.blit(head, self.head)
                    counter -= 1
                else:
                    diff = (self.head[0] - self.prior_head[0], self.head[1] - self.prior_head[1])
                    if diff == (0, -20):
                        background.surface.blit(worm, (self.head[0], self.head[1]+30*counter))
                    elif diff == (0, +20):
                        background.surface.blit(worm, (self.head[0], self.head[1]-30*counter))
                    elif diff == (-20, 0):
                        background.surface.blit(worm, (self.head[0]+30*counter, self.head[1]))
                    elif diff == (+20, 0):
                        background.surface.blit(worm, (self.head[0]-30*counter, self.head[1]))
                counter+=1

    def up(self):
        background.surface.fill(background.color)
        self.prior_head = self.head
        self.head = (self.head[0], self.head[1]-20)
        background.surface.blit(head, self.head)
        self.update_snake()

    def down(self):
        background.surface.fill(background.color)
        self.prior_head = self.head
        self.head = (self.head[0], self.head[1]+20)
        background.surface.blit(head, self.head)
        self.update_snake()
    
    def left(self):
        background.surface.fill(background.color)
        self.prior_head = self.head
        self.head = (self.head[0]-20, self.head[1])
        background.surface.blit(head, self.head)
        self.update_snake()

    def right(self):
        background.surface.fill(background.color)
        self.prior_head = self.head
        self.head = (self.head[0]+20, self.head[1])
        background.surface.blit(head, self.head)
        self.update_snake()

    def grow(self):
        self.grow_size += 1

    def colision(self):
        pass
    
def pregame_launch():
    background = Gamebackground(500, 500, (50, 168, 82), food_location=(260.0, 260.0))
    snake = Snake()
    food = pygame.image.load(Path("static/food1.png")).convert_alpha()
    food = pygame.transform.smoothscale(food, (32, 32))
    worm = pygame.image.load(Path("static/worm.png")).convert_alpha()
    worm = pygame.transform.smoothscale(worm, (32, 32))
    head = pygame.image.load(Path("static/shead.png")).convert_alpha()
    head = pygame.transform.smoothscale(head, (32, 32))

    clock = pygame.time.Clock()
    running = True

    return background, clock, running, snake, food, worm, head

background, clock, running, snake, food, worm, head  = pregame_launch()
snake.spawn_worm()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            final_score = snake.grow_size
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                snake.left()
            elif event.key == pygame.K_w:
                snake.up()
            elif event.key == pygame.K_d:
                snake.right()
            elif event.key == pygame.K_s:
                snake.down()
    background.show_splash()
    background.check_snake(snake=snake)
    
    clock.tick(60)

pygame.quit()