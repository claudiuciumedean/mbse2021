# MBSE2021

## How to run the simulation?
* Run the Simulation_Manager.py file using your favorite Python editor or the command line. If you get some build erros, make sure you have all the required Python packages installed.


## Simulator operation
The simulator is organized into three main parts:
* The Simulation_Manager.py file, which is the main file and orchestrates the whole simulation
* The Simulation_Constants.py file, which includes the complete parameter list of the simulator;
* The components files World.py, Coordinates.py, Area.py, Person.py, Wearable.py, implementing the system's components.

When the Simulation_Manager.py is executed, the simulation starts. The 2D world with the moving people is generated and kept updated throughout the entire run, while the bottom plot keeps track of how many people are healthy, infected, recovered or dead. Moreover, the logged data are printed on the output terminal, and at the same time written in the CSV file. The simulation terminates when the script is manually stopped or when the number of simulated days reaches its predetermined value.
