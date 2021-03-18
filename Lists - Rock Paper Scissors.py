#import random for cpu move and sleep for structure
import random
from time import sleep
#dictionary for each object to show what it beats cause who uses that many if statements
objectBeats = {
    'ROCK': "SCISSORS", 
    'PAPER': "ROCK", 
    'SCISSORS': "PAPER",
    'PC': ["CONSOLE", "SCISSORS", "ROCK", "PAPER"],
    'CONSOLE': "ROCK"
    }
#list of moves for cpu move selection
objects = ['ROCK', 'PAPER', 'SCISSORS', 'PC', 'CONSOLE']
#defines the header duh..
def header():
    print("COMPUTER: Hey...")
    sleep(1)
    print("COMPUTER: I don't supppose you'd play rock paper scissors with me?")
    sleep(2)
    print("COMPUTER: YES? ALRIGHT! I'LL SMASH YOUR FACE IN!")
    sleep(3)
#define the game algorithm and takes player input
def game():
    global playerscore, cpuscore, rounds

    rounds = int(input("COMPUTER: HOW MANY ROUNDS YOU WANT TO GET BEATEN? "))
    for i in range(1,rounds+1,1):
        sleep(1)
        print("COMPUTER: ROUUNNDDD {}!!".format(i))
        sleep(0.5)
        print("BEGINNNN!")
        print("YOU HAVE THE OPTION OF:", *objects, sep="\n")
        move = str(input("ENTER YOUR CHOICE AS SHOWN E.G. 'ROCK': ")).upper()
        #randomly selects move for cpu
        cpumove = objects[random.randint(0,2)]
        #determines if player's move beats cpu's move
        #conditions to display whether the player won, drew or lost
        if cpumove in objectBeats.get(move):
            print("COMPUTER: AW DARN, IT. I HAD {}. \n +10 POINTS FOR YOU!".format(cpumove))
            playerscore += 10
            print("CPU SCORE: {} \n YOUR SCORE: {}".format(cpuscore, playerscore))
        elif cpumove in move:
            print("COMPUTER: AHHH, WE HAD THE SAME! CALL IT A DRAW +0 POINTS.")
            print("CPU SCORE: {} \n YOUR SCORE: {}".format(cpuscore, playerscore))
        else:
            print("COMPUTER: AHA! I WIN, I HAD {}. \n +10 POINTS FOR ME!".format(cpumove))
            cpuscore += 10
            print("CPU SCORE: {} \n YOUR SCORE: {}".format(cpuscore, playerscore))
        
        
#while loop for repeating the game
again = "y"
header()
rounds = 1
while rounds > 0 and again !="n":
    playerscore = 0
    cpuscore = 0
    game()
    print("COMPUTER: GAME END!!")
    #conditions for player win, lose or draw   
    if playerscore > cpuscore:
        sleep(1)
        print("COMPUTER: DAMN IT, I GUESS YOU WIN. \n YOU HAD {} POINTS \n I HAD {} POINTS. SEE YA!".format(playerscore, cpuscore))
    elif cpuscore > playerscore:
        sleep(1)
        print("COMPUTER: HAHA! VICTORY IS MINE! \n I HAD {} POINTS \n YOU HAD A MEASLY {}. GOODBYE!".format(cpuscore, playerscore))
    elif cpuscore == playerscore:
        sleep(1)
        print("COMPUTER: AHH, LOOKS LIKE WE HAD THE SAME SCORE - TRULY YOU WERE A GREAT COMPETITOR WITH {} POINTS.".format(playerscore))
    again = input("COMPUTER: WANT ANOTHER GAME?(y/n) ").lower()
