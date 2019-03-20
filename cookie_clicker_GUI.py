from tkinter import Button, Label, Tk, PhotoImage
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
            self.random_bonus_upgrade = int(data["random_bonus_upgrade"])
        else:
            self.score = 0        
            self.auto_click_upgrade = 0
            #SOme upgrades have to be 1 by default to have a cost... 
            self.cookies_per_click_upgrade = 1
            self.random_bonus_upgrade = 0


class CookieClickerMainGUI:

    def __init__(self, root, data=''):
        self.root = root
        self.upgrade_controller = UpgradesController(data)
        root.geometry("700x700")
        root.title("Cookie Clicker")
        self.photo = PhotoImage(data=cookieimage)
        
        #Inits the score for the game, will change if .dat file exists
        self.score = self.upgrade_controller.score
        self.auto_click_upgrade = self.upgrade_controller.auto_click_upgrade
        self.cookies_per_click_upgrade = self.upgrade_controller.cookies_per_click_upgrade
        self.random_bonus_upgrade = self.upgrade_controller.random_bonus_upgrade

        #inital GUI components
        self.label = Label(root,text="Welcome to Cookie Clicker",font=("Helvetica", 16))
        self.version_label = Label(root,text="version 1.0",font=("Helvetica",10))
        self.cookie_button = Button(root,text="click me!", command=self.cookie_clicked, image=self.photo)
        self.upgrades_button = Button(root,text="Upgrades",command=self.upgrades_GUI_menu, font=("Helvetica",10))
        self.save_button = Button(root,text="Save data",command=self.export_data, font=("Helvetica",10))
        self.score_label = Label(root,text=str(self.score),font=("Helvetica", 30))
        self.cookie_debt_label = Label(root,text="You are in cookie debt",font=("Helvetica", 20))
        self.dark_mode_button = Button(root, text="Dark mode", command=self.dark_mode, font=("Helvetica",10))
        self.light_mode_button = Button(root,text="Light mode", command=self.light_mode, font=("Helvetica",10))
        self.import_upgrades_button = Button(root,text="import data",command=self.import_upgrades, font=("Helvetica",10))


        #pack the widgets inside the screen
        self.score_label.pack()
        self.label.pack()
        self.version_label.pack()
        self.cookie_button.pack()
        self.upgrades_button.pack()
        self.save_button.pack()
        self.dark_mode_button.pack()
        self.import_upgrades_button.pack()

    # ----------------------- IMPORT/EXPORT DATA --------------------------------------------
        
        
    def export_data(self):
        '''Exports the data into a dictionary into the dat file that was created from the cookie_clicker.py file'''
        
        export_data = {"score":self.score,"auto_click_upgrade":self.upgrade_controller.auto_click_upgrade,
        "cookies_per_click_upgrade":self.upgrade_controller.cookies_per_click_upgrade,
        "random_bonus_upgrade":self.upgrade_controller.random_bonus_upgrade}
        
        with open('cookie.dat','wb') as f:
            pickle.dump(export_data,f)
        f.close()

    def import_upgrades(self):
        '''Applies all existing upgrades, it then adds back the cookies that the user gets refunded because they don't have to
        pay for the upgrade twice'''

        for num in range(int(self.auto_click_upgrade)):
            self.auto_click()
            self.score += 100
        for num in range(int(self.cookies_per_click_upgrade)):
            self.cookies_per_click()
            self.score += 20
        for num in range(int(self.random_bonus_upgrade)):
            self.random_bonus()
            self.score += 10000

        self.import_upgrades_button.pack_forget()

    # ----------------------- Dark mode/light mode --------------------------------------------

    def dark_mode(self):
        self.dark_mode_button.pack_forget()
        self.light_mode_button.pack()
        self.root.config(bg="black")
        #self.photo.config(bg="black")
        self.score_label.config(fg="white",bg="black")
        self.label.config(fg="white",bg="black")
        self.version_label.config(fg="white",bg="black")
        self.save_button.config(fg="white",bg="black")
        self.upgrades_button.config(fg="white",bg="black")
        self.light_mode_button.config(fg="white",bg="black")

    def light_mode(self):
        self.dark_mode_button.pack()
        self.light_mode_button.pack_forget()
        self.root.config(bg="white")
        self.score_label.config(fg="black", bg="white")
        self.save_button.config(fg="black", bg="white")
        self.upgrades_button.config(fg="black", bg="white")
        self.label.config(fg="black", bg="white")
        self.version_label.config(fg="black", bg="white")


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

        #Really, these varibles need to be in __init__ concider moving these if we want to progressivly increase the cost of the cookies
        auto_click_price = "Buy Auto-click: $" + str(100 * self.upgrade_controller.auto_click_upgrade)
        cookies_per_click_price = "Buy more cookies per click: $" + str(20 * self.upgrade_controller.cookies_per_click_upgrade)
        random_bonus_price = "Buy Random Bonus: $" + str(10000)

        #Buttons

        self.auto_click_button = Button(self.root2, text=auto_click_price, command=self.auto_click)

        self.cookies_per_click_button = Button(self.root2, text=cookies_per_click_price,command=self.cookies_per_click)
        
        self.random_bonus_button = Button(self.root2, text=random_bonus_price,command=self.random_bonus)
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
        try:
            self.auto_click_button.pack_forget()
        except:
            pass

        

    def random_bonus(self):
        '''Random bonus of 10000 cookies, it can only be purchased once, it costs 10,000 cookies, this function is called when the button is pressed,
        however it does not actaully do the logic of the random cookie, but rather starts a thread so we can use time.sleep without python crashing'''
        self.score -= 10000
        self.upgrade_controller.random_bonus_upgrade += 1
        self.score_label.config(text=str(self.score))
        random_thread = threading.Thread(target=self.random_bonus_thread_run)
        random_thread.start()
        try:
            self.random_bonus_button.pack_forget()
        except:
            pass


    # ----------------------- THREADED FUNCTIONS --------------------------------------------

    def auto_click_thread_run(self):
        while True:
            time.sleep(1)
            self.score += 1
            self.score_label.config(text=str(self.score))

    def random_bonus_thread_run(self):
        '''This is the target of the random_bonus_buttton command that starts the 1% chance of getting 10,000 bonus cookies'''
        while True:
            time.sleep(1)
            if 10 == random.randint(1,100):
                self.score += 10000
                print("Here are 10000 random cookies... yay!")


