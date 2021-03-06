image bg dormitory1-1 = "screens/dormitory/dormitory1-1.jpg"
image bg dormitory 1-2 = "screens/dormitory/dormitory1-2.jpg"
image bg dormitory2 = "screens/dormitory/dormitory2.jpg"
image bg dormitory3 = "screens/dormitory/dormitory3.jpg"
image bg dormitory4 = "screens/dormitory/dormitory4.jpg"
image bg dormitory5 = "screens/dormitory/dormitory5.jpg"
image bg dormitory6-1 = "screens/dormitory/dormitory6-1.jpg"
image bg dormitory6-2 = "screens/dormitory/dormitory6-2.jpg"
image bg dormitory6-3 = "screens/dormitory/dormitory6-3.jpg"
image bg dormitory6-4 = "screens/dormitory/dormitory6-4.jpg"
image bg dormitory6-5 = "screens/dormitory/dormitory6-5.jpg"
image bg dormitory6-6 = "screens/dormitory/dormitory6-6.jpg"
image bg dormitory6-7 = "screens/dormitory/dormitory6-7.jpg"
image bg dormitory6-8 = "screens/dormitory/dormitory6-8.jpg"
image bg dormitory7-1 = "screens/dormitory/dormitory7-1.jpg"
image bg dormitory7-2 = "screens/dormitory/dormitory7-2.jpg"
image bg dormitory7-3 = "screens/dormitory/dormitory7-3.jpg"
image bg dormitory7-4 = "screens/dormitory/dormitory7-4.jpg"
image bg dormitory7-5 = "screens/dormitory/dormitory7-5.jpg"
image bg dormitory8-1 = "screens/dormitory/dormitory8-1.jpg"
image bg dormitory8-2 = "screens/dormitory/dormitory8-2.jpg"
image bg dormitory8-3 = "screens/dormitory/dormitory8-3.jpg"
image bg dormitory8-4 = "screens/dormitory/dormitory8-4.jpg"
image bg dormitory9-1 = "screens/dormitory/dormitory9-1.jpg"
image bg dormitory9-2 = "screens/dormitory/dormitory9-2.jpg"
image bg dormitory9-3 = "screens/dormitory/dormitory9-3.jpg"
image bg dormitory10-1 = "screens/dormitory/dormitory10-1.jpg"
image bg dormitory10-2 = "screens/dormitory/dormitory10-2.jpg"
image bg dormitory10-3 = "screens/dormitory/dormitory10-3.jpg"
image bg dormitory11-1 = "screens/dormitory/dormitory11-1.jpg"
image bg dormitory11-2 = "screens/dormitory/dormitory11-2.jpg"
image bg dormitory12-1 = "screens/dormitory/dormitory12-1.jpg"
image bg dormitory12-2 = "screens/dormitory/dormitory12-2.jpg"
image bg dormitory12-3 = "screens/dormitory/dormitory12-3.jpg"
image bg dormitory12-4 = "screens/dormitory/dormitory12-4.jpg"
image bg dormitory13_1a = "screens/dormitory/dormitory13-1a.jpg"
image bg dormitory13_2a = "screens/dormitory/dormitory13-2a.jpg"
image bg dormitory13_1b = "screens/dormitory/dormitory13-1b.jpg"
image bg dormitory13_2b = "screens/dormitory/dormitory13-2b.jpg"
image bg dormitory14 = "screens/dormitory/dormitory14.jpg"
image bg dormitory15-1 = "screens/dormitory/dormitory15-1.jpg"
image bg dormitory15-2 = "screens/dormitory/dormitory15-2.jpg"
image bg dormitory16 = "screens/dormitory/dormitory16.jpg"


