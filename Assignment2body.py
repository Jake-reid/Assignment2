"""
Items for hire GUI -- Jake Reid-Williams
27/05/2016
https://github.com/Jake-reid/Assignment2

This program fetches a series of items(with name, description, cost and availability)
Displays a menu and adds a button for each item in the csv to the GUI
Through the menu the user can veiw an items description, hire / return or add an item
Multiple items can be hired or returned at the same time
Any changes made will only save to the file on exiting the program
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from Item import Items #didnt manage to get the Items working
import Itemslist
# from Assignment1 import read_write_csv  importing this made the program run the entire assignment 1, so i re defined it here
from Asgn1 import read_write_csv
import csv





class ItemListAPP(App):

    def __init__(self, **kwargs):
        """
        Initialize the main app and read from the csv using a function from the previous assignment
        """
        self.saveList = read_write_csv('r',[])


        self.totalCost=0.0
        self.changeList=[]
        self.instanceList = []
        self.itemList={}
        self.menuChoice='l'
        super(ItemListAPP, self).__init__(**kwargs)

        for i in range(0, len(self.saveList)):
            self.itemList[self.saveList[i][0]]= self.saveList[i][1:]
           # Itemslist(Items(self.saveList[0], self.saveList[1], self.saveList[2], self.saveList[3]))
    infoBar = StringProperty()
    def build(self):
        """
        Initiate kivy and create buttons for items
        """
        self.title = "Items for Hire - Jake Reid"
        self.root = Builder.load_file('ItemListGUI.kv')
        self.create_item_buttons()
        self.root.ids.listMenu.state = 'down' #starts the program set to list items
        return self.root

    def click_Quit(self):
        """
        Save using the read/write function from Assignment 1 and Quit
        """
        read_write_csv('w', self.saveList)
        ItemListAPP.stop(self)

    def click_Menu(self, menu):
        """
        Allows only one menu to be selected at a time
        """

        if menu != 'Hire item':
            self.root.ids.hireMenu.state = 'normal'
        if menu != 'Return item':
            self.root.ids.returnMenu.state = 'normal'
        if menu != 'List item':
            self.root.ids.listMenu.state = 'normal'



    def click_menuHire(self, instance):
        """
        Next 3 functions force the Menu buttons into a down state until another is clicked
        """
        self.infoBar = 'Select an item to Hire'
        self.click_Menu(instance.text)
        instance.state='down'
        self.menuChoice = 'h'

    def click_menuReturn(self, instance):
        self.infoBar = 'Select an item to Return'
        self.click_Menu(instance.text)
        instance.state='down'
        self.menuChoice = 'r'

    def click_menuList(self, instance):
        self.infoBar = 'Select an item to List'
        self.click_Menu(instance.text)
        instance.state='down'
        self.menuChoice = 'l'

    def create_item_buttons(self):
        """
        create buttons for each item in items.csv(via a dict)
        different colours represent the availability
        """
        for key in self.itemList:

            newButton = Button(text=key)

            newButton.bind(on_release=self.button_click)
            if self.itemList[key][2] == 'out':
                newButton.background_color = (1, .5, 1, 0.5)
            else:
                newButton.background_color = (.5, 1, .5, 1)

            self.root.ids.entriesBox.add_widget(newButton) #creation of the buttons is handled with add_widget


    def button_click(self, instance):
        """
        Defines what happens when the item buttons are clicked.
        The action taken is determined by which menu button is currently pressed(default button is List)
        """
        if self.menuChoice == 'l':
            self.infoBar = "{}: {}. ${} per day.  Item is currently {}".format(instance.text, self.itemList[instance.text][0], self.itemList[instance.text][1], self.itemList[instance.text][2])

        elif self.menuChoice == 'h':
            self.items_to_change(instance, 'in')
            #self.totalCost = 0.0

        elif self.menuChoice == 'r':
            self.infoBar = "What items do you wish to return"
            self.items_to_change(instance, 'out')


    def items_to_change(self, name, inOrout):
        """
        Handles hiring/returning multiple items by storing the button location in a list
        """
        if self.itemList[name.text][2] == inOrout:
            name.state = 'down'
            if name not in self.changeList:
                self.changeList.append(name)
                self.totalCost += float(self.itemList[name.text][1])
            elif name.state == 'down':
                self.totalCost -= float(self.itemList[name.text][1])
                name.state = 'normal'
                self.changeList.remove(name)
        else:
            self.infoBar = 'That item is currently unavailable'
        if self.menuChoice == 'h':
            self.infoBar = "This will cost ${:.2f} per day".format(self.totalCost)


    def confirmItems(self):
        """
        send the names of the items to be hired/returned a saving program
        """
        for name in self.changeList:
            self.confirmChanges(name)
        self.changeList = []


    def confirmChanges(self, name):
        """
        Sets an item to in/out as required
        """
        name.state = 'normal'
        if self.menuChoice == 'h':
            self.itemList[name.text][2] = 'out'
            name.background_color = (1, .5, 1, 0.5)
            for i in range (0, len(self.saveList)):
                if self.saveList[i][0] == name.text:
                    self.saveList[i][3] = 'out'

        elif self.menuChoice == 'r':
            self.itemList[name.text][2]= 'in'
            name.background_color = (.5, 1, .5, 1)
            for i in range (0, len(self.saveList)):
                if self.saveList[i][0] == name.text:
                    self.saveList[i][3] = 'in'
 #   def take_item(self, instance):


    def add_new_item(self):
        """
        Opens popup window for user input
        """
        self.infoBar = "Enter the item data"
        # this opens the popup
        self.root.ids.popup.open()

    def create_new_item(self, newName, newDesc, newCost):
        """
        Adds the item to the dict with user inputs.  T
        :param newName:  User input
        :param newDesc:  User input
        :param newCost:  User input
        :return:
        """
        while True:
            try:
                if len(newName)>0 and len(newDesc)>0 and float(newCost) > -1:
                    newValue =[]
                    newValue.append(newName)
                    newValue.append(newDesc)
                    newValue.append(newCost)
                    newValue.append('in')
                    self.saveList.append(newValue)

                    self.itemList[newName] = newValue[1:]

                    # Creates a new button with the properties desired
                    newButton = Button(text=newName)
                    newButton.bind(on_release=self.button_click)
                    newButton.background_color = (.5, 1, .5, 1)
                    self.root.ids.entriesBox.add_widget(newButton)
                    self.root.ids.popup.dismiss()
                    self.clearAll()
                    break
                else:
                    raise AttributeError
            except ValueError:
                self.infoBar = "ITEM NOT ADDED: The cost has to be 0.00 or higher"
                break
            except AttributeError:
                self.infoBar = "ITEM NOT ADDED: Please make sure to enter both a NAME and DESCRIPTION"
                break

    def clearAll(self):
        """
        empties the text in the popup textboxes
        :return:
        """
        self.root.ids.newValue = []
        self.root.ids.newName.text = ''
        self.root.ids.newDesc.text = ''
        self.root.ids.newCost.text = ''

    def cancel_new_item(self):
        """
        Clears the textboxes in the popup and closes it
        """
        self.root.ids.popup.dismiss()
        self.clearAll()
        self.infoBar = ""


ItemListAPP().run()