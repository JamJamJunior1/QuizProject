from tkinter import *
from functools import partial  # to make sure there aren't any unnecessary windows

import random

class Quiz:
    def __init__(self, parent):

        # variable formatting
        background_color = "dark turquoise"    # slate blue maybe?

        # Quiz Main Screen GUI
        self.quiz_frame = Frame(width=300, height=480, bg=background_color,
                                     pady=10)  # experiment with these
        self.quiz_frame.grid()

        # Quiz Heading (row 0)
        self.quiz_label = Label(self.quiz_frame, text="Quiz",
                                          font=("Arial", "10", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.quiz_label.grid(row=0)

        # User Instructions (row 1)
        self.user_instructions = Label(self.quiz_frame, text="Answer the question provided",
                                  font="Arial 10 bold", wrap=250, justify=LEFT, bg=background_color, padx=10, pady=10,)
        self.user_instructions.grid(row=1)

        # Answer label (row 2)
        self.converted_label = Label(self.quiz_frame, font="Arial 14 bold", fg="purple", bg=background_color, pady=10, text="Question")
        self.converted_label.grid(row=2)

        # Answer entry box (row 3)
        self.to_convert_entry = Entry(self.quiz_frame, width=20, font="Arial 10 bold")
        self.to_convert_entry.grid(row=3)

        # History / Help button frame (row 4)
        self.hist_help_frame = Frame(self.quiz_frame)
        self.hist_help_frame.grid(row=4, pady=10)

        self.answer_hist_button = Button(self.hist_help_frame, font="Arial 12 bold", fg="purple", bg=background_color, pady=10, text="Answer History", width=15)
        self.answer_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold", fg="purple", bg=background_color, pady=10, text="Help", width=5)
        self.help_button.grid(row=0, column=1)

if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    something = Quiz(root)
    root.mainloop()
