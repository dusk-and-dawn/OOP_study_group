class leaderboard: 
    def __init__(self, name, scores):
        self.name = name 
        self.scores = scores 

    def highest_score(self):
        return self.scores[0]
    
    def add_score(self, value):
        self.scores.append(value)

    