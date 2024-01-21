import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("TicTacToe")
        self.board = [" " for i in range(9)]
        self.buttons = []
        self.create()
        self.currentplayer = "X"

    def create(self):
        custom=("Arial",80)
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", width=3, height=1,font=custom,
                                   command=lambda row=i, col=j: self.onbuttonclick(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def onbuttonclick(self, row, col):
        index = 3 * row + col
        if self.board[index] == " ":
            self.board[index] = self.currentplayer
            self.buttons[index].config(text=self.currentplayer)
            if self.checkwinner():
                messagebox.showinfo("Game Over", f"AI wins!")
                self.resetboard()
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.resetboard()
            else:
                if self.currentplayer == "X" :
                    self.currentplayer = "O"
                else :
                    self.currentplayer = "X"
                self.aimove()

    
    def aimove(self):
        bestscore = float('-inf')
        bestmove = None

        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                score = self.minimax(False)
                self.board[i] = " "
                if score > bestscore:
                    bestscore = score
                    bestmove = i

        if bestmove is not None:
            self.board[bestmove] = "O"
            self.buttons[bestmove].config(text="O")

            if self.checkwinner():
                messagebox.showinfo("Game Over", f"AI wins!")
                self.resetboard()
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.resetboard()
            else:
                if self.currentplayer == "X" :
                    self.currentplayer = "O"
                else :
                    self.currentplayer = "X"
                

    def minimax(self, maximizingplayer):
        if self.checkwinner():
            return -1 if maximizingplayer else 1
        elif " " not in self.board:
            return 0

        if maximizingplayer:
            maxeval = float('-inf')
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = "O"
                    eval = self.minimax(False)
                    self.board[i] = " "
                    maxeval = max(maxeval, eval)
            return maxeval
        else:
            mineval = float('inf')
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = "X"
                    eval = self.minimax(True)
                    self.board[i] = " "
                    mineval = min(mineval, eval)
            return mineval

    def checkwinner(self):
        for i in range(3):
            if self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] != " " :
                return True
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != " ":
                return True
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return True
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return True
        return False

    def resetboard(self):
        self.board = [" " for i in range(9)]
        for button in self.buttons:
            button.config(text="")
        self.currentplayer = "X"

    def run(self):
        self.root.mainloop()


game = TicTacToe()
game.run()
