#init python: 
#    class Plant(self):
#        def __init__ ():
#            species = "string"
#        #this variable tracks the plant's current stage. Options are: "seed", "sprout", "middle", "fullgrown", and "harvestable"
#            currentStage = "seed";
#        #this variable keeps track of how many days it's been able to grow. It's used in the grow() function alongside the next three
#            growingDays = 0;
#        #these four variables set how long til the next stage. Example: from seed-date, it takes daysToSprout to get to the Sprout stage. Then it takes daysToMidGrowth to get to the midGrowth stage. 
#            daysToSprout = 1;
#            daysToMidGrowth = 2;
#            daysToFullGrowth = 2;
#            daysToHarvest = 1;
#        #these three variables determine what kind of care the plant needs at this moment
#            needsWater = False;
#            needsWeeding = False;
#            readyToHarvest = False;
        
#        #this method adds to the growingDays variable and triggers the next method, which changes the image if necessary
#        def growthTracker(self):
#            if self.needsWater == False and self.needsWeeding == False and self.readyToHarvest == False:
#                growingDays += 1;
#        #could add a penalty here later, for forgetting to care for the plant? lesser quality? it wilts?
#            else:
#                pass;
        
#        #this method changes the image if it needs to be changed and adjusts the growingDays as needed
#        def visibleGrowth(self):
#            if self.currentStage == "seed":
#                if growingDays == daysToSprout:
#                    #put in sprout image
#                    growingDays = 0;
#            elif self.currentStage == "sprout":
#                if growingDays == daysToMidGrowth:
#                    #put in midGrowth image
#                    growingDays = 0;
#            elif self.currentStage == "middle":
#                if growingDays == daysToFullGrowth:
#                    #put in fullGrowth image
#                    growingDays = 0;
#            elif self.currentStage == "fullgrown":
#                if growingDays == daysToHarvest:
#                    #put in harevestable image
#                    self.readyToHarvest = True;
#                    growingDays = 0;
    