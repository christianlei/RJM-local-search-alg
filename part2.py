import part1 as p1
import queue


class JumpFunction:
    def __init__(self):
        self.board_size = 5
        board = p1.Board()
        board.create_board(self.board_size)
        self.board = board
        self.rjm_board = board.board
        self.moves_board = []
        self.find_moves_to_start()
        self.calculate_moves_to_goal()
        self.objective_value = self.objective_function()

    def print_board_and_objective_function(self):
        self.board.print_board()
        self.print_moves_board()
        print(self.objective_value)

    def rerun_objective_function(self):
        self.moves_board = []
        self.find_moves_to_start()
        self.calculate_moves_to_goal()
        self.objective_value = self.objective_function()

    def calculate_moves_to_goal(self):
        moves_to_goal = float("inf")
        moves_required = 4
        for c in range(len(self.moves_board[4])):
            moves_to_start = self.moves_board[4][c]
            if self.rjm_board[4][c] == moves_required:
                if moves_to_start != '--' and moves_to_start + 1 < moves_to_goal:
                    moves_to_goal = moves_to_start + 1
            moves_required -= 1

        moves_required = 4
        for r in range(len(self.moves_board[0])):
            moves_to_start = self.moves_board[r][4]
            if self.rjm_board[r][4] == moves_required:
                if moves_to_start != '--' and moves_to_start + 1 < moves_to_goal:
                    moves_to_goal = moves_to_start + 1
            moves_required -= 1

        if moves_to_goal != float("inf"):
            self.moves_board[self.board_size - 1][self.board_size - 1] = moves_to_goal

    def find_moves_to_start(self):
        for r in range(self.board_size):
            self.moves_board.append([])
            for c in range(self.board_size):
                mz = MazeSquare(r, c, self.rjm_board[r][c])
                moves_to_start = self.bfs(mz)
                self.moves_board[r].append(moves_to_start)

    def bfs(self, maze_square):
        visited = [[False for col in range(len(self.rjm_board))] for row in range(len(self.rjm_board[0]))]
        depth = 0
        if maze_square.is_start():
            return depth
        q = queue.Queue()
        mz = MazeSquare(0, 0, self.rjm_board[0][0])
        q.put(mz)
        size_of_depth = q.qsize()
        while not q.empty():
            maze_square_from_queue = q.get()
            if maze_square_from_queue == maze_square:
                return depth
            children = maze_square_from_queue.next_move(self.rjm_board)
            for i in range(len(children)):
                if not visited[children[i].r][children[i].c]:
                    q.put(children[i])
                    visited[children[i].r][children[i].c] = True

            size_of_depth -= 1
            if size_of_depth == 0:
                size_of_depth = q.qsize()
                depth += 1
        return '--'

    def objective_function(self):
        goal_distance = self.moves_board[self.board_size - 1][self.board_size - 1]
        if goal_distance == '--':
            return 1000000
        return -goal_distance

    def print_moves_board(self):
        print("Moves from start: ")
        for r in range(self.board_size):
            print_string = ""
            for c in range(self.board_size):
                char = str(self.moves_board[r][c])
                if char == '--':
                    print_string += char + " "
                else:
                    print_string += str(self.moves_board[r][c]) + "  "
            print(print_string)


class MazeSquare:
    def __init__(self, r, c, j):
        self.r = r
        self.c = c
        self.jump = j
        self.board_size = 5

    def __eq__(self, other):
        return self.r == other.r and self.c == other.c

    def is_start(self):
        return self.r == 0 and self.c == 0

    def next_move(self, rjm_board):
        next_moves = []
        row_back = self.r - self.jump
        row_forward = self.r + self.jump
        col_up = self.c + self.jump
        col_down = self.c - self.jump
        if row_back >= 0:
            next_moves.append(MazeSquare(row_back, self.c, rjm_board[row_back][self.c]))
        if row_forward < self.board_size:
            next_moves.append(MazeSquare(row_forward, self.c, rjm_board[row_forward][self.c]))
        if col_up < self.board_size:
            next_moves.append(MazeSquare(self.r, col_up, rjm_board[self.r][col_up]))
        if col_down >= 0:
            next_moves.append(MazeSquare(self.r, col_down, rjm_board[self.r][col_down]))
        return next_moves
