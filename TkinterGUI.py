from starwars_api.StarSearch import StarSearch as Search
from starwars_api.StarSearch import ObjectClasses
from tkinter import *
import datetime
import requests

search = Search()
complete_object_dict = search.complete_object_dict_maker()

people_list = []
film_list = []
planet_list = []
species_list = []
starship_list = []
vehicle_list = []
complete_viewable_dict_of_lists = {}


def fill_viewable_items_list(box, filtered_people_list, filtered_films_list, filtered_planets_list,
                             filtered_species_list, filtered_starships_list, filtered_vehicles_list, first_run):
    print("list_box_categorize called. " + str(datetime.datetime.now().time()))
    box.delete(0, END)
    box.insert(END, "========PEOPLE===========")
    list_box_loop_fill(box, filtered_people_list)
    box.insert(END, "========FILMS============")
    list_box_loop_fill(box, filtered_films_list)
    box.insert(END, "========PLANETS==========")
    list_box_loop_fill(box, filtered_planets_list)
    box.insert(END, "========SPECIES==========")
    list_box_loop_fill(box, filtered_species_list)
    box.insert(END, "========STARSHIPS========")
    list_box_loop_fill(box, filtered_starships_list)
    box.insert(END, "========VEHICLES=========")
    list_box_loop_fill(box, filtered_vehicles_list)

    if first_run:
        complete_viewable_dict_of_lists.update({"people":filtered_people_list})
        complete_viewable_dict_of_lists.update({"films": filtered_films_list})
        complete_viewable_dict_of_lists.update({"planets": filtered_planets_list})
        complete_viewable_dict_of_lists.update({"species": filtered_species_list})
        complete_viewable_dict_of_lists.update({"starships": filtered_starships_list})
        complete_viewable_dict_of_lists.update({"vehicles": filtered_vehicles_list})


def list_box_loop_fill(fillable_list_box, filling_list):
    print("list_box_loop_fill called. " + str(datetime.datetime.now().time()))
    for entry in filling_list:
        fillable_list_box.insert(END, entry)


def viewlist_on_select(event):
    print(list_box.get(event.widget.curselection()[0]))
    search_term = list_box.get(event.widget.curselection()[0])
    detail_label_string.set(search_term)
    populate_details(search_term)


def populate_details(search_string):
    viewable_object = complete_object_dict[search_string]
    print("Viewable_object dict type: " + str(type(viewable_object)))
    detail_list_box.delete(0, END)
    if type(viewable_object) == ObjectClasses.Person:
        fill_person(viewable_object)
    if type(viewable_object) == ObjectClasses.Film:
        fill_film(viewable_object)
    if type(viewable_object) == ObjectClasses.Planet:
        fill_planet(viewable_object)
    if type(viewable_object) == ObjectClasses.Species:
        fill_species(viewable_object)
    if type(viewable_object) == ObjectClasses.Starship:
        fill_starship(viewable_object)
    if type(viewable_object) == ObjectClasses.Vehicle:
        fill_vehicle(viewable_object)


def fill_person(person_object):
    detail_list_box.insert(END, "Birth Year : " + str(person_object.birth_year))
    detail_list_box.insert(END, "Eye Color  : " + str(person_object.eye_color))
    detail_list_box.insert(END, "Gender     : " + str(person_object.gender))
    detail_list_box.insert(END, "Hair Color : " + str(person_object.hair_color))
    detail_list_box.insert(END, "Height     : " + str(person_object.height))
    detail_list_box.insert(END, "Mass       : " + str(person_object.mass))
    detail_list_box.insert(END, "Skin Color : " + str(person_object.skin_color))
    detail_list_box.insert(END, "Homeworld  : " + search.url_name_dict[person_object.homeworld])
    for film_url in person_object.films:
        detail_list_box.insert(END, "Films      : {}".format(search.url_name_dict[film_url]))
    for species_url in person_object.species:
        detail_list_box.insert(END, "Species    : " + search.url_name_dict[species_url])
    for starship_url in person_object.starships:
        detail_list_box.insert(END, "Starships  : " + search.url_name_dict[starship_url])
    for vehicle_url in person_object.vehicles:
        detail_list_box.insert(END, "Vehicles   : " + search.url_name_dict[vehicle_url])
    detail_list_box.insert(END, "Created    : " + str(person_object.created))


