import random
class Enemy(): #character for enemy
    def __init__(self, name, hp, ap, dp, rank, exp, lvnxt):
        self.name = name
        self.hp = hp
        self.ap = ap
        self.dp = dp
        self.rank = rank
        self.exp = exp
        self.lvnxt = lvnxt
        self.alive = True
        self.stats = {
                    "Name": name,
                    "Health Point" : hp,
                    "Attack Point" : ap,
                    "Defence Point" : dp,
                    "Rank" : rank,
                    "Exp" : exp,
                    "lvlNext" : lvnxt,
                    }
        self.level()

    #Print out the stats of jobs
    def __repr__(self):
        rps = ""
        for k,v in self.stats.items():
            rps += "\n {0}:{1}".format(k,v)
        return rps

    #Cal Diff Jobs Leveling
    def level(self):
        if self.name == "Warrior":
            while self.exp >= self.lvnxt:
                self.rank += 1
                self.exp = self.exp - self.lvnxt
                self.lvnxt = round(self.lvnxt * 1.5) 
                self.hp += max(100)
                self.ap += random.randint(1, 5)
                self.dp += random.randint(1, 3)
        if self.name == "Tanker":
            while self.exp >= self.lvnxt:
                self.rank += 1
                self.exp = self.exp - self.lvnxt
                self.lvnxt = round(self.lvnxt * 1.5) 
                self.hp += max(100)
                self.ap += random.randint(1, 3)
                self.dp += random.randint(1, 5)
    
    #Cal Damage when hiting
    def attack(self,other):
        attack = self.ap * 1.5
        hit = attack - other.dp
        if attack >= other.dp :
            other.hp -= hit
            print("\nYour {0} Hit Enemy {1} For {2} HP, Enemy {3} HP Left {4}".format(self.name, other.name, hit, other.name, other.hp))
        else :
            print("\nYour Attack is too Low")

#Variable 
Warrior = Enemy("Warrior", 100, random.randint(5, 20), random.randint(1, 10), 1, 0, 100)
Tanker = Enemy("Tanker",100, random.randint(1, 10), random.randint(5, 15), 1, 0, 100)


def enemy_1(created): 
    jobs = {"1":Warrior, "2":Tanker}
    job = ""
    while not job in ['1', '2']:
        job = str(random.randint(1,2))
        for i in job :
            created = jobs[i]
    print(created)
    return created

def enemy_2(created): 
    jobs = {"1":Warrior, "2":Tanker}
    job = ""
    while not job in ['1', '2']:
        job = str(random.randint(1,2))
        for i in job :
            created = jobs[i]
    print(created)
    return created

def enemy_3(created): 
    jobs = {"1":Warrior, "2":Tanker}
    job = ""
    while not job in ['1', '2']:
        job = str(random.randint(1,2))
        for i in job :
            created = jobs[i]
    print(created)
    return created


