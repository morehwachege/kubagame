import tkinter as tk

class BoardGuiTk(tk.Frame):
    color ="White"
    rows = 7
    column = 7
    square_size = 20 x 20

    def canvas_size(self):
        return (self.column)
