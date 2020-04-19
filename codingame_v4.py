import sys
import math

class game_params:
    
    def __init__(self, my_team_id, my_score = 0, my_magic = 0, opponent_score = 0, opponent_magic = 0):
        self.my_team_id = my_team_id
        self.my_score = my_score
        self.my_magic = my_magic
        self.opponent_score = opponent_score
        self.opponent_magic  = opponent_magic
   
    def update(self, my_score, my_magic, opponent_score, opponent_magic, snaffles_in_game):
        self.my_score = my_score
        self.my_magic = my_magic
        self.opponent_score = opponent_score
        self.opponent_magic = opponent_magic
        self.snaffles_in_game = snaffles_in_game        
             
class simulation:
    
    '''
    action =  {type:"MOVE", x:x, y:y, thrust:thrust, id:none}
    '''
    
    def __init__(self, wizards, opponent_wizards, snaffles, bludgers):
    
        for w in wizards:
            w.next_point()
    
        for w in opponent_wizards:
            w.next_point()
        
        for s in snaffles:
            s.next_point()
            
        for b in bludgers:
            b.next_point()
    
    def change_move(self, wizard, action):
        
        magnitude = math.sqrt((wizard.x - action["x"])**2 + (wizard.y - action["y"] )**2)  
        if (action["type"] == "MOVE"):

            self.vx_f = round(((wizard.x - action["x"])/magnitude)*action["thrust"])
            self.vy_f = round(((wizard.y - action["y"])/magnitude)*action["thrust"])
            self.x_f = round(wizard.x + self.vx_f)
            self.y_f = round(wizard.y + self.vy_f)   
    
    
class entity:
    
    def __init__(self, entity_id, entity_type, x, y, vx, vy, state):
        self.entity_id = entity_id 
        self.entity_type = entity_type 
        self.x_0 = x
        self.y_0 = y
        self.vx_0 = vx
        self.vy_0 = vy
        self.state_0 = state 
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.state = state

                
    def update(self, x, y, vx, vy, state):
        self.x_0 = self.x
        self.y_0 = self.y
        self.vx_0 = self.vx
        self.vy_0 = self.vy
        self.state_0 = self.state
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.state = state


class wizard(entity):
    
    def next_point(self):
        self.x_f = round(self.x + self.vx)
        self.y_f = round(self.y + self.vy)
        self.vx_f = round(0.75*self.vx)
        self.vy_f = round(0.75*self.vy)
        
    def find_closest_snaffle(self, snaffles):
        
        min_snaffle_distance = sys.maxsize
        
        for s in snaffles:
            
            d = (self.x - s.x)**2 +(self.y - s.y)**2 
            
            if(d < min_snaffle_distance):
                min_snaffle_distance = d
                snaffle_id  = s.entity_id
                snaffle_x = s.x
                snaffle_y  = s.y  
                
        return snaffle_id, snaffle_x, snaffle_y
        
class snaffle(entity):
        
    def next_point(self):
        self.x_f = round(self.x + self.vx)
        self.y_f = round(self.y + self.vy)
        self.vx_f = round(0.75*self.vx)
        self.vy_f = round(0.75*self.vy)
        
class bludger(entity):
    
    def next_point(self):
        self.x_f = round(self.x + self.vx)
        self.y_f = round(self.y + self.vy)
        self.vx_f = round(0.9*self.vx)
        self.vy_f = round(0.9*self.vy)

turn = 0
wizards = []
opponent_wizards = []
snaffles = []
bludgers = []

my_team_id = int(input())  # if 0 you need to score on the right of the map, if 1 you need to score on the left
game = game_params(my_team_id)