def fill_film(film_object):
    detail_list_box.insert(END, "Episode ID   :" + str(film_object.episode_id))
    detail_list_box.insert(END, "Opening Crawl:" + str(film_object.opening_crawl))
    detail_list_box.insert(END, "Director     :" + str(film_object.director))
    detail_list_box.insert(END, "Producer     :" + str(film_object.producer))
    detail_list_box.insert(END, "Release Date :" + str(film_object.release_date))
    for species_url in film_object.species:
        detail_list_box.insert(END, "Species    : " + search.url_name_dict[species_url])
    for starship_url in film_object.starships:
        detail_list_box.insert(END, "Starships  : " + search.url_name_dict[starship_url])
    for vehicle_url in film_object.vehicles:
        detail_list_box.insert(END, "Vehicles   : " + search.url_name_dict[vehicle_url])
    for person_url in film_object.characters:
        detail_list_box.insert(END, "Characters   :" + search.url_name_dict[person_url])
    for planet_url in film_object.planets:
        detail_list_box.insert(END, "Planets      :" + search.url_name_dict[planet_url])
    detail_list_box.insert(END, "Created      :" + str(film_object.created))


def fill_planet(planet_object):
    detail_list_box.insert(END, "Diameter       :" + str(planet_object.diameter))
    detail_list_box.insert(END, "Rotation Period:" + str(planet_object.rotation_period))
    detail_list_box.insert(END, "Orbital Period :" + str(planet_object.orbital_period))
    detail_list_box.insert(END, "Gravity        :" + str(planet_object.gravity))
    detail_list_box.insert(END, "Population     :" + str(planet_object.population))
    detail_list_box.insert(END, "Climate        :" + str(planet_object.climate))
    detail_list_box.insert(END, "Terrain        :" + str(planet_object.terrain))
    detail_list_box.insert(END, "Surface Water  :" + str(planet_object.surface_water))
    for person_url in planet_object.residents:
        detail_list_box.insert(END, "Residents      :" + search.url_name_dict[person_url])
    for film_url in planet_object.films:
        detail_list_box.insert(END, "Films      :" + search.url_name_dict[film_url])
    detail_list_box.insert(END, "Created        :" + str(planet_object.created))


def fill_species(species_object):
    detail_list_box.insert(END, "Classification  :" + str(species_object.classification))
    detail_list_box.insert(END, "Designation     :" + str(species_object.designation))
    detail_list_box.insert(END, "Average Height  :" + str(species_object.average_height))
    detail_list_box.insert(END, "Average Lifespan:" + str(species_object.average_lifespan))
    detail_list_box.insert(END, "Eye Colors      :" + str(species_object.eye_colors))
    detail_list_box.insert(END, "Hair Colors     :" + str(species_object.hair_colors))
    detail_list_box.insert(END, "Skin Colors     :" + str(species_object.skin_colors))
    detail_list_box.insert(END, "Language        :" + str(species_object.language))
    detail_list_box.insert(END, "Homeworld      :" + search.url_name_dict[species_object.homeworld])
    for person_url in species_object.people:
        detail_list_box.insert(END, "People      :" + search.url_name_dict[person_url])
    for film_url in species_object.films:
        detail_list_box.insert(END, "Films      :" + search.url_name_dict[film_url])
    detail_list_box.insert(END, "Created         :" + str(species_object.created))


def fill_starship(starship_object):
    detail_list_box.insert(END, "Model                 : " + str(starship_object.model))
    detail_list_box.insert(END, "Class                 : " + str(starship_object.starship_class))
    detail_list_box.insert(END, "Manufacturer          : " + str(starship_object.manufacturer))
    detail_list_box.insert(END, "Cost (In Credits)     : " + str(starship_object.cost_in_credits))
    detail_list_box.insert(END, "Length                : " + str(starship_object.length))
    detail_list_box.insert(END, "Crew                  : " + str(starship_object.crew))
    detail_list_box.insert(END, "Passengers            : " + str(starship_object.passengers))
    detail_list_box.insert(END, "Max Atmosphering Speed: " + str(starship_object.max_atmosphering_speed))
    detail_list_box.insert(END, "Hyperdrive Rating     : " + str(starship_object.hyperdrive_rating))
    detail_list_box.insert(END, "MGLT                  : " + str(starship_object.MGLT))
    detail_list_box.insert(END, "Cargo Capacity        : " + str(starship_object.cargo_capacity))
    detail_list_box.insert(END, "Consumables           : " + str(starship_object.consumables))
    for film_url in starship_object.films:
        detail_list_box.insert(END, "Films      : " + search.url_name_dict[film_url])
    for person_url2 in starship_object.pilots:
        detail_list_box.insert(END, "Pilots      :" + search.url_name_dict[person_url2])
    detail_list_box.insert(END, "Created               :" + str(starship_object.created))


