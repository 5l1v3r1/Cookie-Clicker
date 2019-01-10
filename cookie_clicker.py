#coded by sc1341
from tkinter import *
import os #make the folder
import pickle #save the data 
from getpass import getuser #gets the username from the computer
import subprocess
from cookie_clicker_GUI import CookieClickerMainGUI
from cookie_clicker_GUI import UpgradesController
#from image import image

#global variables
global username  #gets the username for changing directories
username = getuser()
'''

INFO: 

The CookieClickerGUI is the class that runs the GUI, it takes two arguments, the root tk() class (which we 
defined as root) and the data
, the data comes from the import_data function where it takes all data and changes the score if the data is present, if 
not, then the score sets to zero. This program MUST be run on the desktop at the moment

NOTES TO SELF:

the pack () function can take an arg but it throws an error, you have to tell the widget itself where it should go



QUESTIONS:
What type of data structure should hold the information regarding that upgrades are enabled?
THe logic should be done in a way where it does not have to be calculated every single time, rather it should
hold how much the cookie should go up every time... I also want to log what upgrades are enabled and pickle it
out to the dat file when we are done with the game... then when the data gets pickled back in we can use a 
standardized format such as a list, to bring the data back into the game, also make sure to write all of this data
in a binary format so the user wont be able to tell what is going on so they canot cheat. 


Upgrades we want in the program:

Autoclick

Random + 100 cookies (update the small label at the bottom)

'''

def import_data():
    '''Trys to import existing data from the folder, if not, create it with
    create_dat_file function'''
    data = ''
    win = False
    mac = False
    
    try:
        os.chdir("C://Users/{}/Desktop/cookie_clicked".format(username))
        win = True
    except:
        try:
            os.chdir("/users/{}/Desktop/cookie_clicked".format(username))
            mac = True
        except:
            print("Fatal error")
    try:
        if mac:    
            files = subprocess.check_output(['ls'])
        else:
            files = subprocess.check_output(['dir'])
        for file in files:
            if file == "cookie.dat":
                print("Data dump found")
                with open('cookie.dat') as f:
                    data = pickle.load(f)
                    f.close()
                    break
            else:
                create_dat_file()
                break
    except:
        pass
    return data


def create_dat_file():
    '''Creates the dat file for exporting and importing'''
    f = open('cookie.dat','wb')
    f.close()
    print("file created")
      

def change_directory_cookie_folder():
    '''works on mac and windows, changes the directory to the cookie folder, if dir does not exist
    it creates it, it supports the file structures of mac and windows'''
    try:
        os.chdir("C://Users/{}/Desktop/cookie_clicked".format(username))
    except:
        try:
            os.mkdir("C://Users/{}/Desktop/cookie_clicked".format(username))
        except:
            try:
                os.mkdir("/users/{}/Desktop/cookie_clicked".format(username))
            except FileExistsError:
                os.chdir("/users/{}/Desktop/cookie_clicked".format(username))
                
                
def check_import_data(data):
    '''This checks the data if there was any and updates to the previous SESSION, else it does nothing this is
    run once in the __init__ method, data is from the .dat file when the class object is created, this also formats the data 
    that comes in from  the file and changes the variables that it needs to'''
    
    #escape clause if there is no data, this works because the class does nothing and sets score to zero if ! data
    if data == '':
        pass
    else:
        score = int(data["score"])
        GUIObject.upgrade_controller.auto_click_upgrade = int(data["auto_click_upgrade"])
        GUIObject.upgrade_controller.cookies_per_click_upgrade = int(data["cookies_per_click_upgrade"])
        parsed_data = None
    return parsed_data
    
def main():
    change_directory_cookie_folder()
    data = import_data()
    parsed_data = check_import_data(data)
    root = Tk()
    window = CookieClickerMainGUI(root, parsed_data)
    root.mainloop()


if __name__ == '__main__':
    main()
    ''' Psudo code here, not good ot use this aftre the dunder main function but idk we will see what happens
    while True:
        time.wait(60)
        window.export_data()'''
