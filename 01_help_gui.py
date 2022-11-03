from tkinter import *
from functools import partial  # to make sure there aren't any unnecessary windows

import random


class Quiz:
    def __init__(self, parent):

        # variable formatting
        background_color = "dark turquoise"    # slate blue maybe?

        # Quiz Main Screen GUI
        self.quiz_frame = Frame(width=640, height=480, bg=background_color,
                                     pady=10)
        self.quiz_frame.grid()

        # Quiz Heading (row 0)
        self.quiz_label = Label(self.quiz_frame, text="Cool Quiz Boogaloo",
                                          font=("Arial", "14", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.quiz_label.grid(row=0)

        # Help Button (row 1)
        self.help_button = Button(self.quiz_frame, text="Help",
                                  font="Arial 14", padx=10, pady=10, command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure()

class Help:
    def __init__(self, partner):

        background = "maroon"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

                # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background,pady=10)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="Arial 14 bold", bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="hi",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="orange",
                                  font="Arial 14 bold", command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    something = Quiz(root)
    root.mainloop()
