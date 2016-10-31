## The script of the game goes in this file.
init:
    pass
    

## The game starts here.

label start:
    python: 
        pass
        #pcName = renpy.input ("what is your name?")
        #player = Player(pcName, 100, 50)
        #inventory = Inventory()
    
    show screen quickNav
##MC thinking to self before initial scene opens
    "Not a trace for two months, so I guess the police are just... giving up." 

# show dorm_room
    "I guess I better get ready for cl-"
    "Vweerym!" with vpunch
    
    "!! What was that?!"
    
    "NeeeenRYM!" with vpunch
    
    "It's coming from Nadia's closet... what is it?"
    
    "Let's pretend I continued  the dialogue. The Player finds a portal and falls in."
    
    "AHHHH!" with vpunch
    jump testingScene

label testingScene:
    "blargh"


label worldMap:
    show screen worldMap
    show screen quickNav
    $renpy.pause()
    
label inventoryScreen:
    show screen inventory
    show screen quickNav
    $renpy.pause()
    
label mountain_clearing:
    $hideTheScreens()
    pass

label lake:
    $hideTheScreens()
    pass
    
label nadiasPlace:
    $hideTheScreens()
    pass
    
label outskirts:
    $hideTheScreens()
    pass
    
label farm:
    $hideTheScreens()
    show screen farmMap
    show screen quickNav
    $renpy.pause()

label forest:
    $hideTheScreens()
    pass
    
    





    return
