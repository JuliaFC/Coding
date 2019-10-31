
import math

def FindCenter(n, m, garden):
    
    return (math.floor(n/2), math.floor(m/2))

def EatCarrots(pos_x, pos_y, length, width, total_carrots, garden):

    neighbors = [(pos_x+1, pos_y), (pos_x-1, pos_y), (pos_x, pos_y+1), (pos_x, pos_y-1)]
    neighbors = [(x, y) for (x, y) in neighbors if((x >= 0 and x < length) and (y >=0 and y < width))]
    max_carrots = 0

    for (x, y) in neighbors:
        if (garden[x][y] > max_carrots):
            max_carrots = garden[x][y]
            pos_x = x
            pos_y = y
        

    garden[pos_x][pos_y] = 0;
    awake = (max_carrots != 0)
    total_carrots += max_carrots
    for g in garden:
        print(g)
    print('----------------')
    return (awake, total_carrots, pos_x, pos_y)

def HungryRabbit(garden):
    
    length = len(garden)
    width = len(garden[0])
    pos_x, pos_y = FindCenter(length, width, garden)
    carrots = 0;
    awake = True;
    print(pos_x)
    print(pos_y)
    while awake:
        awake, carrots, pos_x, pos_y = EatCarrots(pos_x, pos_y, length, width, carrots, garden)
    
    return carrots
              
print(HungryRabbit(([
	[1, 2, 4, 2],
	[6, 3, 8, 1],
	[3, 5, 6, 2],
	[5, 7, 8, 1]
])))