init:
    $ event("dormitory_introduction", "act == 'dormitory'", event.once(), event.only())
    if persistent.mod_disable_original_events == False:
        $ event("dormitory1", "act == 'dormitory'", event.choose_one('dormitory'), priority=200)
        $ event("dormitory2", "act == 'dormitory'", event.choose_one('dormitory'), priority=200)
        $ event("dormitory3", "act == 'dormitory' and inhibition > 90", event.choose_one('dormitory'), priority=190)
        $ event("dormitory4", "act == 'dormitory' and inhibition > 90", event.choose_one('dormitory'), priority=190)
        $ event("dormitory5", "act == 'dormitory' and inhibition > 90", event.choose_one('dormitory'), priority=190)
        $ event("dormitory6", "act == 'dormitory' and deviance > 0", event.choose_one('dormitory'), priority=180)
        $ event("dormitory7", "act == 'dormitory' and inhibition != 100", event.choose_one('dormitory'), priority=180)
        $ event("dormitory8", "act == 'dormitory'", event.choose_one('dormitory'), priority=200)
        $ event("dormitory9", "act == 'dormitory' and new_game_plus == True", event.choose_one('dormitory'), priority=180)
        $ event("dormitory10", "act == 'dormitory' and inhibition != 100", event.choose_one('dormitory'), priority=180)
        $ event("dormitory11", "act == 'dormitory' and inhibition != 100", event.choose_one('dormitory'), priority=180)
        $ event("dormitory12", "act == 'dormitory'", event.choose_one('dormitory'), priority=200)
        $ event("dormitory13", "act == 'dormitory' and deviance > 5 and inhibition < 100", event.choose_one('dormitory'), priority=180)


label dormitory_introduction:
    scene bg school_grounds2 with fade
    pov "Today is a special day for me and the rest of the staff here at Ashford. From now on, we can finally offer our students the opportunity to live near the heart of study."
    pov "It gives me great pleasure to introduce a person who is the embodiment of our Ashford spirit:"
    menu:
        "Susan Marina":
            show susan_marina normal at center
            susan_marina "Thank you [povTitle] [povLastName]. \nAs I stand here before you all, I remember my own years as a student. Though many changes has come to pass, I am really proud to be able to tell you this: Ashford is still a front runner in modern education."
            susan_marina "You students hold our banner high, you make us proud and you make us want to work even harder to assist you in becoming the pride of our nation. \nThank you all, I hope that our new dormitory will be another solid reason for future students to choose Ashford as their catapult into the wonderful world of knowledge."
    
        "Jack Drake" if new_game_plus == True:
            show jack_drake smile at center
            jack_drake "Whoaa, whazup kids?! This is gonna be so sweet, I mean - now you get the chance to actually sleep at school! And it's ok! \nI remember when I studied here, well - I didn't exactly study, and not here but that's not important right now. What's important is that we have each other, and that we know how to dance! As long as you dance, they can't take your shoes, right?"
            "students" "Uh, right..."
            jack_drake "Yeeeeehaaaaw!"
            pov "Eh, Jack..."
            jack_drake "I'm so happy right now, I only wish I could show you even more gratitude for showing up to celebrate me!"
            pov "Wait, no Jack, It's..."
            jack_drake "I'm gonna Jack-o-lantern you all!"
            "Students" "That sounds... weird..."
            jack_drake "Right in the schnaaauuuz!"
            pov "Jack!"
            jack_drake "Achtung!"
            pov "Oh, for the love of..!"
            "Students" "Run!"
            jack_drake "We're gonna drop it like it's cold!"
    return
    

label dormitory1:

    if behavior < 45:
        scene bg dormitory1-1 with fade
        "A new student is moving into the dormitory, I hope she will get accustomed quickly."
    else:
        scene bg dormitory1-2 with fade
        "When a student moves into the dormitory you can be sure that a helping hand and a new friend is close by."
        $ morale += 1
    $ population += 1
    return


label dormitory2:

    scene bg dormitory2 with fade
    girl "Umm, hello?"
    pov "Hello there, is everything okay?"
    if inhibition > 90:
        girl "Yeah [povTitle] [povLastName], but would you please knock before entering next time?"
        pov "Ah, yes, yes of course."
    else:
        girl "Yeah [povTitle] [povLastName], you just surprised me"
        pov "Oh, sorry about that."
    return


label dormitory3:

    scene bg dormitory3 with fade
    girl "Ah!"
    pov "Oh, sorry about that!"
    $ morale -= 1
    return


label dormitory4:

    scene bg dormitory4 with fade
    girl "Oh!"
    pov "I'm terribly sorry."
    girl "I-it's ok..."
    "You quickly make an exit."
    $ morale -= 1
    return


