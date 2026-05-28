# This is the problem definition for the 8-puzzle problem. It defines the state space, the actions, and the goal test.
from typing import TypeAlias
from AbstractEnvironment import BaseEnvironment
# State structure: ( 2D Board Matrix, [Empty Row, Empty Col] )
PuzzleStateType: TypeAlias = tuple[list[list[int]], list[int]]

class PuzzleEnvironment(BaseEnvironment[list[list[int]], list[int]]):

    def __init__(self, puzzle_board: list[list[int]], goal_board: list[list[int]]):
        self.R = len(puzzle_board)
        self.C = len(puzzle_board[0]) if self.R > 0 else 0
        start_empty_tile = self.find_empty_tile(puzzle_board)
        end_empty_tile = self.find_empty_tile(goal_board)
        self.initial_puzzle_state: PuzzleStateType = (puzzle_board, start_empty_tile)
        self.final_puzzle_state: PuzzleStateType = (goal_board, end_empty_tile)

    def find_empty_tile(self, board: list[list[int]]) -> list[int]:
        for r in range(0,self.R):
            for c in range(0,self.C):
                if board[r][c] == 0:
                    return [r,c]
        return [-1, -1]
    
    def get_initial_puzzle_state(self) -> PuzzleStateType:
        return self.initial_puzzle_state
    
    def valid_action(self,current_tile_index, r, c) -> bool:
        cr , cc = current_tile_index
        if cr + r < self.R and cc + c < self.C and cr + r >= 0 and cc + c >= 0:
            return True
        return False

    def swap_tile(self, puzzle_board_state, ind_i, ind_j) -> list[list[int]]:
        next_board_state: list[list[int]] = [row.copy() for row in puzzle_board_state]
        ir, ic = ind_i
        jr, jc = ind_j
        next_board_state[ir][ic], next_board_state[jr][jc] = next_board_state[jr][jc], next_board_state[ir][ic]
        return next_board_state

    def get_next_states(self, current_puzzle_state: PuzzleStateType) -> list[PuzzleStateType]:
        [r,c] = current_puzzle_state[1]
        next_puzzle_states = []
        actions = [[0,1],[0,-1],[1,0],[-1,0]]
        for action in actions:
            if not self.valid_action([r,c],action[0],action[1]):
                continue
            next_board_state: list[list[int]] = self.swap_tile(current_puzzle_state[0],[r,c],[r+action[0],c+action[1]])
            next_puzzle_states.append((next_board_state,[r+action[0],c+action[1]]))
        return next_puzzle_states
    
    def check_goal(self, current_puzzle_state: PuzzleStateType) -> bool:
        return current_puzzle_state == self.final_puzzle_state