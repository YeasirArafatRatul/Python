#simple
import random
"""
def random_walk(n):
    "//comment returns coordinates after 'n' block random walk"
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N','S','E','W'])
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = x + 1
        elif step == 'W':
            x = x - 1
        else:
            print('No Movement')
        return(x,y)

for i in range(20):
     walk = random_walk(20)
     print(walk,"Distance from home = ",
           abs(walk[0]) + abs(walk[1]))
"""


#complex

def random_walk_two(n):
    
    x,y = 0,0
    
    for i in range(n):
        """dx/dy = distance of x/y from 0 in a graph"""
        (dx,dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x += dx
        y += dy
    return(x,y)

"""
for i in range(20):
     walk = random_walk_two(20)
     print(walk,"Distance from home = ",
           abs(walk[0]) + abs(walk[1]))
"""




"""MONTE CARLO METHOD"""

number_of_walks = 2000

for walk_length in range(1,31):
    no_transport = 0
    for i in range(number_of_walks):
        (x,y)= random_walk_two(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_percentage = float(no_transport)/ number_of_walks
    print("walk size = ", walk_length,
                "/% of no transport = ", 100*no_transport_percentage)
        