label dormitory5:

    scene bg dormitory5 with fade
    "Looks like some of the students are ready to bunk."
    pov "I'm sorry, I didn't realize..."
    "sleepy girl" "M-[povTitle] [povName]..."
    pov "Bye!"
    return


label dormitory6:

    scene bg dormitory6-1 with fade
    if deviance < renpy.random.randint(1,10) and inhibition > (85 + renpy.random.randint(1,10) ):
        if deviance < renpy.random.randint(1,10):
            if renpy.random.randint(1,2) == 1:
                "You walk into the dormatory and see a girl reading in bed."
                scene bg dormitory6-7
                girl "W-hoa..."
                scene bg dormitory6-8
                girl "Oh, [povTitle] [povLastName], I didn't hear you come in!"
                pov "Just passing through."
                "Hmm, I wonder what she was reading?"
                $ inhibition -= 1
            else:
                "You walk into the dormatory and see a girl reading in bed."
                scene bg dormitory6-7
                girl "W-hoa..."
                scene bg dormitory6-8
                girl "Oh, [povTitle] [povLastName], I didn't hear you come in!"
                pov "Just passing through."
                "Hmm, I wonder what she was reading?"
        else:
            "It's nice to relax a bit after school!"
            scene bg dormitory6-2
            girl "Hey!"
            pov "On my way."
            $ inhibition -= 1
    else:
        "Hey, it's that girl again."
        scene bg dormitory6-7
        girl "..."
        scene bg dormitory6-2
        "She's so into the magazine, she doesn't even know you're there!"
        girl "Mmm..."
        pov "Geez, she's really got a sweet little body..."
        scene bg dormitory6-3
        girl "Oh, that's it..."
        "She still doesn't now she's got a spectator. How is it possible?"
        scene bg dormitory6-4
        girl "Aaah!"
        pov "Oh Lord!"
        scene bg dormitory6-5
        girl "..."
        pov "Ah, I didn't... I mean..."
        girl "W-what!"
        "You turn around and get the hell outta there!"
        $ deviance += 1
        $ morale -= 1
    return
        
label dormitory7:

    scene bg dormitory7-1 with fade
    if inhibition < 85 and deviance > 10:
        girl "Gee [povTitle] [povLastName], you seem to have grown a likeness to the dormitory."
        pov "But of course, it was build thanks to me after all."
        scene bg dormitory7-2
        girl "That's right, you must be really proud!"
        pov "I take it you like the rooms?"
        girl "Oh yes, very much."
        pov "You seem to have a little more experience than your fellow students."
        girl "Ya think?"
        menu:
            "Sure, and really well developed too.":
                scene bg dormitory7-2
                girl "Oh hush!"
                pov "I'm dead serious, you're more of a woman than any of the other girls I've seen so far."
                scene bg dormitory7-3
                girl "I-I wish I could believe you."
                pov "Trust me, you're simply beautiful."
                girl "T-thank you, I'm just not used to..."
                pov "I never say stuff I don't mean. You're a true beauty, and I bet all the boys glance at your sexy curves."
                scene bg dormitory7-4
                girl "You're so sweet..."
                pov "And you're so hot."
                girl "Oh, this is so strange... but it feels so sexy!"
                pov "I'm gonna go now, but I'd really love to have a glimpse of that sweet body of yours first."
                girl "I-I'm not sure..."
                menu:
                    "It would surely make me dream about you, not only day dreaming that is.":
                        scene bg dormitory7-3
                        girl "I-I think you'd better go before someone walks in on us."
                        if new_game_plus == True:
                            "What a fucking waste of sweet talk..."

                    "I wouldn't want you to feel uncomfortable, I just... your eyes are so beautiful...":
                        girl "Mhm, you're really sexy."
                        pov "God, you make me so hard."
                        girl "*gasp*"
                        scene bg dormitory7-5
                        "Sweet maker... they're perfect!"
                        girl "B-but don't tell anybody about this!"
                        pov "I would never."
                        "This day... Think I'll mark it in my calendar."

            "I'm serious! I know experience when I see it.":
                scene bg dormitory7-3
                girl "I-I'm not that kind of girl. I don't date a lot of boys."
                pov "You misunderstood me, I..."
                girl "It's getting late and you really shouldn't be here."
                pov "I'm truly sorry if I offended you in some way."
                girl "..."
                "Just great..."
    else:
        if renpy.random.randint(1,2) == 1:
            girl "It's nighty night-time!"
            pov "Sweet dreams."
        else:
            girl "Oh, it's time to go to bed!"
            pov "Already?"
            scene bg dormitory7-2
            girl "Mhm, it's important to get proper rest."
            pov "Good girl."
    return


