from snakes_n_ladders import Player, Snake, Ladder, list_of_ladders, list_of_snakes

res = []

for i in range(1, 10000):
    player1 = Player("Kuba")
    rounds = 0
    while True:
        print("new turn")

        player1.take_turn()

        for snake in list_of_snakes:
            if snake.head == player1.current:
                player1.current = snake.tail 
        
        for ladder in list_of_ladders:
            if ladder.bottom == player1.current:
                player1.current = ladder.top
        
        if player1.current == 100:
            rounds += 1
            print(f"game finished after {rounds} rounds")
            res.append(rounds)
            break

        rounds += 1
avg = 0
for i in res:
    avg += i 

print(avg/len(res))


    
    