def fill_vehicle(vehicle_object):
    detail_list_box.insert(END, "Model                 :" + str(vehicle_object.model))
    detail_list_box.insert(END, "Class                 :" + str(vehicle_object.vehicle_class))
    detail_list_box.insert(END, "Manufacturer          :" + str(vehicle_object.manufacturer))
    detail_list_box.insert(END, "Cost (In Credits)     :" + str(vehicle_object.cost_in_credits))
    detail_list_box.insert(END, "Length                :" + str(vehicle_object.length))
    detail_list_box.insert(END, "Crew                  :" + str(vehicle_object.crew))
    detail_list_box.insert(END, "Passengers            :" + str(vehicle_object.passengers))
    detail_list_box.insert(END, "Max Atmosphering Speed:" + str(vehicle_object.max_atmosphering_speed))
    detail_list_box.insert(END, "Cargo Capacity        :" + str(vehicle_object.cargo_capacity))
    detail_list_box.insert(END, "Consumables           :" + str(vehicle_object.consumables))
    for film_url in vehicle_object.films:
        detail_list_box.insert(END, "Films      :" + search.url_name_dict[film_url])
    for person_url in vehicle_object.pilots:
        detail_list_box.insert(END, "Pilots      :" + search.url_name_dict[person_url])
    detail_list_box.insert(END, "Created               :" + str(vehicle_object.created))


def category_content_list_generator(category_string, page_count, film_bool):
    print("category_content_list_generator called. " + str(datetime.datetime.now().time()))
    full_list = []
    lead_string = "title" if film_bool else "name"
    for page_num in range(1, page_count + 1):
        r = requests.get("https://www.swapi.co/api/" + category_string + "/?page=" + str(page_num)).json()
        list_box_list = [entry[lead_string] for entry in r["results"]]
        full_list.extend(list_box_list)

        if category_string == "people":
            people_list.extend(list_box_list)
        if category_string == "films":
            film_list.extend(list_box_list)
        if category_string == "planets":
            planet_list.extend(list_box_list)
        if category_string == "species":
            species_list.extend(list_box_list)
        if category_string == "starships":
            starship_list.extend(list_box_list)
        if category_string == "vehicles":
            vehicle_list.extend(list_box_list)

    return full_list


class FilteringApp:

    def set_filter_frame(self, frame, category_num, category_string, page_count, film_bool):
        Label(frame, text=category_string.upper(), width=25, bg="black", fg="lightblue").grid(row=2*category_num+1)
        filter_value = StringVar(frame)
        filter_value.set("All")
        OptionMenu(frame, filter_value, *{"All"},
                   *category_content_list_generator(category_string, page_count, film_bool),
                   command=self.apply_filter).grid(row=2*category_num+2, sticky="ew")

    def apply_filter(self, filter_value):
        print("Filter_Value: " + str(filter_value))


def close_program():
    sys.exit()


class FilterButton:

    def buttonframe_packing(self, label_text):
        button = Button(filterbar_frame, text=label_text, width=20, bd=2, relief=RAISED, bg="black", fg="lightblue")
        if label_text == "ALL":
            button.bind("<Button>", self.apply_all_button_filter)
        if label_text == "PEOPLE":
            button.bind("<Button>", self.apply_people_button_filter)
        if label_text == "FILMS":
            button.bind("<Button>", self.apply_films_button_filter)
        if label_text == "PLANETS":
            button.bind("<Button>", self.apply_planets_button_filter)
        if label_text == "SPECIES":
            button.bind("<Button>", self.apply_species_button_filter)
        if label_text == "STARSHIPS":
            button.bind("<Button>", self.apply_starships_button_filter)
        if label_text == "VEHICLES":
            button.bind("<Button>", self.apply_vehicle_button_filter)
        return button

    def apply_all_button_filter(self, click_event):
        fill_viewable_items_list(list_box, complete_viewable_dict_of_lists["people"], complete_viewable_dict_of_lists["films"],
                                 complete_viewable_dict_of_lists["species"], complete_viewable_dict_of_lists["planets"],
                                 complete_viewable_dict_of_lists["starships"], complete_viewable_dict_of_lists["vehicles"], False)

    def apply_people_button_filter(self, click_event):
        fill_viewable_items_list(list_box, complete_viewable_dict_of_lists["people"], [], [], [], [], [], False)

    def apply_films_button_filter(self, click_event):
        fill_viewable_items_list(list_box, [], complete_viewable_dict_of_lists["films"], [], [], [], [], False)

    def apply_planets_button_filter(self, click_event):
        fill_viewable_items_list(list_box, [], [], complete_viewable_dict_of_lists["planets"], [], [], [], False)

    def apply_species_button_filter(self, click_event):
        fill_viewable_items_list(list_box, [], [], [], complete_viewable_dict_of_lists["species"], [], [], False)

    def apply_starships_button_filter(self, click_event):
        fill_viewable_items_list(list_box, [], [], [], [], complete_viewable_dict_of_lists["starships"], [], False)

    def apply_vehicle_button_filter(self, click_event):
        fill_viewable_items_list(list_box, [], [], [], [], [], complete_viewable_dict_of_lists["vehicles"], False)

