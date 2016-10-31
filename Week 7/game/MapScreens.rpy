#####################################################################
## The QuickNav Hide Screens Function                              ##
#####################################################################

##this removes the previous screens from view when using the quickNav menu

init python:
    def hideTheScreens():
        renpy.hide_screen ("worldMap")
        renpy.hide_screen ("inventory")
        renpy.hide_screen ("farmMap")

#####################################################################
## The Quick Navigation Bar                                        ##
#####################################################################

screen quickNav: #quickNav bar at the bottom of the screen
#use the variable $showQuickNav to hide/unhide
    
    zorder 200
    imagemap:
        ground "GUI/quickNav/quickBar.png" at Position(xpos = 433, ypos = 647)
        idle "GUI/quickNav/quickBar.png" 
        hover "GUI/quickNav/hover.png"

        
        hotspot (2, 0, 152, 76) clicked Jump("quickBar_Map")#Map-->should go to the main map screen
        hotspot (155, 2, 155, 74) clicked Jump("quickBar_Bag")#Bag--> should open the inventory screen
        hotspot (310, 3, 157, 73.0) clicked Jump("quickBar_Zal") #Zal--> goes to dialogue w/ Zal
        hotspot (464, 3, 157, 73.0) action ShowMenu('save') #Menu

##when the hotspots are clicked, these happen:
label quickBar_Zal:
    $hideTheScreens()
    "You found Zal!"
label quickBar_Map:
    $hideTheScreens()
    jump worldMap
label quickBar_Bag:
    $hideTheScreens()
    jump inventoryScreen



#####################################################################
## The Main Map--> Navigating the World                            ##
#####################################################################
screen worldMap: #the map navigation map
    imagemap:
        ground "GUI/mainMapScreen/Map.png" at center #Position(xpos = 252, ypos = 51)
        hover "GUI/mainMapScreen/MapHoverspots.png"
        
        hotspot (383, 20, 180, 123) clicked Jump("mountainClicked")
        hotspot (101, 104, 275, 144) clicked Jump ("lakeClicked")
        hotspot (775, 497, 186, 115) clicked Jump ("nadiasPlaceClicked")
        hotspot (601, 63, 281, 205) clicked Jump ("fvClicked")
        hotspot (670, 275, 277, 220) clicked Jump ("outskirtsClicked")
        hotspot (304, 503, 426, 202) clicked Jump ("farmClicked")
        hotspot (8, 249, 295, 455) clicked Jump ("forestClicked")

       
label mountainClicked:
    "This is the mountain clearing. Do you want to go there?"
    menu:
        "Yes":
            jump mountain_clearing
        "No":
            screen mainMap
            
label lakeClicked:
    "This is the lake. Do you want to go there?"
    menu:
        "Yes":
            jump lake
        "No":
            screen mainMap
            
label nadiasPlaceClicked:
    "This is Nadia's Lab Do you want to go there?"
    menu:
        "Yes":
            jump nadiasPlace
        "No":
            screen mainMap
            
label fvClicked:
    "This is the Village. You're not allowed there!"
    screen mainMap

label outskirtsClicked:
    "These are the Village Outskirts. Do you want to go there?"
    menu:
        "Yes":
            jump outskirts
        "No":
            screen mainMap

label farmClicked:
    "This is your farm! Do you want to go home?"
    menu:
        "Yes":
            jump farm
        "No":
            screen mainMap

label forestClicked:
    "This is the forest. Do you want to go there?"
    menu:
        "Yes":
            jump forest
        "No":
            screen mainMap
         
            

#####################################################################
## The Farm Map--> Navigating Home                                 ##
#####################################################################
screen farmMap: #navigating at your farm
    imagemap:
        ground "GUI/farmMap/farmMap.png"
        hover "GUI/farmMap/farmMapHighlight.png"
        
        hotspot (0, 0, 365, 404) clicked Jump ("unusedField_clicked")
        hotspot (778, 22, 485, 385) clicked Jump ("usableField_clicked")
        hotspot (377, 0, 192, 209) clicked Jump ("house_clicked")
        hotspot (588, 5, 169, 163) clicked Jump ("p_Shed_clicked")
        hotspot (2, 409, 1275, 307) clicked Jump ("animalPlaceholder_clicked")

label unusedField_clicked:
    "This is the unusable field"
    
label usableField_clicked:
    "You can plant here"
    
label house_clicked:
    "You live here!"
    
label p_Shed_clicked:
    "This is the procssing shed!"
    
label animalPlaceholder_clicked:
    "Animal sheds will be here... eventually"



