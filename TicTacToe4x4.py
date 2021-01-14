# CSE 210 Brother Hayes
#Tic Tac Toe 4x4 week 2 solo checkpoint
# Chandler Owen 1-8-21


#Main function will run the game
def main():
    count = 1
    while True:
        a_list = []
        print('\n')
        print(f"Welcome to Tic-Tac-Toe 4x4 Game #{count}")
        player = next_player("")
        board = create_board()
        while not is_winner(board):
            display_board(board)
            make_move(player, board, a_list)
            player = next_player(player)
            if is_draw(board) == True:
                break
        if is_draw(board) == True:
            display_board(board)
            print("Draw!")
            str_c = input("Would you like to play again?(y or n): ")
            str_d = 'y'
            if (str_c == str_d):
                count = count + 1
            else:
                print("See Ya Later!")
                return False
        else:
            display_board(board)
            player = next_player(player)
            str_a = input(f"well done {player}! Would you like to play again?(y or n): ")
            str_b = 'y'
            if (str_a == str_b):
                count = count + 1
            else:
                print("See Ya Later!")
                return False

#Creat the board spaces
def create_board():
    board = []
    for square in range(16):
        board.append(square + 1)
    return board

#display the board
def display_board(board):
    print()
    print(f"{board[0]} |{board[1]} |{board[2]} |{board[3]} ")
    print('--+--+--+--')
    print(f"{board[4]} |{board[5]} |{board[6]} |{board[7]} ")
    print('--+--+--+--')
    print(f"{board[8]} |{board[9]:^2}|{board[10]:^2}|{board[11]:^2}")
    print('--+--+--+--')
    print(f"{board[12]:^2}|{board[13]:^2}|{board[14]:^2}|{board[15]:^2}")
    print()

#checks if the game ends in a tie
def is_draw(board):
    for square in range(16):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 

#checks if any row or column is complete for a win
def is_winner(board):
     return (board[0] == board[1] == board[2] == board[3] or
            board[4] == board[5] == board[6] == board[7] or
            board[8] == board[9] == board[10] == board[11] or
            board[12] == board[13] == board[14] == board[15] or
            board[0] == board[5] == board[10] == board[15] or
            board[3] == board[6] == board[9] == board[12] or
            board[1] == board[5] == board[9] == board[13] or
            board[0] == board[4] == board[8] == board[12] or
            board[2] == board[6] == board[10] == board[14] or
            board[3] == board[7] == board[11] == board[15])

#determine if the move is valid and available
def make_move(player, board, a_list):
    while True:
        try:
            square = int(input(f"{player}'s turn to choose a square (1-16): "))
        except ValueError:
            print("Must be a valid number (1-16).")
            display_board(board)
            continue
        if square > 16 or square < 1:
            print("Must be a valid number (1-16).")
            display_board(board)
        else:
            a_list.append(square)
            if anyduplicate(a_list) == True:
                print('\n')
                print("Pick a new square " + player)
                a_list.pop()
                display_board(board)
                continue
            board[square - 1] = player
            return False
            
#check if duplicate square is picked
def anyduplicate(a_list):
    seen = set()
    for x in a_list:
        if x in seen:
            return True
        else:
            seen.add(x)
    return False

#switch turns from x's to o's
def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

#call main to start the program
if __name__ == "__main__":
    main()