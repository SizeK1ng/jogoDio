import tkinter as tk
from tkinter import messagebox
import random

class GameOfTicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")

        self.current_player = "X"
        self.board = [""] * 9

        self.buttons = []
        for i in range(9):
            button = tk.Button(root, text="", font=("Helvetica", 24), height=2, width=5,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def make_move(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Fim de jogo", f"Jogador {self.current_player} venceu!")
                self.reset_game()
            elif all(cell != "" for cell in self.board):
                messagebox.showinfo("Fim de jogo", "Empate!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.ai_move()

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def reset_game(self):
        for i in range(9):
            self.board[i] = ""
            self.buttons[i].config(text="")
        self.current_player = "X"

    def ai_move(self):
        best_score = -float("inf")
        best_move = None

        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "O"
                score = self.minimax(self.board, 0, False)
                self.board[i] = ""
                if score > best_score:
                    best_score = score
                    best_move = i

        if best_move is not None:
            self.make_move(best_move)

    def minimax(self, board, depth, is_maximizing):
        scores = {"X": -1, "O": 1, "tie": 0}

        if self.check_winner():
            return scores[self.current_player]
        elif all(cell != "" for cell in board):
            return scores["tie"]

        if is_maximizing:
            best_score = -float("inf")
            for i in range(9):
                if board[i] == "":
                    board[i] = "O"
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ""
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(9):
                if board[i] == "":
                    board[i] = "X"
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ""
                    best_score = min(score, best_score)
            return best_score

if __name__ == "__main__":
    root = tk.Tk()
    game = GameOfTicTacToe(root)
    root.mainloop()
