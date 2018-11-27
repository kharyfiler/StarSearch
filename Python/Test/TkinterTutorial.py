from tkinter import *
import tkinter.messagebox


def doNothing():
    print("ok ok I won't...")


root = Tk()  # this builds the root window

# **** Main Menu ****

first_menu = Menu(root)  # this creates a first_menu within the root window
root.config(menu=first_menu)

subMenu = Menu(first_menu)  # this creates a subMenu within the first_menu
first_menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(first_menu)
first_menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

# **** The Toolbar ****

toolbar = Frame(root, bg="blue")
insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# **** The Statusbar ****

status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)  # bd stands for bordered
status.pack(side=BOTTOM, fill=X)

# **** The Messagebox ****

# tkinter.messagebox.showinfo("Window Title", "Monkeys can live up to 300 years.")
#
# answer = tkinter.messagebox.askquestion("Question 1", "Do you like silly faces?")  # the user will click "Yes" or "No
#                                                                                    # and the answer will be stored
# if answer == "yes":
#     print(" :D ")

# **** Shapes and Graphics ****

canvas = Canvas(root, width=200, height=100)
canvas.pack()

black_line = canvas.create_line(0, 0, 200, 50)  # starting point and ending point of line
red_line = canvas.create_line(0, 100, 200, 25, fill="red")
green_box = canvas.create_rectangle(25, 25, 130, 60, fill="green")

canvas.delete(red_line)  # this deletes canvas elements
canvas.delete(ALL)

# **** Images and Icons ****

luke_skywalker = PhotoImage(file="luke-skywalker-force-awakens.png")
label = Label(root, image=luke_skywalker)
label.pack()

root.mainloop()