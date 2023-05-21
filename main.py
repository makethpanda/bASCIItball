from playscii import GameObject, GameManager
from playscii.input import Input
import curses
from curses import init_color
import math
import random
from _curses import error as size_error 
from abc import ABC, abstractmethod
import time

#playscii.print_at("Hello, world!", 10, 10)

ZALGO = "⠀     ⠀⠀⠀⠀⣆⣴⡄⠀⠀⠀⠀⠀⠀⣧⣤⣤⠀⠀⠀⠀⠀⠀\n" \
"⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠉⠋⠨⠀⠀⠀⠀⠀⠀⠉⡏⠁⠀⠀⠀⠀⠀⡀\n"\
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠦⡀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⣰⡃⠀\n"\
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣯⢳⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⢀⡇\n"\
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡍⠫⣿⡦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⣠⠾⠋⠀⡜⡆⠀\n"\
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠙⠻⠿⠯⣭⣋⣋⢚⡲⡷⣷⡶⡞⠋⠁⠀⠀⠀⣿⠀\n"\
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⡇⠀⠈⠳⠄⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀\n"\

PENTAGRAM = "⠀⠀⠀⠀⠀⢰⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠂⠀⠀⠀⠀\n"\
"⠀⠀⠀⠀⠀⠀⢿⣿⣶⣄⠀⠀⠀⡀⠀⠀⢀⣠⣾⣿⡏⠀⠀⠀⠀⠀\n"\
"⠀⠀⠀⠀⠀⠀⠘⣿⣬⣽⣾⣿⡟⠛⣻⣵⣿⣛⣹⡿⠀⠀⠀⠀⠀⠀\n"\
"⠀⠀⠀⠀⠀⠀⢀⣻⣷⠋⠀⣙⣿⣿⣟⡉⠈⢻⣷⣅⠀⠀⠀⠀⠀⠀\n"\
"⠀⠀⠀⠀⠀⠀⣾⡏⣿⣦⣾⠟⠋⠈⠻⢿⡦⣾⡞⣿⡆⠀⠀⠀⠀⠀\n"\
"⠀⠀⠀⠀⠀⢸⣿⣼⣿⣯⡁⠀⠀⠀⠀⠀⣹⡿⣴⣼⣿⠀⠀⠀⠀⠀\n"\
"⠀⠀⠀⣠⣴⣿⣿⡁⠀⢿⣇⠀⠀⠀⠀⢠⣿⠃⠈⣻⢿⣦⣄⠀⠀⠀\n"\
"⢀⣴⣾⣿⣿⣶⣿⣷⣶⣞⣿⣴⣶⣦⣴⣮⣽⣤⣰⣿⣣⣽⣿⣷⣤⡀\n"\
"⠀⠀⠀⠀⠀⠀⠀⠻⣷⣤⣻⢷⠀⠀⣸⡿⣡⣾⡿⠁⠉⠉⠉⠉⠉⠉\n"\
"⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⡿⢿⢿⣿⠻⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀\n"\
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"\
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"\
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"\


BASKET ="|    \n" \
        "|~~\ "

SCOREFIRST = " ____\n" \

RANDBALL = "█"

SCOREAREA = "\%/\n" \

PLAYERTHROW = "  o//\n" \
              "  8\n" \
              " / > "

PLAYERLOAD = "  o \n" \
              "  \\\\ \n" \
              "  >>O"

PLAYRUN = "  o \n" \
          " /8\ \n" \
          " / > "

IDLE = "  o \n" \
       " /8\ \n" \
       " / \ "

IDLE2 = "  o \n" \
        " (8) \n" \
        " / \ "

IDLEBALL = "  o \n" \
           " |8\ \n" \
           " ||O "

IDLEBALL2 = "  o \n" \
            " |8\ \n" \
            " ||o "

HAPPY = " \o/ \n" \
        "  8  \n" \
        " / \ "


PLAYRUNB = "  o \n" \
           " /8\ \n" \
           " / >O"

