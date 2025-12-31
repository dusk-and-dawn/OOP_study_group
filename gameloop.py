import pygame 
from snake import pregame_launch, post_game, Snake, Gamebackground 


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
post_game()