import heapq
from collections import deque
import time

class PuzzleState:
    def __init__(self, puzzle, parent=None, move=""):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move
        if self.parent is None:
            self.cost = 0
        else:
            self.cost = parent.cost + 1

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def __hash__(self):
        return hash(str(self.puzzle))

    def get_blank_pos(self):
        # პოულობს თავსატეხში ცარიელი ადგილის პოზიციას
        for i, row in enumerate(self.puzzle):
            if 0 in row:
                return i, row.index(0)

    def get_neighbors(self):
        # ამჟამინდელი თავსატეხის მდგომარეობის მეზობელი მდგომარეობები ცარიელი სივრცის გადაადგილებით.
        # აბრუნებს PuzzleState ობიექტების სიას, რომლებიც წარმოადგენენ მოქმედ მეზობელ მდგომარეობებს.
        neighbors = []
        blank_pos = self.get_blank_pos()
        i, j = blank_pos

        # Move up
        if i > 0:
            puzzle_copy = [row[:] for row in self.puzzle]
            puzzle_copy[i][j], puzzle_copy[i-1][j] = puzzle_copy[i-1][j], puzzle_copy[i][j]
            neighbors.append(PuzzleState(puzzle_copy, self, "Up"))

        # Move down
        if i < len(self.puzzle) - 1:
            puzzle_copy = [row[:] for row in self.puzzle]
            puzzle_copy[i][j], puzzle_copy[i+1][j] = puzzle_copy[i+1][j], puzzle_copy[i][j]
            neighbors.append(PuzzleState(puzzle_copy, self, "Down"))

        # Move left
        if j > 0:
            puzzle_copy = [row[:] for row in self.puzzle]
            puzzle_copy[i][j], puzzle_copy[i][j-1] = puzzle_copy[i][j-1], puzzle_copy[i][j]
            neighbors.append(PuzzleState(puzzle_copy, self, "Left"))

        # Move right
        if j < len(self.puzzle[i]) - 1:
            puzzle_copy = [row[:] for row in self.puzzle]
            puzzle_copy[i][j], puzzle_copy[i][j+1] = puzzle_copy[i][j+1], puzzle_copy[i][j]
            neighbors.append(PuzzleState(puzzle_copy, self, "Right"))

        return neighbors


def solve_puzzle_bfs(initial_board, goal_board):
    # თავსატეხის ამოხსნა Breadth-First Search ალგორითმის გამოყენებით.
    # აბრუნებს გზას მიზნის მდგომარეობამდე და შესრულების დროს.
    start_time = time.time()
    initial_state = PuzzleState(initial_board)
    goal_state = PuzzleState(goal_board)

    open_list = deque()
    open_list.append(initial_state)
    closed_set = set()

    while open_list:
        current_state = open_list.popleft()
        closed_set.add(current_state)

        if current_state == goal_state:
            path = []
            while current_state.parent:
                path.append(current_state.puzzle)
                current_state = current_state.parent
            path.append(initial_board)
            path.reverse()
            end_time = time.time()
            return path, end_time - start_time

        for neighbor in current_state.get_neighbors():
            if neighbor not in closed_set:
                open_list.append(neighbor)

    return None, time.time() - start_time


def solve_puzzle_astar(initial_board, goal_board):
    # თავსატეხის ამოხსნა A* ალგორითმის გამოყენებით.
    # აბრუნებს გზას მიზნის მდგომარეობამდე და შესრულების დროს.
    start_time = time.time()
    initial_state = PuzzleState(initial_board)
    goal_state = PuzzleState(goal_board)

    open_list = []
    heapq.heappush(open_list, initial_state)
    closed_set = set()

    while open_list:
        current_state = heapq.heappop(open_list)
        closed_set.add(current_state)

        if current_state == goal_state:
            path = []
            while current_state.parent:
                path.append(current_state.puzzle)
                current_state = current_state.parent
            path.append(initial_board)
            path.reverse()
            end_time = time.time()
            return path, end_time - start_time

        for neighbor in current_state.get_neighbors():
            if neighbor not in closed_set:
                heapq.heappush(open_list, neighbor)

    return None, time.time() - start_time


# Get initial board from user
print("Enter the initial board (3x3 grid):")
initial_board = []
for i in range(3):
    row = input(f"Enter row {i+1}: ")
    initial_board.append([int(num) for num in row.split()])

# Get goal board from user
print("Enter the goal board (3x3 grid):")
goal_board = []
for i in range(3):
    row = input(f"Enter row {i+1}: ")
    goal_board.append([int(num) for num in row.split()])

# Solve the puzzle using BFS
bfs_path, bfs_execution_time = solve_puzzle_bfs(initial_board, goal_board)

# Solve the puzzle using A*
astar_path, astar_execution_time = solve_puzzle_astar(initial_board, goal_board)

# Print the results
if bfs_path:
    print("BFS Path:")
    for board in bfs_path:
        for row in board:
            print(row)
        print()
    print("BFS execution Time:", bfs_execution_time)
else:
    print("No solution found using BFS.")

if astar_path:
    print("A* Path:")
    for board in astar_path:
        for row in board:
            print(row)
        print()
    print("A* execution Time:", astar_execution_time)
else:
    print("No solution found using A*.")