PLAYRAN = "  o \n" \
          " /8\ \n" \
          "  >\ "

PLAYRANB = "  o \n" \
           " /8\ \n" \
           " O>\ "


BALL = "O"

BALLINHAND = ""

CONFETTY = "."

global AIToggle
a = int(input("Do you wish to let the AI play? (1 for yes, 0 for no)"))
if a == 1:
    AIToggle = True
else:
    AIToggle = False
if AIToggle:
    from Player import AIAgent
    agent = AIAgent()
global AI
AI = 0
global AI2
AI2 = ""
global AIchargetime
AIchargetime = 0
global AIactionphase
AIactionphase = 0




class Player(GameObject): # Player inherits the GameObject class
    def __init__(self): # Constructor of your object
        super().__init__(pos=(0, 2), render=PLAYRUN)
        self.shootTime = 0
        self.isshooting = False
        self.AirTime = 0
        self.power = 0
        self.recoveryTime  = 1
        self.hasball = False
        self.ballobject = None
        self.rightmodel = PLAYRUN
        self.leftmodel = PLAYRAN
        self.loadmodel = PLAYERLOAD
        self.throwmodel = PLAYERTHROW
        self.idlemodel = IDLE
        self.idlemodel2 = IDLE2
        self.animationtimer = 0.5
    
    def hasBall(self, ball):
        self.leftmodel = PLAYRUNB
        self.rightmodel = PLAYRANB
        self.loadmodel = PLAYERLOAD
        self.throwmodel = PLAYERTHROW
        self.hasball = True
        self.ballobject = ball
        self.idlemodel = IDLEBALL
        self.idlemodel2 = IDLEBALL2

    
    def resetAnimations(self):
        self.hasball = False
        self.ballobject = None
        self.render = PLAYRUN
        self.leftmodel = PLAYRUN
        self.rightmodel = PLAYRAN
        self.isshooting = False
        self.shootTime = 0
        self.AirTime = 0
        self.power = 0
        self.idlemodel = IDLE
        self.idlemodel2 = IDLE2
        if self.y < 2 or self.y > 2:
            self.y = 2
    
    def update(self): # This method is called every frame. self.delta_time is the time it took between the frames.
        global AI, AI2, AIchargetime, AIToggle
        if (Input.get_key('space') or (AI==3 and AIToggle)) and self.isshooting == False and int(self.recoveryTime) == 0 and self.y == 2 and self.hasball == True:
            self.shootTime += 10*self.delta_time
            AIchargetime += 10*self.delta_time
            print(AIchargetime)
            self.render = self.loadmodel
            self.animationtimer = 0.5
            if self.shootTime > 15:
                self.isshooting = True
                self.recoveryTime = 4
                self.power = int(self.shootTime)/3
        elif self.shootTime > 0 :
            self.power = int(self.shootTime)/3
            self.recoveryTime = 4
            self.isshooting = True
        if self.isshooting == True:
            if AIToggle:
                AI2 = "throw"
            self.animationtimer = 0.5
            self.hasball = False
            self.shootTime = 0
            AIchargetime = 0
            self.render = self.throwmodel
            self.AirTime += 10*self.delta_time
            ballin = 0
            if self.AirTime < 2:
                self.y += 10*self.delta_time*self.power
            elif (self.AirTime > 2 and self.AirTime < 4) or self.y > 2:
                if self.ballobject != None:
                    self.ballobject.applyforce((int(self.power*10), int(self.power*10)))
                    self.ballobject = None
                self.y -= 10*self.delta_time*self.power
            else:
                self.resetAnimations()
                self.isshooting = False
        else:
            if AIToggle:
                AI2 = "nothrow"
            if Input.get_key('right') or AI == 1:
                self.render = self.rightmodel
                if self.x < 77:
                    self.x += 20*self.delta_time
                self.animationtimer = 0.5
            if Input.get_key('left')or AI == 2:
                self.render = self.leftmodel
                self.x -= 20*self.delta_time
                self.animationtimer = 0.5
            else:
                if self.animationtimer > 0:
                    self.animationtimer -= 1*self.delta_time
                else:
                    self.animationtimer = 0.5
                    if self.y < 2 or self.y > 2:
                        self.y = 2
                    if self.render == self.idlemodel:
                        self.render = self.idlemodel2
                    else:
                        self.render = self.idlemodel
        if self.recoveryTime > 0:
            print("recovery: " + str(self.recoveryTime) + " seconds")
            self.recoveryTime -= 1*self.delta_time
        else:
            if self.render == "HAPPY": 
                self.render = self.idlemodel
            self.recoveryTime = 0