# filter people
root = Tk()
root.title("Star Search")

# Add menu bar
ObjectClasses_menu = Menu(root)
root.config(menu=ObjectClasses_menu)
file_menu = Menu(ObjectClasses_menu)
ObjectClasses_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Quit", command=close_program)

# Create frames
invisible_frame = Frame(root)
filterbar_frame = Frame(root, bg="black")
list_box_frame = Frame(root)
rightmost_frame = Frame(root)
searchfield_frame = Frame(rightmost_frame)
picture_frame = Frame(rightmost_frame)
details_frame = Frame(rightmost_frame)


detail_label_string = StringVar(details_frame)
detail_label_string.set("Details")

# Add status bar
status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)  # bd stands for bordered
status.pack(side=BOTTOM, fill=X)

# Add header
header_label = Label(root, text="In a galaxy far far away...", font=250, bg="black", fg="lightblue")
header_label.pack(side=TOP, fill=X)

# Fill Frames
# ** Begin filterbar_frame **
# Label(filterbar_frame, text="ITEM FILTER", font="bold", width=25, bd=4, relief=RIDGE, bg="black",
#       fg="lightblue").grid(row=0)
filter_app = FilteringApp()
filter_app.set_filter_frame(invisible_frame, 0, "films", 1, True)
filter_app.set_filter_frame(invisible_frame, 1, "people", 9, False)
filter_app.set_filter_frame(invisible_frame, 2, "planets", 5, False)
filter_app.set_filter_frame(invisible_frame, 3, "species", 4, False)
filter_app.set_filter_frame(invisible_frame, 4, "starships", 4, False)
filter_app.set_filter_frame(invisible_frame, 5, "vehicles", 4, False)

top_spacer_label = Label(filterbar_frame, width=25, height=14, bg="black").grid(row=0)

Label(filterbar_frame, text="CATEGORY FILTERS", font="bold", width=20, bd=4, relief=RIDGE, bg="black",
      fg="lightblue").grid(row=1)
button_app = FilterButton()
button_app.buttonframe_packing("ALL").grid(row=2)
button_app.buttonframe_packing("PEOPLE").grid(row=3)
button_app.buttonframe_packing("FILMS").grid(row=4)
button_app.buttonframe_packing("PLANETS").grid(row=5)
button_app.buttonframe_packing("SPECIES").grid(row=6)
button_app.buttonframe_packing("STARSHIPS").grid(row=7)
button_app.buttonframe_packing("VEHICLES").grid(row=8)

bottom_spacer_label = Label(filterbar_frame, width=25, height=24, bg="black").grid(row=9)
# ** End filterbar_frame **

# ** list_box_frame **
Label(list_box_frame, text="VIEWABLE ITEMS", font="bold", bd=4, relief=RIDGE, width=25, bg="black", fg="lightblue").pack()
list_box = Listbox(list_box_frame, selectmode="single", height=50, width=31, bd=5, relief=RIDGE, bg="black",
                   fg="lightblue")
fill_viewable_items_list(list_box, people_list, film_list, planet_list, species_list, starship_list, vehicle_list, True)
list_box.bind("<<ListboxSelect>>", viewlist_on_select)
list_box.pack()
# ** end list_box_frame **

# ** Begin rightmost_frame **
# ** Pic **
pic_1 = PhotoImage(file="/home/kfiler/PycharmProjects/StarSearch/PNGs/luke-skywalker-force-awakens.png")
Label(picture_frame, image=pic_1, height=424, width=424, bd=4,relief=RIDGE).pack()
# ** End Pic **
# ** Detail **
Label(details_frame, textvariable=detail_label_string, font="bold", bd=4, relief=RIDGE, width=45, bg="black", fg="lightblue").pack()
detail_list_box = Listbox(details_frame, font="DejaVu", height=15, width=45, bd=4, relief=RIDGE, bg="black", fg="white")
detail_list_box.pack()
# ** End Detail **
# ** End rightmost_frame **

# Pack Frames
filterbar_frame.pack(side=LEFT)
list_box_frame.pack(side=LEFT)
picture_frame.pack()
details_frame.pack()
rightmost_frame.pack(side=LEFT)

root.mainloop()