label dormitory8:

    if renpy.random.randint(1,2) == 1 and new_game_plus == True:
        scene bg dormitory8-3 with fade
        pov "Hello girls!"
        girl1 "*giggle*"
        girl2 "*sigh*"
        pov "Oh, I won't bother you. I was just wandering around, thinking about the unscheduled test you're going to have tomorrow... ah chucks! Did I say that out loud?"
        scene bg dormitory8-4
        girl1 "W-what?"
        girl2 "T-test?"
        pov "It was supposed to be a surprise. Just forget I said anything, ok?"
        girls "..."
    else:
        scene bg dormitory8-1 with fade
        pov "Good evening girls, getting ready for bed already?"
        girl1 "Well, it has been a long day..."
        pov "And you've earned some rest!"
        scene bg dormitory8-2       
        girl1 "*giggle*"
        girl2 "..."
    return


label dormitory9:
    
    scene bg dormitory9-1 with fade
    "girlie" "[povTitle] [povName], I'm so glad to see you!"
    pov "Ok? Is there something wrong?"
    "girlie" "Well, it's so awfully dark and..."
    pov "Yes, it's a pitch black in here."
    "girlie" "[povTitle] [povName]..."
    "girlie" "..."
    "girlie" "Is there a Boogeyman?"
    pov "Oy! That was unexpected."
    "girlie" "What?"
    menu:
        "Oh, nevermind. Dry those tears sweetie, there's nothing to be afraid of here.":
            scene bg dormitory9-2
            "Girlie" "Are you sure?"
            pov "I can asure you that no Boogeyman will ever find his way to Ashford while I'm principal."
            "girlie" "Really?"
            pov "Really."
            "girlie" "Pinkie promise?"
            pov "Eh, yeah, pinkie... promise..."
            "This seems to calm her somewhat. As you leave, you start to wonder if there actually is such a thing as a Boogeyman."
            pov "One weird evening, coming up."
            $ morale += 1

        "Well, scientists have never found any evidence pointing in that direction.":
            "Girlie" "But my friend said that he comes at night when you least expect it!"
            pov "In this case, I'd put my money on the scientists."
            "Girlie" "But can you trust the scientists?"
            pov "See THAT'S a different story."
            "Girlie" "Wha..?"
            pov "You see, scientists usually work in the direction of the money."
            scene bg dormitory9-2
            "Girlie" "What does that mean?"
            pov "It means that if there are strong, monetary forces at large, some scientists tend to let their work adjust to who's paying the bill."
            "Girlie" "So... If the Boogeyman had more money than the... Eh..."
            pov "Monetary forces."
            "Girlie" "Monetary forces, right. If so, the scientists would listen to HIM?"
            pov "Well, in theory, I guess you could say that."
            "Girlie" "So what if he EXISTS, and just pay the scientists so that they will say he DOESN'T?"
            pov "I guess we'll never know for sure, unless..."
            "Girlie" "Unless?"
            pov "Haha, unless you don't wake up in the morning!"
            scene bg dormitory9-3
            "girlie" "Oh!"
            pov "Well, I'll be on my way now. Don't let the bed bugs bite. Or the Boogeyman for that matter, bwahahahaha!"
            scene bg dormitory9-1
            "Girlie" "I don't want to..."
            "You walk away with a smile on your face. Your students are so imaginative and open minded!"
            "*singing* Hush now, hush – here comes the Boogeyman!"
            $ morale -= 1
    return


