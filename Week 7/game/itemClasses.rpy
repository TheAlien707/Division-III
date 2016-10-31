#####################################################################
## Item Class                                                      ##
#####################################################################
init python:
    class Item(store.object):
        def __init__(self, name, player=None, health = 0, stamina = 0, image="", cost=0):
            self.name = name
            self.player=player # which character can use this item?
            self.health = health # does this item restore hp?
            self.stamina = stamina # does this item restore mp?
            self.image=image # image file to use for this item
            self.cost=cost # how much does it cost in shops?
        def use(self): ##how is it used
            if self.health>0: #healing item
                player.health = player.health+self.hp
                if player.health> player.maxHealth: # can't heal beyond max health
                    player.health = player.maxHealth
                inventory.drop(self) # consumable item - drop after use
            elif self.stanima>0: #stamina restoring
                player.stanima = player.stanima + self.stanima
                if player.stanima > player.maxStamina: # can't increase stamina beyond max stamina
                    player.stanima = player.maxStamina
                inventory.drop(self) # consumable item - drop after use
                


