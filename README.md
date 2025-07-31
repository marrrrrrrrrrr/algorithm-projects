# Algorithm Projects

This repository contains various algorithmic and AI projects implemented in Python. Each project demonstrates different problem-solving skills and classic algorithms through interactive console applications.

---

## Projects

### Tic-Tac-Toe with Minimax AI

A console-based Tic-Tac-Toe game where you play against an AI opponent powered by the minimax algorithm. The AI always makes the optimal move, making it a challenging game for the player.

- **Features:**  
  - Play against an unbeatable AI  
  - Input validation and game status checking  
  - Clear console interface

- **Technologies:** Python 3, Minimax algorithm

- **How to Run:**  
  Run the script `tic_tac_toe.py` inside the `tic-tac-toe-minimax` folder.

  Choose to play first or second.

  Enter moves using numbers 1–9.

  The game ends with a win, loss, or draw message.



<br><br>
---
<br><br>




# 8-Puzzle Solver (BFS and A*)

A console-based Python program that solves the classic 3x3 sliding puzzle using **Breadth-First Search (BFS)** and **A\*** algorithms. The solver compares both methods in terms of solution paths and execution time.

---

## 📌 Description

The 8-puzzle is a sliding puzzle having 8 numbered square tiles and one empty space. The goal is to move the tiles using the blank space to reach a specific end configuration.

This project takes an initial puzzle configuration and a target (goal) configuration as input and solves the puzzle using:

- **Breadth-First Search (BFS)**
- **A\* Search Algorithm**

The solution path is displayed step-by-step for each method, along with the time taken to compute the solution.

---

## Features

- Accepts user input for both initial and goal states.
- Implements BFS and A* for pathfinding.
- Displays execution time for both algorithms.

---

##  Algorithms Used

- **BFS** explores nodes level by level to find the shortest solution.
- **A\*** uses a cost function (g + h) to prioritize efficient paths.

---

##  How to Run

Run the script `8-puzzle.py` inside the `8-puzzle` folder.

Enter your initial and goal puzzle boards when prompted.

View the step-by-step solution path and execution time for each algorithm.
