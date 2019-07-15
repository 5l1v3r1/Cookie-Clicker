# Cookie-Clicker
Computer Science Principles sem 1 final exam project

(The Readme has not been updated to the most reccent code)

Structure of the program:

Cookie_clicker.py is the main project where the main function is run. The cookie_clicker_GUI.py file holds the classes we need to make the GUI run on the program. There are two classes stored in there...

1. UpgradesController

UpgradesController helps us keep track of all of the upgrades that the player has bought in the menu, every time the button is pressed, the command argument calls the specified function and it runs. Every function that is an upgrade function is denoted with the title of the upgrade (ex: auto_click). In those functions, another variable is changed, these variables hold the number of times that the upgrade has been clicked, changing the effect of the number of cookies. These special variables are stored in the class UpgradesController. They are first initialized with the __init__ method so that existing user data from the .dat file can be parsed and the variables can be changed accordingly to the number of upgrades that the user had from previous sessions. All of these variables can be found with the name of the upgrade followed by _upgrade (ex auto_click_upgrade)

2. CookieClickerMainGUI

This class is the main GUI component to the program, it is the main tkinter GUI and holds all of the widgets, and the functions that those widgets control.


Methods of CookieClickerMainGUI:

export_data - exports the data to the dat file when the save button is clicked

cookie_clicked - when the big cookie is clicked, this function adds to the score

upgrades_GUI_menu - shows the upgrade menu screen to purchase upgrades

UPGRADE FUNCTIONS ------------

Upgrade functions: these are the functions that run when an upgrade is purchased, some of these functions run other functions that open threads to add to the score

cookies_per_click - adds the number of cookies added to the score per click by the user

auto_click - This opens a thread in the auto_click_thread_run function that auto-adds to the score when purchased, this can be bought multiple times, each time it is bought a new thread is opened

random_bonus - this opens a thread in the random_bonus_thread_run function, the user has a random chance to get a thousand cookies every second, the user has a 1% chance per thread

no_negative - this displays a message to the user that they are in cookie debt when the score reaches below -1000



------------------------------------------------------------

Modules Used:

tkinter: GUI Module, the entire tkinter library is not imported because we don't need all of it...

os: chdir and mkdir to change directories to the cookie folder that is created

pickle: Exports and imports data from the .dat file

getpass.getuser() -- Gets the username of the user on the computer so that the program can move around the directory structure easily

from cookie_clicker_GUI import CookieClickerMainGUI: Main GUI class

from cookie_clicker_GUI import UpgradesController: UpgradesController class (see definition/purpose)

from image import image: Base64 encoded image of the cookie (easier to work with in the PhotoImage method, also no extentions)

time - allows the threads to sleep and not crash python

threading - allows us to create multiple threads in the program per upgrade

------------------------------------------------------------

Classes of Cookieclicker.py


class Filemanager
Methods:
1. __init__ -- Sets a few of the variables and changes the wd to Desktop
2. create_dat_file -- Creates the dat file inside of the folder so that game data can be saved
3. make_directory -- Makes the folder on the desktop that holds the cookie_clicker.dat file
4. import_data -- Gets the data from the cookie.dat file




--------------------------------------------------------------

Current issues:

Add easter egg


Write better Doc Strings

Customization

Figure out how to close all of the threads running on the machine..

.join()? ._Thread_stop()?
Idk how to fix this rn




# To do:
Finish Customizaiton Screen
Current issue list
Write better doc Strings
Choose what algorithm that you want to showcase for the final
