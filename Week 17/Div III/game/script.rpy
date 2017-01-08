## The script of the game goes in this file.
init:
    image blue = Solid("#5F9F9F")
    

##"start" runs every time the game is loaded

label start:
    python: 
        playerName = renpy.input ("What is your name?")
        #player = Player(playerName, 100, 50)
        #inventory = Inventory()
        renpy.free_memory()
    #show screen quickNav
    jump portalTime

#first scene of the game yay
label portalTime:
##MC thinking to self before initial scene opens
    "Not a trace for two months, so I guess the police are just... giving up." 

# show dorm_room
    show screen quickNav
    "I guess I better get ready for cl-"
    "Vweerym!" with vpunch
    
    "!! What was that?!"
    
    "NeeeenRYM!" with vpunch
    
    "It's coming from Nadia's closet... what is it?"
    
    "Let's pretend I continued  the dialogue. The Player finds a portal and falls in."
    
    "AHHHH!" with vpunch
    jump firstScene
    
label firstScene:
    "Let's go to the map..."
    call screen worldMap
    
label mountain_clearing:
    scene bg mountain at right with fade
    show screen quickNav
    show screen infoBar
    "You're at the mountain!"

label lake:
    show screen quickNav
    show screen infoBar
    scene bg lake at right with fade
    "You're at the lake!"
    show Marrin base
    "This is Marrin. They work here!"
    $renpy.pause()
    
label outskirts:
    show screen quickNav
    show screen infoBar
    scene blue
    "The Outskirts aren't implemented yet!"
    $renpy.pause()
    jump worldMap

label farmTime:
    show screen quickNav
    show screen infoBar
    call screen farmMap
    $renpy.pause

label forest:
    show screen quickNav
    show screen infoBar
    scene bg forestClearing at right with fade
    "This is the forest!"
    $renpy.pause()

label nadiasPlace:
    show screen quickNav
    show screen infoBar
    scene bg nadiasPlace at right
    show Nadia standing
    n "Hey, [playerName]! This is my house!"

    return
