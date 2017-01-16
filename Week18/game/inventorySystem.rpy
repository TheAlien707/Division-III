#init python:

######################################################################
### Inventory Class                                                 ##
######################################################################

#    class Inventory:
#        global money;
#        def __init__(self):
#            self.items = []
#        def add(self, item): # a simple method that adds an item; could add an is-there-space thing. forces player to use/drop something to pick up?
#            self.items.append(item)
#        def drop(self, item):
#            self.items.remove(item)
#        def buy(self, item):
#            if money >= item.cost:
#                self.items.append(item)
#                money -= item.cost
#            else:
#                #produce an error message
#                pass
#        def sell(self, item):
#            self.items.remove(item)
#            money += item.cost
            

######################################################################
### Item Class   Note: still in init_python block                   ##
######################################################################
#    class Item:
#        def __init__(self, name, cost, energy, foodType, image):
#            self.name = name;
#            self.cost = cost; ##how much to buy/sell it
#            self.energy = energy; ##how much energy does it give the player for eating it
#            self.foodType = foodType; ##foodtype determines what kind of animal food it makes. "plant" = herbivore; "fish" or "meat" = carnivore; and "insect" = insectivore
#            self.image = image;

######################################################################
### The inventory screen                                            ##
######################################################################
#screen inventory:
#    add "Gui/inventory/Inventory.png" at Position (xpos = 470, ypos = 0) 
##   #coordinates of the topmost left item position box size is 112 X 107
#    $ x = 37 
#    $ y = 92
##    $ i = 0
#    $ totalItems = playerStuff.items
#    for item in totalItems:
#        item
    
    

#label inventoryLabel:
#    show screen infoBar
#    show screen showHideQuickNav
#    call screen inventory

#######################################################################
#### Instatiating the Items                                         ###
#######################################################################
#python: 
#######################################################################
#### Flowers                                                         ##
#######################################################################
#    dTFlower = Item("Dragon Tears", cost = 25, energy = 0, foodType = "plant", image = "images/items/WeepingDragon.png")
    

#######################################################################
#### Food                                                            ##
#######################################################################
#    aspBerries = Item("AspBerries", cost = 5, energy = 10, foodType = "plant", image = "images/items/AspBerry")



#######################################################################
#### Found Items                                                     ##
#######################################################################