class Randball(GameObject):
    def __init__(self):
        super().__init__(pos=(50, 10), render=RANDBALL)
        self.isinhand = False
        self.velocity = (0, 0)
        self.gravity = 5
        self.weight = 1
        self.invincibilityFrames = 0
    
    def setup(self):
        self.isinhand = False
        self.velocity = (0, 0)#x and y
        self.gravity = 1
        self.weight = 1
    
    def applyforce(self, force):
        force = (force[0]*2, force[1]*2)
        self.isinhand = False
        self.render = RANDBALL
        # use laws of physics to calculate velocity
        max_velocity = 10000
        magnitude = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)
        if magnitude > max_velocity:
            self.velocity = (self.velocity[0] * max_velocity / magnitude, self.velocity[1] * max_velocity / magnitude)
        self.velocity = (force[0]/self.weight - self.velocity[0]*0.01, force[1]/self.weight - self.velocity[1]*0.01)
    
    def physicsRefresh(self):
        #apply air resistance
        #self.velocity = (self.velocity[0]*0.99 - self.velocity[0]*self.velocity[0]*0.01, self.velocity[1]*0.99 - self.velocity[1]*self.velocity[1]*0.01)
        self.velocity = (self.velocity[0]*0.99 - self.velocity[0]*0.01, self.velocity[1]*0.99 - self.velocity[1]*0.01)
        #apply gravity and friction
        self.velocity = (self.velocity[0], self.velocity[1]-self.gravity+self.velocity[0]*0.05)
        #apply velocity
        self.x += self.velocity[0]*self.delta_time
        if self.x < 1:
            self.x = 1
            self.velocity = (-self.velocity[0]*0.9, self.velocity[1]*0.9)
        if self.x > 79:
            self.x = 79
            self.velocity = (-self.velocity[0]*0.9, self.velocity[1]*0.9)
        self.y += self.velocity[1]*self.delta_time
        if self.y < 0:
            self.y = 0
            self.velocity = (self.velocity[0]*0.9, -self.velocity[1]*0.9)
        if self.y > 19:
            self.y = 19
            self.velocity = (self.velocity[0]*0.9, -self.velocity[1]*0.9)
        if random.randint(0, 100) < 45:
            self.gravity = random.randint(-10, 10)
            self.applyforce((random.randint(-100, 100), random.randint(-100, 100)))
            self.weight = random.randint(1, 10)

        
    def draw(self, board):
        #return super().draw(board)
        render_text = self.render.split('\n')
        x, y = int(self.x), int(self.y)
        if len(render_text) == 1 and render_text[0] == '':
            return
        for i in range(len(render_text)):
            if not (0 <= y - i < len(board)):
                break
            for j in range(len(render_text[i])):
                if not (0 <= x + j < len(board[0])):
                    continue
                #color using the curses color parameter
                board[~(y - i)][x + j] = render_text[i][j] 
                #board[~(y - i)][x + j] = render_text[i][j]
           
            

    def update(self):# This method is called every frame. self.delta_time is the time it took between the frames.
        self.physicsRefresh()       

