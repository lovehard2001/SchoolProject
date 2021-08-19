import random
from Char import Char

Warrior = Char("Warrior", 100, random.randint(5, 20), random.randint(1, 10), 1, 0, 100)
Tanker = Char("Tanker",100, random.randint(1, 10), random.randint(5, 15), 1, 0, 100)

def choose_character_1(created): 
    jobs = {"1":Warrior, "2":Tanker}
    job = ""
    while not job in ['1', '2']:
        job = input("\nChoose your character 1 : 1 for Warrior , 2 for Tanker\n :   ")
        for i in job :
            created = jobs[i]
    print(created)
    return created
                
def choose_character_2(created): 
    jobs = {"1":Warrior, "2":Tanker}
    job = ""
    while not job in ['1', '2']:
        job = input("\nChoose your character 2 : 1 for Warrior , 2 for Tanker\n :   ")
        for i in job :
            created = jobs[i]
    print(created)
    return created
    
def choose_character_3(created): 
    jobs = {"1":Warrior, "2":Tanker}
    job = ""
    while not job in ['1', '2']:
        job = input("\nChoose your character 3 : 1 for Warrior , 2 for Tanker\n :   ")
        for i in job :
            created = jobs[i]
    print(created)
    return created
            
                
    


