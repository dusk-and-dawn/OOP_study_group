from snakes_n_ladders import Player, Snake, Ladder, list_of_ladders, list_of_snakes
from statistics import stdev
import numpy as np
from scipy import stats
res = []

for i in range(1, 100000):
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
print(stdev(res))
print(stdev(res)/(avg/len(res)))
print(min(res))
print(max(res))


data = np.array(res)

mean = data.mean()
print(f"{mean}")
std = data.std(ddof=1)
se = std / np.sqrt(len(data))

z = 1.96
lower = mean - z * se
upper = mean + z * se

print(lower, upper)

over100 = [i for i in res if i>=100]
print(len(over100))
    



