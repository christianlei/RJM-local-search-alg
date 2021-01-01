import random
import numpy as np


class Board:
    def __init__(self):
        self.board = []
        self.r_max = 0
        self.c_max = 0
        self.r_min = 0
        self.c_min = 0
        self.board_size = 0

    def get_board_size(self):
        board_size = input('Rook Jumping Maze size (5-10)? ')
        while (int(board_size) < 5) or (int(board_size) > 10):
            board_size = input('Rook Jumping Maze size (5-10)? ')
        self.create_board(int(board_size))
        self.print_board()

    def create_board(self, board_size):
        self.r_max = board_size - 1
        self.c_max = board_size - 1
        self.board_size = board_size
        for r in range(self.r_max + 1):
            self.board.append([])
            for c in range(self.c_max + 1):
                if r == self.r_max and c == self.c_max:
                    self.board[r].append(0)
                    break
                max_move = max(self.r_max - r, r - self.r_min, self.c_max - c, c - self.c_min)
                self.board[r].append(random.randint(1, max_move))
        self.board = np.array(self.board, dtype=np.int)

    def print_board(self):
        for r in range(self.r_max + 1):
            print_string = ""
            for c in range(self.c_max + 1):
                print_string += str(self.board[r][c]) + " "
            print(print_string)
