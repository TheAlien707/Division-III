#####################################################################
## Inventory Class                                                 ##
#####################################################################
init python:
    class Inventory(store.object):
        def __init__(self, money=0):
            self.money = money
            self.items = []
        def add(self, item): # a simple method that adds an item; could add an is-there-space thing. forces player to use/drop something to pick up?
            self.items.append(item)
        def drop(self, item):
            self.items.remove(item)
        def buy(self, item):
            if self.money >= item.cost:
                self.items.append(item)
                self.money -= item.cost



#####################################################################
## The inventory screen                                            ##
#####################################################################
screen inventory:
    add "Gui/inventory/Inventory.png" at center 
    #coordinates of the topmost left item position
    $ x = 33 
    $ y = 91
    


#####################################################################
## The inventory screen                                            ##
#####################################################################
#screen inventory:
#    imagemap:
#        ground "GUI/inventory/Inventory.png" at center
#        hover "GUI/inventory/hover.png"
#        selected_idle "Gui/inventory/clicked.png"
#        selected_hover "Gui/inventory/clicked.png"
#
###Row 1
#    hotspot (33, 91, 105, 105) clicked Jump ("item1")
#    hotspot (146, 91, 105, 105) clicked Jump ("item2")
#    hotspot (256, 91, 105, 105) clicked Jump ("item3")
#    hotspot (370, 91, 105, 105) clicked Jump ("item4")
#    hotspot (481, 91, 105, 105) clicked Jump ("item5")
#    hotspot (591, 91, 105, 105) clicked Jump ("item6")
#    hotspot (706, 91, 105, 105) clicked Jump ("item7")
###Row 2
#    hotspot (33, 196, 105, 105) clicked Jump ("item8")
#    hotspot (146, 196, 105, 105) clicked Jump ("item9")
#    hotspot (256, 196, 105, 105) clicked Jump ("item10")
#    hotspot (370, 196, 105, 105) clicked Jump ("item11")
#    hotspot (481, 196, 105, 105) clicked Jump ("item12")
#    hotspot (591, 196, 105, 105) clicked Jump ("item13")
#    hotspot (706, 196, 105, 105) clicked Jump ("item14")
###Row 3
#    hotspot (33, 304, 105, 105) clicked Jump ("item15")
#    hotspot (146, 304, 105, 105) clicked Jump ("item16")
#    hotspot (256, 304, 105, 105) clicked Jump ("item17")
#    hotspot (370, 304, 105, 105) clicked Jump ("item18")
#    hotspot (481, 304, 105, 105) clicked Jump ("item19")
#    hotspot (591, 304, 105, 105) clicked Jump ("item20")
#    hotspot (706, 304, 105, 105) clicked Jump ("item21")
###Row 4
#    hotspot (33, 412, 105, 105) clicked Jump ("item22")
#    hotspot (146, 412, 105, 105) clicked Jump ("item23")
#    hotspot (256, 412, 105, 105) clicked Jump ("item24")
#    hotspot (370, 412, 105, 105) clicked Jump ("item25")
#    hotspot (481, 412, 105, 105) clicked Jump ("item26")
#    hotspot (591, 412, 105, 105) clicked Jump ("item27")
#    hotspot (706, 411, 105, 105) clicked Jump ("item28")
###Row 5
#    hotspot (33, 515, 105, 105) clicked Jump ("item29")
#    hotspot (146, 515, 105, 105) clicked Jump ("item30")
#    hotspot (256, 515, 105, 105) clicked Jump ("item31")
#    hotspot (370, 515, 105, 105) clicked Jump ("item32")
#    hotspot (481, 515, 105, 105) clicked Jump ("item33")
#    hotspot (591, 515, 105, 105) clicked Jump ("item34")
#    hotspot (706, 515, 105, 105) clicked Jump ("item35")

#####################################################################
## Using the items                                                 ##
#####################################################################
##these screens shouldn't cover the whole screen, just part of it? or maybe they should take over...

label item1:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory

label item2:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory

label item3:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    
label item4:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    
label item5:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    
label item6:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    
label item7:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    
label item8:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    
label item9:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory

label item10:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    
label item11:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory

label item12:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory

label item13:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    
label item14:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    
label item15:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    
label item16:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    
label item17:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    
label item18:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    
label item19:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory

label item20:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    
label item21:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory

label item22:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory

label item23:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    
label item24:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    
label item25:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    
label item26:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    
label item27:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    
label item28:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    
label item29:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory

label item30:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    
label item31:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory

label item32:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory

label item33:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    
label item34:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    
label item35:
    pass
    ##place item_image at truecenter
    ##next to image should be the # of that item the PC is carrying
    ##import description of the item
    ##Option to destroy the item
    ##Option to go back to inventory
    