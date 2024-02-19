from tkinter import *

count = 0

window = Tk() #instantiate an instanccce of window
window.geometry("600x600")
window.title("Zaf Code first GUI program")

icon = PhotoImage(file='ukraine.png')
window.iconphoto(True,icon)
window.config(background="#5cfcff")

label =Label(window,
             text='Hello',
             font= ('arial', 40, 'bold'),
             fg ='#00FF00',
             bg='black')
label.pack()
#label.place(x=0,y=0)

photo = PhotoImage(file='sun.png')
def click():
    print("You clicked the button!")
button = Button(window,
                text="click me!",
                command=click,
                font=("ComicSans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound='bottom')

button.pack()

window.mainloop() #place window on computer computer screen, lsiten for events


