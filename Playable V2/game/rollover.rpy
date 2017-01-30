#this script handles all the functions relevant to "rollover"--> the changing of the day
#It is called EITHER at midnight (24:00) or when the Player goes to sleep in their house

#########################################################################
## Time Maintenance                                                    ##
#########################################################################

#Time should be reset to 6:00
#Day should have one added to it

#########################################################################
## Fish                                                                ##
#########################################################################

#Breeding Function
#       For every two fish present, there is a chance (should be no higher than 60%
#               but no lower than 30%
#       For them to breed and produce a clutch of eggs (randomly 2-4 eggs)
#       Those eggs hatch to full-grown after ~3 days

#       There should never be more than ~20 fish in the tank

#Dirtiness Function
#       Tank becomes dirty every few days depending on how many fish there are + randomness
#       The more fish = the more often to clean it
#       With max fish = once a day cleanings

#########################################################################
## Gummzies                                                            ##
#########################################################################

#Breeding Function
#       Only two gummzies will breed at a time so this only needs to run once
#       But each night there is a 30%-40% chance that the gummzies will produce a Cluster
#               There should never be more than one Cluster at a time though
#       Which will hatch into full-grown 6-10 Gummzies after ~4 days
#       There should never be more than ~30 Gummzies in the tank

#Dirtiness Function
#       Tank becomes dirty every few days depending on how many Gummzies there are + randomness
#       The more Gummzies = the more often to clean it
#       With max Gummzies = once a day cleanings

#       Whenever cleaned, it should call the Happniess function to add to the in-a-row variable
#       If it's not clean at rollover, it should reset the in-a-row variable

#Happiness Function
#       This determines on a scale of 1-100, how happy the Gummzies are
#       Happier Gummzies are more likely to produce Sweet Goo
#       The math should be based on how many gummzies there are (more = bad) and how many days-in-a-row they've been clean (more = good)

#Sweet Goo Function
#       This decides if the Gummzies will produce goo that night or not
#       It compares the Happniess % to a random number (1-100 or something)
#       If their Happiness is higher than the number, then they'll produce goo
#       How much goo depends on how many Gummzies there are (more Gummzies = more goo)
#               Probably something like one unit per three Gummzies
#       If there is sweet goo in the tank when rollover is called, then the Gummzies eat it (it goes away)

#########################################################################
## Animals                                                             ##
#########################################################################

#Old Age Function
#       Age should go up by one
#       If they reach their maximum age, then they die
#       They are removed from the game and the player gets a scene with the corpse the next morning

#Food Check Fucntion
#       If the animal has been fed, this calls the "Production Function"
#       Otherwise, it calls the "Starvation Function"

#Production Function"
#       Depending on what the animal produces, it does one of three things
#       If the animal produces a daily item, it resets the "harvested" boolean so it can be harvested again
#       If the animal produces an "after time" item, it subtracts from the variable tracking how many days til harvest time
#               Once that variable reaches 0, then the "harvest boolean" gets reset so it can be harvested
#       For meat producers, there's a days-fed variable. More days fed = more meat at butcher time. 

#Starvation function
#       A variable that tracks how many days the animal has starved goes up by one
#       A random number 1-10 is selected
#       Compares the two numbers and if the Starvation variable is higher than the random one, the animal dies
#       Otherwise, it simply doesn't produce anything that day

#########################################################################
## Plants                                                              ##
#########################################################################

#Water Check Function
#       If True, then calls "Growing Function"
#       If False, then it calls the "Withering Function"

#Growing Function
#       "growingDays" is added to and is compared to "days to sprout/growth/etc" 
#       It updates the image accordingly (look @PlantClasses)
#       And it checks to see if it's harvest time

#Withering Function
#       "dry days" variable goes up one
#       Depending on the rarity of the plant, a random number 1-5 is selected
#       "Dry Days" is compared to the random number; if it's bigger than it, the plant dies
#       Otherwise it just doesn't get a "growing day" 

