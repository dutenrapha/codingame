import sys
import math


def distance(x_wizard, y_wizard, x_target, y_target):
    return math.sqrt((x_wizard - x_target)**2 +(y_wizard - y_target)**2)


def near_snaffle_position(position_wizard, iformation_snaffle):

    x_nearest_snaffle = -1
    y_nearest_snaffle = -1
    nearest_snaffle_id = -1
    min_snaffle_distance = sys.maxsize
    
    x_wizard, y_wizard = position_wizard
    
    for id_snaffle, x_snaffle, y_snaffle in iformation_snaffle:
        
        snaffle_distance = distance(x_wizard, y_wizard, x_snaffle, y_snaffle)
        

        if(snaffle_distance < min_snaffle_distance):
            min_snaffle_distance = snaffle_distance
            x_nearest_snaffle = x_snaffle
            y_nearest_snaffle = y_snaffle
            nearest_snaffle_id = id_snaffle
 
    return nearest_snaffle_id, x_nearest_snaffle, y_nearest_snaffle
            

def snaffle_near_hotzone(deallocated_snaffles):
    
    x_hotest_snaffle = -1
    id_hotest_snaffle = -1
    hoteste_zone = -1
    
    for id_snaffle, x_snaffle, y_snaffle in deallocated_snaffles:
        
        if (x_snaffle <=3000 and x_snaffle >=500):
            x_hotest_snaffle = x_snaffle
            id_hotest_snaffle = id_snaffle
            hoteste_zone = 0
        elif (x_snaffle >=13000 and x_snaffle<=15500):
            x_hotest_snaffle = x_snaffle
            id_hotest_snaffle = id_snaffle
            hoteste_zone = 1
            
    
    return hoteste_zone, id_hotest_snaffle, x_hotest_snaffle
            
        
    
    
    
# Grab Snaffles and try to throw them through the opponent's goal!
# Move towards a Snaffle to grab it and use your team id to determine towards where you need to throw it.
# Use the Wingardium spell to move things around at your leisure, the more magic you put it, the further they'll move.

my_team_id = int(input())  # if 0 you need to score on the right of the map, if 1 you need to score on the left




# game loop
while True:
    my_score, my_magic = [int(i) for i in input().split()]
    opponent_score, opponent_magic = [int(i) for i in input().split()]
    entities = int(input())  # number of entities still in game
    informations_wizards = []
    informations_snaffle = {}
    magic = 0;
    for i in range(entities):

        entity_id, entity_type, x, y, vx, vy, state = input().split()
        entity_id = int(entity_id)
        x = int(x)
        y = int(y)
        vx = int(vx)
        vy = int(vy)
        state = int(state)

        if (entity_type=="WIZARD"):
            informations_wizards.append((entity_id, x, y, state))
            
        if (entity_type=="SNAFFLE"):
            informations_snaffle[entity_id] = [x, y, state]

    for i in range(2):
        deallocated_snaffles = []
        entity_id_wizard, x_wizard, y_wizard, state_wizard = informations_wizards[i]
        
        if(state_wizard == 1):
            
            if(my_team_id == 0):
                print("THROW 16000 3750 500")
            else:
              
                print("THROW 0 3750 500")
            
        else:
            
            for j in informations_snaffle:
                
                entity_id_snaffle = j
                x_snaffle = informations_snaffle[j][0]
                y_snaffle = informations_snaffle[j][1]
                state_snaffle = informations_snaffle[j][2]
                
                if(state_snaffle != 1):
                    deallocated_snaffles.append((entity_id_snaffle, x_snaffle, y_snaffle))
            
            
            hoteste_zone, id_hotest_snaffle, x_hotest_snaffle = snaffle_near_hotzone(deallocated_snaffles)
            
            if(hoteste_zone != -1 and my_magic >= 20 and magic == 0):
                magic = 1
                if(my_team_id == 0):
                    print("WINGARDIUM" + " " + str(id_hotest_snaffle) + " " + "16000" + " " + "3750" + " " + str(my_magic))
                else:
                    print("WINGARDIUM" + " " + str(id_hotest_snaffle) + " " + "0" + " " + "3750" + " " + str(my_magic))
                                
            else:
       
                nearest_snaffle_id, x_nearest_snaffle, y_nearest_snaffle = near_snaffle_position((x_wizard, y_wizard), deallocated_snaffles)
                          
                if(len(deallocated_snaffles) != 0):
                    informations_snaffle[nearest_snaffle_id][2] = 1
                    print("MOVE " + str(x_nearest_snaffle) + " " + str(y_nearest_snaffle) + " 150")
                else:
                    print("MOVE 8000 3750 150")
        
                
                
        
