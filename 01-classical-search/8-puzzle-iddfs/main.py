import sys
import time
import tracemalloc  # Built-in memory tracking library
from puzzle_env import PuzzleEnvironment
from iddfs_solver import iddfs

def print_board(board: list[list[int]]) -> None:
    """Utility to clearly print out your custom grid layout vertically."""
    for row in board:
        formatted_row = [str(tile) if tile != 0 else "_" for tile in row]
        print("  ".join(formatted_row))
    print("-" * (len(board[0]) * 4))

def main() -> None:
    # 4x4 Configuration Matrix (15-Puzzle)
    initial_board = [
        [1, 2, 3, 4],
        [5, 0, 7, 8],
        [9, 6, 10, 11],
        [13, 14, 15, 12]
    ]

    goal_board = [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]

    # Calculate grid size dynamically for clear presentation logging
    rows = len(initial_board)
    cols = len(initial_board[0]) if rows > 0 else 0
    puzzle_name = f"{(rows * cols) - 1}-Puzzle" if rows and cols else "N-Puzzle"
    
    print(f"[+] Initializing {puzzle_name} Solver Configuration ({rows}x{cols})...")
    env = PuzzleEnvironment(puzzle_board=initial_board, goal_board=goal_board)
    
    print("[+] Core Algorithm: Iterative Deepening DFS (Uninformed)\n")
    print("[~] Initiating search sequences...")
    
    # --- START RESOURCE TRACKING ---
    tracemalloc.start()  # Start tracking memory allocations
    start_time = time.perf_counter()
    
    success, solution_path = iddfs(env)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()   # Stop tracking memory
    # --- END RESOURCE TRACKING ---
    
    execution_time = end_time - start_time
    
    if success:
        print("\n==================================================")
        print("                 SEARCH RESULTS                   ")
        print("==================================================")
        print("Status:          SUCCESS")
        print(f"Optimal Depth:   {len(solution_path) - 1} moves")
        print(f"Execution Time:  {execution_time:.6f} seconds")
        print(f"Current Memory:  {current_mem / 1024:.2f} KB")
        print(f"Peak Memory:     {peak_mem / 1024:.2f} KB (Linear Stack Max)")
        print("==================================================\n")
        
        print("--- Chronological Move Execution Path ---")
        for step, state in enumerate(solution_path):
            board_matrix, empty_tile_idx = state
            print(f"Step {step} | Empty Tile Array Index: {empty_tile_idx}")
            print_board(board_matrix)
    else:
        print("\n❌ Status: FAILED (Exceeded maximum allowed search limits without matching goal configuration)")

if __name__ == "__main__":
    main()
