import random

class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:

            print(f"Player {player} turn")
            print()
            self.show_board()

            # taking user input
            print()
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()



















# # pip install pygame
# # ⭕Tic Tac Toe❌

# import pygame as pg,sys
# from pygame.locals import *
# import time


# #initialize global variables
# XO = 'x'
# winner = None
# draw = False
# width = 400
# height = 400
# white = (255, 255, 255)
# line_color = (10,10,10)

# #TicTacToe 3x3 board
# TTT = [[None]*3,[None]*3,[None]*3]

# #initializing pygame window
# pg.init()
# fps = 30
# CLOCK = pg.time.Clock()
# screen = pg.display.set_mode((width, height+100),0,32)
# pg.display.set_caption("Tic Tac Toe")



# # #loading the images
# # opening = pg.image.load('tic tac opening.png')
# # x_img = pg.image.load('x.png')
# # o_img = pg.image.load('o.png')

# #resizing images
# # x_img = pg.transform.scale(x_img, (80,80))
# # o_img = pg.transform.scale(o_img, (80,80))
# # opening = pg.transform.scale(opening, (width, height+100))

# def game_opening():
#     screen.blit(opening,(0,0))
#     pg.display.update()
#     time.sleep(1)
#     screen.fill(white)

#     # Drawing vertical lines
#     pg.draw.line(screen,line_color,(width/3,0),(width/3, height),7)
#     pg.draw.line(screen,line_color,(width/3*2,0),(width/3*2, height),7)
#     # Drawing horizontal lines
#     pg.draw.line(screen,line_color,(0,height/3),(width, height/3),7)
#     pg.draw.line(screen,line_color,(0,height/3*2),(width, height/3*2),7)
#     draw_status()