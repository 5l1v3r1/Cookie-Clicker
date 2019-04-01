# coded by sc1341
import os
import pickle
from getpass import getuser
import logging
from cookie_clicker_GUI import CookieClickerMainGUI



class FileManager:

    def __init__(self):
        self.path = "C://Users/" + getuser() + "/Desktop"
        os.chdir("C://Users/" + getuser() + "/Desktop")
        logging.basicConfig(filename="cookielogs.log", level=logging.INFO)

    def create_dat_file(self):
        '''Creates the dat file on the machine, this function also assumes that the folder already exists'''
        try:
            f = open(self.path + "/cookie_clicker" + "cookie.dat", "wb")
            f.close()
            logging.info("Creating file inside of existing cookie folder")
        except FileNotFoundError:
            os.mkdir(self.path + "/cookie_clicker")
            logging.info("Created folder")

    def make_directory(self):
        """Makes the folder, this is a seperate function because it is called only when the file and the
        folder both do not exist"""
        os.mkdir(self.path + "/cookie_clicker")
        os.chdir(self.path + "/cookie_clicker")

    def import_data(self):
        '''Imports the data from the existing dat file on the folder on the desktop'''
        logging.info("Locating data")
        try:
            os.chdir(self.path + "/cookie_clicker")
            try:
                with open("cookie.dat", "rb") as f:
                    #Errors here???
                    data = pickle.load(f)
                return data
            except FileNotFoundError:
                logging.info("Folder exists, but the file was not found")
                self.create_dat_file()
                return ''
        except FileNotFoundError:
            logging.info("Folder and dat file does not exist... creating folder and file")
            self.make_directory()
            self.create_dat_file()
            return ''



def main():
    fileman = FileManager()
    GUI = CookieClickerMainGUI(fileman.import_data())


if __name__ == '__main__':
    main()