class Ball(GameObject):
    def __init__(self):
        super().__init__(pos=(50, 10), render=BALL)
        self.isinhand = False
        self.velocity = (0, 0)
        self.gravity = 5
        self.weight = 1
        self.invincibilityFrames = 0
    
    def setup(self):
        self.isinhand = False
        self.velocity = (0, 0)#x and y
        self.gravity = 1
        self.weight = 1
    
    def on_collision(self, other):
        return super().on_collision(other)
    
    def applyforce(self, force):
        force = (force[0]*2, force[1]*2)
        self.invincibilityFrames = 10
        print("BALLFLYIN")
        self.isinhand = False
        self.render = BALL
        # use laws of physics to calculate velocity
        max_velocity = 100
        magnitude = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)
        if magnitude > max_velocity:
            self.velocity = (self.velocity[0] * max_velocity / magnitude, self.velocity[1] * max_velocity / magnitude)
        self.velocity = (force[0]/self.weight - self.velocity[0]*0.01, force[1]/self.weight - self.velocity[1]*0.01)
        print("thrown with force", force, "and velocity", self.velocity)
        self.invincibilityFrames = 20
        velo = self.physicsRefresh()
        print("velo", velo)
    
    def physicsRefresh(self):
        #apply air resistance
        #self.velocity = (self.velocity[0]*0.99 - self.velocity[0]*self.velocity[0]*0.01, self.velocity[1]*0.99 - self.velocity[1]*self.velocity[1]*0.01)
        self.velocity = (self.velocity[0]*0.99 - self.velocity[0]*0.01, self.velocity[1]*0.99 - self.velocity[1]*0.01)
        #apply gravity and friction
        self.velocity = (self.velocity[0], self.velocity[1]-self.gravity+self.velocity[0]*0.05)
        #apply velocity
        self.x += self.velocity[0]*self.delta_time
        if self.x < 1:
            self.x = 1
            self.velocity = (-self.velocity[0]*0.9, self.velocity[1]*0.9)
        if self.x > 79:
            self.x = 79
            self.velocity = (-self.velocity[0]*0.9, self.velocity[1]*0.9)
        self.y += self.velocity[1]*self.delta_time
        if self.y < 0:
            self.y = 0
            self.velocity = (self.velocity[0]*0.9, -self.velocity[1]*0.9)
        if self.y > 19:
            self.y = 19
            self.velocity = (self.velocity[0]*0.9, -self.velocity[1]*0.9)

    def update(self):# This method is called every frame. self.delta_time is the time it took between the frames.
        if not self.isinhand:
            self.physicsRefresh()
        else:
            self.render = BALLINHAND
        if self.invincibilityFrames > 0:
            self.invincibilityFrames -= 1
        else:
            self.invincibilityFrames = 0

class Basket(GameObject):
    def __init__(self):
        super().__init__(pos=(76, 10), render=BASKET)
        self.x = 76
        self.y = 10
        self.width = 4
        self.height = 2

class ScoreFirst(GameObject):
    def __init__(self):
        super().__init__(pos=(71, 10), render=SCOREFIRST)
        self.x = 72
        self.y = 10
        self.width = 3
        self.height = 1

class ScoreSecond(GameObject):
    def __init__(self):
        super().__init__(pos=(72, 10), render=SCOREAREA)
        self.x = 72
        self.y = 9
        self.width = 2
        self.height = 1

