#init python:
#    class Building (object):
#        def __init__ ():
#        #upgradeLevel determines the capacities of the building
#            upgradeLevel = 0;
#            description = "string";

##############################################################################################
### Player's Home                                                                          ###
##############################################################################################
screen playerHome:
    imagemap:
        ground "GUI/farmMap/home.png" at right
        hover "GUI/farmMap/homeHighlight.png"
        
        hotspot (265, 358, 190, 88) clicked Jump ("clickedDiary")
        hotspot (544, 347, 178, 136) clicked Jump ("clickedChest")
        hotspot (729, 345, 314, 253) clicked Jump ("clickedBed")
    #add an imagebutton to go "exit" back to farm

label wentHome:
    show screen infoBar
    show screen showHideQuickNav
    call screen playerHome
    "Welcome home! Here you can sleep or store items or read your diary. But none of that is implemented yet! Yay!"
    $renpy.pause()
    

label clickedDiary:
    "You'll be able to get information here, later. It'll hold a record of what you've done and seen."
    call wentHome

label clickedChest:
    "This is where you can store items."
    call wentHome

label clickedBed:
    "Do you want to go to sleep?"
    menu:
        "Yes":
            pass
            #call day rollover function
        "No":
            call wentHome

##############################################################################################
### The Processing Shed                                                                    ###
##############################################################################################

screen pShed: 
    imagemap:
        ground "GUI/farmMap/ProcessingShed.png" at right
        hover "GUI/farmMap/ProcessingShedHover.png"
        
        hotspot (167, 306, 334, 337) clicked Jump ("clickedToolTable")
        hotspot (501, 220, 238, 188) clicked Jump ("clickedFishTank")
        hotspot (739, 210, 247, 195) clicked Jump ("clickedGummzieTank")
        #add an imagebutton to go "exit" back to farm

label pShedLabel:
    show screen infoBar
    show screen quickNav
    call screen pShed

label clickedToolTable:
    "This is where you can process things, like livestock into meat or plants into animal feed."
    jump pShedLabel 
#   There will need to be a ~thing~ here to process items into animal feed. 
#       like you select "Process to Animal Feed" and then it shows the player three images (meat, fish, and plant). 
#       The player selects one and then it goes to inventory and shows the player what they can use to create the Feed
#       Energy is taken, the item is destroyed, and time ticks along. The animal feed pops into the player's inventory
#       And the player is returned to the PShed
#   Also the ability to "call up" a list of animals to be processed
#       Which will require a function in which the animal is destroyed from game
#       Relevant variables are adjusuted (Nry's Vegetarian freakout and/or Kahon's Rage triggered. Note: figure out something to prioritize those two so they don't happen at once?)
#       And the correct amount of meat is put in the player's inventory; energy taken and time ticked forward
#       And the player returned to the PShed

label clickedFishTank:
    "This is where some little fishies will live! They'll be bait and a possible food source for your livestock! They also don't exist yet!"
    jump pShedLabel 
#   Here will be the ability to harvest fish and clean their tank and check on them
#       The first two take time/energy, but the last one just prints out how the fish are doing (how many there are and such)
#       Can't harvest if there's two or less fish

label clickedGummzieTank:
    "This is where little Gummzie worms live! They're very cute and very not implemented yet!"
    jump pShedLabel 
#   Here will be the same as the fish, but with Gummzies this time. 
#       They also have the option of harvesting "Sweet Goo" if "happiness" is maintained (random chance that gets more likely the more days-in-a-row the tank is kept clean)
#               Should never exceed like, 45% chance
#       Harvesting Gummzies/Goo and cleaning takes time/energy
#       Can't harvest if there's two or less gummzies


##############################################################################################
### Animal Houses                                                                          ###
##############################################################################################

#####################################################################
## Snuzzie House                                                   ##
#####################################################################
screen snuzzieHouse:
    modal True
    imagemap:
        ground "GUI/animalHouses/SnuzzieHouse_empty.png" at right
        #hover ""
        
#        hotspot clicked Jump
#        hotspot clicked Jump
    #add an imagebutton to go "exit" back to farm

"So this is where Snuzzies will live, but I'm still working on how. I have a few ideas and will be testing them soon!"
"But, for now, this is all I've got. Back to the farm with you!"
call screen farmMap

#####################################################################
## Keyu House                                                      ##
#####################################################################
screen keyuHouse:
    modal True
    imagemap:
        ground "GUI/animalHouses/KeyuHouse_empty.png" at right
        #hover ""
        
#        hotspot clicked Jump
#        hotspot clicked Jump
    #add an imagebutton to go "exit" back to farm

"So this is where Snuzzies will live, but I'm still working on how. I have a few ideas and will be testing them soon!"
"But, for now, this is all I've got. Back to the farm with you!"
call screen farmMap


#####################################################################
## Trog House                                                      ##
#####################################################################
screen trogHouse:
    modal True
    imagemap:
        ground "GUI/animalHouses/TrogHouse_empty.png" at right
        #hover ""
        
#        hotspot clicked Jump
#        hotspot clicked Jump
    #add an imagebutton to go "exit" back to farm

"So this is where Snuzzies will live, but I'm still working on how. I have a few ideas and will be testing them soon!"
"But, for now, this is all I've got. Back to the farm with you!"
call screen farmMap