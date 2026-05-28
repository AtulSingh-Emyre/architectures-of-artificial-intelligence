# N-Puzzle Solver: Memory-Efficient State Space Search via IDDFS

A modular, portfolio-grade implementation of the **Iterative Deepening Depth-First Search (IDDFS)** algorithm designed to solve generalized \(R \times C\) N-Puzzle configurations (such as the classic 8-puzzle).

## 📌 Problem Statement

The N-Puzzle is a classic combinatorial optimization problem consisting of a grid of numbered square tiles in a random order, with one tile missing. The goal is to transition the board from a chaotic **Initial State** to a structured **Goal State** by sliding adjacent tiles into the empty space.

While algorithms like Breadth-First Search (BFS) guarantee finding the shortest path to a solution, their memory consumption grows exponentially (\(O(b^d)\)) because they cache every generated layer of the search tree. For deep state-spaces, standard BFS quickly exhausts available system RAM.

### The Solution: IDDFS
This project leverages **Iterative Deepening DFS (IDDFS)** to achieve optimal performance:
1. **Optimality of BFS:** It guarantees finding the absolute shortest sequence of moves to solve the puzzle.
2. **Memory Efficiency of DFS:** It limits space complexity to a linear boundary (\(O(d)\)) by exploring paths depth-first up to a progressively increasing depth threshold, completely avoiding RAM bloat.

---

## 🏗️ Architecture & Project Structure

The codebase strictly follows modern software engineering principles, decoupling game mechanics and environment abstractions from the core AI search logic:

```text
├── AbstractEnvironment.py  # Generic interfaces and types (BaseEnvironment, I, S)
├── puzzle_env.py           # N-Puzzle mechanics, grid validation, and move generators
├── iddfs_solver.py         # The Iterative Deepening Depth-First Search engine
├── main.py                 # Application entry point and configuration pipeline
└── README.md               # Project documentation
```

### Module Breakdown:
* **`AbstractEnvironment.py`**: Defines generic abstract base classes (`BaseEnvironment`) ensuring that the search engine (`iddfs_solver.py`) is decoupled and capable of solving *any* discrete state-space problem, not just the N-Puzzle.
* **`puzzle_env.py`**: Encapsulates the tile positions, grid dimensions, valid slide-move generation (`Up`, `Down`, `Left`, `Right`), and state comparison logic.
* **`iddfs_solver.py`**: Houses the recursive Depth-Limited Search (DLS) algorithm alongside the iterative loop that deepens the search window incrementally.
* **`main.py`**: Coordinates the runtime lifecycle—bootstrapping the environment, running the solver, and reporting evaluation diagnostics.

---

## 💡 Key Optimization: Branch-Cycle Prevention

Because N-Puzzle moves are fully reversible (e.g., sliding a tile `Left` and immediately back `Right`), a naive recursive DFS will quickly become trapped oscillating back and forth between identical states, wasting depth limits and failing on complex boards.

To prevent this without breaking the linear \(O(d)\) space complexity guarantee of IDDFS, this implementation utilizes an optimized **Active Branch Path Tracking** strategy:

```python
# A look inside iddfs_solver.py
path_set.add(current_puzzle_state)

for next_puzzle_state in next_puzzle_states:
    if next_puzzle_state in path_set:
        continue # Instantly prune backward cycles in O(1) time
        
    curr_branch = depth_limited_search(game_env, next_puzzle_state, depth - 1, path_set)
    ...

path_set.remove(current_puzzle_state) # Clean up during backtracking
```

* **Linear Overhead**: Rather than maintaining a massive global visited cache that grows exponentially, a temporary `set` maps only the current active ancestry branch.
* **Instant Pruning**: Cyclical moves are filtered out in **\(O(1)\)** time, allowing the engine to successfully solve deeper puzzle permutations without system crashes.

---

## 🚀 Execution & Sample Output

To run the application, execute the entry script from your terminal:

```bash
python main.py
```

### Sample Performance Analytics:
```text
[+] Initializing 8-Puzzle Solver Configuration...
[+] Core Algorithm: Iterative Deepening DFS (Uninformed)

[~] Searching at Depth Limit: 0...
[~] Searching at Depth Limit: 1...
[~] Searching at Depth Limit: 2...
[~] Searching at Depth Limit: 3...
[~] Searching at Depth Limit: 4... Success!

==================================================
                 SEARCH RESULTS                   
==================================================
Status:          SUCCESS
Optimal Depth:   4 moves
Memory Profile:  O(d) ~ Linear Call Stack Max
Path Sequence:   [Initial State] -> State 1 -> State 2 -> State 3 -> [Goal State]
==================================================
```

---

## 💎 Portfolio Highlights

This project serves as an excellent demonstration of clean AI engineering because it showcases:
* **Interface-Driven Design**: The separation of `puzzle_env` and `iddfs_solver` via `AbstractEnvironment` demonstrates an ability to write reusable, loosely-coupled code.
* **Algorithmic Complexity Awareness**: Solves a complex combinatorial puzzle while balancing the fundamental time-vs-memory trade-offs of graph traversals.
