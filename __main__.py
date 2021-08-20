from ChooseCharacter import choose_character_1, choose_character_2, choose_character_3
from Enemy import Enemy, enemy_1, enemy_2, enemy_3

def play(chars):
    attack = False
    game_over = False
    turn = 0
    print("Battle Start.The following character are present : \n")
    for c in chars:
        print(c)
        print("")
        if c.alive == True :
            while not game_over :
                n = list(chars)
                for i in len(n):
                    sel = (input("Choose Character to attack: {0} {1}".format((i+1),(chars))))
                    attack = True
                    while attack == True:
                        sel(attack)
                        attack == False
                        while attack == False:
                            Enemy(attack)

                                   
  #  while not game_over:
   #     print("It's the turn of Yours, Please select a character to attack: ".format(chars[turn].name))
    #    possible = []
     #   for i in list(len(chars)):
      #      if not i == turn :
       #         possible.append(i)
        #        print(" - ({0}) : {1} ".format(i,chars[i].c))
       # sel = -1
       # while not sel in possible :
       #     s = input("Selection : ")
        #    try :
         #       sel = int(s)
          #  except :
           #     print("That's not a valid choice")

 #       chars[turn].attack(chars[sel])
  #      if chars[sel].hp <= 0 :
   #         game_over = True
    #        print("That was it! {0} has died and the game is over.".format(chars[sel].name))
     #   turn += 1
      #  if turn == len(chars): turn =0

def start_game():
    start_game = False
    while start_game is False :
        print("Start the Games ?")
        answer = input("\n(Y)es\n(N)o\nAnswer: ").lower()
        if answer == "y" :
            start_game = True
        elif answer == "n" :
            print("Quited")
            exit() 
    

def main() :   
    chars = []
    enemy = []
    
    menu = ""
    print("Testing 123")
    start_game()
    while start_game == True:
        menu = ""
    while not menu.lower() in ['c', 'l', 'b']:
        menu = input("\nMENU\n[C]reate Character \n[L]ist of Character\n[P]lay\n[Q]uit\n: ").lower()
        if menu == 'c':
            chars.append(choose_character_1(chars))
            chars.append(choose_character_2(chars))
            chars.append(choose_character_3(chars))
            menu = ""
        elif menu == 'l' :
            print(chars)
            menu = ""
        elif menu == 'p' :
            play(chars)
            enemy.append(enemy_1(enemy))
            enemy.append(enemy_2(enemy))
            enemy.append(enemy_3(enemy))
        elif menu == 'b' :
            print("\nPrepare Yourself !")


if __name__ == "__main__":
  main()

