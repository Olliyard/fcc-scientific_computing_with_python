import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, val in kwargs.items():
            for _ in range(val):
                self.contents.append(key)
        
    def draw(self, amount):
        if amount > len(self.contents):
            return self.contents

        balls = []
        for _ in range(amount):
            balls.append(self.contents.pop(random.randrange(len(self.contents))))
        return balls
        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):  #Hat object, balls and amount to draw, number of balls to draw total, number of experiments to perform.
    no_input_balls = []
    succes = 0
    for key in expected_balls:
        no_input_balls.append(expected_balls[key])
    
    for _ in range(num_experiments):
        nhat = copy.deepcopy(hat)
        balls = nhat.draw(num_balls_drawn)
        
        balls_drawn = []
        for key in expected_balls:
            balls_drawn.append(balls.count(key))
        
        if balls_drawn >= no_input_balls:
            succes += 1
        
    return succes/num_experiments