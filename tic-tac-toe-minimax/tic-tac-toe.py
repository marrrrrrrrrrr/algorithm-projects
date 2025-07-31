board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
COMPUTER = 'O'
PLAYER = 'X'

def main():
    print("Computer: O Vs. You: X")
    player = int(input("Enter to play 1(st) or 2(nd): "))

    for i in range(9):
    	# ამოწმებს დასრულდა თუ არა თამაში
        if check_game_status(board) != '-':
            break
        if (i + player) % 2 == 0:
            # კომპიუტერის რიგი
            computer_turn()
        else:
            # მოთამაშის რიგი
            display_board(board)
            player_turn()

    # იძახებს check_game_status ფუნქციას, რათა გააანალიზოს დაფა და განსაზღვროს თამაშის მიმდინარე მდგომარეობა
    result = check_game_status(board)
    display_board(board)

    if result == COMPUTER:
        print("Computer Wins!!!")
    elif result == PLAYER:
        print("You Win!!!")
    else:
        print("Draw!!!")

def display_board(board):
    # გამოაქვს საწყისი დაფა
    print("Current State Of Board:\n")
    print(board[0] + "  " + board[1] + "  " + board[2])
    print()
    print(board[3] + "  " + board[4] + "  " + board[5])
    print()
    print(board[6] + "  " + board[7] + "  " + board[8])
    print()

def player_turn():
    # ამუშავებს მოთამაშის რიგს თამაშში, სწორი ნაბიჯის შემდეგ კი შესაბამისად განაახლებს დაფას
    validMove = False
    while not validMove:
        pos = int(input("Enter position from [1...9]: "))
        if is_valid_move(pos):
            validMove = True
            board[pos - 1] = PLAYER
        else:
            print("Invalid Move! Please try again.")

def computer_turn():
    # ამუშავებს კომპიუტერის სვლას თამაშში. იყენებს minimax ალგორითმს კომპიუტერისთვის საუკეთესო ნაბიჯის დასადგენად და აახლებს დაფას
    bestScore = float('-inf')
    bestMove = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = COMPUTER
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = i
    if bestMove != -1:
        board[bestMove] = COMPUTER

def minimax(board, depth, isMaximizingPlayer):
    # ახორციელებს minimax ალგორითმს კომპიუტერისთვის საუკეთესო ნაბიჯის დასადგენად.
    result = check_game_status(board)

    if result != '-':
        if result == COMPUTER:
            return 1
        elif result == PLAYER:
            return -1
        else:
            return 0

    # ამოწმებს დამთავრდა თუ არა თამაში და აბრუნებს შესაბამის ქულას
    if isMaximizingPlayer:
        bestScore = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = COMPUTER
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = PLAYER
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                bestScore = min(score, bestScore)
        return bestScore

def is_valid_move(pos):
    # ამოწმებს, არის თუ არა მოცემული პოზიცია სწორი ნაბიჯი
    return pos >= 1 and pos <= 9 and board[pos - 1] == ' '

def check_game_status(board):
    # ამოწმებს დაფის მდგომარეობას იმის დასადგენად, არსებობს გამარჯვებული თუ თამაში ფრედ დასრულდა.
    winningCombinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for combination in winningCombinations:
        if board[combination[0]] != ' ' and board[combination[0]] == board[combination[1]] == board[combination[2]]:
            return board[combination[0]]

    if ' ' in board:
        return '-'
    else:
        return ' '


main()