# game loop
while True:
   
    print(turn, file=sys.stderr)
   
    snaffles_in_game = []
    my_score, my_magic = [int(i) for i in input().split()]
    opponent_score, opponent_magic = [int(i) for i in input().split()]
    entities = int(input())  # number of entities still in game
                       
    
    for i in range(entities):
        # entity_id: entity identifier
        # entity_type: "WIZARD", "OPPONENT_WIZARD" or "SNAFFLE" or "BLUDGER"
        # x: position
        # y: position
        # vx: velocity
        # vy: velocity
        # state: 1 if the wizard is holding a Snaffle, 0 otherwise. 1 if the Snaffle is being held, 0 otherwise. id of the last victim of the bludger.
        entity_id, entity_type, x, y, vx, vy, state = input().split()
        entity_id = int(entity_id)
        x = int(x)
        y = int(y)
        vx = int(vx)
        vy = int(vy)
        state = int(state)
        
        if(turn == 0):
             
            if(entity_type == "WIZARD"):
                w = wizard(entity_id, entity_type, x, y, vx, vy, state)
                wizards.append(w)
                
            elif(entity_type == "OPPONENT_WIZARD"):  
                w = wizard(entity_id, entity_type, x, y, vx, vy, state)
                opponent_wizards.append(w)
                       
            elif(entity_type == "BLUDGER"):
                b = bludger(entity_id, entity_type, x, y, vx, vy, state)
                bludgers.append(b)
                
            elif(entity_type == "SNAFFLE"):
                s = snaffle(entity_id, entity_type, x, y, vx, vy, state)
                snaffles.append(s)
            
        else: 
            
            if(entity_type == "WIZARD"):
                for w in wizards:
                    if(w.entity_id == entity_id):
                        w.update(x, y, vx, vy, state)
            elif(entity_type == "OPPONENT_WIZARD"):
                for w in opponent_wizards:
                    if(w.entity_id == entity_id):
                        w.update(x, y, vx, vy, state)
            elif(entity_type == "BLUDGER"):
                for b in bludgers:
                    if(b.entity_id == entity_id):
                        b.update(x, y, vx, vy, state)
            elif(entity_type == "SNAFFLE"):
                for s in snaffles:
                    if(s.entity_id == entity_id):
                        s.update(x, y, vx, vy, state)
    turn+=1                   
  
    for i in range(2):
        
        snaffle_id, snaffle_x, snaffle_y = wizards[i].find_closest_snaffle(snaffles)
        
        snaffles_temp  = snaffles.copy()
        for s in snaffles:
            if(s.entity_id == snaffle_id):
                snaffles.pop(snaffles.index(s))
        
        action =  {"type":"MOVE", "x":14000, "y":30, "thrust":150, id:-99}
        try1 = simulation(wizards, opponent_wizards, snaffles, bludgers)
        try1.change_move(wizards[i], action)
        print("MOVE "+ str(snaffle_x) + " " + str(snaffle_y) + " 150")
        
    snaffles = snaffles_temp.copy()
    print("a", file=sys.stderr)
    print(snaffles, file=sys.stderr)
    '''for w in wizards:
        
       print("Wizards id:" + str(w.entity_id), file=sys.stderr) 
       print("x_0: " + str(w.x_0) , file=sys.stderr)
       print("y_0: " + str(w.y_0) , file=sys.stderr)
       print("vx_0: " + str(w.vx_0) , file=sys.stderr)
       print("vy_0 " + str(w.vy_0) , file=sys.stderr)
       print("state_0: " + str(w.state_0), file=sys.stderr)
       print("x: " + str(w.x) , file=sys.stderr)
       print("y: " + str(w.y) , file=sys.stderr)
       print("vx: " + str(w.vx) , file=sys.stderr)
       print("vy " + str(w.vy) , file=sys.stderr)
       print("state: " + str(w.state), file=sys.stderr)
       print("x_f: " + str(w.x_f) , file=sys.stderr)
       print("y_f: " + str(w.y_f) , file=sys.stderr)
       print("vx_f: " + str(w.vx_f) , file=sys.stderr)
       print("vy_f " + str(w.vy_f) , file=sys.stderr)
       print("\n", file=sys.stderr)
       
    print("\n", file=sys.stderr)
    for w in opponent_wizards:
       
        print("Oppnent wizards id:" + str(w.entity_id), file=sys.stderr) 
        print("x_0: " + str(w.x_0) , file=sys.stderr)
        print("y_0: " + str(w.y_0) , file=sys.stderr)
        print("vx_0: " + str(w.vx_0) , file=sys.stderr)
        print("vy_0 " + str(w.vy_0) , file=sys.stderr)
        print("state_0: " + str(w.state_0), file=sys.stderr)
        print("x: " + str(w.x) , file=sys.stderr)
        print("y: " + str(w.y) , file=sys.stderr)
        print("vx: " + str(w.vx) , file=sys.stderr)
        print("vy " + str(w.vy) , file=sys.stderr)
        print("state: " + str(w.state), file=sys.stderr)
        print("x_f: " + str(w.x_f) , file=sys.stderr)
        print("y_f: " + str(w.y_f) , file=sys.stderr)
        print("vx_f: " + str(w.vx_f) , file=sys.stderr)
        print("vy_f " + str(w.vy_f) , file=sys.stderr)
        print("\n", file=sys.stderr)
        
    print("\n", file=sys.stderr)
    for b in bludgers:
        
        print("Bludgers id:" + str(b.entity_id), file=sys.stderr) 
        print("x_0: " + str(b.x_0) , file=sys.stderr)
        print("y_0: " + str(b.y_0) , file=sys.stderr)
        print("vx_0: " + str(b.vx_0) , file=sys.stderr)
        print("vy_0 " + str(b.vy_0) , file=sys.stderr)
        print("state_0: " + str(b.state_0), file=sys.stderr)
        print("x: " + str(b.x) , file=sys.stderr)
        print("y: " + str(b.y) , file=sys.stderr)
        print("vx: " + str(b.vx) , file=sys.stderr)
        print("vy " + str(b.vy) , file=sys.stderr)
        print("state: " + str(b.state), file=sys.stderr)
        print("x_f: " + str(b.x_f) , file=sys.stderr)
        print("y_f: " + str(b.y_f) , file=sys.stderr)
        print("vx_f: " + str(b.vx_f) , file=sys.stderr)
        print("vy_f " + str(b.vy_f) , file=sys.stderr)
        print("\n", file=sys.stderr)'''
        
    print("\n", file=sys.stderr)
    for s in snaffles:
        
        print("Snaffle id:" + str(s.entity_id), file=sys.stderr) 
        print("x_0: " + str(s.x_0) , file=sys.stderr)
        print("y_0: " + str(s.y_0) , file=sys.stderr)
        print("vx_0: " + str(s.vx_0) , file=sys.stderr)
        print("vy_0 " + str(s.vy_0) , file=sys.stderr)
        print("state_0: " + str(s.state_0), file=sys.stderr)
        print("x: " + str(s.x) , file=sys.stderr)
        print("y: " + str(s.y) , file=sys.stderr)
        print("vx: " + str(s.vx) , file=sys.stderr)
        print("vy " + str(s.vy) , file=sys.stderr)
        print("state: " + str(s.state), file=sys.stderr)
        print("x_f: " + str(s.x_f) , file=sys.stderr)
        print("y_f: " + str(s.y_f) , file=sys.stderr)
        print("vx_f: " + str(s.vx_f) , file=sys.stderr)
        print("vy_f " + str(s.vy_f) , file=sys.stderr)
        print("\n", file=sys.stderr)
   
        
  
    
    
    
    
    
    
    
