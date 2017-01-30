init -1 python:
######################################################################
### Inventory Class                                                 ##
######################################################################

    class Inventory:
        global money;
        def __init__(self):
            self.items = []
        def __getitem__(self):
            return self.items
        def add(self, item): # a simple method that adds an item; could add an is-there-space thing. forces player to use/drop something to pick up?
            self.items.append(item)
        def drop(self, item):
            self.items.remove(item)
        def buy(self, item):
            if money >= item.cost:
                self.items.append(item)
                money -= item.cost
            else:
                #produce an error message
                pass
        def sell(self, item):
            self.items.remove(item)
            money += item.cost


#   playerBag is the inventory of all the items in their backpack currently
    playerBag = Inventory()

#   playerChest is an extended inventory; the chest at the PC's house can hold items too
    playerChest = Inventory()

#  #Squiz's store has an inventory, but it will work a little differently than the players
#  #it has all the same functionality but it gets "reset" at rolloever--> she only stocks her usual stuff 
#  #and she only has a set amount of $$ each day. When the player sells to her, 
#  #she'll have that in stock for that day only
    SquizStore = Inventory()


######################################################################
### Item Class   Note: still in init_python block                   ##
######################################################################
    class Item:
        def __init__(self, name, cost, purpose, energy, foodType, descript):
            self.name = name;
            self.cost = cost; ##how much to buy/sell it
            self.purpose = purpose; ##what does it do
            self.energy = energy; ##how much energy does it give the player for eating it
            self.foodType = foodType; ##foodtype determines what kind of animal food it makes. "plant" = herbivore; "fish" or "meat" = carnivore; and "insect" = insectivore
            self.descript = descript;
        def __getitem__(self):
            return self.name
            return self.cost
            return self.purpose

#######################################################################
#### Instatiating the Items                                         ###
#######################################################################
    
#######################################################################
#### Flowers                                                         ##
#######################################################################
    dTFlower = Item("Dragon Tears", cost = 25, purpose = "none", energy = 0, foodType = "plant", descript = "legend has it that they sprout from crystalized tears")
    

#######################################################################
#### Food                                                            ##
#######################################################################
    aspBerries = Item("AspBerries", cost = 5, purpose = "+ energy", energy = 10, foodType = "plant", descript = "tangy and flavorful berries")



#######################################################################
#### Found Items                                                     ##
#######################################################################



######################################################################
### The Player's Inventory Screen: "playerBag"                      ##
######################################################################
screen inventory:
    add "GUI/inventory/Inventory.png" at right #image
#   #There are nine lines for items. If the player has more than that many items, then they need another page
#   #deal w/ that laters
    $x = 575;
    $y = 115;
    $ibX = 555 ##imagebutton positions
    $ibY = 111
    $eachItem = 0
    $itemToShow = 0
    ##initilizing the button's variables
    $itemName = "before For Loop"
    $itemIndexNumber = 0
    ##sorts the inventory into alphabetical order
    $playerBag.items.sort(reverse=True)
    $howManyItems = len(playerBag.items)
    #for every item in the list
    for eachItem in range (howManyItems):
        button:          
            $itemName = "In the for Loop" #playerBag.items[itemToShow].name
            $itemIndexNumber = itemToShow
            hbox: #name should be no more than 20 characters
                xpos x
                xmaximum 315 #300 ##w/ qty
                ypos y
                $textStorage = playerBag.items[itemToShow].name
                text("[textStorage]")
            $x +=  335
            hbox: #Cost
                xpos x
                xmaximum 125 #120 ##w/ qty
                ypos y
                $textStorage = playerBag.items[itemToShow].cost
                text("[textStorage]")
            $x += 140 #95 ##w/ qty
            hbox: #purpose ##previously named "effect" until renpy threw a fit
                xpos x
                xmaximum 165 #145 ##w/ qty
                ypos y  
                $textStorage = playerBag.items[itemToShow].purpose
                text("[textStorage]")
            $x += 130
            imagebutton:
                idle "GUI/inventory/idleItem.png" at Position (xpos = ibX, ypos = ibY)
                hover "GUI/inventory/chosenItem.png"
                action Return (itemName), Return (itemIndexNumber), Jump ("itWorks")       
        $x = 580;
        $y += 60
        $ibY += 60
        $itemToShow += 1
        $eachItem += 1
    
#    if len(playerBag.items) > 9:
#        imagebutton: 
#            idle "GUI/inventory/Back.png" at Position (xpos = 400, ypos = 640)
#            hover "GUI/inventory/BackHighlight.png"
#            action Jump ("backWorks")
#        imagebutton:
#            idle "GUI/inventory/Next.png" at Position (xpos = 785, ypos = 640)
#            hover "GUI/inventory/NextHighlight.png"
#            action Jump ("nextWorks")

label itWorks:
    "yayyyy!!!!"
    "you clicked %(itemName)s"
    "it's number is %(itemIndexNumber)s"
    $renpy.pause()

label backWorks:
    text "Went back a screen!!!"
    $renpy.pause()

label nextWorks:
    text "Went ahead a screen!!!"
    $renpy.pause()

label inventoryLabel:
    show screen infoBar
    show screen showHideQuickNav
    call screen inventory
