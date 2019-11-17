#Rock paper scissor game created and programmed by Rudra Shah

import random as rand
import time
import sys

def update_progress(job_title, progress):
    length = 20
    block = int(round(length*progress))
    msg = "\r{0}: [{1}] {2}%".format(job_title, "#"*block + "-"*(length-block), round(progress*100, 2))
    if progress >= 1: msg += " Let\'s start the Game\r\n"
    sys.stdout.write(msg)
    sys.stdout.flush()

for i in range(100):
    time.sleep(0.1)
    update_progress("Loading game resource", i/100.0)
update_progress("Loading game resource", 1)
userResponseL = input('\n  WELCOME TO ROCK PAPER GAME, \n Press ENTER to start the game ')
userResponse = userResponseL.lower()
point = 0
Tround = 0
ComputerPoint = 0

while userResponse:
    randInt = rand.randint(0,2)
    computerResponse = ['rock','paper','scissor']
    CompResponse = computerResponse[randInt]
    userResponse = input('\nRock, paper, scissor!! Choose it ~~~: ')
    if CompResponse=='rock' and userResponse=='paper':
        print('\nHurray!! Point on your way!! \n you got \'1\' point')
        print(userResponse,'covered',CompResponse)
        point+=1
        Tround+=1
    elif CompResponse=='paper' and userResponse=='scissor':
        print('\nHurray!! Point on your way!! \n you got \'1\' point')
        print(userResponse,'cut\'s the ',CompResponse)
        point+=1
        Tround+=1
    elif CompResponse=='scissor' and userResponse=='rock':
        print('\nHurray!! Point on your way!! \n you got \'1\' point')
        print(userResponse,'rock broke',CompResponse)
        point+=1
        Tround+=1
    elif CompResponse==userResponse:
        print('\nThat\'s tie point goes to computer as well as user!! \n both got \'1\' point' )
        print(CompResponse,'and',userResponse)
        ComputerPoint+=1
        point+=1
        Tround+=1
    else:
        print('\noh!No! point goes to computer!! \n computer got \'1\' point' )
        print(CompResponse,'was over taken by',userResponse)
        ComputerPoint+=1
        Tround+=1
    if(Tround==5):
        print('\nFinal score!! After',Tround,'round','User Score-:',point,'and','computer score-:',ComputerPoint)
        break


print('\n\nThanks for playing Rock, Paper, Scissor Game \n Created and programmed by Rudra Shah.')

