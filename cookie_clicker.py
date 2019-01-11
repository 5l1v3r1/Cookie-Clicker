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
global path
path = ''
username = getuser()


def import_data():
    '''Trys to import existing data from the folder, if not, create it with
    create_dat_file function'''
    data = ''
    win = False
    mac = False
    
    try:
        os.chdir("C://Users/{}/Desktop/cookie_clicked".format(username))
        path = "C://Users/{}/Desktop/cookie_clicked".format(username)
        win = True
    except:
        try:
            os.chdir("/users/{}/Desktop/cookie_clicked".format(username))
            path = "/users/{}/Desktop/cookie_clicked".format(username)
            mac = True
        except:
            print("Fatal error")
    
    if mac:    
        files = subprocess.check_output(['ls'])
    elif win:
        files = subprocess.check_output(['dir'])
        
    else:
        pass

    for file in files:
        if str(file) in "cookie.dat":
            print("Data dump found")
            with open(path + '/' + 'cookie.dat','rb') as f:
                data = pickle.load(f)
                f.close()
                break #This break is important here
        else:
            create_dat_file()
            break

    return data


def create_dat_file():
    '''Creates the dat file for exporting and importing'''
    try:
        f = open(path + '/' + 'cookie.dat','wb')
        f.close()
        print("file created")
    except:
        pass
      

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
            except:
                os.chdir("/users/{}/Desktop/cookie_clicked".format(username))
                

def main():
    change_directory_cookie_folder()
    data = import_data()
    root = Tk()
    GUI = CookieClickerMainGUI(root, data)
    root.mainloop()


if __name__ == '__main__':
    main()

