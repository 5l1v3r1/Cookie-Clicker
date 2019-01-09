from tkinter import *
import os #make the folder
import pickle #save the data 
import getpass #gets the username from the computer
import subprocess
import sys
from cookie_clicker_GUI import CookieClickerMainGUI
from image import image

python_file_name = sys.argv[0]

#global variables
global username  #gets the username for changing directories
username = getpass.getuser()


'''
Order things must be run in:

1. change_directory_cookie_folder()
2. import_data()
3. Create object and run __init__
4.class takes over with all of the funcitons regarding the actual game, export has to be inside class?? check this

INFO: 

The CookieClickerGUI is the class that runs the GUI, it takes two arguments, the root tk() class (which we 
defined as root) and the data
, the data comes from the import_data function where it takes all data and changes the score if the data is present, if 
not, then the score sets to zero. This program MUST be run on the desktop at the moment

NOTES TO SELF:

the pack () function can take an arg but it throws an error, you have to tell the widget itself where it should go


'''


def import_data():
    '''Trys to import existing data from the folder, if not, create it with
    create_dat_file function'''
    data = ''
    try:
        os.chdir("C://Users/{}/Desktop/cookie_clicked".format(username))
    except FileNotFoundError:
        try:
            os.chdir("/users/{}/Desktop/cookie_clicked".format(username))
        except:
            print("Fatal error")
    try:
        files = subprocess.check_output(['ls'])
        for file in files:
            if file == "cookie.dat":
                print("Data dump found")
                with open('cookie.dat') as f:
                    data = pickle.load(f)
                    f.close()
            else:
                create_dat_file()
    except:
        pass
    return data


def create_dat_file():
    '''Creates the dat file for exporting and importing'''
    f = open('cookie.dat','wb')
    f.close()
    print("file created")
    

def export_data(data):
    '''Make this happen every minute or something'''
    pass
    

    
def change_directory_cookie_folder():
    '''works on mac and windows, changes the directory to the cookie folder, if dir does not exist
    it creates it, it supports the file structures of mac and windows'''
    try:
        os.chdir("C://Users/{}/Desktop/cookie_clicked".format(username))
    except FileNotFoundError:
        try:
            os.mkdir("C://Users/{}/Desktop/cookie_clicked".format(username))
        except FileNotFoundError:
            try:
                os.mkdir("/users/{}/Desktop/cookie_clicked".format(username))
            except FileExistsError:
                os.chdir("/users/{}/Desktop/cookie_clicked".format(username))
        
    
def main():
    change_directory_cookie_folder()
    data = import_data()
    root = Tk()
    window = CookieClickerMainGUI(root, data)
    root.mainloop()


def test_cases():
    print(score)
    print(username)
    print(str(os.getcwd()))


if __name__ == '__main__':
    main()
    test_cases()
