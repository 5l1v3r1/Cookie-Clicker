# Cookie-Clicker
Computer Science Principles sem 1 final exam project

Structure of the progam:

Cookie_clicker.py is the main project where the main function is run. The cookie_clicker_GUI.py file holds the classes we need to make the GUI run on the program. There are two classes stored in there...

1. UpgradesController 

UpgradesController helps us keep track of all of the upgrades that the player has bought in the menu, evertime the button is pressed, the command argument calls the specified function and it runs. Every function that is an upgrade function is denoted with the title of the upgrade (ex: auto_click). In those functions, another variable is changed, these variables hold the number of times that the upgrade has been clicked, changing the effect of the number of cookies. These special variables are stored in the classs UpgradesController. They are first initialzed with the __init__ method so that existing user data from the .dat file can be parsed and the variables can be changed accordingly to the number of upgrades that the user had from previous sessions. All of these variables can be found with the name of the upgrade followed by _upgrade (ex auto_click_upgrade)



2. CookieClickerMainGUI

This class is the main GUI component to the program, it is the main tkinter GUI and holds all of the widgets, and the functions that those widgets control.


Methods of CookieClickerMainGUI:

export_data - exports the data to the dat file when the save button is clicked

cookie_clicked - when the big cookie is clicked, this funciton adds to the score

upgrades_GUI_menu - shows the upgrade menu screen to purchase upgrades

UPGRADE FUNCTIONS ------------

Upgrade functions: these are the funcitons that run when an upgrade is purchased, some of these funcitons run other functions that open threads to add to the score

cookies_per_click - adds the number of cookies added to the score per click by the user

auto_click - This opens a thread in the auto_click_thread_run function that auto-adds to the score when purchaed, this can be bought multiple times, each time it is bought a new thread is opened

random_bonus - this opens a thread in the random_bonus_thread_run funciton, the user has a random chance to get a thousand cookies every second, the user has a 1% chance per thread

no_negative - this displays a message to the user that they are in cookie debt when the score reaches below -1000

------------------------------------------------------------


Known Issues so far:

:-)


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

time - allows the threads to sleep and not crash python

threading - allows us to create multiple threads in the program per upgrade

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

Current issues:


have to add more upgrades

make it prettier?

dark mode?








