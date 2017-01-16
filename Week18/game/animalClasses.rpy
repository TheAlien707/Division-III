#init python:
#    import random
    
    
    
#    #this is the base class of all the animals
#    class Animal (object):
#        def __init__ (self, name):
#            self.name = name;
#            self.species = "species";
#            self.shortLife = 0;
#            self.longLife = 0;
#            self.lifespan = 0;
#            self.age = 0;
            
#        ill = False;
#        meatProduced = 0;


#    #this function determines the sex of certain "mammalian" animals
#    def determineSex(name):
#    ##determine sex
#        sexNum = random.randint(1,5);
#    ##declares sex as female
#        if sexNum == 1 or sexNum == 2:
#            sex = "female";
#            canBePreg = True;
#    ##declares sex as intersex and determines if the Trog can bear young or produce them
#        elif sexNum == 3:
#            sex = "intersex";
#            fertilityNum = random.randint(1,3)
#            if fertilityNum == 1:
#                canBePreg = False;
#                canImpreg = False;
#                #^^this Trog is infertile^^
#            elif fertilityNum == 2:
#                canBePreg = True;
#                canImpreg = False;
#                #^^this Trog can bear young^^
#            elif fertilityNum == 3:
#                canBePreg = False;
#                canImpreg = True;
#                #^^this Trog can impregnate another Trog^^
#    ##declares sex as male
#        elif sexNum == 4 or sexNum == 5:
#            sex = "male";
#            canImpreg = True;
#        return sex
#        return canImpreg
#        return canBePreg
    
#    class Trog (Animal):
#        def __init__ (self, name):
#            self.name = name;
#            self.sex = "string";
#            self.canBePreg = False;
#            self.canImpreg = False;
#            self.species = "Trog"
#            self.shortLife = 2;
#            self.longLife = 4;
#            self.lifespan = random.randint(shortLife, longLife);
#        determineSex(name)





   
##    class Trog(Animal):
##        def __init__ (self, name):
##            self.sex = "string";
##            self.canBePreg = False;
##            self.canImpreg = False;
##        #standard stats
##            self.species = "Trog";
##        #determine lifespan of Trog    
##            self.shortLife = 1;
##            self.longLife = 4;
##            self.lifespan = random.randint(shortLife, longLife);
##        determineSex(name)

###function determines the sex of animals    


###method creates a random age for the wild animal to be
##    def wildAnimalAgeFinder(lifespan):
##        randomAge = (lifespan/2)+ random.randint(1,6);
##        while randomAge >= lifespan-3:
##            randomAge-= 1;
##        if randomAge < lifespan-3:
##            return randomAge;
    
##    def wildTrog(wildName):
##        wildTrog = Trog(wildName);
##        wildTrog.age = wildAnimalAgeFinder(wildTrog.lifespan);
##        checkAnimalDebug(wildName);
        
##    def checkAnimalDebug(animalName):
##        ageToSay = animalName.age;
##        speciesToSay = animalName.species;
##        sexToSay = animalName.sex;
##        nameToSay = animalName.name;
##        lifespanToSay = animalName.lifespan;
##        return ageToSay;
##        return SpeciesToSay;
##        return sexToSay;
##        return nameToSay;
##        return lifespanToSay;

    
    