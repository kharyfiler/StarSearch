import sys
import Main.StarSearch
from tkinter import *

search = Main.StarSearch.StarSearch()


def close_program():
    sys.exit()


def filterbar_gridding(label_text, column_num, set_string, entry_string, resource_int):
    Label(filterbar_frame, text=label_text, bg="black", fg="lightblue").grid(row=0, column=column_num, padx=2, pady=2)
    dropdown_value = StringVar(filterbar_frame)
    dropdown_value.set(set_string)
    entry_list = [entry[entry_string] for entry in search.get_all_resources(resource_int)]
    OptionMenu(filterbar_frame, dropdown_value, *entry_list).grid(row=1, column=column_num)


def buttonframe_packing(label_text):
    Button(viewing_button_frame, text=label_text, bg="black", fg="lightblue").pack(anchor=W)


root = Tk()
root.title("Star Search")

# Add menu bar
main_menu = Menu(root)
root.config(menu=main_menu)
file_menu = Menu(main_menu)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Quit", command=close_program)

# Create frames
filterbar_frame = Frame(root, bg="black")
viewing_button_frame = Frame(root)
viewing_list_frame = Frame(root)
searchfield_frame = Frame(root)
detail_frame = Frame(root)

# Add status bar
status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)  # bd stands for bordered
status.pack(side=BOTTOM, fill=X)

# Add header
header_label = Label(root, text="In a galaxy far far away...", font=250, bg="black", fg="lightblue")
header_label.pack(side=TOP, fill=X)

# ** Begin filterbar_frame **
Label(filterbar_frame, text="Filter By:", bg="black", fg="lightblue").grid(row=1, padx=2, pady=2)

# todo: improve/move base category references into a dictionary, static dictionary?
filterbar_gridding("Film", 1, search.get_first_film().title, "title", 0)
filterbar_gridding("Person", 2, search.get_first_person().name, "name", 1)
filterbar_gridding("Planet", 3, search.get_first_planet().name, "name", 2)
filterbar_gridding("Species", 4, search.get_first_species().name, "name", 3)
filterbar_gridding("Starship", 5, search.get_first_starship().name, "name", 4)
filterbar_gridding("Vehicle", 6, search.get_first_vehicle().name, "name", 5)

filterbar_frame.pack(side=TOP, fill=X)
# ** End filterbar_frame **

# ** Begin viewing_button_frame **
buttonframe_packing("All")
buttonframe_packing("FILMS")
buttonframe_packing("PLANETS")
buttonframe_packing("SPECIES")
buttonframe_packing("STARSHIPS")
buttonframe_packing("VEHICLES")
viewing_button_frame.pack(side=LEFT, anchor=N)
# ** End viewing_button_frame **

# ** Begin viewing_list_frame **
Label(viewing_list_frame, text="VIEWING", bg="black", fg="lightblue").pack()
viewing_list_frame.pack(side=LEFT, anchor=N)
# ** End viewing_list_frame **

# ** Begin searchfield_frame **
search_field = Entry(searchfield_frame)
search_field.pack(side=TOP)
# ** End searchfield_frame **

# ** Begin detail_frame **
# ** End detail_frame **

# # Create a dropdown menu
# # Create a Tkinter variable
# tkvar = StringVar(root)
#
# # Dictionary with options
# choices = {"Films", "People", "Planets", "Species", "Starships", "Vehicles"}
# tkvar.set("Films")  # set the default option
#
# popupMenu = OptionMenu(main_frame, tkvar, *choices)
# Label(main_frame, text="Set a filter").grid(row=1, column=1)
# popupMenu.grid(row=2, column=1)
#
# # on change dropdown value
# def change_dropdown(*args):
#     print(tkvar.get())
#
#
# # link function to change dropdown
# tkvar.trace('w', change_dropdown)

root.mainloop()