import tkinter as tk
from tkinter import messagebox
import random

# Global game variables
board = [""] * 9
player_turn = "X"
vs_computer = False
buttons = []
game_window = None
mode_window = None

# Function to start the game
def start_game(mode):
    global vs_computer, game_window, board, player_turn, buttons

    vs_computer = (mode == "pvc")
    mode_window.destroy()  # Close mode selection window

    game_window = tk.Tk()
    game_window.title("Tic-Tac-Toe")
    
    board = [""] * 9
    player_turn = "X"
    buttons = []

    frame = tk.Frame(game_window)
    frame.pack()

    for i in range(9):
        btn = tk.Button(frame, text="", font=("Arial", 20), width=5, height=2,
                        command=lambda i=i: on_click(i))
        btn.grid(row=i//3, column=i%3)
        buttons.append(btn)

    game_window.mainloop()

# Function to check for a winner
def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]
    
    for a, b, c in winning_combinations:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]  # Return winner symbol

    if "" not in board:
        return "Draw"  # Game is a tie

    return None  # No winner yet

# Function for handling button clicks
def on_click(index):
    global player_turn

    if board[index] or check_winner():
        return

    board[index] = player_turn
    buttons[index].config(text=player_turn, state=tk.DISABLED)

    winner = check_winner()
    if winner:
        show_winner(winner)
        return

    # Switch turns
    if vs_computer and player_turn == "X":
        player_turn = "O"
        game_window.after(500, computer_move)
    else:
        player_turn = "X" if player_turn == "O" else "O"

# Function for computer's move
def computer_move():
    global player_turn
    empty_cells = [i for i in range(9) if board[i] == ""]
    
    if empty_cells:
        move = random.choice(empty_cells)
        board[move] = "O"
        buttons[move].config(text="O", state=tk.DISABLED)

    winner = check_winner()
    if winner:
        show_winner(winner)
    else:
        player_turn = "X"

# Function to display the winner and ask if they want to play again
def show_winner(winner):
    message = "It's a Draw!" if winner == "Draw" else f"{winner} Wins!"
    messagebox.showinfo("Game Over", message)
    ask_play_again()

# Function to ask if the player wants to play again
def ask_play_again():
    play_again = messagebox.askyesno("Play Again?", "Do you want to play another match?")
    
    if play_again:
        go_back_to_mode_selection()
    else:
        game_window.destroy()

# Function to go back to the mode selection window
def go_back_to_mode_selection():
    game_window.destroy()
    open_mode_selection()

# Function to open the mode selection window
def open_mode_selection():
    global mode_window
    mode_window = tk.Tk()
    mode_window.title("Select Game Mode")

    tk.Label(mode_window, text="Choose Game Mode", font=("Arial", 14)).pack(pady=10)

    tk.Button(mode_window, text="Player vs Player", command=lambda: start_game("pvp"), width=20, height=2).pack(pady=5)
    tk.Button(mode_window, text="Player vs Computer", command=lambda: start_game("pvc"), width=20, height=2).pack(pady=5)

    mode_window.mainloop()

# ------------------- Start the Mode Selection Window -------------------
open_mode_selection()
5
