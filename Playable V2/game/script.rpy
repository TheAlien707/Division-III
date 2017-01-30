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
##tested, works fine
        global zalNeeded
        zalNeeded = False
        global zalsDescription
        zalsDescription = "default string"

##  a variables that determines when to show/hide the quickNav bar
##  "No" means hide, "Yes" means show, and "Unavail" means that it's not available currently
        quickNavShow = "No";     
    $playerName = renpy.input ("What is your name?")#"Kaipo"; ## going with a default to speed up tests--> input this later < renpy.input ("What is your name?") >
    jump portalTime

#first scene of the game yay
label portalTime:
##MC thinking to self before initial scene opens
    "A super cool intro is gonna be here, one day. For now..."
    "Let's just explore a bit."
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
    "Are those footsteps?"
    jump demo_Marrin

label demo_Marrin:
    show Marrin base 
    "It's Marrin! They're a fisherman and spend most of their time here."
    Marrin "Hey, [playerName]!"
    Marrin "What are you up to?"
    jump MarrinConvo

label MarrinConvo:
    menu:
        "I'm just exploring!":
            Marrin "Hey, that's pretty cool!"
            Marrin "I'd go with you but I probably should actually work today, haha."
            Marrin "Have fun!"
            $rude = False
        "I wanted to see what was at the lake":
            Marrin "Fish! Well, {i}in{/i} the lake, technically."
            Marrin "There's probably some other animals running about, snuzzies and the like, but I don't know much about them."
            Marrin "You'd have to ask Kahon. I dunno where's she's at right now though."
            $rude = False
        "What's it to you?":
            Marrin "Wow, uh.."
            Marrin "I take it back, I guess."
            $rude = True
    jump MarrinLeaves

label MarrinLeaves:
    if rude == False: ##if you're not rude, then this
        Marrin "I gotta get to fishing though, but you should come by later and hang out!"
        Marrin "See you later!!"
    else: ##if you are rude, so this
        Marrin "I'm gonna go... fish"
        Marrin "Maybe you should try it, later."
        Marrin "Might chill you out....."
    hide Marrin base
    "Looks like you're alone now."
    jump worldMapLabel

label forest:
    show screen infoBar
    show screen showHideQuickNav
    scene bg forestClearing at right with fade
    "This is the forest!"
    show Ayhen base
    jump AyhenConvo

label AyhenConvo:
    Ayhen "Oh, hello."
    Ayhen "I was actually hoping you'd come by."
    Ayhen "Can you deliver something to Nadia for me?"
    jump AyhenQuestion

label AyhenQuestion:
    menu:
        "What is it?":
            Ayhen "Oh, she just wanted some berries."
            Ayhen "I'd bring them myself, but Squiz needs my help with something and I'm not going to have time..."
            Ayhen "I'd really appreciate it if you could bring them."
            jump AyhenQuestion
        "Sure!":
            Ayhen "Thank you!"
            $playerBag.add(aspBerries)
            "Ayhen hands you a basket of Asp Berries!"
            $playerBag.add(dTFlower)
            $playerBag.add(dTFlower)
            $playerBag.add(dTFlower)
            Ayhen "...."
            Ayhen "Could you... also give her these? Just for her table. Cheer up her room, a bit?"
            "Ayhen hands you some flowers!"
            $said = "Yes"
            jump AyhenLast
        "I can't, sorry.":
            $said = "No"
            Ayhen "Ah, it's.. It's okay, I shouldn't have assumed."
            Ayhen "You're a farmer! Of course you're busy."
            Ayhen "I'll just... figure something out."
            jump AyhenLast
        "Do it yourself.":
            $said = "Rude"
            Ayhen "....."
            Ayhen "I'm sorry, you're right, I said I could do it... "
            Ayhen "I'll just... figure something out."
            jump AyhenLast

label AyhenLast:
    if said == "Yes":
        Ayhen "Thanks again, [playerName]."
        Ayhen "I need to get back to work now though."
        Ayhen "I'll see you around!"
    elif said == "No":
        Ayhen "I should probably go."
        Ayhen "Maybe if I skip lunch I'll have time..."
        Ayhen "Goodbye, [playerName]"
    elif said == "Rude":
        Ayhen "I... I'm going to get back to work."
    hide Ayhen
    "Well, we should probably get going then..."
    jump worldMapLabel

label nadiasPlace:
    show screen infoBar
    show screen showHideQuickNav
    scene bg nadiasPlace at right
    show Nadia standing
    n "Hey, [playerName]!"
    n "What can I do for you?"
    jump nadiaConvo
    
label nadiaConvo:
    menu:
        "I brought you something!":
            $creditDue = False
            jump deliveryTime
        "Ayhen asked me to deliver something.":
            $creditDue = True
            jump deliveryTime

label deliveryTime:
    $foundOut = False
    if creditDue == False: ##player lied and said they were bringing the stuff
        n "Really? That's nice of you. What is it?"
        menu: 
            "Some berries.":
                $playerBag.drop(aspBerries)
                n "Huh, I asked Ayhen to get me some of these."
                n "She must've forgotten."
                n "Thanks, [playerName]!"
            "A bouquet of flowers.":
                $playerBag.drop(dTFlower)
                $playerBag.drop(dTFlower)
                $playerBag.drop(dTFlower)
                n "You got me... flowers?"
                n "That's a bit odd."
                n "Don't get me wrong, I love flowers."
                n "Just... nevermind. Thanks, [playerName]."
            "It's berries and some flowers.":
                $playerBag.drop(aspBerries)
                $playerBag.drop(dTFlower)
                $playerBag.drop(dTFlower)
                $playerBag.drop(dTFlower)
                n "...These are the berries I asked Ayhen to get me."
                n "And these are my favorite flower."
                n "[playerName], when you said that you \"got me something\", did you mean {i}Ayhen{/i} asked you to bring me these?"
                n "That's not cool."
                $foundOut = True
    elif creditDue == True: ##player said stuff was from Ayhen
        n "Is it the berries I asked her for? She's so helpful."
        menu:
            "Yes, here they are.":
                $playerBag.drop(aspBerries)
                n "Perfect, I wanted to run some tests on these!"
                n "Did you know that each color tastes completely different?"
                n "And yet they all grow on the same plant!"
            "Yes, and some flowers":
                $playerBag.drop(aspBerries)
                $playerBag.drop(dTFlower)
                $playerBag.drop(dTFlower)
                $playerBag.drop(dTFlower)
                n "Oh, Ayhen. She always knows when I need more flowers."
                n "Isn't she so nice?"
    jump nadiaEnd
    
label nadiaEnd:
    if foundOut == False:
        n "I've got some stuff that I need to keep an eye on, [playerName], so I have to get back to it."
        n "Thanks for stopping by and dropping this off!"
        n "You should come by later and we can catch up."
    else:
        n "I'm pretty busy right now so I don't really have time to deal with your... nonsense."
        n "So to keep things brief: lying is a jerk move."
        n "Don't take credit from other people."
        n "And go away to think about what you did."
    jump worldMapLabel
    
    return
