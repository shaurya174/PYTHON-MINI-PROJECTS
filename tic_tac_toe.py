def print_tic_tac_toe(user_list):
    """
    Prints the tic-tac-toe board in a formatted way.
    
    Parameters:
    user_list (list): The current state of the tic-tac-toe board.
    """
    for i in range(0, 9, 3):
        print(f" {user_list[i]} | {user_list[i+1]} | {user_list[i+2]} ")
        if i < 6:  # Don't print the separator line after the last row
            print("---|---|---")

def replace_elt(user_list, prev, new):
    """
    Replaces all occurrences of 'prev' with 'new' in the user_list.
    
    Parameters:
    user_list (list): The list representing the board.
    prev (str): The value to be replaced.
    new (str): The value to replace with.
    
    Returns:
    list: A new list with replacements made.
    """
    return [new if x == prev else x for x in user_list]

def win(user_list):
    """
    Checks if there is a winning condition in the tic-tac-toe board.
    
    Parameters:
    user_list (list): The list representing the board.
    
    Returns:
    bool: True if there is a winning condition, False otherwise.
    """
    # Check rows for a win
    for i in range(0, 9, 3):
        if user_list[i] == user_list[i+1] == user_list[i+2] and user_list[i] != ' ':
            return True

    # Check columns for a win
    for j in range(0, 3):
        if user_list[j] == user_list[j+3] == user_list[j+6] and user_list[j] != ' ':
            return True

    # Check diagonals for a win
    if user_list[0] == user_list[4] == user_list[8] and user_list[0] != ' ':
        return True
    if user_list[2] == user_list[4] == user_list[6] and user_list[2] != ' ':
        return True

    return False

def draw(user_list):
    """
    Checks if the game is a draw, meaning the board is full with no winners.
    
    Parameters:
    user_list (list): The list representing the board.
    
    Returns:
    bool: True if the game is a draw, False otherwise.
    """
    # Check if there are any positions left that are still numeric (i.e., unfilled)
    return all(not i.isdigit() for i in user_list)  # All positions are filled with 'X' or 'O'

def tic_tac_toe():
    """
    Runs the main tic-tac-toe game loop.
    """
    matrix = ['1','2','3','4','5','6','7','8','9']  # Initial board setup with positions
    player1 = input("Enter Name Of Player 1: ")
    player2 = input("Enter Name Of Player 2: ")
    
    # Instructions for players
    print("RULES OF PLAY: ")
    print("One By One Enter X/O")
    print(f"{player1} -> X\n{player2} -> O")
    print("To enter X/O Choose Which Position You Want To Change")
    print("Available Inputs -> 1,2,3,4,5,6,7,8,9")
    print("LET'S START")
    
    current_turn = ""
    print_tic_tac_toe(matrix)
    
    while True:
        # Player 1's turn
        current_turn = player1
        user_choice = input(f"Enter Which Position You Want To Change {player1}: ")
        matrix = replace_elt(matrix, user_choice, 'X')
        print(f"{player1} entered X at position {user_choice}")
        print("Current TIC-TAC-TOE: ")
        print_tic_tac_toe(matrix)
        
        if win(matrix):
            print("Congratulations!!")
            print(f"{current_turn} wins the game!!!")
            break
        if draw(matrix):
            print("Both Of You Win!!")
            print("It's A Draw")
            break

        # Player 2's turn
        current_turn = player2
        user_choice = input(f"Enter Which Position You Want To Change {player2}: ")
        matrix = replace_elt(matrix, user_choice, 'O')
        print(f"{player2} entered O at position {user_choice}")
        print("Current TIC-TAC-TOE: ")
        print_tic_tac_toe(matrix)
        
        if win(matrix):
            print("Congratulations!!")
            print(f"{current_turn} wins the game!!!")
            break
        if draw(matrix):
            print("Both Of You Win!!")
            print("It's A Draw")
            break

tic_tac_toe()
