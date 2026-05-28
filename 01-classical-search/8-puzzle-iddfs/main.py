import sys
import time
import tracemalloc  # Built-in memory tracking library
from puzzle_env import PuzzleEnvironment
from iddfs_solver import iddfs

def print_board(board: list[list[int]]) -> None:
    """Utility to clearly print out your 3x3 layout vertically."""
    for row in board:
        formatted_row = [str(tile) if tile != 0 else "_" for tile in row]
        print("  ".join(formatted_row))
    print("-" * 12)

def main() -> None:
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

    
    print("Initializing 8-Puzzle Environment...")
    env = PuzzleEnvironment(puzzle_board=initial_board, goal_board=goal_board)
    
    print("Starting Iterative Deepening Depth-First Search (IDDFS)...")
    
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
        print(f"\n🎉 Goal Reached Successfully!")
        print(f"⏱️  Execution Time : {execution_time:.6f} seconds")
        
        # Convert bytes to Kilobytes for scannable metrics
        print(f"💾 Current Memory  : {current_mem / 1024:.2f} KB")
        print(f"📈 Peak Memory     : {peak_mem / 1024:.2f} KB")
        print(f"🧩 Total Steps     : {len(solution_path) - 1}\n")
        
        print("--- Execution Path ---")
        for step, state in enumerate(solution_path):
            board_matrix, empty_tile_idx = state
            print(f"Step {step} | Empty Tile Position: {empty_tile_idx}")
            print_board(board_matrix)
    else:
        print("\n❌ Failed to find a valid solution branch.")

if __name__ == "__main__":
    main()
