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
            self.random_bonus_upgrade = 0


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

    # ----------------------- EXPORT DATA --------------------------------------------
        
        
    def export_data(self):
        '''Exports the data into a dictionary into the dat file that was created from the cookie_clicker.py file'''
        
        export_data = {"score":self.score,"auto_click_upgrade":self.upgrade_controller.auto_click_upgrade,
        "cookies_per_click_upgrade":self.upgrade_controller.cookies_per_click_upgrade}
        
        with open('cookie.dat','wb') as f:
            pickle.dump(export_data,f)
        f.close()
    # ----------------------- MAIN COOKIE CLICKED --------------------------------------------

    def cookie_clicked(self):
        '''Adds to the score when the cookie button is clicked, it then updates the label and prints out the results'''
        self.score += self.upgrade_controller.cookies_per_click_upgrade
        self.score_label.config(text=str(self.score))
        print("Button clicked: the score is: " + str(self.score))



    # ----------------------- MENU WINDOW --------------------------------------------

    def upgrades_GUI_menu(self):
        '''This creates a pop-up window to modify your upgrades, it is easy to add more buttons/upgrades from here'''

        #Creates our root window
        self.root2 = Tk()
        self.root2.geometry("500x300")
        self.root2.title("Upgrades Menu")

        #Prices of the upgrades, this saves space in the "text" part of the button creation
        auto_click_price = "Buy Auto-click: $" + str(100 * self.upgrade_controller.auto_click_upgrade)
        cookies_per_click_price = "Buy more cookies per click: $" + str(20 * self.upgrade_controller.cookies_per_click_upgrade)
        random_bonus_price = "Buy Random Bonus: $" + str(10000)

        #Buttons

        self.auto_click_button = Button(self.root2, text=auto_click_price, command=self.auto_click)

        self.cookies_per_click_button = Button(self.root2, text=cookies_per_click_price,command=self.cookies_per_click)
        
        self.random_bonus_button = Button(self.root2, text="Random Bonus",command=self.random_bonus)
        #Pack the buttons
        self.cookies_per_click_button.pack()
        self.auto_click_button.pack()
        self.random_bonus_button.pack()
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
        t1.start()
        self.auto_click_button.pack_forget()

        

    def random_bonus(self):
        '''Random bonus of 1000 cookies, it can only be purchased once, it costs 10,000 cookies, this function is called when the button is pressed,
        however it does not actaully do the logic of the random cookie, but rather starts a thread so we can use time.sleep without python crashing'''
        self.score -= 10000
        self.upgrade_controller.random_bonus_upgrade += 1
        self.score_label.config(text=str(self.score))
        random_thread = threading.Thread(target=self.random_bonus_thread_run)
        random_thread.start()
        self.random_bonus_button.pack_forget()

            
    def no_negative(self):
        while True:
            if self.score < -1000:
                print("You are in cookie debt")
                self.cookie_debt_label.pack()
            else:
                pass

    # ----------------------- THREADED FUNCTIONS --------------------------------------------

    def auto_click_thread_run(self):
    	while True:
    		time.sleep(1)
    		self.score += 1
    		self.score_label.config(text=str(self.score))

    def random_bonus_thread_run(self):
        while True:
            time.sleep(1)
            if 10 == random.randint(1,100):
                self.score += 1000
                print("Here are 100 random cookies... yay!")
    
