# Cookie-Clicker
Computer Science Principles sem 1 final exam project

Structure of the progam:

Cookie_clicker.py is the main project where the main function is run. The cookie_clicker_GUI.py file holds the classes we need to make the GUI run on the program. There are two classes stored in there...

1. UpgradesController 

UpgradesController helps us keep track of all of the upgrades that the player has bought in the menu, evertime the button is pressed, the command argument calls the specified function and it runs. Every function that is an upgrade function is denoted with the title of the upgrade (ex: auto_click). In those functions, another variable is changed, these variables hold the number of times that the upgrade has been clicked, changing the effect of the number of cookies. These special variables are stored in the classs UpgradesController. They are first initialzed with the __init__ method so that existing user data from the .dat file can be parsed and the variables can be changed accordingly to the number of upgrades that the user had from previous sessions. All of these variables can be found with the name of the upgrade followed by _upgrade (ex auto_click_upgrade)



2. CookieClickerMainGUI

This class is the main GUI component to the program, it is the main tkinter GUI and holds all of the widgets, and the functions that those widgets control.


Methods of CookieClickerMainGUI:


check_import_data	

cookie_clicked

upgrades_GUI_menu

cookies_per_click

auto_click

------------------------------------------------------------


Known Issues so far:

1. The time.sleep() function does not work in tkinter, there has to be another way to figure out time in the auto-click loop


------------------------------------------------------------

Modules Used:

tkinter: GUI Module

os: chdir and mkdir to change directories to the cookie folder that is created

pickle: Exports and imports data from the .dat file

getpass: Gets the username of the current user on the computer so it can be formatted into a string used to change or create directories (ex: C://Users/str(getpass.getuser())/Desktop/)

subprocess: Allows us to use the "ls" command to search for the .dat file by bringing in the data we get back as a list to iterate through

from cookie_clicker_GUI import CookieClickerMainGUI: Main GUI class

from cookie_clicker_GUI import UpgradesController: UpgradesController class (see definition/purpose)

from image import image: Base64 encoded image of the cookie (easier to work with in the PhotoImage method, also no extentions)

------------------------------------------------------------

Functions of cookie_clicker.py:

import_data

create_dat_file

export_data

change_directory_cookie_folder

main

--------------------------------------------------------------

Steps to adding an upgrade feature to the program:

1. Create the upgrade variable in the UpgradeController class and format it as the other ones are

2. Add the variable to be exported in the export data dictoinary

3. Add a line in the if statment when the data is imported so the data will be updated if data exists

4. Create a button for the upgrade option

5. Create a function that takes an effect on the score of the game


--------------------------------------------------------------

Current problems:

the cookies will not import at all

the auto click has to go

have to add more upgrades

it overall kinda sucks

make it prettier?









