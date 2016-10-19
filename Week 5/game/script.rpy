## The script of the game goes in this file.
init:
    pass
    

## The game starts here.

label start:
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
    jump nadDia
    
label nadDia:
    hide screen quickNav
    show Nadia standing
    n "hello I am an example dialogue from an NPC"
    "me" "hello I am the PC talking"
    n "where would you like to go?"
    menu:
        "I want to go to the forest!":
            jump farm
        "I want to go to the farm!":
            n "Well the farm isn't built yet so off to the forest you go"
            jump farm

label farm:
    hide screen quickNav
    scene bg forestClearing
    show Nadia standing at left
    show Squiz base at right
    "yay errybody is here"
    show Zal base at truecenter
    "whoops forgot Zal! She's floating so you can see here"

label mainMapScreen:
    call screen mainMap
    "is there a map?"
    #tried show screen didn't work. SCream?




    return
