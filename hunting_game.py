import random
import string

class World:
    
    def __init__(self, m, n, probability):
        self.m = m
        self.n = n
        self.data = [["_" for j in range(self.n)]for i in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if random.random() < probability:
                    self.data[i][j] = "#"

    def print_world(self):
        for i in range(self.m):
            for j in range(self.n):
                print self.data[i][j],
            print
        print

    def get_free_position(self):
        a = random.randint(0, self.m -1)
        b = random.randint(0, self.n - 1)
        while self.data[a][b] != "_":
            a = random.randint(0, self.m -1)
            b = random.randint(0, self.n - 1)
        return (a,b)

class Robot:
    
    def __init__(self, world, position):
        self.name = random.choice(string.ascii_uppercase)
        self.world = world
        self.position = position
        self.world.data[self.position[0]][self.position[1]] = self.name
        self.history = []

    def __str__(self):
        return self.name

    def change_position(self, x, y):
        self.world.data[self.position[0]][self.position[1]] = "_"
        self.world.data[x][y] = self
        self.position = (x,y)
                
    def random_move(self):
        i = random.randint(0,1)
        j = random.choice([-1,1])
        return (i,j)
        # move(0,-1) meaning the 0th index decrements by 1, robot is moving up 

    def move_towards_goal(self, goal):
        for i in range(0,2):
            if self.position[i] != goal[i]:
                if goal[i] > self.position[i]:
                    if goal[i] - self.position[i] <= (self.world.m / 2):
                        return (i,1)
                    else: return (i,-1)
                else:
                    if self.position[i] - goal[i] <= (self.world.m / 2):
                        return (i,-1)
                    else: return (i,1)

            
    
    def move_robot(self, move):
  	# to ensure robot wont move out of the world
        x = self.position[0]
        y = self.position[1]
        if move == (1,-1) and self.world.data[x][y - 1] == "_":
            self.change_position(x, (y - 1) % self.world.n)
        elif move == (1,1) and self.world.data[x][(y + 1) % self.world.n] == "_":
            self.change_position(x, (y + 1) % self.world.n)
        elif move == (0,1) and self.world.data[(x + 1) % self.world.m] [y]== "_":
            self.change_position((x + 1) % self.world.m, y)
        elif move == (0,-1) and self.world.data[(x - 1)][y] == "_":
            self.change_position((x - 1) % self.world.m, y)

            
world = World(10, 15, 0.08)      
robot1 = Robot(world, world.get_free_position())
print "Robot1 is ", robot1
robot2 = Robot(world, world.get_free_position())
print "Robot2 is ", robot2
robot3 = Robot(world, world.get_free_position())
print "Robot3 is ", robot3
robot4 = Robot(world, world.get_free_position())
print "Robot4 is ", robot4

def hunting_game(world, robots, running):
    print "Robot",running, "is running."
    world.print_world()
    for i in range(15):
        for robot in robots:
            robot.history.append(robot.position)
            if robot == running:
                robot.move_robot(robot.random_move())
            else:
                robot.move_robot(robot.move_towards_goal(running.position))
        world.print_world()
    

def print_history(robots):
    for robot in robots:
        print "Robot's", robot, "history is: ", robot.history

hunting_game(world, [robot1,robot2,robot3,robot4], robot1)
print_history([robot1,robot2,robot3,robot4])