class Confetty(GameObject):
    def __init__(self):
        super().__init__(pos=(71, 10), render=CONFETTY)
        self.x = 72
        self.y = 10
        self.width = 1
        self.height = 1
        self.isout = 0
        self.velocity = (0, 0)#x and y
        self.gravity = 0.6
        self.weight = 0.6
    
    def update(self):
        #if touching ground
        self.physicsRefresh()
        if self.isout <= 0:
            #delete self
            self.render = ""
        else:
            self.render = CONFETTY
            self.isout -= 1

        
    def applyforce(self, force):
        force = (force[0], force[1])
        # use laws of physics to calculate velocity
        max_velocity = 10000
        magnitude = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)
        if magnitude > max_velocity:
            self.velocity = (self.velocity[0] * max_velocity / magnitude, self.velocity[1] * max_velocity / magnitude)
        self.velocity = (force[0]/self.weight - self.velocity[0]*0.01, force[1]/self.weight - self.velocity[1]*0.01)
        velo = self.physicsRefresh()
    def physicsRefresh(self):
        #apply air resistance
        #self.velocity = (self.velocity[0]*0.99 - self.velocity[0]*self.velocity[0]*0.01, self.velocity[1]*0.99 - self.velocity[1]*self.velocity[1]*0.01)
        self.velocity = (self.velocity[0]*0.99 - self.velocity[0]*0.01, self.velocity[1]*0.99 - self.velocity[1]*0.01)
        #apply gravity and friction
        self.velocity = (self.velocity[0], self.velocity[1]-self.gravity+self.velocity[0]*0.05)
        #apply velocity
        self.x += self.velocity[0]*self.delta_time
        if self.x < 1:
            self.x = 1
            self.velocity = (-self.velocity[0]*0.9, self.velocity[1]*0.9)
        if self.x > 79:
            self.x = 79
            self.velocity = (-self.velocity[0]*0.9, self.velocity[1]*0.9)
        self.y += self.velocity[1]*self.delta_time
        if self.y < 0:
            self.y = 0
            self.velocity = (self.velocity[0]*0.9, -self.velocity[1]*0.9)
        if self.y > 19:
            self.y = 19
            self.velocity = (self.velocity[0]*0.9, -self.velocity[1]*0.9)
    
