#!/usr/bin/env python
# coding: utf-8
# Author : Adithya Gowtham R


import os

def clear_output():
    # For Linux and MACOS use:
    os.system('clear')
    # For Windows use:
    # os.system('cls')

def display_board(board):
    """
        Function to display the tic-tac-toe board. 
        
        INPUT : Takes in an input board, a list of size 9.
        
        OUTPUT : Prints the board in the required conformation
        
    """
    b = board.copy()
    print(f"\n {b[0]}|{b[1]}|{b[2]}\n-------\n {b[3]}|{b[4]}|{b[5]}\n-------\n {b[6]}|{b[7]}|{b[8]} ")



def player_input():
    
    """
        Function to assign a marker ("x" or "o") to the player.
        
        INPUT : Takes in input from the end-user.
        
        RETURN VALUE : Returns the markers for both the players.
        
    """
    
    marker_1 = 0; marker_2 = 0
    state = 0
    
    while True:
        if state >=2 :
            clear_output()
            print("Invalid Marker, please choose a valid marker")
            
        avl_markers = ["x","o"]
        marker_1 = input("Player 1 : Please choose a marker (x or o)")
        
        if marker_1 not in avl_markers:
            state += 1
            print("Invalid Marker, please choose a valid marker")
            continue
        
        avl_markers.remove(marker_1)
        marker_2 = avl_markers[0]
        clear_output()
        print(f"Player1 has been assigned \"{marker_1}\" and Player2 has been assigned \"{marker_2}\"\n")
        
        return marker_1,marker_2


def place_marker(board, marker, position):
     
    """
        Function to place a marker ("x" or "o") on the board.
        
        INPUT : Takes in a board (a list of size 9), a marker ("x" or "o") and a position (in range(1,10)).
        
        RETURN VALUE : Returns the board after the position update.
        
    """
    
    if marker not in ['x','o']:
        print("Please check marker!")
    elif board[position-1] == " ":
        board[position-1] = marker
    else:
        print("Position is not empty! Please check position")
        
    return board    



def win_check(board, mark):
    
    """
        Function to check whether a player('s mark) has won the game.
        
        INPUT : Takes in a board (a list of size 9) and a marker ("x" or "o").
        
        RETURN VALUE : Returns the win_state (True if the marker wins or False if not).
        
    """
    
    if mark not in ["x","o"]:
        print("Please recheck mark!")
        return False
    
    win_state = False
    
    for i,ele in enumerate(board):
        if i in [0,3,6]:
            if ele == mark :
                if board[i+1] == mark:
                    if board[i+2] == mark:
                        win_state = True
                
        if i in [0,1,2]:
            if ele == mark:
                if board[i+3] == mark:
                    if board[i+6] == mark:
                        win_state = True
        
        if i == 0:
            if ele == mark:
                if board[i+4] == mark:
                    if board[i+8] == mark:
                        win_state = True
                        
        if i == 2:
            if ele == mark:
                if board[i+2] == mark:
                    if board[i+4] == mark:
                        win_state = True
    
    return win_state

import random

def choose_first():
    """
        Function to choose which players goes first.
        
        RETURN VALUE : Returns a random integer in range(1,3)
            
    """
    return random.randint(1,2)



def space_check(board, position):
    
    """
        Function to check whether a board position is empty or not.
        
        INPUT : Takes in a board (a list of size 9) and a position (in range(1,10)).
        
        RETURN VALUE : Returns "True" is position is empty and "False" if its not.
            
    """
    
    if board[position-1] == ' ':
        return True 
    return False



def full_board_check(board):
    
    """
        Function to check whether the board is full or not.
        
        INPUT : Takes in a board (a list of size 9).
        
        RETURN VALUE : Returns "True" is board is full and "False" if its not.
            
    """
    
    free_spaces = len([ele for ele in board if ele==' '])
    if free_spaces == 0:
        return True
    return False


