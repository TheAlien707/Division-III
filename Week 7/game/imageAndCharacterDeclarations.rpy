init: 
##image declaration
##backgrounds
    image bg forestClearing = "images/backgrounds/forestClearing.png"
    image bg lake = "images/backgrounds/Lake.png"
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
##items
    image food AspBerry = "images/items/AspBerry.png"
    image flower WeepingDragon = "images/items/WeepingDragon.png"
##character's short names and color
    define n = Character('Nadia',
                        who_color="#c8ffc8")
    define me = Character('Me')
    define s = Character('Squiz')
    define z = Character('Zal')
    define nr = Character('Nry')
    define k = Character('Kahon')
    define a = Character('Ayhen')
    define m = Character('Marrin')
    define zy = Character('Zyhon')
    define ve = Character('Village Elders')

#####################################################################
## Player Class                                                    ##
#####################################################################
init python: 
    class Player(renpy.store.object):
        def __init__(self, name, maxHealth = 0, maxStamina = 0):
            self.name=name
            self.maxStamina = maxStamina
            self.stamina = maxStamina
            self.maxHealth = maxHealth
            self.health = maxHealth

