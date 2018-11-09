from functools import reduce
from random import randint
from copy import deepcopy
from util import NumberGenerator


class Board:
    def __init__(self, dimension, win_lose_condition):
        self.score = 0
        self.win_lose_condition = win_lose_condition
        self.number_generator = NumberGenerator()
        self.__init_board(dimension)
        self.__compute_next_board()

    def show(self):
        for row in self.board:
            for data in row:
                print(data, end=" ")
            print()

    def move(self, direction):
        self.board = deepcopy(self.next_board[direction])

        self.__put_number()
        self.__compute_next_board()
        self.__check_status()

    def get_score(self):
        return self.score

    def __init_board(self, dimension):
        self.board = [
            [0 for _ in range(dimension)] for _ in range(dimension)
        ]
        self.__put_number()

    def __put_number(self):
        empty_col_loc = []
        row_idx = 0
        for row in self.board:
            col_idx = 0
            for col in row:
                if col == 0:
                    empty_col_loc.append((row_idx, col_idx))
                col_idx += 1
            row_idx += 1

        filled_empty_index = randint(0, len(empty_col_loc) - 1)
        number_to_fill = self.number_generator.generate()

        selected_empty_col = empty_col_loc[filled_empty_index]
        self.board[selected_empty_col[0]][selected_empty_col[1]] = number_to_fill


    def __compute_next_board(self):
        matrix = deepcopy(self.board)

        a = [self.__shift(row) for row in matrix]
        s = map(list, zip(*[self.__shift(row[::-1])[::-1] for row in map(list, zip(*matrix))]))
        d = [self.__shift(row[::-1])[::-1] for row in matrix]
        # bug
        w = map(list, zip(*[self.__shift(row) for row in map(list, zip(*matrix))]))

        self.next_board = {
            "a": a,
            "s": [x for x in s],
            "d": d,
            "w": [x for x in w]
        }

    def __check_status(self):
        if reduce(
            lambda status_accum, current_board: status_accum and (current_board == self.board),
            self.next_board,
            True
        ):
            self.win_lose_condition.status = "lose"
        else:
            self.win_lose_condition.track_biggest(self.__get_biggest_num())

    def __get_biggest_num(self):
        return reduce(
            lambda row_accum, row: max(row_accum, reduce(
                lambda data_accum, data: max(data_accum, data),
                row,
                -1
            )),
            self.board,
            -1
        )

    def __shift(self, array_list):
      array_list = self.__remove_zero(array_list)
      for i in range(len(array_list) - 1):
        current = array_list[i]
        shifted = self.__remove_zero(array_list[(i+1):])

        if len(shifted) != 0 and current == shifted[0]:
          current += shifted[0]
          self.score += current
          shifted.reverse()
          shifted.pop()
          shifted.reverse()
          shifted += [0]

        array_list = array_list[0:i] + [current] + shifted

      return array_list

    def __remove_zero(self, array_list):
      length = len(array_list)
      cloned_list = deepcopy(array_list)
      cloned_list.reverse()
      while(len(cloned_list) != 0 and cloned_list[len(cloned_list) - 1] == 0):
        cloned_list.pop()
      cloned_list.reverse()
      return cloned_list + [0] * (length - len(cloned_list))
