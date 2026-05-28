# SmartEV-Route: Optimal Electric Vehicle Routing using Uniform Cost Search

An implementation of the **Uniform Cost Search (UCS)** algorithm applied to a real-world logistics and sustainability challenge: optimizing the navigation path for Electric Vehicles (EVs) across a weighted directed graph.

## 📌 Problem Statement

Standard navigation systems optimize purely for distance or time. However, Electric Vehicles (EVs) must optimize for **cumulative energy consumption and monetary cost**, where roads have varying elevation, traffic conditions, and infrastructure fees.

In this project, you are tasked with building an AI routing engine for a commercial EV fleet. The vehicle needs to travel from a designated **Origin Hub** to a **Destination Depot** across a complex mixed-terrain urban network. The cost of traversing any road segment is determined by multiple factors:

1. **Incline & Decline**: Uphill roads draw more battery power; downhill roads trigger regenerative braking (reducing cumulative cost).
2. **Traffic Density**: Heavy traffic causes idling, which drains auxiliary battery systems.
3. **Infrastructure Fees**: Certain segments include congestion pricing or tolls.

### Objective

Given a directed, weighted graph representing the city's road grid, implement the **Uniform Cost Search** algorithm to find the absolute **lowest-cost path** from the start node to the target node. Your implementation must strictly adhere to the algorithmic constraints defined below to ensure correctness, optimality, and efficiency.

---

## 🗺️ Graph Topology & Dataset

The network is modeled as a Directed Graph $G = (V, E)$. 

### Node Representation

Nodes represent intersections, delivery hubs, or charging stations:
* `S` : Fleet Origin Hub (Start)
* `G` : Distribution Depot (Goal)
* `A, B, C, D, E, F` : Intermediate street intersections

### Edge Cost Matrix

The edge weights represent the **Total Energy-Cost Units** required to traverse that specific street segment.

| Source Node | Target Node | Operational Cost ($g(n)$ units) | Street Type / Condition |
| :--- | :--- | :--- | :--- |
| **S** | A | 4 | Residential road, low traffic |
| **S** | B | 2 | Expressway, optimal speed |
| **A** | C | 5 | Heavy uphill incline |
| **B** | A | 1 | Downhill slope connector |
| **B** | D | 8 | Construction zone, high delay |
| **B** | F | 10 | Highway segment with toll |
| **C** | D | 2 | Flat arterial road |
| **C** | G | 6 | **Goal Route Alpha** (High traffic) |
| **D** | F | 2 | Fleet-only bypass lane |
| **F** | G | 3 | **Goal Route Beta** (Clear flow) |

---

## 🛠️ Project Requirements & Constraints

To ensure this project demonstrates portfolio-grade software engineering, your solution must satisfy the following constraints:

1. **Uninformed Strategy**: The agent has no heuristic knowledge of the geographical distance to the goal ($h(n) = 0$). It must rely purely on accumulated historical path cost $g(n)$.
2. **Graph Search Compliance**: You must implement an explicit **Explored Set (Closed List)** to prevent infinite loops caused by cyclic routes (e.g., $S \rightarrow B \rightarrow A \rightarrow C$).
3. **Optimal Goal Testing**: The algorithm must **only** check if the goal condition is met when a node is *popped from the priority queue*, not when it is first discovered/generated.
4. **Efficiency Constraint**: Checking if an unexpanded node already exists in the priority queue frontier must operate in **$O(1)$ time complexity** using an augmented tracking map or a lazy-deletion strategy.
5. **Path Reconstruction**: Your solution must track and reconstruct the complete path (sequence of nodes) from start to goal, not just the final cost.

---

## 🚀 Expected Output

Your program should accept the graph configuration and output the exact sequence of intersections visited, along with the total minimized cost. 

**Expected Analytical Verification:**
* **Optimal Path:** `S` $\rightarrow$ `B` $\rightarrow$ `A` $\rightarrow$ `C` $\rightarrow$ `D` $\rightarrow$ `F` $\rightarrow$ `G`
* **Total Operational Cost:** `13` units

*(Note: Although path $S \rightarrow B \rightarrow F \rightarrow G$ has fewer stops/edges, its total cost is $2 + 10 + 3 = 15$, making it sub-optimal compared to the UCS solution).*
