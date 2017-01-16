init: 
##image declaration
##backgrounds
    image bg forestClearing = "images/backgrounds/forestClearing.png"
    image bg lake = "images/backgrounds/lake.png"
    image bg mountain = "images/backgrounds/mountain.png"
    image bg nadiasPlace = "images/backgrounds/nadiasHouse.png"
    image bg storeAndBar = "images/backgrounds/storeAndBar.png"
    image bg farm = "images/backgrounds/farm.png"
##plants
    image plant plantedSeed = "images/plants/plantedSeed.png"
    image plant wiltedPlant = "images/plants/wiltedPlant.png"
    image aspberry sprout = "images/plants/AspBerry_Sprout.png"
    image aspberry mid = "images/plants/AspBerry_Growing.png"
    image aspberry fullGrown = "images/plants/AspBerry_FullGrown.png"
    image aspberry harvest = "images/plants/AspBerry_Harvest.png"
    image WD sprout = "images/plants/WD_Sprout.png"
    image WD mid = "images/plants/WD_MidGrowth.png"
    image WD fullGrown = "images/plants/WD_FullGrown.png"
##characters
    image Nadia sitting = "images/characters/Nadia_Sitting.png"
    image Nadia standing = "images/characters/Nadia_Standing.png"
    image Nadia working = "images/characters/Nadia_Working.png"
    image Marrin base = "images/characters/Marrin_Base.png"
    image Marrin boat = "images/characters/MarrinBoat.png"
    image Zyhon base = "images/characters/Zyhon.png"
    image Squiz base = "images/characters/Squiz_Standing.png"
    image Zal base = "images/characters/Zal_perched.png"
    image Ayhen working = "images/characters/Ayhen_working.png"
    image Kahon base = "images/characters/Kahon_base.png"
    image Nry base = "images/characters/Nry_lying.png"

##sprites (these are seperate because they will not appear in conversations)
    image Zyhek base = "images/characters/Zyhek.png"
    image Nahryn base = "images/characters/Nahryn.png"
##animals
    image Mlurr yellow_standing = "images/animals/Mlurr.png"
    image Trog purple_sitting = "images/animals/Trog_Sitting.png"
    image Keyu green_standing = "images/animals/Keyu.png"
    image Snuzzie green_standing = "images/animals/Snuzzie.png"
##character short names
    define n = Character ('Nadia')

#####################################################################
## Player Class Functions                                          ##
#####################################################################

## A function for changing energy (through different things like taking away for farming or giving for eating something)
##   it should receive variables like how much to take away or give
##   and there'd need to be a check to make sure that the player has enough energy to do the thing (Zal popping up to tell you no if you don't)


## A function for changing money (it should take "cost" as a variable)

#####################################################################
## Timekeeping                                                     ##
#####################################################################
init python:
    #adds an hour every 60 minutes
    def minutesToHours():
       if minutes >= 60:
           global minutes
           global hour
           minutes -= 60;
           hour +=1;

    #function adds 10 minutes whenever the player travels
    def travellingTime():
        global minutes
        minutes += 20;
        minutesToHours();
    
    #Function adds time for doing tasks around the farm
    #How much time is dependent on the difficulty of the action (easy, med, and hard)
    #Might later change that to more complexity later, but not worth it currently
    def farmActions(type):
        global minutes
        if type == "easy":
           minutes += 5;
        elif type == "med":
           minutes += 10;
        elif type == "hard":
            minutes += 20;
        minutesToHours();

    
## A function for keeping track of time
##   uses miltary time for easiness
##   would need to keep track of minutes and hours
##   and have a function to add an hour every 60 minutes
##   to keep time easy, use five minutes as the smallest increment

## Things that take time: 
##      traveling on the world map--> ~10 minutes?
##      caring for animals--> dependent on action? caring for, washing, getting produce, feeding...
##      caring for plants--> ditto ^^^
##      Talking to people? maybe five minutes per dialogue? Would be tricky to keep track of. Contemplate
##      Location specific actions--> fishing, hunting, etc. 
##      Eating! And processing stuff @ the PShed. Probably the smallest unit of time though. 
##      Forced bedtime @ Midnight to do rollover. Could punish players for hitting the forced bedtime by giving them half energy the next day. Maybe complicated though?


