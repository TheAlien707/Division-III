init python:
    showQuickNav = False

#####################################################################
## The Main Map--> Navigating the World                            ##
#####################################################################
screen mainMap: #the map navigation map
    imagemap:
        ground "GUI/mainMapScreen/Map.png" at center #Position(xpos = 252, ypos = 51)
        hover "GUI/mainMapScreen/MapHoverspots.png"
        
        hotspot (75, 58, 88, 100) clicked Jump("mountainClicked")
        hotspot (154, 150, 157, 121) clicked Jump ("lakeClicked")
        hotspot (445, 136, 72, 55) clicked Jump ("nadiaLabClicked")
        hotspot (537, 56, 139, 113) clicked Jump ("fvClicked")
        hotspot (465, 208, 287, 307) clicked Jump ("outskirtsClicked")
        hotspot (243, 406, 118, 116) clicked Jump ("farmClicked")
        hotspot (52, 246, 156, 218) clicked Jump ("forestClicked")
        

label mapScreen:
    #call screen mainMap
    scene bg ForestClearing
    "Is there a map here?"

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
            
label nadiaLabClicked:
    "This is Nadia's Lab Do you want to go there?"
    menu:
        "Yes":
            jump nadiaLab
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
    pass

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

        
        hotspot (5, 5, 148, 73) clicked Jump("quickBar_Map")#Map-->should go to the main map screen
        hotspot (160, 5, 148, 73) clicked Jump("quickBar_Bag")#Bag--> should open the inventory screen
        hotspot (316, 5, 148, 73) clicked Jump("quickBar_Zal") #Zal--> goes to dialogue w/ Zal
        hotspot (469, 5, 148, 73) action ShowMenu('save') #Menu

#debugging stuff
label quickBar_Zal:
    "You found Zal!"
label quickBar_Map:
    jump mainMapScreen
label quickBar_Bag:
    "Found the bag!"
        
