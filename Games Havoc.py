def ttt():
 #Implementation of Two Player Tic-Tac-Toe game in Python.

 ''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''

 theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

 board_keys = []

 for key in theBoard:
    board_keys.append(key)

 ''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

 def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Now we'll write the main function which has all the gameplay functionality.
 def game():

     turn = 'X'
     count = 0


     for i in range(10):
         printBoard(theBoard)
         print("It's your turn," + turn + ".Move to which place?")

         move = input()        

         if theBoard[move] == ' ':
             theBoard[move] = turn
             count += 1
         else:
             print("That place is already filled.\nMove to which place?")
             continue

         # Now we will check if player X or O has won,for every move after 5 moves. 
         if count >= 5:
             if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                 printBoard(theBoard)
                 print("\nGame Over.\n")                
                 print(" **** " +turn + " won. ****")                
                 break
             elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                 printBoard(theBoard)
                 print("\nGame Over.\n")                
                 print(" **** " +turn + " won. ****")
                 break
             elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                 printBoard(theBoard)
                 print("\nGame Over.\n")                
                 print(" **** " +turn + " won. ****")
                 break
             elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                 printBoard(theBoard)
                 print("\nGame Over.\n")                
                 print(" **** " +turn + " won. ****")
                 break
             elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                 printBoard(theBoard)
                 print("\nGame Over.\n")                
                 print(" **** " +turn + " won. ****")
                 break
             elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                 printBoard(theBoard)
                 print("\nGame Over.\n")                
                 print(" **** " +turn + " won. ****")
                 break 
             elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                 printBoard(theBoard)
                 print("\nGame Over.\n")                
                 print(" **** " +turn + " won. ****")
                 break
             elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                 printBoard(theBoard)
                 print("\nGame Over.\n")                
                 print(" **** " +turn + " won. ****")
                 break 

         # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
         if count == 9:
          print("\nGame Over.\n")                
          print("It's a Tie!!")

         # Now we have to change the player after every move.
         if turn =='X':
          turn = 'O'
         else:
          turn = 'X'        
    
     # Now we will ask if player wants to restart the game or not.
     restart = input("Do want to play Again?(y/n)")
     if restart == "y" or restart == "Y":  
         for key in board_keys:
             theBoard[key] = " "

         game()

 if __name__ == "__main__":
    game()


def guessnum():
 import random
 print("enter to quit")
 count=0
 while True:
    r=input('enter range')
    if r!='':
         n=random.randint(0,int(r))
         if n%2==0:
           print('no. is even')
         else:
           print('no. is odd')
         while True:
           guess =int(input('guess;'))
           if n==guess:
               print('correct')
               print("took",count,"tries")
               break
           elif n>guess:
              print('you guessed too low')
              count+=1
           elif n<guess:
              print ('you guessed too high')
              count+=1
    elif r=='':
            break
    else:
            print('invalid output')

def madlib():
 print("Madlibs game")
 while True:
     print("choices\n1.FESTIVAL JOYS!!  2. QUIT")
     n=int(input("enter choice"))
     if n==1:
         holi=input("enter holiday")
         cloth=input("enter cloth")
         place=input("enter place")
         celeb=input("enter celeb")
         bf=input("enter name of best friend")
         verb=input("enter activity")
         adj=input("enter adj")
         verb2=input("enter activity 2")
         ani=input("enter animal in plural") 
         print("I cant believe its already %s ! i cant wait to \n put on my %s and visit %s as it has \n always been my dream . This year , im going to dress up as \n %s with %s before i %s . \n the evening was %s and i planned to %s as much as i could with  \n my %s . Finally, all of my %s are ready to go!" %(holi,cloth,place,celeb,bf,verb,adj,verb2,bf,ani))
   
     elif n==2:
         break
        
def rps():
    
 from random import randint

 #create a list of play options
 t = ["Rock", "Paper", "Scissors"]

 #assign a random play to the computer
 computer = t[randint(0,2)]

 #set player to False
 player = False

 while player == False:
 #set player to True
     player = input("0 to quit. Rock, Paper, Scissors?")
     if player!="0":
      if player == computer:
          print("Tie!")
      elif player == "Rock" or "rock" or "ROCK":
          if computer == "Paper":
             print("You lose!", computer, "covers", player)
          else:
             print("You win!", player, "smashes", computer)
      elif player == "Paper" or "paper" or "PAPER":
         if computer == "Scissors":
             print("You lose!", computer, "cut", player)
         else:
             print("You win!", player, "covers", computer)
      elif player == "Scissors" or "scissors" or " SCISSORS":
         if computer == "Rock":
             print("You lose...", computer, "smashes", player)
         else:
             print("You win!", player, "cut", computer)
      else:
         print("That's not a valid play. Check your spelling!")
      #player was set to True, but we want it to be False so the loop continues
      player = False
      computer = t[randint(0,2)]
     elif player=="0":
         player= True

#main program
print("1. Tic Tac Toe 2. Guess Number 3.Madlibs 4.Rock Paper and Scissors 5.Quit")
while True:
 user=int(input("Enter your Choices"))
 if user==1:
    ttt()
 elif user==2:
    guessnum()
 elif user==3:
    madlib()
 elif user==4:
    rps()
 elif user==5:
     break
 else:
    print("Invalid Input")            
