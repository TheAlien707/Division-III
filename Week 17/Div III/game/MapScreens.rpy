#############################################################################
## The Information Bar's Widgets:                                         ###
#############################################################################
#init python
#    def showTime():
#        timeWidget = Text(str(timeVar)); ##timeVar is what time it is. timeWidget is the displayable
#        ui.at(Position(xalign = , yalign = )); ##What position to display at
#        ui.add(timeWidget); ##actually add the widget

##the energy widget is more complicated as there are two important variables to consider: the player's current energy and the player's maximum
##Ultimately, the player will see the widgets in a ratio "currentEnergy / maxEnergy" but their widgers must be seperate

#    def showCurrentEnergy():
#        currentEnergyWidget = Text(int(currentEnergy)); ##currentEnergy is the PCs current energy
#        ui.at(Position(xalign = , yalign = )); ##gives it position
#        ui.add(currentEnergyWidget); ##actually add it
    
#    def showMaxEnergy():
#        maxEnergyWidget = Text(int(maxEnergy)); ##maxEnergy is the PCs maximum energy
#        ui.at(Position(xalign = , yalign = )); ##gives it position
#        ui.add(maxEnergyWidget); ##actually add it

#    def showDate():
#        dateWidget = Text(str(currentDate)); #currentDate is the variable that tracks the current day
#        ui.at(Position(xalign = , yalign = )); ##gives it position
#        ui.add(dateWidget); ##actually add it  

#    def showMoney():
#        money = Text(str(moneyNum)); #moneyNum is the variable that keeps track of the player's money
#        ui.at(Position(xalign = , yalign = )); ##gives it position
#        ui.add(money); ##actually add it  

#    def showLocation():
#        locationWidget = Text(str(currentLocation)); #displays where the player currently is
#        ui.at(Position(xalign = , yalign = )); ##gives it position
#        ui.add(locationWidget); ##actually add it  

##this final widget is the "Zal Help Text"; when the player does different things (changes location or clicks on an item), Zal gives a quick description of that item
#    def showZalHelpText():
#        helpTextWidget = Text(str(zalHelpText)); #this widget shows Zal's help text, which is a description of different items and locations
#        ui.at(Position(xalign = , yalign = ));
#        ui.add(locationWidget); 
#############################################################################
## The Actual Information Bar Screen                                      ###
#############################################################################

screen infoBar: #the left-hand bar that displays various information such as time and money
    imagemap:
        ground "GUI/quickNav/infoBar.png" at left
#    fixed:
#        text "[playerName]" at (56, 40, 137, 33)
#    $showTime();
#    $showCurrentEnergy();
#    $showMaxEnergy();
#    $showDate();
#    $showMoney();
#    $showLocation();
#    if the player clicked on something, then the mini-zal should give a description of it:
#        $showZalHelpText();

##Notes:
##    Name: (56, 40, 137, 33)
##    Date: (47, 118, 62, 29)
##    Time: (160, 141, 52, 27)
##    Current Energy: (34, 187, 26, 15)
##    Max Energy: (73, 194, 28, 16)
##    Money: (140, 206, 48, 22)
##    Location: (51, 262, 151, 24)
##    Zal's Frame: (47, 322, 166, 195)
##    Zal's Help: (35, 564, 178, 113)
    
    


#####################################################################
## The Quick Navigation Bar                                        ##
#####################################################################

screen quickNav: #quickNav bar at the bottom of the screen
    imagemap:
        ground "GUI/quickNav/quickBar.png" at Position(xpos = 555, ypos = 640)
        idle "GUI/quickNav/quickBar.png" 
        hover "GUI/quickNav/hover.png"

        
        hotspot (2, 0, 152, 76) clicked Jump("quickBar_Map")#Map-->should go to the main map screen
        hotspot (155, 2, 155, 74) clicked Jump("quickBar_Bag")#Bag--> should open the inventory screen
        hotspot (310, 3, 157, 73.0) clicked Jump("quickBar_Zal") #Zal--> goes to dialogue w/ Zal
        hotspot (464, 3, 157, 73.0) action ShowMenu('save') #Menu

##when the hotspots are clicked, these happen:
label quickBar_Zal:
    "You found Zal!"
label quickBar_Bag:
    $config.window_hide_transition
    hide screen quickNav
    call inventoryScreen
