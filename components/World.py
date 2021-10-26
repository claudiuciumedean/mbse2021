import tkinter as tk
import components.Area as Area

from Simulation_Constants import Simulation_Constants

class World:  
    def __init__(self, persons):
        self.frame_size_x = Simulation_Constants.WORLD_SIZE
        self.frame_size_y = Simulation_Constants.WORLD_SIZE
        self.persons = persons

        #self.area_size_x = Simulation_Constants.AREA_SIZE
        #self.area_size_y = Simulation_Constants.AREA_SIZE
        #self.state = Area.AreaStates.GREEN
        #self.create_areas(self.area_size_x, self.area_size_y, self.state)

    def live(self):
        for person in self.persons:
            person.walk()
            person.wearable.get_close_persons(self.persons)

    def create_areas(self, area_size_x, area_size_y, state):
        self.area_size_x = area_size_x
        self.area_size_y = area_size_y
        self.state = state

        self.areas = []
        for i in range(6):
            self.areas.append(i)

        print(self.areas)
        print(self.state)

    def changeColor(self):
        self.state = Area.area_states
























'''     
def main():  # Main method to run gui
    gui = tk.Tk()
    World(gui, "Corona spreading sumulation", "1000x600")
    gui.mainloop()
    return None
    
    
class World:  # instance attributes of world upon initialisation
    def __init__(self, gui, title, geometry):


        self.gui = gui
        self.gui.title(title)
        self.gui.geometry(geometry)

        self.area1 = tk.Frame(master=self.gui, width=200, height=200, highlightbackground="red",
                              highlightcolor="red",
                              highlightthickness=5)
        self.label1 = tk.Label(master=self.area1, text="Area 1")
        self.label1.place(relx=0.5, rely=0.5, anchor='center')
        self.area1.place(x=0, y=0)

        self.area2 = tk.Frame(master=self.gui, width=200, height=200, highlightbackground="green",
                              highlightcolor="green",
                              highlightthickness=5)
        self.label2 = tk.Label(master=self.area2, text="Area 2")
        self.label2.place(relx=0.5, rely=0.5, anchor='center')
        self.area2.place(x=0, y=400)

        self.area3 = tk.Frame(master=self.gui, width=200, height=200, highlightbackground="green",
                              highlightcolor="green",
                              highlightthickness=5)
        self.label3 = tk.Label(master=self.area3, text="Area 3")
        self.label3.place(relx=0.5, rely=0.5, anchor='center')
        self.area3.place(x=400, y=0)

        self.area4 = tk.Frame(master=self.gui, width=200, height=200, highlightbackground="red",
                              highlightcolor="red",
                              highlightthickness=5)
        self.label4 = tk.Label(master=self.area4, text="Area 4")
        self.label4.place(relx=0.5, rely=0.5, anchor='center')
        self.area4.place(x=400, y=400)

        self.area5 = tk.Frame(master=self.gui, width=200, height=200, highlightbackground="red",
                              highlightcolor="red",
                              highlightthickness=5)
        self.label5 = tk.Label(master=self.area5, text="Area 5")
        self.label5.place(relx=0.5, rely=0.5, anchor='center')
        self.area5.place(x=800, y=0)

        self.area6 = tk.Frame(master=self.gui, width=200, height=200, highlightbackground="orange",
                              highlightcolor="orange",
                              highlightthickness=5)
        self.label6 = tk.Label(master=self.area6, text="Area 6")
        self.label6.place(relx=0.5, rely=0.5, anchor='center')
        self.area6.place(x=800, y=400)


main()
'''