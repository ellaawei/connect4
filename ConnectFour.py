import tkinter as tk
from tkinter import messagebox

class ConnectFour:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Connect Four")
        self.window.geometry("700x600")
        self.player_turn = "X"

        self.buttons = []
        for i in range(6):
            row = []
            for j in range(7):
                button = tk.Button(self.window, command=lambda row=i, column=j: self.click(row, column), height=3, width=6)
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def click(self, row, column):
        if self.buttons[0][column]['text'] == "":
            for i in range(5, -1, -1):
                if self.buttons[i][column]['text'] == "":
                    self.buttons[i][column]['text'] = self.player_turn
                    if self.check_win():
                        messagebox.showinfo("Game Over", f"Player {self.player_turn} wins!")
                        self.window.quit()
                    self.player_turn = "O" if self.player_turn == "X" else "X"
                    break

    def check_win(self):
        for row in self.buttons:
            for i in range(len(row) - 3):
                if row[i]['text'] == row[i+1]['text'] == row[i+2]['text'] == row[i+3]['text'] != "":
                    return True
        for column in range(len(self.buttons[0])):
            for i in range(len(self.buttons) - 3):
                if self.buttons[i][column]['text'] == self.buttons[i+1][column]['text'] == self.buttons[i+2][column]['text'] == self.buttons[i+3][column]['text'] != "":
                    return True
        for row in range(len(self.buttons) - 3):
            for column in range(len(self.buttons[0]) - 3):
                if self.buttons[row][column]['text'] == self.buttons[row+1][column+1]['text'] == self.buttons[row+2][column+2]['text'] == self.buttons[row+3][column+3]['text'] != "":
                    return True
        for row in range(3, len(self.buttons)):
            for column in range(len(self.buttons[0]) - 3):
                if self.buttons[row][column]['text'] == self.buttons[row-1][column+1]['text'] == self.buttons[row-2][column+2]['text'] == self.buttons[row-3][column+3]['text'] != "":
                    return True
        return False

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = ConnectFour()
    game.run()