label quickBar_Map:
    hide screen quickNav
    $config.window_hide_transition
    call screen worldMap



#####################################################################
## The Main Map--> Navigating the World                            ##
#####################################################################
screen worldMap(): #the map navigation map
    imagemap:
        ground "GUI/mainMapScreen/Map.png" at Position (xpos = 200, ypos = 10)
        hover "GUI/mainMapScreen/MapHoverspots.png"
        
        hotspot (446, 47, 351, 169) clicked Jump ("mountainClicked")
        hotspot (94, 45, 290, 162) clicked Jump ("lakeClicked")
        hotspot (877, 454, 293, 189) clicked Jump ("nadiasPlaceClicked")
        hotspot (876, 31, 291, 208) clicked Jump ("fvClicked")
        hotspot (957, 245, 262, 187) clicked Jump ("outskirtsClicked")
        hotspot (452, 291, 353, 289) clicked Jump ("farmClicked")
        hotspot (99, 213, 345, 461) clicked Jump ("forestClicked")

       
label mountainClicked:
    scene bg mountain
    "This is the Plataeu. Do you want to go there?"
    menu:
        "Yes":
            call mountain_clearing
        "No":
            show screen worldMap
            
label lakeClicked:
    scene bg lake
    "This is the lake. Do you want to go there?"
    menu:
        "Yes":
            call lake
        "No":
            show screen worldMap
            
label nadiasPlaceClicked:
    scene bg nadiasPlace
    "This is Nadia's Lab Do you want to go there?"
    menu:
        "Yes":
            call nadiasPlace
        "No":
            show screen worldMap
            
label fvClicked:
    "This is the Village. You're not allowed there!"
    show screen worldMap

label outskirtsClicked:
    "These are the Village Outskirts. Do you want to go there?"
    menu:
        "Yes":
            call outskirts
        "No":
            show screen worldMap

label farmClicked:
    scene bg farm
    "This is your farm! Do you want to go home?"
    menu:
        "Yes":
            call farmTime
        "No":
            show screen worldMap

label forestClicked:
    scene bg forest
    "This is the forest. Do you want to go there?"
    menu:
        "Yes":
            call forest
        "No":
            show screen worldMap
         
            

#####################################################################
## The Farm Map--> Navigating Home                                 ##
#####################################################################
screen farmMap: #navigating at your farm
    imagemap:
        ground "GUI/farmMap/farmMap.png" at right
        hover "GUI/farmMap/farmMapHighlight.png"
        
        hotspot (0, 0, 365, 404) clicked Jump ("unusedField_clicked")
        hotspot (778, 22, 485, 385) clicked Jump ("usableField_clicked")
        hotspot (377, 0, 192, 209) clicked Jump ("house_clicked")
        hotspot (588, 5, 169, 163) clicked Jump ("p_Shed_clicked")
        hotspot (0, 439, 227, 186) clicked Jump ("snuzzie_House_clicked")
        hotspot (234, 404, 347, 259) clicked Jump ("keyu_House_clicked")
        hotspot (674, 448, 149, 203) clicked Jump ("trog_House_clicked")
        hotspot (825, 413, 453, 304) clicked Jump ("animalPlaceholder_clicked")

label unusedField_clicked:
    "This is the unusable field"
    
label usableField_clicked:
    "You can plant here"
    
label house_clicked:
    "You live here!"
    
label p_Shed_clicked:
    "This is the procssing shed! Shall we go there?"
    menu:
        "Yes":
            hide screen farmMap
            call screen pShed
        "No":
            call screen farmMap

label snuzzie_House_clicked:
    "This is where Snuzzies live! Shall we go there?"
    menu:
        "Yes":
            call screen snuzzieHouse
        "No":
            call screen farmMap

label keyu_House_clicked:
    "This is where Keyu live! Shall we go there?"
    menu:
        "Yes":
            call screen keyuHouse
        "No":
            call screen farmMap
    
label trog_House_clicked:
    "This is where Trogs live! Shall we go there?"
    menu:
        "Yes":
            call screen trogHouse
        "No":
            call screen farmMap

label animalPlaceholder_clicked:
    "More animal sheds will be here... eventually"

#####################################################################
## Outskirts Village                                               ##
#####################################################################


