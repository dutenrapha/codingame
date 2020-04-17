import sys
import math

class game_params:
    
    def __init__(self, my_team_id, my_score = 0, my_magic = 0, opponent_score = 0, opponent_magic = 0, snaffles_in_game = []):
        self.my_team_id = my_team_id
        self.my_score = my_score
        self.my_magic = my_magic
        self.opponent_score = opponent_score
        self.opponent_magic  = opponent_magic
        self.snaffles_in_game = snaffles_in_game
   
    def update(self, my_score, my_magic, opponent_score, opponent_magic, snaffles_in_game):
        self.my_score = my_score
        self.my_magic = my_magic
        self.opponent_score = opponent_score
        self.opponent_magic = opponent_magic
        self.snaffles_in_game = snaffles_in_game
        
        self.update_dealocated_snaffles()
        
    def update_dealocated_snaffles(self):
        
        self.dealocated_snaffles = []
        for s in self.snaffles_in_game:
            if(s.state == 0):
   
                self.dealocated_snaffles.append(s.entity_id)
                
    def closest_goal_snaffle(self):
        element_disct = {}
        for s in self.snaffles_in_game:
            element_disct[s.entity_id] = s.x
        
        if(self.my_team_id == 0):
            return min(element_disct, key=element_disct.get)
        else:
            return max(element_disct, key=element_disct.get)
            
        
                    
class entity:
    def __init__(self, entity_id, entity_type, x, y, vx, vy, state):
        self.entity_id = entity_id 
        self.entity_type = entity_type
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.state = state
        
    def update(self, x, y, vx, vy, state):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.state = state

class wizard(entity):
    def magic(self):
        print("wizard", file=sys.stderr)
        
class snaffle(entity):
    def throw(self):
        print("snaffle", file=sys.stderr)
        
class bludger(entity):
    def run(self):
        print("bludger", file=sys.stderr)

turn = 0
wizards = []
opponent_wizards = []
bludgers = []

my_team_id = int(input())  # if 0 you need to score on the right of the map, if 1 you need to score on the left
game = game_params(my_team_id)
    
# game loop
while True:
    turn+=1
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
 
        if(turn == 1):
             
            if(entity_type == "WIZARD"):
                w = wizard(entity_id, entity_type, x, y, vx, vy, state)
                wizards.append(w)
            elif(entity_type == "OPPONENT_WIZARD"):
                w = wizard(entity_id, entity_type, x, y, vx, vy, state)
                opponent_wizards.append(w)
            elif(entity_type == "BLUDGER"):
                b = bludger(entity_id, entity_type, x, y, vx, vy, state)
                bludgers.append(b)
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
        
        if(entity_type == "SNAFFLE"):
            s = snaffle(entity_id, entity_type, x, y, vx, vy, state)
            snaffles_in_game.append(s)
                    
    game.update(my_score, my_magic, opponent_score, opponent_magic, snaffles_in_game)

    for i in range(2):
        
        print("snaffles in game " + str(len(game.snaffles_in_game)), file=sys.stderr)
        print("snaffle mais próxima do gol " +str(game.closest_goal_snaffle()), file=sys.stderr)
        print("sanffles desalocadas " + str(game.dealocated_snaffles), file=sys.stderr)
        
            
            if(s.entity_id == target):
                print("MOVE " + str(s.x) + " " + str(s.y) + " 150")
        
        if(len(game.dealocated_snaffles) != 0):
            
            informations_snaffle[nearest_snaffle_id][2] = 1
                print("MOVE " + str(x_nearest_snaffle) + " " + str(y_nearest_snaffle) + " 150")
            else:
                print("MOVE 8000 3750 150")

        
    
                

        # Edit this line to indicate the action for each wizard (0 ≤ thrust ≤ 150, 0 ≤ power ≤ 500, 0 ≤ magic ≤ 1500)
        # i.e.: "MOVE x y thrust" or "THROW x y power" or "WINGARDIUM id x y magic"
        print("MOVE 8000 3750 100")
