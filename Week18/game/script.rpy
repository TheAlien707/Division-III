##"start" runs every time the game is loaded

label start:
    init python: 
##  the following are different player stats:
        global maxEnergy;
        maxEnergy = 100;
        global currentEnergy;
        currentEnergy = 100;
        global hour 
        hour = 6;
        global minutes 
        minutes = 30;
        global money;
        money = 0;
        global date;
        date = 0;
        global location;
        location = "";
##  a variable that determines if Zal is giving a description or not
        global zalNeeded
        zalNeeded = False
##  a variables that determines when to show/hide the quickNav bar
##  "No" means hide, "Yes" means show, and "Unavail" means that it's not available currently
        quickNavShow = "No"; 
    $playerName = "Kaipo"; ## going with a default to speed up tests--> input this later < renpy.input ("What is your name?") >
    
###Inventories:
#  #playerBag is the inventory of all the items in their backpack currently
#    $playerBag = Inventory()
    
#  #playerChest is an extended inventory; the chest at the PC's house can hold items too
#    $playerChest = Inventory()
    
#  #Squiz's store has an inventory, but it will work a little differently than the players
#  #it has all the same functionality but it gets "reset" at rolloever--> she only stocks her usual stuff 
#  #and she only has a set amount of $$ each day. When the player sells to her, 
#  #she'll have that in stock for that day only
#    $SquizStore = Inventory()
    
    jump portalTime

#first scene of the game yay
label portalTime:
##MC thinking to self before initial scene opens
    "~~skipping beginning scenes~~"
    jump worldMapLabel
    
    
label mountain_clearing:
    show screen infoBar
    show screen showHideQuickNav
    scene bg mountain at right with fade
    "You're at the mountain!"

label lake:
    show screen infoBar
    show screen showHideQuickNav
    scene bg lake at right with fade
    "You're at the lake!"
    show Marrin base
    "This is Marrin. They work here!"
    $renpy.pause()

label forest:
    show screen infoBar
    show screen showHideQuickNav
    scene bg forestClearing at right with fade
    "This is the forest!"
    $renpy.pause()

label nadiasPlace:
    show screen infoBar
    show screen showHideQuickNav
    scene bg nadiasPlace at right
    show Nadia standing
    n "Hey, [playerName]! This is my house!"

    return
