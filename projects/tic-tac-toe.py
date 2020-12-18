#!/usr/bin/python3
#tictactoe game
import time
import os
a = ["_"," "," "," "," "," "," "," "," "," "]
player = 'player1'

def clear():
    os.system('clear')

def board(a):
    print(f"\n{player}'s move...\n")
    print(a[7] + ' | ' + a[8] + ' | ' + a[9])
    print('---------')
    print(a[4] + ' | ' + a[5] + ' | ' + a[6])
    print('---------')
    print(a[1] + ' | ' + a[2] + ' | ' + a[3])

def user_input():
    #to get a position number from the user
    position = 0
    while True:
        try:
            position = int(input("\nEnter your position..."))
            break
        except:
            print("\ncheck your input")
    return position 

def check_input(position):
    #checking the input if it is valid or not
    if position in range(1, 10) and a[position] == ' ':
        return True
    else:
        print("\nCheck your input") 
        return False

def check_result(a):
    #checking rows and diagonals for x
    if a[7] == a[8] == a[9] == "X" or a[4] == a[5] == a[6] == "X" or a[1] == a[2] == a[3] == "X" or a[1] == a[5] == a[9] == "X" or a[3] == a[5] == a[7] == "X":
        return True
    #checking coloumns for x
    elif a[1] == a[4] == a[7] == "X" or a[2] == a[5] == a[8] == "X" or a[3] == a[6] == a[9] == "X":
        return True
    #checking rows and diagonals for O
    elif a[7] == a[8] == a[9] == "O" or a[4] == a[5] == a[6] == "O" or a[1] == a[2] == a[3] == "O" or a[1] == a[5] == a[9] == "O" or a[3] == a[5] == a[7] == "O":
        return True
    #checking coloumns for O 
    elif a[1] == a[4] == a[7] == "O" or a[2] == a[5] == a[8] == "O" or a[3] == a[6] == a[9] == "O":
        return True
    else:
        return False

def draw_check(a):
    #checking for draw
    if " " not in a:
        return True
    else:
        return False

#game starts
print("Welcome to tic-tac-toe\n\nPlayer1 is X and Player2 is O\n\nLoading...")
time.sleep(3)
while True:
    #player1's
    if player == "player1":
        clear()
        board(a)
        position = user_input()
        if check_input(position):
            a[position] = "X"
            if check_result(a):
                board(a)
                print("Player1 wins the game!!!")
                break
            elif draw_check(a):
                print("It's a stalemate!")
                break
            player = "player2"
        else:
            continue
    else:
        #player2's
        clear()
        board(a)
        position = user_input()
        if check_input(position):
            a[position] = "O"
            if check_result(a):
                board(a)
                print("Player1 wins the game!!!")
                break
            elif draw_check(a):
                print("It's a stalemate!")
                break
            player = "player1"
        else:
            continue
