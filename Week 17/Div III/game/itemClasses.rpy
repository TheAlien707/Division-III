######################################################################
### Item Class                                                      ##
######################################################################
#init python:
#    class Item(store.object):
#        def __init__(self, name, player=None, health = 0, energy = 0, image="", cost = 0, descript = "", type, animalFood):
#            self.name = name
#            self.player=player # which character can use this item?
#            self.health = health # does this item restore hp?
#            self.energy = energy # does this item restore energy?
#            self.image= image # image file to use for this item
#            self.cost= cost # how much does it cost in shops?
#            self.descript = "string" #what does Zal say when Player clicks on the item?
#            self.type = "string" #meat, plant, fish, dairy, cloth (feathers and wool count as),  
#            self.animalFood = False #boolean that determines if the item can be processed into animal food. will turn into one of three types of animal food if True (meat, plant, or fish, depending). 
#        def use(self): ##how is it used
#            if self.energy > 0: # it's for stamina restoring
#                player.energy = player.energy + self.energy
#                if player.energy > player.maxEnergy: # can't increase beyond max 
#                    player.energy = player.maxEnergy
#                inventory.drop(self) # consumable item - drop after use

######################################################################
### Foods                                                           ##
######################################################################



######################################################################
### Found Items                                                     ##
######################################################################