label dormitory10:
    
    scene bg dormitory10-1 with fade
    "You stumble in on a girl who is ether examining her underwear or her body."
    menu:
        "Leave as quietly as possible.":
            "You realize that there is a thin line between a students trust and her disliking."

        "Just a few more seconds...":
            "It looks like she's measuring or comparing herself..."
            girl "He said I was pretty... But I KNOW that Yuki's got a thing for him."
            pov "Oh boy..."
            scene bg dormitory10-2
            girl "I just wish I had a better body..."
            pov "This is ridiculous!"
            menu:
                "Walk away before it's to late!":
                    "As you leave, you think to yourself about how fragile it can be to be young."

                "Only a couple of seconds more...":
                    girl "Perhaps he's not into me at all. Are my breasts to small?"
                    pov "I better bite my tongue."
                    girl "Am I starting to get fat?"
                    pov "Are you serious?"
                    scene bg dormitory10-3
                    girl "I'm really nothing special at all..."
                    pov "This is to much."
                    "You leave, convinced that someone will talk some sense into her and tell her that she's beautiful."
                    pov "To be young..."
    return


label dormitory11:
    
    scene bg dormitory11-1 with fade
    "In their spare time, some of the students express themselves with rather spectacular outfits."
    scene bg dormitory11-2
    girl "Hey, don't sneak up like that!"
    pov "My bad, I'll just go now."
    $ morale += 1
    return
    
    
label dormitory12:
    if renpy.random.randint(1,3) == 1:
        scene bg dormitory12-1 with fade
        "It's a good feeling when school's done and you can take some time to just relax."
    else:
        if renpy.random.randint(1,2) == 1:
            scene bg dormitory12-2 with fade
            "Sometimes you wish that the lessons would never end."
        else:
            scene bg dormitory12-3 with fade
            "You almost run into a wide eyed girl clutching her bag real tight."
            scene bg dormitory12-4
            girl "Oh!"
            if evil_points > 0:
                pov "Hey, stop ogling the floor when moving, will you?"
                girl "Yikes!"
                pov "*grumble grumble*"
                $ morale -= 1
            else:
                pov "Whoopsie daisey!"
    return


label dormitory13:
    
    $ randImg = renpy.random.choice(["a", 'b'])
    $ renpy.show("bg dormitory13_1"+randImg)
    with fade
    "glasses" "Hey Uki, check out my..."
    $ renpy.show("bg dormitory13_2"+randImg)
    "glasses" "Oh! You're not Uki!"
    menu:
        "No I am not.":
            pov "Haha, I'm afraid not!"
            "glasses" "..."
            "She doesn't seem to respond that well to your disarming sense of humour."
            $ morale -= 1

        "Yes I am!":
            pov "Actually, my full name is Uki [povLastName]! Isn't that weird?"
            "glasses" "That IS weird!"
            $ renpy.show("bg dormitory13_1"+randImg)
            "You laugh it off and then you leave."

        "Disappointed?" if evil_points > 0:
            pov "Sorry to make you disappointed, but I gotta tell you that I'M not."
            "glasses" "R-really? I-I mean thanks!"
            "This will make dreaming a whole lot sweeter tonight!"
    return


label dormitory14:
    scene bg dormitory14 with fade
    "It feels so good retiring to the dorm, filling your head with fresh air and positive thinking!"
    return


label dormitory15:
    scene bg dormitory15-1 with fade
    "pink" "Then she said that she found my speech really interresting and that It certainly didn't pass unnoticed by the audience!"
    "blue" "Good for you!"
    "pink" "Yeah! She said that the only time she's ever heard something like that was when she watched these old retrospective movies with her grandfather."
    "blue" "Must be really cool movies."
    "pink" "I guess so! Her grandfather is from Germany and apparently fought in some big war."
    "blue" "That makes it even more impressive, I mean, he must have heard a lot of speeches."
    scene bg dormitory15-2 with fade
    "pink" "Wait a minute..."
    "blue" "And so sweet of her to draw that picture of you holding a speech in fron of that crowd of people!"
    "pink" "Yeah... but she spelled my name wrong."
    "blue" "She did?"
    "pink" "My family name is Hiller, you know."
    "blue" "What did she write?"
    "pink" "I can't remember..."
    scene bg dormitory15-1 with fade
    "pink" "But I put it up in my locker!"
    $ academics -= 1
    return


label dormitory16:
    scene bg dormitory16 with fade
    "After a hard days work, a cuddle with someone you care for refills the energy."
    return
    