def player_choice(board):
    
    """
        Function to accept a position choice from the user and check if it's a free position.
        
        INPUT : Takes in a board (a list of size 9) and position(range(1,10)) from the user.
        
        RETURN VALUE : Returns the accepted position if its valid.
            
    """
    
    ch = True
    
    while ch:
        pos = input("Please enter a board position to place the marker (in 1-9): ")
        
        if pos == '' or not pos.isdigit():
            print("\nPlease enter a number! ")
            continue
            
        pos = int(pos)
        
        if pos not in list(range(1,10)):
            print("\nPlease enter a number in the range 1 to 9 only!")
            continue
        
        if not space_check(board,pos):
            print("\nPosition occuied! Please select an unoccupied position")
            continue
            
        ch = False

    return pos


def replay():
    
    """
        Function to check whether the user wants to play the game again.
        
        INPUT : Takes in a user choice in ["Y",'y',"N",'n'].
        
        RETURN VALUE : Returns "True" if the user wants to play again and "False" if not.
            
    """
    
    while True:
        
        ch = input("\nDo you want to continue playing? (Y or N) : ")
        
        if ch == 'y' or ch == 'Y':
            return True
        
        elif ch == 'n' or ch == 'N':
                return False
        else:
            print("\nPlease enter Y to continue and N to quit!")


def tic_tac_toe():
    
    """
        Function to play the tic-tac-toe game.
        
        INPUT : Takes in user input for marker choice, positions and replay.
            
    """
    
    print('Welcome to Tic Tac Toe!')

    try :

        while True:

            board = [' ']*9

            t1, t2 = player_input()
            p1_p2 = choose_first()

            if p1_p2 == 1 :
                print("Player 1 moves first!")
                m1 = t1; m2 = t2
            else :
                print("Player 2 moves first!")
                m1 = t2; m2 = t1

            flag = True

            while True:

                display_board(board)

                if p1_p2 == 1:
                    if not flag:
                        clear_output()
                        flag = False
                    pos_1 = player_choice(board)
                    while True:
                        if space_check(board,pos_1):
                            place_marker(board,m1,pos_1)
                            break
                        else:
                            board = place_marker(board,m1,pos_1)

                    if full_board_check(board) : 
                        clear_output()
                        print("Draw!")
                        break 

                    if win_check(board,m1): print("\nCongratulations! Player 1 wins!"); break

                    clear_output()
                    display_board(board)

                    pos_2 =  player_choice(board)
                    while True:
                        if space_check(board,pos_2):
                            place_marker(board,m2,pos_2)
                            break
                        else:
                            board = place_marker(board,m2,pos_2)

                    if full_board_check(board) : 
                        clear_output()
                        print("Draw!")
                        break 

                    if win_check(board,m2): print("\nCongratulations! Player 2 wins!"); break

                if p1_p2 == 2:
                    if not flag:
                        clear_output()
                        flag = False

                    pos_1 =  player_choice(board)
                    while True:
                        if space_check(board,pos_1):
                            place_marker(board,m1,pos_1)
                            break
                        else:
                            board = place_marker(board,m1,pos_1)

                    clear_output()
                    display_board(board)
                    if full_board_check(board) : 
                        clear_output()
                        print("Draw!")
                        break 

                    if win_check(board,m1): print("\nCongratulations! Player 2 wins!"); break

                    pos_2 = player_choice(board)
                    while True:
                        if space_check(board,pos_2):
                            place_marker(board,m2,pos_2)
                            break
                        else:
                            board = place_marker(board,m2,pos_2)

                    if win_check(board,m2): print("\nCongratulations! Player 1 wins!"); break

                    clear_output()
                    if full_board_check(board) : 
                        print("Draw!")
                        break 

            if not replay():
                break

            clear_output()

    except Exception:
        print("Game crashed! Please reset and try again...\n")


if __name__ == "__main__":
    # Calling the tic-tac-toe function
    tic_tac_toe()

# EOC
