# Rocket Simulator 🚀

A Python-based script which uses object-oriented programming to allow the user to create custom rockets and simulate their flight. The ignition of engines can be simulated, and the DeltaV, height, etc. can be seen by the user. (Maybe on a GUI in the future?)

## Technologies 🕹️

* `Python`

## Features ✨

* Users can build custom rockets by giving the script the total mass of the rocket, the mass of the rocket's fuel, the engine's ISP, and the engine's burn time.
* Can calculate the DeltaV of a rocket based off of user-inputs.
* On engine ignition, the different details of the rocket and it's flight are show in the terminal (soon a GUI).
* Air drag and gravity decay are accounted for, making the simulation extremely realistic.

## The Process 🗺️

Going into this, I did not intend to fully flesh out the project. Rather, I wanted to start working with and learning object-oriented programming to bring my programming skills to the next level. I chose specifically to make rocketships the focus of my program because they are an interest of mine. This, however, would force me to learn basic rocket science to actually develop the program. Over time, the project went from simply calculating the DeltaV of a rocket to actually calculating the rocket's flight from engine ignition to burnout. The complexity of the project would require me to apply information I already knew, and learn new information. Though it's still a work in progress, I am very happy with how it turned out so far.

## How to Run the Project 💻

1. Clone the repository.
2. Open main.py.
3. Modify the parameters of the "Rocket()" class in a text editor of your choosing. The rocket parameters are total mass, fuel mass, engine's ISP in seconds, the engine's burn time, drag coefficient, and cross-sectional area.
	* For the drag coefficient, use a number between 0.2-0.3 for long, slender, and smooth rockets. For shorter, more blunt rockets, use a number between 0.5-0.7.
    * The cross-sectional area is the are of the front of the rocket.
5. Run main.py in the terminal.