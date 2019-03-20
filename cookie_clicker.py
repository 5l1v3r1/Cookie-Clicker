#coded by sc1341
import os
import pickle
from getpass import getuser
import subprocess
from cookie_clicker_GUI import CookieClickerMainGUI
from tkinter import *
from cookie_clicker_GUI import UpgradesController

#global variable
global path

#default is windows, changed if ! win
path = 'C://Users/{}/Desktop/'.format(getuser())

def import_data():
    '''Trys to import existing data from the folder, if not, create it with
    create_dat_file function'''
    data = ''
    win = False
    mac = False
    
    try:
        os.chdir("C://Users/{}/Desktop/cookie_clicker".format(getuser()))
        path = "C://Users/{}/Desktop/cookie_clicker".format(getuser())
        win = True
    except:
        try:
            os.chdir("/users/{}/Desktop/cookie_clicker".format(getuser()))
            path = "/users/{}/Desktop/cookie_clicker".format(getuser())
            mac = True
        except:
            print("Fatal error")
    
    if mac:    
        files = subprocess.check_output(['ls'])
        files = files.decode()
        files = files.split("\n")

    elif win:
        try:
            files = subprocess.check_output(['dir'])
            files = files.decode()
            files = files.split("\n")
        except:
            files = []
    else:
        pass

    #There is no way that this works
    for file in files:
        if str(file) in "cookie.dat":
            try:
                print("Data dump found")
                f = open(path + '/' + 'cookie.dat','rb')
                data = pickle.load(f)
                f.close()
                break
            except:
                create_dat_file()
                break

    return data


class FileManager:

    def __init__(self):
        self.path = os.cwd()
        self.win = False
        self.mac = False


    def create_dat_file(self):
        '''Creates the dat file on the machine'''
        pass

    def find_dat_file(self):
        '''Finds the dat file on the machine and reads the data from it, it return the data in a dictionary format?'''
        pass

def create_dat_file():
    '''Creates the dat file for exporting and importing'''
    try:
        f = open(path + '/' + 'cookie.dat', 'wb')
        f.close()
    except:
        pass
      

def change_directory_cookie_folder():
    '''works on mac and windows, changes the directory to the cookie folder, if dir does not exist
    it creates it, it supports the file structures of mac and windows'''
    try:
        os.chdir("C://Users/{}/Desktop/cookie_clicker".format(getuser()))
    except:
        try:
            os.mkdir("C://Users/{}/Desktop/cookie_clicker".format(getuser()))
        except:
            try:
                os.mkdir("/users/{}/Desktop/cookie_clicker".format(getuser()))
            except:
                os.chdir("/users/{}/Desktop/cookie_clicker".format(getuser()))

def main():
    change_directory_cookie_folder()
    data = import_data()
    root = Tk()
    GUI = CookieClickerMainGUI(root, data)
    root.mainloop()


if __name__ == '__main__':
    main()

