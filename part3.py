import part2 as p2
import random
import copy


class HillDescent:
    def __init__(self):
        self.iteration_count = 0
        self.jump_function = p2.JumpFunction()
        self.best_jump_function = copy.deepcopy(self.jump_function)
        # self.jump_function.print_board_and_objective_function()
        self.get_interation_count()
        self.perform_stochastic_local_search()
        self.print_best_objective_value()

    def print_best_objective_value(self):
        self.best_jump_function.print_board_and_objective_function()

    def perform_stochastic_local_search(self):
        for i in range(self.iteration_count):
            jump_function_prime = copy.deepcopy(self.jump_function)
            self.change_random_jump_number(jump_function_prime.rjm_board, jump_function_prime.board_size)
            jump_function_prime.rerun_objective_function()
            # jump_function_prime.print_board_and_objective_function()
            if jump_function_prime.objective_value <= self.jump_function.objective_value:
                self.jump_function = copy.deepcopy(jump_function_prime)
                if jump_function_prime.objective_value <= self.best_jump_function.objective_value:
                    self.best_jump_function = copy.deepcopy(self.jump_function)

    def get_interation_count(self):
        iteration_count = input('Iterations? ')
        self.iteration_count = int(iteration_count)

    def change_random_jump_number(self, rjm_board, board_size):
        r_max = board_size - 1
        r_min = 0
        c_max = board_size - 1
        c_min = 0
        random_row = random_column = 0
        while random_column != 4 and random_row != 4:
            random_row = random.randrange(board_size)
            random_column = random.randrange(board_size)
        max_move = max(r_max - random_row, random_row - r_min, c_max - random_column, random_column - c_min)
        jump = random.randint(1, max_move)
        while rjm_board[random_row][random_column] == jump:
            jump = random.randint(1, max_move)
        rjm_board[random_row][random_column] = jump