class GameManager(GameManager): # Inherits GameManager
    def __init__(self): # Constructor: If you want to keep track of the object, construct them here!
        super().__init__((80, 20)) # (80, 20) is the size of your game screen.
        self.player = (Player())
        self.basket = (Basket())
        self.ball = (Ball())
        self.randball = (Randball())
        self.scorefirst = (ScoreFirst())
        self.scoresecond = (ScoreSecond())
        self.set_title("BASCIItball") # set_title changes the title which will appear at the top of your game.
        self.scoreObject = (GameObject((10, 10), "score: 0"))
        self.steve = (GameObject((50, 18), "Stephen is :"))
        self.scoreframes = 0
        self.recoveryTime = 20
        self.score = 0
        self.terrormode = False
        self.terrorrecovery = 0
        self.confetty = []
        for i in range(0, 10):
            self.confetty.append((Confetty()))
    
    def start(self):
        self.__stdscr = curses.initscr()
        self.setup()
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_RED, -1)
        #make the red brighter
        
        curses.init_pair(2, curses.COLOR_GREEN, -1)
        #make the green neon
        init_color(2, 0, 1000, 0)
        curses.init_pair(3, curses.COLOR_YELLOW, -1)
        #make the yellow brighter
        init_color(3, 1000, 1000, 0)
        curses.init_pair(4, curses.COLOR_BLUE, -1)
        curses.init_pair(5, curses.COLOR_MAGENTA, -1)
        #make the magenta neon
        init_color(5, 1000, 0, 1000)
        while True:
            if self.__flags['quit']:
                curses.endwin()
                break
            curr_time = time.time()
            self.delta_time = curr_time - self.__old_time
            self.__old_time = curr_time
            self.update()
            self.__clear_board()
            for game_object in self.__game_objects:
                game_object.delta_time = self.delta_time
                game_object.update()
                #if game object is Randball
                if game_object == self.randball:
                    #specific color
                    game_object.draw(self.__board)
                game_object.draw(self.__board)
            try:
                self.__update_board()
            except size_error:
                curses.resize_term(self.height + 5, self.width + 10)
                self.__stdscr.refresh()
            time.sleep(0.02)
    
    def __update_board(self):
        self.__stdscr.clear()
        padding = ' ' * ((curses.COLS - self.width) // 2)
        self.__stdscr.addstr(padding + '-' * (self.width + 2) + '\n')
        self.__stdscr.addstr(padding + f"|{self.__title:^{self.width}}|\n")
        #if title contains "terrormode"
        if "terrormode" in self.__title:
            #specific color
            self.__stdscr.addstr(padding + f"|{self.__title:^{self.width}}|\n", curses.color_pair(random.randint(1, 5)))
        self.__stdscr.addstr(padding + '-' * (self.width + 2) + '\n')
        for row in self.__board:
            self.__stdscr.addstr(padding + '|')
            for curr in row:
                #only change the color if it's a randball
                if curr == '█' or curr == '.':
                    self.__stdscr.addstr(f"{curr:^1}", curses.color_pair(random.randint(1, 6)))
                elif curr in PENTAGRAM:
                    #red
                    self.__stdscr.addstr(f"{curr:^1}", curses.color_pair(1))
                else:
                    self.__stdscr.addstr(f"{curr:^1}")
            self.__stdscr.addstr('|\n')
        self.__stdscr.addstr(padding + '-' * (self.width + 2))
        self.__stdscr.refresh()

    def setup(self): # This is called right before the first update call.
        self.add_object(self.player) # Register the object to your manager. If the object is not registered, they will not appear on the screen.
        self.add_object(self.ball)
        self.add_object(self.scorefirst)
        self.add_object(self.scoresecond)
        self.add_object(self.basket)
        self.add_object(self.scoreObject)
        self.add_object(self.steve)

    def update(self): # This is called every frame.
        global AI2, AI, state, action, reward, AIchargetime, AIactionphase, AIToggle
        #stop player from going off screen
        if self.player.x < 1:
            self.player.x = 2
        if self.player.x > 78:
            self.player.x = 77
        # if player is colliding with ball
        # if player is pretty much on top of ball
        if abs((self.player.x+1) - self.ball.x) < 2 and self.player.y == self.ball.y+2 and self.ball.isinhand == False and self.ball.invincibilityFrames == 0:
            self.player.animationtimer = 0.5
            self.ball.isinhand = True
            self.player.hasBall(self.ball)
            if AIToggle:
                AI2 = "ball"
        if self.ball.isinhand == True:
            self.ball.x = self.player.x+3
            self.ball.y = self.player.y+1
        if Input.get_key_down('A'):
            #AIToggle = not AIToggle
            print("let's not do that")
        if Input.get_key_down('q'): # if 'q' key is pressed,
            self.quit() # quit the game.
            print("nah")
        if Input.get_key_down('b') and not AIToggle:
            self.terrormode = True
            for i in range(0, 10):
                self.randball = (Randball())
                self.add_object(self.randball)
        if self.ball.on_collision(self.basket):
            self.ball.applyforce((-1, 1))
        if self.ball.on_collision(self.scorefirst) and self.recoveryTime == 0:
            self.scoreframes = 50
        if self.ball.on_collision(self.scoresecond):
            if self.scoreframes > 0 or self.scoreframes < 0:
                self.scoreframes = 0
                self.score += 2
                if AIToggle:
                    AI2 = "scored"
                self.scoreObject.render = "Score: "+str(self.score)
                self.player.render = HAPPY
                self.player.animationtimer = 0.5
                for i in range(10):
                    self.add_object(self.confetty[i])
                    self.confetty[i].isout = 60
                    self.confetty[i].x = 72
                    self.confetty[i].y = 10
                    self.confetty[i].render = CONFETTY
                    self.confetty[i].applyforce((random.randint(1, 5), random.randint(5, 10)))
            self.recoveryTime = 20
        if self.scoreframes > 0:
            self.scoreframes -= 1
        if self.recoveryTime > 0:
            self.recoveryTime -= 1
        ################################AI
        if AIactionphase == 0 and AIToggle:
            state = [self.player.x, self.player.y, self.ball.x, self.ball.y, self.score]
            action = agent.get_action(state)
            if action == 0:
                AI = 1
                self.steve.render = "Stephen is going right"
            elif action == 1:
                self.steve.render = "Stephen is going left"
                AI = 2
            elif action == 2:
                #update player
                AI = 3
                self.steve.render = "Stephen is shooting:"+str(AIchargetime)
            else:
                print("error")
            AIactionphase = 1
            
            #edit self.scoreObject = (GameObject((50, 18), "Stephen is :"))
        elif AIToggle:
            if AI2 == "scored":
                AI = 0
                reward = 15
            elif AI2 == "throw":
                AI = 0
                reward = 5 + int(AIchargetime/2)
            elif AI2 == "notthrow":
                AI = 0
                reward = 0
            elif AI2 == "ball":
                AI = 0
                reward = 5
            #check if player is closer to ball
            elif abs(self.player.x - self.ball.x) < abs(state[0] - self.ball.x) and (not self.ball.isinhand):
                reward = 2
            else: reward = -1
            next_state = [self.player.x, self.player.y, self.ball.x, self.ball.y, self.score]
            agent.train(state, action, reward, next_state, False)
            AIactionphase = 0
            AI2 = ""
        ################################AI

        if self.score > 1000 and self.score <= 1003 and self.terrormode == False:
            self.terrormode = True
            for i in range(0, 10):
                self.randball = (Randball())
                self.add_object(self.randball)
        if self.terrormode == True:
            self.terrorrecovery = 10
            #set title well
            self.__title = "bASCIItball"
            #remplace random letters from the title with randballs
            for i in range(random.randint(0, 10)+self.score):
                if random.randint(0, 1) == 0:
                    self.__title = self.__title.replace(random.choice(self.__title), '█')
            #append "terrormode" to the title
            self.__title += " CR1TICAL ERROR"
            #have the texts move and change color and say cryptic zalgo stuff
            self.scoreObject.render = "Score: "+str(self.score)
            self.scoreObject.x = random.randint(0, 80)
            self.scoreObject.y = random.randint(0, 25)
            self.scoreObject.color = random.randint(1, 6)
            #change a random randball's render to a random zalgo character
            if random.randint(0, 10) == 0:
                self.randball.render = random.choice(ZALGO)
            self.terrorrecovery -= 1
            #turn a random randball into a pentagram
            if random.randint(0, 5) == 0:
                self.randball.render = PENTAGRAM
            #turn another random randball into a pentagram
            if random.randint(0, 5) == 0:
                self.randball.render = PENTAGRAM
            #turn another random randball into a zalgo
            if random.randint(0, 10) == 0:
                self.randball.render = ZALGO
            #have the word "run" repeated on the screen outside of the board
            if random.randint(0, 10) == 0:
                self.__stdscr.addstr(random.randint(0, 20), random.randint(0, 80), "run", curses.color_pair(random.randint(1, 6)))
            #have the word "die" repeated on the screen outside of the board
            if random.randint(0, 10) == 0:
                self.__stdscr.addstr(random.randint(0, 20), random.randint(0, 80), ":D", curses.color_pair(random.randint(1, 6)))
            #have the word "help" repeated on the screen outside of the board
            if random.randint(0, 10) == 0:
                self.__stdscr.addstr(random.randint(0, 20), random.randint(0, 80), "help", curses.color_pair(random.randint(1, 6)))
            #have the word "pain" repeated on the screen outside of the board
            if random.randint(0, 10) == 0:
                self.__stdscr.addstr(random.randint(0, 20), random.randint(0, 80), "qdj&ééèç", curses.color_pair(random.randint(1, 6)))
            if self.terrorrecovery <= 0 and self.score > 12:
                self.terrormode = False
                #delete most of the randballs
                for game_object in self.__game_objects:
                    if game_object == self.randball:
                        del game_object
                #reset title
                self.__title = "bASCIItball"
                #reset terrorrecovery
                self.terrorrecovery = 20*self.score
                #move score object back to normal
                self.scoreObject.x = 0
                self.scoreObject.y = 0
        

            
if __name__ == "__main__":

    # apply this globally 
    manager = GameManager()
    manager.start()