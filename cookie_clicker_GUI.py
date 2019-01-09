from tkinter import *
from image import image as cookieimage
import time


class UpgradesController:

    def __init__(self, data):
        #LOGIC TO PARSE DATA GOES HERE
        self.auto_click_upgrade = 0


class CookieClickerMainGUI:

    def __init__(self, root, data=''):
        self.upgrade_controller = UpgradesController(data)
        root.geometry("700x700")
        root.title("Cookie Clicker")
        self.photo = PhotoImage(data=cookieimage)
        #Inits the score for the game, will change if .dat file exists
        self.score = 0
        self.data = data
        self.score = self.check_data(self.data)
        self.label = Label(root,text="Hello",font=("Helvetica", 16))
        self.cookie_button = Button(root,text="click me!", command=self.cookie_clicked, image=self.photo)
        self.upgrades_button = Button(root,text="Upgrades",command=self.upgrades_GUI_menu)
        self.score_label = Label(root,text=str(self.score),font=("Helvetica", 20))

        #pack the widgets inside the screen
        self.score_label.pack()
        self.label.pack()
        self.cookie_button.pack()
        self.upgrades_button.pack()
        
    def check_data(self,data):
        '''This checks the data if there was any and updates to the previous score, else it does nothing'''
        if self.data == '':
            self.score = 0
        else:
            self.score = int(data)
        return self.score

    def cookie_clicked(self):
        '''Adds to the score when the cookie button is clicked, it then updates the label... the defualt it 
        the label updates ever 200 milliseconds, do not change this!'''
        self.score += 1
        self.score_label.config(text=str(self.score))
        print("Button clicked: the score is: " + str(self.score))

    def upgrades_GUI_menu(self):
        '''This creates a pop-up window to modify your upgrades, it is easy to add things from here'''
        self.root2 = Tk()
        self.root2.geometry("500x300")
        self.root2.title("Upgrades Menu")
        self.auto_click_button = Button(self.root2, text="Buy Auto-click", command=self.auto_click)
        self.auto_click_button.pack()
        self.root2.mainloop()

    def auto_click(self):
        '''Sets the autoclick to run, it subtracts the score by 100 times the number of upgrades that the auto_click 
        has, it then sets the updatecontroller.aut_click_upgrade += 1'''
        self.score -= 100 * self.upgrade_controller.auto_click_upgrade
        self.upgrade_controller.auto_click_upgrade += 1
        while True:
            #THis is a known issue that causes the program to freeze than crash, concider time.time?
            sleep(60-self.upgrade_controller.auto_click_upgrade)
            self.score += 1




