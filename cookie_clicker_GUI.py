from tkinter import *
from image import image as cookieimage
import time
import pickle
import random
import threading

class UpgradesController:

    def __init__(self, data): 
        if data != '':
            self.score = int(data["score"])
            self.auto_click_upgrade = int(data["auto_click_upgrade"])
            self.cookies_per_click_upgrade = int(data["cookies_per_click_upgrade"])
        else:
            self.score = 0        
            self.auto_click_upgrade = 0
            #All upgrades have to be 1 by default, tis is due to the logic of the game using the upgrade number to determine the cost
            self.cookies_per_click_upgrade = 1


class CookieClickerMainGUI:

    def __init__(self, root, data=''):

        self.upgrade_controller = UpgradesController(data)
        root.geometry("700x700")
        root.title("Cookie Clicker")
        self.photo = PhotoImage(data=cookieimage)
        
        #Inits the score for the game, will change if .dat file exists
        self.data = data
        self.score = self.upgrade_controller.score

        #inital GUI components
        self.label = Label(root,text="Welcome to Cookie Clicker",font=("Helvetica", 16))
        self.cookie_button = Button(root,text="click me!", command=self.cookie_clicked, image=self.photo)
        self.upgrades_button = Button(root,text="Upgrades",command=self.upgrades_GUI_menu)
        self.save_button = Button(root,text="Save data",command=self.export_data)
        self.score_label = Label(root,text=str(self.score),font=("Helvetica", 20))
        self.cookie_debt_label = Label(root,text="You are in cookie debt",font=("Helvetica", 20))

        #pack the widgets inside the screen
        self.score_label.pack()
        self.label.pack()
        self.cookie_button.pack()
        self.upgrades_button.pack()
        self.save_button.pack()
        
        
    def export_data(self):
        '''Exports the data into a dictionary into the dat file that was created from the cookie_clicker.py file'''
        
        export_data = {"score":self.score,"auto_click_upgrade":self.upgrade_controller.auto_click_upgrade,
        "cookies_per_click_upgrade":self.upgrade_controller.cookies_per_click_upgrade}
        
        with open('cookie.dat','wb') as f:
            pickle.dump(export_data,f)
        f.close()


    def cookie_clicked(self):
        '''Adds to the score when the cookie button is clicked, it then updates the label... the defualt it 
        the label updates ever 200 milliseconds, do not change this!'''
        self.score += self.upgrade_controller.cookies_per_click_upgrade
        self.score_label.config(text=str(self.score))
        print("Button clicked: the score is: " + str(self.score))



    # ----------------------- MENU WINDOWS --------------------------------------------

    def upgrades_GUI_menu(self):
        '''This creates a pop-up window to modify your upgrades, it is easy to add more buttons/upgrades from here'''
        self.root2 = Tk()
        self.root2.geometry("500x300")
        self.root2.title("Upgrades Menu")
        self.auto_click_button = Button(self.root2, text="Buy Auto-click: $" + str(100 * self.upgrade_controller.auto_click_upgrade), command=self.auto_click)
        self.cookies_per_click_button = Button(self.root2, text="Buy more cookies per click: $" + str(20 * self.upgrade_controller.cookies_per_click_upgrade,
        command=self.cookies_per_click))
        
        self.random_bonus_button = Button(self.root2, text="Random Bonus",command=self.random_bonus)
        #Pack the buttons
        self.cookies_per_click_button.pack()
        self.auto_click_button.pack()
        self.root2.mainloop()

    # ----------------------- UPGRADE FUNCTIONS --------------------------------------------

    def cookies_per_click(self):
        '''The number of cookies per click'''
        self.score -= 20 * self.upgrade_controller.cookies_per_click_upgrade + 20
        self.upgrade_controller.cookies_per_click_upgrade += 1
        self.score_label.config(text=str(self.score))

    def auto_click(self):
        '''Sets the autoclick to run, it subtracts the score by 100 times the number of upgrades that the auto_click 
        has, it then sets the updatecontroller.auto_click_upgrade += 1'''
        self.score -= 100 * self.upgrade_controller.auto_click_upgrade
        self.upgrade_controller.auto_click_upgrade += 1
        self.score_label.config(text=str(self.score))
        t1 = threading.Thread(target=self.auto_click_thread_run)
        #Possibly open a thread here?
        '''
        while True:
            #THis is a known issue that causes the program to freeze than crash, concider time.time?
            time1 = time.time()
            if (sum(time1) + 1) == time.time():    
                self.score += 1 '''
    def random_bonus(self):
        '''Random bonus of 1000 cookies, it can only be purchased once'''
        self.random_bonus_button.pack_forget()
        while True:
            if 10 == random.randint(1,100):
                self.score += 1000
            
            
    def no_negative(self):
        while True:
            if self.score < -1000:
                print("You are in cookie debt")
                self.cookie_debt_label.pack()
            else:
                pass
    def auto_click_thread_run(self):
        pass
                
    
'''
Added mac and windows feature so the file check works
Updated docs
Removed import_data form the GUI class, it is messy and dumb to do it that way, the data must be parsed before even entering the object
Removed calloing the export function from the cookie_clicked function because it slows down the program noticlbly to call revusive function in tkinter
Do not need line 10 in cookie_clicker
Do not need sys module at the moment in cookie_clicker or the GUI

Problems:
    the dat file is not creating WTF is happening there?
    
    
Can we open a sleeper thread that takes a perameter? 

options:
    thread that uses how many times it was bought to increase price and abilities
    
    sleeper thread to run the function normally
    
    

'''
