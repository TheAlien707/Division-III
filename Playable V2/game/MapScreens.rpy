#############################################################################
## The Information Bar Functions                                          ###
#############################################################################    



#############################################################################
## The  Information Bar Screen                                            ###
#############################################################################

screen infoBar: #the left-hand bar that displays various information such as time and money
    imagemap:
        ground "GUI/quickNav/infoBar.png" at left
    
    text "[playerName]" at Position (xpos = 60, ypos = 40)
    text "Day: [date]" at Position (xpos = 43, ypos = 120)
    text "[hour]:[minutes]" at Position (xpos = 160 , ypos = 141)
    text "[currentEnergy]" at Position (xpos = 30, ypos = 180)
    text "[maxEnergy]" at Position (xpos = 73, ypos = 195)
    text "[money]" at Position (xpos = 165, ypos = 205)
    text "[location]" at Position (xpos = 50, ypos = 260)
    
    vbox:
        viewport:
            xpos 38
            ypos 565
            mousewheel True
            draggable True
            scrollbars None
            xmaximum 160
            ymaximum 105
            if zalNeeded == True:
                text([zalsDescription])

    


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

screen showHideQuickNav:
    zorder 300
    if quickNavShow == "Yes": #Make the quickNav at the bottom of the screen
        imagemap:
            ground "GUI/quickNav/quickBar.png" at Position(xpos = 555, ypos = 640)
            idle "GUI/quickNav/quickBar.png" 
            hover "GUI/quickNav/hover.png"
            
            hotspot (2, 0, 152, 76) clicked Jump("quickBar_Map")#Map-->should go to the main map screen
            hotspot (155, 2, 155, 74) clicked Jump("quickBar_Bag")#Bag--> should open the inventory screen
            hotspot (310, 3, 157, 73.0) clicked Jump("quickBar_Zal") #Zal--> goes to dialogue w/ Zal
            hotspot (464, 3, 157, 73.0) action ShowMenu('save') #Menu
                
        imagebutton:
            idle "GUI/quickNav/showHide_show.png" at Position (xpos = 1443 , ypos = 655)
            hover "GUI/quickNav/showHide_hideToggle.png"
            action [ SetVariable ("quickNavShow", "No") ]
        
    elif quickNavShow == "No": #QuickNav is hidden
        imagebutton:
            idle "GUI/quickNav/showHide_hide.png" at Position (xpos = 1443 , ypos = 655)
            hover "GUI/quickNav/showHide_showToggle.png"
            action [ SetVariable ("quickNavShow", "Yes")] #the QuickNav bar was hidden and the Player clicked showHide so now it should be shown
            
    elif quickNavShow == "NotAvail": #QuickNav is unavailable
        imagebutton:
            idle "GUI/quickNav/showHide_nA.png" at Position (xpos = 1443 , ypos = 655)       

##when the hotspots are clicked, these happen:
label quickBar_Zal:
    "You found Zal!"
label quickBar_Bag:
    $config.window_hide_transition
    call inventoryLabel
label quickBar_Map:
    $config.window_hide_transition
    call screen worldMap



#####################################################################
## The Main Map--> Navigating the World                            ##
#####################################################################
screen worldMap(): #the map navigation map
    zorder 100
    imagemap:
        ground "GUI/mainMapScreen/Map.png" at Position (xpos = 190, ypos = 0)
        hover "GUI/mainMapScreen/MapHoverspots.png"
        
        hotspot (446, 47, 351, 169) clicked Jump ("mountainClicked")
        hotspot (94, 45, 290, 162) clicked Jump ("lakeClicked")
        hotspot (877, 454, 293, 189) clicked Jump ("nadiasPlaceClicked")
        hotspot (876, 31, 291, 208) clicked Jump ("fvClicked")
        hotspot (957, 245, 262, 187) clicked Jump ("outskirtsClicked")
        hotspot (452, 291, 353, 289) clicked Jump ("farmClicked")
        hotspot (99, 213, 345, 461) clicked Jump ("forestClicked")

label worldMapLabel:
    show screen infoBar
    show screen showHideQuickNav
    call screen worldMap


label mountainClicked:
    "This is the Plataeu. Do you want to go there?"
    menu:
        "Yes":
            $travellingTime();
            $location = "Plataeu";
            call mountain_clearing
        "No":
            jump worldMapLabel
            
label lakeClicked:
    "This is the lake. Do you want to go there?"
    menu:
        "Yes":
            $travellingTime();
            $location = "Lake";
            call lake
        "No":
            jump worldMapLabel
            
label nadiasPlaceClicked:
    "This is Nadia's Lab Do you want to go there?"
    menu:
        "Yes":
            $travellingTime();
            $location = "Nadia's";
            call nadiasPlace
        "No":
            jump worldMapLabel
            
label fvClicked:
    "This is the Village. You're not allowed there!"
    jump worldMapLabel

label outskirtsClicked:
    "Sorry, the Outskirts aren't done yet.."
    jump worldMapLabel
    ##when implemented, should:
#   jump goingToTown 

label farmClicked:
    "Do you want to go home?"
    menu:
        "Yes":
            $travellingTime();
            $location = "My Farm";
            call goingToFarm
        "No":
            jump worldMapLabel

label forestClicked:
    "This is the forest. Do you want to go there?"
    menu:
        "Yes":
            $travellingTime();
            $location = "Forest";
            call forest
        "No":
            jump worldMapLabel

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

label goingToFarm:
    show screen infoBar
    show screen showHideQuickNav
    call screen farmMap

label unusedField_clicked:
    "This is the unusable field"
    
label usableField_clicked:
    "You can plant here"
    
label house_clicked:
    "Do you want to go home?"
    menu:
        "Yes":
            call wentHome
        "No":
            return
    
label p_Shed_clicked:
    "This is the procssing shed! Shall we go there?"
    menu:
        "Yes":
            jump pShedLabel
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

#screen outskirtsMap: #navigating the outskirts village
#    imagemap: 
#        ground ""
#        hover ""

#label goingToTown:
#    call scene outskirtsMap


