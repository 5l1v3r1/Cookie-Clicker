# Cookie-Clicker
Computer Science Principles sem 1 final exam project

Structure of the progam:

Cookie_clicker.py is the main project where the main function is run. The cookie_clicker_GUI.py file holds the classes we need to make the GUI run on the program. There are two classes stored in there...

1. UpgradesController 

UpgradesController helps us keep track of all of the upgrades that the player has bought in the menu, evertime the button is pressed, the command argument calls the specified function and it runs. Every function that is an upgrade function is denoted with the title of the upgrade (ex: auto_click). In those functions, another variable is changed, these variables hold the number of times that the upgrade has been clicked, changing the effect of the number of cookies. These special variables are stored in the classs UpgradesController. They are first initialzed with the __init__ method so that existing user data from the .dat file can be parsed and the variables can be changed accordingly to the number of upgrades that the user had from previous sessions. All of these variables can be found with the name of the upgrade followed by _upgrade (ex auto_click_upgrade)


2. CookieClickerMainGUI

This class is the main GUI component to the program, it is the main tkinter GUI and holds all of the widgets, and the functions that those widgets control. 



Known Issues so far:

1. The time.sleep() function does not work in tkinter, there has to be another way to figure out time in the auto-click loop
