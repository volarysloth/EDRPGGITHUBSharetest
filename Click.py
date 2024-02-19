from tkinter import *

window = Tk() #instantiate an instanccce of window

def click():
    print("You clicked the button!")

button = Button(window,
                text="click me!",
                command=click,
                font=("ComicSans",30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=DISABLED)

button.pack()

window.mainloop() #place window on computer computer screen, lsiten for events