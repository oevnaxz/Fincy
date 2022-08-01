label startChapter1:
    $ save_name = "Chapter 01: The Rich Don’t Work for Money"
    #ABSTRACT
    scene plainWhite with fade
    """
    After being transported to the real world, I had a hard time to get accustomed to being a kid again as I did not get a solid explanation as to how I am still alive.
    
    Nonetheless, I maybe morally confused but I'm still glad that I was given another chance at life.
    """

    #FLASH ANIMATION: Meeting his parents, Meeting his bestfriend, Going to School

    """
    After a few days, I have been getting accustomed to my new life and is now dead set on my new journey.

    I promised myself to do all the things I can to be the man and persona I've met on the \"{i}empty space{/i}\" right after I lose my life on the hospital bed.
    """

    #Flashing the Title Screen
    window hide
    show screen title_screen(_("{b}LESSON 1: THE RICH DON’T WORK FOR MONEY{/b}"))
    with dissolve
    pause 2
    hide screen title_screen
    with dissolve
    window auto

    scene kidMCLivingRoom with fade
    play music "audio/bgm/kidMCHouse.ogg" fadein 0.5 volume 0.25
    show kidMC defaultEmotion with dissolve 
    persistent.kidMC "Dad, can you tell me how to get rich?"

    show kidMC unfocused at left with move
    show biologicalDad surprised at right with moveinright
    play sound "audio/sfx/newspaperFlip.mp3" volume 0.5
    biologicalDad "Huh, that's new... why'd you wanna get rich all of a sudden, son?"

    show biologicalDad unfocused at right
    show kidMC defaultEmotion at left
    with dissolve
    persistent.kidMC "Because today, Jimmy’s mom drove up in their new {i}Cadillac{/i}, and they were going to their beach house for the weekend."

    show kidMC unfocused at left
    show biologicalDad confused at right
    with dissolve
    biologicalDad "Well, what does that have to do with you?"

    show biologicalDad unfocused at right
    show kidMC serious at left
    with dissolve
    persistent.kidMC "Because me and Mike were not invited because we were poor kids!"

    show kidMC unfocused at left
    show biologicalDad surprised at right 
    with dissolve
    biologicalDad "They said that? Wow..."
    show biologicalDad defaultEmotion at right with dissolve
    biologicalDad "..."
    show biologicalDad smiling at right with dissolve
    play sound "audio/sfx/newspaperFlip.mp3" volume 0.5
    biologicalDad "Well, son.. if you want to be rich, you have to learn to make money."

    show biologicalDad unfocused at right
    show kidMC defaultEmotion at left 
    with dissolve
    persistent.kidMC "Then how do I make money?"

    show kidMC unfocused at left
    show biologicalDad smiling at right 
    with dissolve
    play sound "audio/sfx/chuckle.mp3" volume 0.5
    biologicalDad "Well, use your head, son."

    show biologicalDad unfocused at right
    show kidMC confused at left 
    with dissolve
    persistent.kidMC "{i}What? That's it? It's like you yourself don't know the answer.{/i}"
    stop music fadeout 1.0

    #TRANSITION INTO ANOTHER DAY
    scene plainWhite with fade
    play sound "audio/sfx/clockTicking.mp3" volume 0.5
    "The next day."
    stop sound fadeout 0.5

    scene afternoonParkNoBench with fade
    play music "audio/bgm/afternoonParkNoBench.ogg" fadein 0.5 volume 0.25
    show mike smiling with dissolve
    "During the days of me getting accustomed to my new life, I've met my supposed-to-be best friend on a park. His name is Mike."
    "And as I remember, the {i}alternate{/i} me I've met after I died mentioned that this guy's dad would make the both of us successful."
    "Do not get me wrong as I did not befriend him because of that. We actually had a lot of things in common. Plus, nothing's wrong with having a companion anyways."
    "Having a companion might help us understand things better. So in a way, it's a win-win situation for the both of us."

    scene plainWhite with fade
    "By some twist of fate, Mike and I attended the same school where the rich people enrolls their kids. Me and Mike were the only poor kids in the school."
    "It's not that we're literally poor as both our parents provided us with the basics like food, shelter, and clothing."
    "But we felt like it because the other boys always had new baseball gloves, new bicycles, new consoles, new everything."

    scene afternoonParkNoBench with fade
    show mike sad with dissolve
    mike "Hey, {b}[persistent.kidMC]{/b}! You were spacing out for a moment." with vpunch

    show mike unfocused at right with move
    show kidMC thinking at left with moveinleft
    persistent.kidMC "Oh, hey Mike."

    show kidMC unfocused at left
    show mike defaultEmotion at right 
    with dissolve
    mike "So, what do we do to make money?"

    show mike unfocused at right
    show kidMC thinking at left 
    with dissolve
    persistent.kidMC "Honestly, I really have no idea."

    show kidMC unfocused at left
    show mike sad at right
    with dissolve
    mike "..."

    show mike unfocused at right
    show kidMC smiling at left 
    with dissolve
    persistent.kidMC "{size=+5}{b}BUT{/b}{/size}, do you want to be my business partner?" with vpunch

    show kidMC unfocused at left
    show mike surprised at right 
    with dissolve
    mike "Yup! Sure!"

    hide kidMC
    hide mike 
    with dissolve

    "Since it was weekend, Mike and I spent our afternoon, thinking of ways on how we could earn money."
    "We often talked thought about what the {i}cool{/i} guys could be doing right now on Jimmy's beach house."
    "It's painful for us to be an {i}outcast{/i}, but that served as our fuel and inspiration to keep thinking of a way to make money."

    scene plainWhite with fade
    #FLASH ANIMATION OF DIFFERENT IDEAS OF WAYS TO MAKE MONEY
    "Finally, after hours of thinking, Mike suddenly remembered an idea from a science book he had read."

    scene afternoonParkNoBench with fade
    show mike surprised with dissolve
    mike "I've got an idea! {b}[persistent.kidMC]{/b}! Hear me out, I think you'll like this!"
    hide mike with dissolve
    
    #FLASH ANIMATION mikeWhispering
    "*whispers*"
    #hide mikeWhispering
    
    show mike unfocused at right
    show kidMC surprised at left 
    with dissolve
    persistent.kidMC "Hmm, sounds great! Here, give me your hand."
    
    hide kidMC
    hide mike 
    with dissolve
    
    #FLASH ANIMATION shakingHands
    persistent.kidMC "Here's to our partnership's first business!"
    stop music fadeout 1.0

    scene plainWhite with fade
    "After finalizing our plan on how we would make money, we immediately started on it."
    "Not wasting even a second - that's how eager and determined we are."

    scene morningNeighborhood with fade
    play music "audio/bgm/neighborhood.ogg" fadein 0.5 volume 0.25
    play sound "audio/sfx/knockingOnDoor.mp3" volume 0.5
    "*knocks*"
    play sound "audio/sfx/openDoor.mp3" volume 0.5
    "Upon opening their doors, the neighbors greeted us with puzzled looks. However, most of them consented with a smile not long after."
    show neighbor smiling with dissolve
    neighbor "Hello kids! What are you going to do with all the {i}tubes{/i} you're collecting?"
    hide neighbor with dissolve

    show kidMC smiling at left with dissolve
    show mike smiling at right with dissolve
    persistent.kidMC "We're sorry our dear neighbors, but we can't tell ya!"
    mike "It's a business secret!"
    stop music fadeout 0.5

    scene plainWhite with fade
    "As weeks pass by, we didn't stop collecting toothpaste tubes to the point that my own mom grew distressed as we had selected our workplace next to her washing machine."
    "And finally..."

    scene backyard with fade
    play music "audio/bgm/backyard.ogg" fadein 0.5 volume 0.25
    show biologicalMom threateningSmile with dissolve
    biologicalMom "{b}WHAT{/b} are you boys doing?" with sshake
    show biologicalMom defaultEmotion with dissolve
    biologicalMom "And I don't want to hear again that it's a business secret. Do something with this mess, or I'm going to {b}THROW{/b} it all out."

    show biologicalMom unfocused at right with move
    show kidMC defaultEmotion at left with moveinleft
    persistent.kidMC "Please, mom. Just one more week."
    persistent.kidMC "We're waiting on some of our neighbors to finish or empty their toothpaste so we could have their tubes."

    show kidMC unfocused at left
    show biologicalMom defaultEmotion at right 
    with dissolve
    biologicalMom "Alright, one week!"
    biologicalMom "I'll give you boys one week to tend to this, or I'll throw these all out."
    
    hide biologicalMom
    hide kidMC 
    with dissolve
    
    show kidMC smiling with dissolve
    persistent.kidMC "Well, would you look at that, Mike. Our newly formed partnership is now being threatened with an eviction by my own mom."
    persistent.kidMC "Never felt this pressure once in a while, kinda missed it."

    show kidMC unfocused at left with move
    show mike confused at right with moveinright
    mike "Huh.. kinda missed it?"

    show mike unfocused at right
    show kidMC flustered at left 
    with dissolve
    persistent.kidMC "Uhh, haha... did I say something?"
    show kidMC smiling at left with dissolve
    persistent.kidMC "Don't mind it, let's start the production right away, partner!"
    persistent.kidMC "{i}Whew... I should be careful with my choice of words for now, nearly blew off my cover{/i}."

    scene backyard with fade
    play sound "audio/sfx/turnOffCarEngine.mp3" fadein 0.5 volume 0.5
    play sound "audio/sfx/burning.mp3" volume 0.5
    show biologicalDad surprised with dissolve
    biologicalDad "Hey there boys. What are you guys doing?"
    stop sound fadeout 0.5
    show biologicalDad unfocused at right with move
    show kidMC serious at left with moveinleft
    menu:
        "... (Continue with what you're doing.)":
            call dadPeeksOperation
        "We're doing our business operation, dad!":
            call explainOperation
    
    show kidMC unfocused at left
    show biologicalDad confused at right 
    with dissolve
    biologicalDad "What are these for anyways? Is this for a science project?"

    show biologicalDad unfocused
    show kidMC serious 
    with dissolve
    persistent.kidMC "Honestly dad, we're doing what you told me to do. We're going to be rich."
    hide biologicalDad with moveoutright

    show kidMC unfocused with dissolve
    show mike smiling at right with moveinright
    mike "Yup, your son and I are business partners! We formed our business partnership weeks ago."

    show kidMC smiling at left
    show mike unfocused at right 
    with dissolve
    persistent.kidMC "Anyways Mike, may I do the honors of breaking the mold?"

    show mike smiling at right 
    show kidMC unfocused at left 
    with dissolve
    mike "Sure thing!"

    hide biologicalDad 
    hide kidMC 
    hide mike 
    with dissolve
    
    #FLASH ANIMATION breakingPlasterMoldWithHammer
    play sound "audio/sfx/stoneBreaking.mp3" volume 0.5
    "*breaks*"
    window hide
    #FLASH ANIMATION nickelIngot with dissolve
    play sound "audio/sfx/nickelPing.mp3" volume 0.5
    pause 1.5
    #hide nickelIngot
    window auto
    
    show biologicalDad surprised with dissolve
    biologicalDad "Oh no! You're casting nickels out of lead!" with vpunch

    show biologicalDad unfocused at right with move
    show mike smiling at left with moveinleft
    mike "Yup! We're going to be rich!"

    show biologicalDad smiling at right
    show mike unfocused at left 
    with dissolve
    play sound "audio/sfx/chuckle.mp3" volume 0.5
    biologicalDad "Haha, you kids. What you're doing is practically illegal."
    hide biologicalDad with dissolve

    show mike defaultEmotion at right with move
    show kidMC confused at left with moveinleft
    persistent.kidMC "Huh? How?"

    hide mike
    hide kidMC 
    with dissolve

    show biologicalDad smiling with dissolve
    biologicalDad "Well.. mainly because you're counterfeiting an item."
    biologicalDad "Basically, you boys are trying to {i}imitate, or forge{/i} something that is authentic, with the {b}intent{/b} to replace something original."

    show biologicalDad unfocused at right with move
    show mike confused at left with moveinleft
    mike "So, this is illegal? I mean - what we're currently doing?"
    show mike unfocused at left with dissolve
    
    dadFriend "Haha, let them go, Alfred. They might be developing a natural talent."
    hide dadFriend with dissolve

    show biologicalDad defaultEmotion with dissolve
    biologicalDad "Kids, don't listen to that guy."
    biologicalDad "And yes, it is illegal, but you boys have shown great creativity and original thought."
    show biologicalDad smiling with dissolve
    biologicalDad "Keep that creativity running. I'm really really proud of you boys!"
    hide biologicalDad with dissolve

    show mike sad at right with move
    show kidMC sad at left with moveinleft
    "..."
    show mike unfocused at right with dissolve
    persistent.kidMC "Well, I guess Jimmy's right. We really {b}ARE{/b} poor."
    hide mike with dissolve

    show kidMC unfocused at left with dissolve
    show biologicalDad smiling at right 
    with moveinright
    biologicalDad "Boys, you're only poor if you give up! The most important thing is that you did something."
    biologicalDad "Most people only talk and dream of getting rich. You've done something. I'm very proud of you boys, and I will never ever get tired of saying this: "
    biologicalDad "{b}Keep going, and don't quit.{/b}"
    
    show biologicalDad unfocused at right
    show kidMC defaultEmotion at left 
    with dissolve
    menu:
        "...":
            pass
        "So, how come you're not rich, Dad?":
            call dadExplains
    
    biologicalDad "..."
    show biologicalDad flustered at right with dissolve
    biologicalDad "Oh I know! If you boys want to learn how to be rich, don't ask me. Talk to your dad, Mike."
    hide kidMC with dissolve

    show biologicalDad unfocused at right with dissolve
    show mike flustered at left with moveinleft
    mike "M-my dad? But why?"

    show mike unfocused at left
    show biologicalDad surprised at right 
    with dissolve
    play sound "audio/sfx/chuckle.mp3" volume 0.5
    biologicalDad "Yeah your dad, your dad and I have the same banker, and he {b}RAVES{/b} about your father everytime I meet him."
    show biologicalDad defaultEmotion with dissolve
    biologicalDad "He's told me several times that your father is brilliant when it comes to making money."

    show biologicalDad unfocused at right
    show mike confused at left 
    with dissolve
    mike "Then.. how come we don't have a nice car and a nice house like the rich kids at school?"

    show mike unfocused at left
    show biologicalDad smiling at right 
    with dissolve
    biologicalDad "Well, a nice car and a nice house doesn't necessarily mean you're rich or you know how to make money."
    show biologicalDad defaultEmotion with dissolve
    biologicalDad "Jimmy's dad works for the sugar plantation. We're not that different - he works for a company, and I work for the government."
    biologicalDad "The company {b}BUYS{/b} the car for him. If ever the sugar company is in financial trouble, Jimmy's dad may soon have nothing."
    show biologicalDad smiling with dissolve
    biologicalDad "And that's the difference between us and your dad, Mike. He seems to be building an empire, and I suspect in a few years he will be a {b}very rich{/b} man."
    hide biologicalDad with dissolve

    show mike surprised at right with move
    show kidMC surprised at left with moveinleft
    "!!!" with vpunch

    hide mike
    hide kidMC 
    with dissolve
    "Upon hearing the news, we both had a new priority, we began cleaning up the mess caused by our now-defunct first business."

    scene backyard with fade
    "We, who had a new clue on how we would get rich, we immediately made plans for how and when we would talk to Mike's dad."
    "After finalizing the plan, Mike had promised me to call as soon as he had talked to his dad."
    stop music fadeout 0.5

    scene jeepneyRideHome with fade
    play sound "audio/sfx/turnOnCarEngine.mp3" volume 0.5
    "Mike caught rode a jeepney not long after they had finished cleaning up."

    scene plainWhite with fade
    "Mike's going to have a talk with his dad by the time he gets home and ask him if he would teach us how to become rich."
    play sound "audio/sfx/telephoneRinging.mp3" volume 0.5
    "And after a few hours..."
    play sound "audio/sfx/pickupTelephone.mp3" volume 0.5
    show mike smiling with dissolve
    mike "Hey {b}[persistent.kidMC]{/b}, my dad agreed to meet with us!"
    show mike unfocused at right with move
    show kidMC sad at left with moveinleft
    persistent.kidMC "{i}Alright, this is the start.{/i}"
    persistent.kidMC "Alright, Mike. See you next Saturday."
    play sound "audio/sfx/hangupTelephone.mp3" volume 0.5
    scene plainWhite with fade
    "A few days went by and it is now the time for me to visit Mike's household and learn how to make money from his father."

    scene richDadFrontHouse with fade
    #INSERT BGM
    play sound "audio/sfx/openDoor.mp3" volume 0.5
    show mike smiling with dissolve
    mike "Hey {b}[persistent.kidMC]{/b}! Dad's on the phone right now and he said to wait inside."

    show mike unfocused at right with move
    show kidMC defaultEmotion at left with moveinleft
    persistent.kidMC "Oh.."
    
    scene richDadLivingRoom with fade
    play music "audio/bgm/jazzyShop.ogg" fadein 0.5 volume 0.25
    "I entered the narrow living room that was filled with old musty overstuffed furnitures."
    "Sitting on the couch were two women, both a little older than my mom."

    show kidMC defaultEmotion with dissolve
    persistent.kidMC "Mike, who are those people?"

    show kidMC unfocused at left with move
    show mike smiling at right with moveinright
    mike "Oh, they work for my dad. They are the managers of the restaurants."

    show mike unfocused at right
    show kidMC thinking at left 
    with dissolve
    persistent.kidMC "Does this go on all the time?"

    show kidMC unfocused at left
    show mike smiling at right 
    with dissolve
    play sound "audio/sfx/offerChair.mp3" volume 0.5
    mike "Hmm, not always but... kinda often. Anyways, take a seat."

    show mike unfocused at right
    show kidMC thinking at left 
    with dissolve
    persistent.kidMC "..."

    show kidMC unfocused at left 
    show mike smiling at right 
    with dissolve
    mike "By the way, I asked my dad if he would teach us to make money."

    show mike unfocused at right 
    show kidMC defaultEmotion at left 
    with dissolve
    persistent.kidMC "Yeah? What did he say to that?"

    show kidMC unfocused at left 
    show mike defaultEmotion at right 
    with dissolve
    mike "Well, he had a funny look on his face at first, and then he said he would make us an offer."

    show mike unfocused at right 
    show kidMC thinking at left 
    with dissolve
    persistent.kidMC "..."
    show kidMC defaultEmotion at left with dissolve
    persistent.kidMC "Do you know what the offer is?"

    show kidMC unfocused at left 
    show mike smiling at right 
    with dissolve
    mike "No, I'm actually stoked and excited to hear it, I'm sure we'll soon find out!"

    play sound "audio/sfx/openDoor.mp3" volume 0.5

    show kidMC surprised at left 
    show mike surprised at right 
    with dissolve
    "!!!" with vpunch

    hide kidMC
    hide mike 
    with dissolve

    show richDad defaultEmotion with dissolve
    play sound "audio/sfx/offerChair.mp3" volume 0.5
    richDad "Ready, boys?"
    hide richDad

    show kidMC serious at left with moveinleft
    show mike smiling at right with moveinright
    "*nods*"
    hide mike with moveoutright
    show richDad smiling at right with moveinright
    show kidMC unfocused at left with dissolve
    richDad "Mike says you want to learn to make money? Is that correct, {b}[persistent.kidMC]{/b}?"
    
    show kidMC defaultEmotion at left
    show richDad unfocused at right 
    with dissolve
    persistent.kidMC "Y-yes, sir."

    show richDad smiling at right 
    show kidMC unfocused at left 
    with dissolve
    richDad "Okay then! Here’s my offer."
    show richDad smiling at right with dissolve
    richDad "I’ll teach you, but I won’t do it {b}classroom-style{/b}."
    richDad "You work for me, I’ll teach you. You don’t work for me, I won’t teach you. Simple as that."
    show richDad defaultEmotion at right with dissolve
    richDad "The reason being is that, I can teach you faster if you work, and we'll both waste our precious time if you just want to sit and listen like you do in school."
    richDad "That’s my offer. Take it or leave it."

    show richDad unfocused at right 
    show kidMC defaultEmotion at left 
    with dissolve
    persistent.kidMC "Ah, may I ask a question first?"

    show kidMC unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad "No. Take it or leave it."
    richDad "I’ve got too much work to do to waste my time."
    play sound "audio/sfx/clockTicking.mp3" volume 0.5

    show richDad unfocused at right 
    show kidMC thinking at left 
    with dissolve
    menu:
        "Take it.":
            $ analytics.event("Chapter 1: Take Offer", "1")
            stop sound fadeout 0.5
            hide richDad with moveoutright
            pass
        "...":
            $ analytics.event("Chapter 1: Take Offer", "0")
            stop sound fadeout 0.5
            call opportunitiesComeAndGo

    show mike smiling at right with moveinright
    mike "Take it."

    hide kidMC 
    hide mike 
    hide richDad 
    with dissolve

    show richDad smiling with dissolve
    richDad "Good. Mrs. Martin will be by in 10 minutes."
    richDad "After I'm done discussing things with her, you'll ride with her to my superette and you can begin working."
    richDad "I'll pay you {b}{i}10 cents an hour{/i}{/b} and you'll be working three hours every Saturday."

    show richDad unfocused at right with move
    show kidMC surprised at left with moveinleft
    persistent.kidMC "But I have a softball game today..."

    show kidMC unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad "Take it, or leave it."

    show richDad unfocused at right 
    show kidMC surprised at left 
    with dissolve
    persistent.kidMC "..."
    show kidMC defaultEmotion at left with dissolve
    persistent.kidMC "I'll take it."

    scene plainWhite with fade
    "30 minutes later."

    scene richDadLivingRoom with fade
    play sound "audio/sfx/closeDoorGently.mp3" volume 0.5
    queue sound "audio/sfx/footSteps.ogg" volume 0.5
    show mrsMartin smiling with dissolve
    mrsMartin "Ready to work, kids?"

    show mrsMartin unfocused at right with move
    show kidMC defaultEmotion at left with moveinleft
    persistent.kidMC "Yes, Mrs. Martin."
    stop music fadeout 0.5

    scene jeepneyRideSuperette with fade
    play sound "audio/sfx/turnOnCarEngine.mp3" volume 0.5
    "Me, Mike, and Mrs. Martin rode a jeepney together to go to one of Benedict's (Mike's Father) superettes."

    scene frontSuperette with fade
    play music "audio/bgm/quirkyShop.ogg" fadein 0.5 volume 0.25
    play sound "audio/sfx/turnOffCarEngine.mp3" volume 0.5
    show kidMC thinking at left with moveinleft
    show mike defaultEmotion at right with moveinright
    "..."
    show mike unfocused at right with dissolve
    persistent.kidMC "Uhmm, if I may ask Mrs. Martin, what are we supposed to do here?"
    show kidMC unfocused at left with dissolve
    hide mike with dissolve
    show mrsMartin smiling at right with moveinright
    mrsMartin "Well, you boys will be dusting, fixing and re-organizing the store shelves."
    
    show mrsMartin unfocused at right with dissolve
    show kidMC defaultEmotion at left with dissolve
    persistent.kidMC "Ahh.. I see.."

    scene cleanShelf1 with fade
    play sound "audio/sfx/featherDusting.mp3" volume 0.5
    "*dusting*"
    scene cleanShelf2 with fade
    play sound "audio/sfx/featherDusting.mp3" volume 0.5
    "*dusting*"
    stop music fadeout 0.5

    scene plainWhite with fade
    "For three weeks, Mike and I reported to Mrs. Martin and worked on the superette for three hours."
    "By noon, our work was over and she dropped three dimes in each of our hands."
    window hide
    show coinsOnOpenHands at truecenter with fade
    play sound "audio/sfx/coinsDropping.ogg" volume 0.5
    pause 1.5
    hide coinsOnOpenHands with fade
    window auto
    "By Wednesday of our fourth week, I am ready to quit. This was not what I wanted when I said I wanted to learn how to earn and make money."

    show kidMC thinking with dissolve
    persistent.kidMC "{i}Wasn't this what I always did back then? Be a slave for some mere cents an hour? I haven't even seen Mike's dad since our first meeting.{/i}"
    persistent.kidMC "{i}Perhaps... am I being scammed? What's his play here? What would he gain?{/i}"

    scene superette with fade
    play music "audio/bgm/quirkyShop.ogg" fadein 0.5 volume 0.25
    show kidMC serious with dissolve
    persistent.kidMC "Mike... I'm quitting."
    persistent.kidMC "School was boring, I can't even use my Saturdays to do the things I want, and 30 cents? That's {b}WAY TOO{/b} low."

    show kidMC unfocused at left with move
    show mike smiling at right with moveinright
    mike "..."

    show mike unfocused at right 
    show kidMC serious at left 
    with dissolve
    persistent.kidMC "... What?"
    persistent.kidMC "Why are you smiling?"
    show kidMC surprised with dissolve
    persistent.kidMC "I mean, aren't you tired of getting these small rewards?"

    show kidMC unfocused at left 
    show mike smiling at right 
    with dissolve
    mike "Well, Dad said this would happen. He said to meet him when you were ready to quit."

    show mike unfocused at right 
    show kidMC surprised at left 
    with dissolve
    persistent.kidMC "Wait, what?"
    show kidMC confused at left with dissolve
    persistent.kidMC "So he's been waiting for me to get fed up?"

    show kidMC unfocused at left 
    show mike smiling at right 
    with dissolve
    mike "Sorta. Dad's kind of different - he doesn’t teach things like your dad."
    show mike defaultEmotion with dissolve
    mike "My dad is quiet and a man of few words. You just wait till this Saturday. I’ll let him know you’re ready."

    show mike unfocused at right 
    show kidMC thinking at left 
    with dissolve
    persistent.kidMC "{i}Well, I'll be damned... I've been played.{/i}"
    show kidMC defaultEmotion at left with dissolve
    persistent.kidMC "So, you mean I've been set up?"

    show kidMC unfocused at left 
    show mike smiling at right 
    with dissolve
    mike "No, not really, but maybe. Dad will explain on Saturday."
    stop music fadeout 0.5

    scene plainWhite with fade
    "I am ready to face Mike's dad. Even my own father was angry with him."
    "He was furious as he thought that Mike's dad was taking advantage of using children to to labor for him and should be investigated."

    scene kidMCLivingRoom with fade
    show biologicalDad confused with dissolve
    play sound "audio/sfx/dropPlate.mp3" volume 0.5
    biologicalDad "Demand what you deserve! Atleast 25 cents an hour or so. If you do not get a raise, quit as soon as possible!" with vpunch
    biologicalDad "Hell, you don't even need that damned job anyway."

    show biologicalDad unfocused at right with move
    show kidMC thinking at left with moveinleft
    persistent.kidMC "..."

    scene richDadFrontHouse with fade
    play sound "audio/sfx/openDoor.mp3" volume 0.5
    show richDad defaultEmotion with dissolve
    richDad "Take a seat and wait in line."

    scene richDadLivingRoom with fade
    play music "audio/bgm/jazzyShop.ogg" fadein 0.5 volume 0.25
    show kidMC thinking with dissolve
    persistent.kidMC "{i}Huh.. weird. Where's Mike?{/i}"
    persistent.kidMC "{i}I guess I should just wait in here.{/i}"
    hide kidMC with dissolve
    "45 minutes went by, and the living room was basically empty. All the employees who are in line before me has already left."
    "I hear Mike's dad talking on the phone for a few minutes. I thought I was being ignored and is just stalling the time."
    "Not long after did I grew impatient and was ready to walk out, but for some reason, I stayed."
    play sound "audio/sfx/footSteps.ogg" volume 0.5
    "A few minutes later, Mike's dad walked out of his office, said nothing and signaled me to come to his office."

    scene richDadOffice with fade
    show richDad defaultEmotion with dissolve
    play sound "audio/sfx/maleGrunt.mp3" volume 0.5
    queue sound "audio/sfx/sitOnLeatherCouch.mp3" volume 0.5
    richDad "{b}[persistent.kidMC]{/b}, I understand that you want a raise or you're going to quit."

    show richDad unfocused at right with move
    show kidMC serious at left with moveinleft
    
    menu:
        "Well, you’re not keeping your end of the bargain.":
            show kidMC unfocused at left 
            show richDad smiling at right 
            with dissolve
            richDad "What are you talking about?"
            pass
        "Yeah, we deserve to be treated better.":
            call treatedBetter
    
    show kidMC unfocused
    show richDad smiling at right 
    with dissolve
    play sound "audio/sfx/chuckle.mp3" volume 0.5
    richDad "I {b}AM{/b} teaching you."

    show richDad unfocused at right 
    show kidMC serious at left 
    with dissolve
    persistent.kidMC "What have you taught me? Nothing!" with sshake
    persistent.kidMC "You haven’t even talked to us once since we agreed to work for some mere cents!"

    show kidMC unfocused at left 
    show richDad surprised at right 
    with dissolve
    richDad "Wow! Now you sound just like most of the people who used to work for me - people I've either fired or who've quit."
    show richDad defaultEmotion at right with dissolve
    richDad "And how do you know that I've taught you nothing?"
    richDad "Does teaching mean {b}{i}talking{/i}{/b} or a {b}{i}lecture{/i}{/b}?"

    show richDad unfocused at right 
    show kidMC serious at left 
    with dissolve
    
    menu:
        "Well, yes.":
            call agreeOnTeachingTalking
        "...":
            call noAnswerTeachingTalking
    
    show kidMC unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad "Well, you'll spend your life blaming a job, low pay, or your boss for your problems if you continue being petty."
    richDad "You’ll live life always hoping for that big break that will solve all your money problems."

    show richDad unfocused at right 
    show kidMC defaultEmotion at left 
    with dissolve
    persistent.kidMC "..."

    show kidMC unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad "..."
    richDad "Or if you’re the kind of person who has no guts, you just give up every time life pushes you."
    richDad "You wanted to win, but the fear of losing was greater than the excitement of winning."
    richDad "{b}So{/b}, in a sense, you could think of my approach as giving you boys a taste of life."

    show richDad unfocused at right 
    show kidMC confused at left 
    with dissolve
    persistent.kidMC "What taste of life?"

    show kidMC unfocused at left 
    show richDad smiling at right 
    with dissolve
    richDad "You boys are the first people who have ever asked me to teach them how to make money. I have more than 150 employees, and not one of them has asked me what I know about money."
    richDad "They ask me for a job and a paycheck, but never to teach them about money."
    show richDad defaultEmotion at right with dissolve
    richDad "So most will spend the best years of their lives working for money, not really understanding what it is they are working for."

    show richDad unfocused at right 
    show kidMC confused at left 
    with dissolve
    persistent.kidMC "..."

    show kidMC unfocused at left 
    show richDad smiling at right 
    with dissolve
    richDad "So when Mike told me you wanted to learn how to make money, I decided to design a course that {b}mirrored{/b} real life."
    show richDad defaultEmotion at right with dissolve
    richDad "I could talk all day and teach you things regarding financial management but after that session, I'm sure both of you would forget it immediately."

    show richDad unfocused at right 
    show kidMC confused at left 
    with dissolve
    
    menu:
        "So what is the lesson I learned from working for only 10 cents an hour?":
            call whatsTheLesson
        "You're just cheap and you exploit your workers!":
            call cheapAndExploit
    
    show kidMC unfocused at left 
    show richDad smiling at right 
    with dissolve
    richDad "This."
    show richDad pointingOnHisHead at right with dissolve
    richDad "This stuff between our ears, use it."

    scene plainWhite with fade
    "It was at that moment that Mike's dad shared the pivotal point of view that separated him from his employees and my dad."
    "It was a singular point of view that made all the difference over a lifetime."
    "Mike's dad explained this point of view over and over, which I called lesson number one which is -"
    "{i}\"The poor and the middle class work for money. The rich have money work for them.\"{/i}"
    "And on that bright Saturday morning, I learned a completely different point of view from what I had been taught by my own dad."
    "I understood that both dads wanted me to learn. Both dads encouraged me to study, but not the same things."
    "For example, my highly \"educated\" dad recommended that I do what he did - study hard, get good grades so that I can find a safe, secured job on a big company."
    "Meanwhile, Mike's dad wanted me to learn how money works so I could make it {b}WORK{/b} for me, not through classrooms, but learn through life with his guidance."

    scene richDadLivingRoom with fade
    show richDad smiling with dissolve
    richDad "{b}[persistent.kidMC]{/b}, you know, I’m really glad that you got angry about working for 10 cents an hour. If you hadn’t got angry and had simply accepted it, I would have to tell you that I could not teach you."
    richDad "You see, true learning takes energy, passion, and a burning desire. Anger is a big part of that formula, for passion is anger and love combined."
    richDad "When it comes to money, most people want to play it safe and feel secure. So passion does not direct them. {b}Fear{/b} does."

    show richDad unfocused at right with move
    show kidMC defaultEmotion at left with moveinleft
    persistent.kidMC "So, is that the reason why they'll take jobs with low pay?"

    show kidMC unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad "Yes. Some people say I exploit people because I don’t pay as much as other business owners does or the government."
    show richDad smiling at right with dissolve
    richDad "But, personally, I'd say the people exploit {i}themselves{/i}. It's their fear, not mine."

    show richDad unfocused at right 
    show kidMC defaultEmotion at left 
    with dissolve
    persistent.kidMC "But don't you feel that you should.. you know, pay them more?"
    
    show kidMC unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad "Well, I don’t have to. And besides, more money will not solve their problems."
    
    show richDad unfocused at right 
    show kidMC thinking at left 
    with dissolve
    menu:
        "So that's why we only receive 10 cents an hour?":
            call reasonFor10Cents
        "Huh.. I don't get it. Why would it not solve their problem?":
            call moneyWontSolveProblem

    scene plainWhite with fade
    "Today, my friends over at school had just started their \"{b}Little League{/b}\" baseball game, but for some reason I was now thankful I had decided to work for 10 cents an hour."
    "I sensed that I was about to learn something my friends wouldn’t learn in school."

    scene richDadLivingRoom with fade
    show richDad smiling with dissolve
    richDad "So.. you ready to learn, {b}[persistent.kidMC]{/b}?"

    show richDad unfocused at right with move
    show kidMC smiling at left with moveinleft
    persistent.kidMC "Absolutely!"
    
    show kidMC unfocused at left 
    show richDad smiling at right 
    with dissolve
    richDad "I have kept my promise. I’ve been teaching you from afar. At nine years old, you’ve gotten a taste of what it feels like to work for money."
    richDad "Just multiply your last month by fifty years and you will have an idea of what most people spend their life doing."

    show richDad unfocused at right 
    show kidMC confused at left 
    with dissolve
    persistent.kidMC "Uhmm.. I don't really understand."

    show kidMC unfocused at left 
    show richDad thinking at right 
    with dissolve
    richDad "Hmm, how do I explain this..."
    show richDad smiling at right with dissolve
    richDad "Ah! How did you feel waiting in line to see me—once to get hired and once to ask for money?"

    show richDad unfocused at right 
    show kidMC defaultEmotion at left 
    with dissolve
    persistent.kidMC "Ugh. Utterly terrible."

    show kidMC unfocused at left 
    show richDad smiling at right 
    with dissolve
    richDad "If you choose to work for money, that is what life will be like."
    show richDad defaultEmotion at right with dissolve
    richDad "And how did you feel when Mrs. Martin dropped three dimes in your hand for three hours of work?"

    show richDad unfocused at right 
    show kidMC surprised at left 
    with dissolve
    menu:
        "I felt like it wasn’t enough.":
            pass
        "It seemed like nothing.":
            pass
        "It was disappointing.":
            pass
    
    show kidMC unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad "And that is how most employees feel when they look at their paychecks—especially after all the tax and other deductions are taken out."
    richDad "At least you got 100\% of your share. After all, the government always takes its share first."

    show richDad unfocused at right 
    show kidMC flustered at left 
    with dissolve
    persistent.kidMC "..."

    show kidMC unfocused at left 
    show richDad smiling at right 
    with dissolve
    richDad "Today, I just wanted to find out if you still have the passion to learn about money as most people don’t.They want to go to school, learn a profession, have fun at their work, and earn lots of money."
    show richDad sad at right with dissolve
    richDad "One day they wake up with big money problems, and then they can’t stop working." 
    richDad "That’s the price of only knowing how to work for money instead of studying how to have money work for you."

    show richDad unfocused at right 
    show kidMC defaultEmotion at left 
    with dissolve
    persistent.kidMC "Yup, I could totally see that."
    show kidMC smiling at left with dissolve
    persistent.kidMC "Oh, and I'm ready to learn, I really am."

    show kidMC unfocused at left 
    show richDad smiling at right 
    with dissolve
    richDad "Good. Now get back to work, but this time, you {b}won't{/b} get any pay."
    
    show richDad unfocused at right 
    show kidMC surprised at left 
    with dissolve
    persistent.kidMC "{b}WHAT?!{/b} That's not fair, you've got to atleast pay me something." with sshake

    show kidMC unfocused at left 
    show richDad smiling at right 
    with dissolve
    play sound "audio/sfx/chuckle.mp3" volume 0.5
    richDad "You said you wanted to learn. If you don’t learn this now, you’ll grow up to be like your dad, earning lots of money only to be in debt up to his eyeballs, hoping more money will solve the problem."
    show richDad smiling at right with dissolve
    richDad "Or you can do what most adults do: Complain that there is not enough pay, quit, and go look for another job."

    show richDad unfocused at right 
    show kidMC confused at left 
    with dissolve
    persistent.kidMC "But what do I do?"

    show kidMC unfocused at left 
    show richDad pointingOnHisHead at right 
    with dissolve
    richDad "Use this, {b}[persistent.kidMC]{/b}. Use this well."
    show richDad smiling at right with dissolve
    richDad "Now get out of here and get back to work."
    stop music fadeout 0.5

    scene plainWhite with fade
    "I didn’t tell my dad that I wasn’t being paid. He wouldn’t have understood it, and I didn’t want to explain something I don't quite understand myself."
    "For three more weeks, Mike and I worked three hours every Saturday for nothing. The work didn’t bother me, and the routine got easier."
    "However, missing those baseball games and not being able to do most of my hobbies in my free time got to me."

    scene superetteCounter with fade
    play music "audio/bgm/quirkyShop.ogg" fadein 0.5 volume 0.25
    play sound "audio/sfx/openShopDoor.mp3" volume 0.5
    show richDad smiling with dissolve
    richDad "Hello, Mrs. Martin."

    show richDad unfocused at right with move
    show mrsMartin smiling at left with moveinleft
    mrsMartin "Good morning, sir Benedict. To what do I owe the pleasure? Is there something wrong?"

    show mrsMartin unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad "Ah, I came by just to check on things. So, how are things going in the superette?"

    show richDad unfocused at right 
    show mrsMartin defaultEmotion at left 
    with dissolve
    mrsMartin "Everything's fine. The boys are doing well actually even without pay."
    mrsMartin "They finish their assigned tasks efficiently."

    show mrsMartin unfocused at left 
    show richDad smiling at right 
    with dissolve
    richDad "Oh, is that so.."
    richDad "Alright, let me get two ice cream on sticks."
    play sound "audio/sfx/coinsDropping.ogg" volume 0.5
    queue sound "audio/sfx/openCashRegister.mp3" volume 0.5
    richDad "Mrs. Martin, I'm gonna have to borrow these two new employees of mine for awhile!"

    show richDad unfocused at right 
    show mrsMartin smiling at left 
    with dissolve
    mrsMartin "Oh sure, no problem!"

    show mrsMartin unfocused at left 
    show richDad smiling at right 
    with dissolve
    richDad "Alright, thanks!"
    show richDad defaultEmotion at right with dissolve
    richDad "Hey boys, come here for a sec."
    show richDad smiling at right with dissolve
    play sound "audio/sfx/chuckle.mp3" volume 0.5
    richDad "Drop those brushes, you won't be needing them for now. Let's go for a walk."
    stop music fadeout 0.5

    scene plainWhite with fade
    "Mike and I suddenly got called by his dad, and to be honest with you, I really have no idea why."
    "But I'm guessing that we might be learning something new this time."

    scene afternoonPark with fade
    play music "audio/bgm/afternoonParkNoBench.ogg" fadein 0.5 volume 0.25
    show richDad defaultEmotion with dissolve
    richDad "So, how's it going, boys?"
    hide richDad with dissolve

    show kidMC defaultEmotion at left 
    show mike smiling at right 
    with dissolve
    "We're doing okay so far."
    hide mike with dissolve

    show kidMC unfocused at left with dissolve
    show richDad smiling at right with moveinright
    richDad "Ahh, I see. Learn anything yet?"

    show richDad unfocused at right 
    show kidMC thinking at left 
    with dissolve
    persistent.kidMC "..."

    show kidMC unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad """
    Well, you boys had better start thinking. You’re staring at one of life’s biggest lessons.
    
    If you learn it, you’ll enjoy a life of great freedom and security. If you don’t, you’ll wind up like Mrs. Martin and most of the people here in the park.
    
    They work very hard for little money, {b}clinging{/b} to the illusion of job security and a skimpy pension after 45 years of service.
    
    If that excites you, I’ll give you a raise to {b}25 cents an hour{/b}.
    """

    show richDad unfocused at right 
    show kidMC surprised at left 
    with dissolve
    persistent.kidMC "Huh, but they are good hardworking people. Are you perhaps making fun of them?"

    show kidMC unfocused at left 
    show richDad smiling at right 
    with dissolve
    play sound "audio/sfx/chuckle.mp3" volume 0.5
    richDad "Haha no, Mrs. Martin is like a mother to me. I would never be that cruel. I may sound unkind because I’m doing my best to point something out to the two of you."

    show richDad unfocused at right 
    show kidMC surprised at left 
    with dissolve
    persistent.kidMC "..."

    show kidMC unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad "I want to expand your point of view so you can see something most people don't because their vision is too narrow."

    hide kidMC 
    hide richDad 
    with dissolve

    "Mike and I sat there, uncertain of his message. He sounded cruel, yet we could sense he was trying to drive home a point."

    show richDad unfocused at right with moveinright
    show kidMC thinking at left with moveinleft
    persistent.kidMC "..."

    show kidMC unfocused at left 
    show richDad smiling at right 
    with dissolve
    richDad "Doesn’t that 25 cents an hour sound good? Doesn’t it make your heart beat a little faster?"

    show richDad unfocused at right 
    show kidMC thinking at left 
    with dissolve
    persistent.kidMC "{i}It does make my heart beat a little faster, twenty five cents is definitely a steal here, but...{/i}"

    show kidMC unfocused at left 
    show richDad slyGrin at right 
    with dissolve
    richDad "No chance huh... How about a dollar per hour?"
    hide richDad with moveoutright
    
    show kidMC thinking at center with move
    play sound "audio/sfx/conscienceIn.mp3" volume 0.5
    show kidMCDevilConscience at topleft with dissolve
    kidMCDevilConscience "{b}TAKE IT! TAKE IT ALREADY!{/b}" with vpunch
    show kidMCDevilConscience unfocused with dissolve
    persistent.kidMC "..."
    play sound "audio/sfx/conscienceIn.mp3" volume 0.5
    show kidMCAngelConscience at topright with dissolve
    kidMCAngelConscience "{b}No!{/b} The raise is a bait!" with vpunch
    show kidMCAngelConscience unfocused with dissolve
    persistent.kidMC "Hmm..."

    play sound "audio/sfx/conscienceOut.mp3" volume 0.5
    hide kidMCDevilConscience
    hide kidMCAngelConscience
    with dissolve
    
    persistent.kidMC "No."
    hide kidMC with dissolve
    
    show richDad slyGrin with dissolve
    richDad "Okay, how about two dollars an hour?"
    hide richDad with dissolve

    show kidMC thinking with dissolve
    persistent.kidMC "..."
    play sound "audio/sfx/conscienceIn.mp3" volume 0.5
    show kidMCDevilConscience at topleft with dissolve
    kidMCDevilConscience "{b}JUST TAKE IT! TAKE IT!{/b}" with sshake
    play sound "audio/sfx/conscienceOut.mp3" volume 0.5
    hide kidMCDevilConscience with dissolve
    persistent.kidMC "{i}I want to say yes. I want the deal. I could picture having lots of things, and the adoration of my friends if I were to flash some cash.{/i}"
    persistent.kidMC "{i}But if I were to accept the raise, then I'm basically working for money - which then would defeat the purpose of Mike's Dad teaching us how to make money work for us.{/i}"
    persistent.kidMC "Hmm..."
    hide kidMC with dissolve

    show kidMC unfocused at left with moveinleft
    show richDad smiling at right with moveinright
    richDad "Hmm, you got the resolve. Alright, how about {b}five{/b} dollars an hour?"

    show richDad unfocused at right 
    show kidMC surprised at left 
    with dissolve
    persistent.kidMC "{i}Huh.. something's wrong. The offer is too big and ridiculous for just re-arranging and dusting the products. I wonder what Mike thinks{/i}."
    hide richDad with dissolve

    show kidMC unfocused at left 
    show mike smiling at right 
    with dissolve
    mike "*nods*"

    hide kidMC 
    hide mike 
    with dissolve
    
    show richDad smiling at center with dissolve
    richDad "Good, most people have a price. And they have a price because of human emotions named fear and greed."
    richDad "First, the fear of being without money {b}MOTIVATES{/b} us to work hard, and then once we get that paycheck, greed or desire starts us thinking about all the wonderful things money can buy. The pattern is then set."
    hide richDad with dissolve

    show richDad unfocused at right
    show kidMC defaultEmotion at left 
    with dissolve
    persistent.kidMC "What pattern?"

    show kidMC unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad """
    The recurring pattern of getting up, going to work, then paying bills. People’s lives are forever controlled by two emotions: {b}fear{/b} and {b}greed{/b}.
    
    Offer them more money and they continue the cycle by increasing their spending, and boys, that's what I call the {b}{i}Rat Race{/i}{/b}.
    
    Basically, once they get a few bucks in their hands, the emotions of joy, desire, and their greed takes over. And again they react, instead of think.
    """

    show richDad unfocused at right 
    show kidMC defaultEmotion at left 
    with dissolve
    persistent.kidMC "So their emotions control their financial decisions?"

    show kidMC unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad """
    Right.
    
    Money is running their lives, and they refuse to tell the truth about that. Money is in control of their emotions and their souls.
    """

    show richDad unfocused at right 
    show kidMC thinking at left 
    with dissolve
    persistent.kidMC "..."

    show kidMC unfocused at left 
    show richDad smiling at right 
    with dissolve
    richDad """
    I want you boys to avoid that trap. That is really what I want to teach you.
    
    Not just to be rich, because being rich does not solve the problem.
    """

    show richDad unfocused at right 
    show kidMC surprised at left 
    with dissolve
    persistent.kidMC "Wait, it doesn't..?"

    show kidMC unfocused at left 
    show richDad surprised at right 
    with dissolve
    richDad """
    No, it doesn't. Due to the human nature of greed, whenever they earn money, people tend to desire something better, prettier... something more fun than what they currently have.

    They desire money for the joy they {b}THINK{/b} it can buy.

    And what happens after that short-lived excitement and joy expires? They soon need more money for more joy, more pleasure, more comfort, and more security.
    """
    hide kidMC with dissolve

    show richDad unfocused at right with dissolve
    show mike surprised at left with moveinleft
    mike "Even rich people do this?"

    show mike unfocused at left 
    show richDad smiling at right 
    with dissolve
    richDad """
    Yes, rich people included. In fact, the reason many rich people are rich isn’t because of desire, but because of fear.

    They believe that money can eliminate the fear of being poor, so they amass tons of it, only to find the fear gets worse.
    """
    show richDad defaultEmotion at right with dissolve
    richDad "And now... they fear losing that money."
    hide mike with dissolve

    show richDad unfocused at right 
    show kidMC thinking at left 
    with dissolve
    menu:
        "So, does that mean that a poor man is happier?":
            call happyBeingPoor
        "So, what do we do? Not work for money until all traces of fear and greed are gone?":
            call notWorkForMoney

    show kidMC unfocused at left 
    show richDad smiling at right 
    with dissolve
    richDad """
    Don’t worry about what I just said. It will make more sense in years to come.

    Just be an observer, not a reactor, to your emotions. Most people do not know that it’s their emotions that are doing the thinking.
    """
    
    show richDad unfocused at right 
    show kidMC defaultEmotion at left 
    with dissolve
    persistent.kidMC "Can you give me an example?"

    show kidMC unfocused at left 
    show richDad smiling at right 
    with dissolve
    richDad "Sure. When a person says \"{i}I need to find a job{/i}.\", it’s most likely an emotion doing the thinking."
    show richDad defaultEmotion at right with dissolve
    richDad "Fear of not having money generates that thought."

    show richDad unfocused at right 
    show kidMC defaultEmotion at left 
    with dissolve
    persistent.kidMC "But... people do need money if they have bills to pay."

    show kidMC unfocused at left
    show richDad defaultEmotion at right 
    with dissolve
    richDad "Sure they do. All I'm saying is that it's fear that is all too often doing the thinking."

    show richDad unfocused at right with dissolve
    
    hide mike 
    hide kidMC 
    with dissolve
    
    show mike confused at left with moveinleft
    mike "Uhh... pardon? Dad? Sorry, I'm afraid I do not quite understand."

    show mike unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad """
    For example, if the fear of not having enough money arises, instead of immediately running out to get a job, they instead might ask themselves this question: \"{i}Will a job be the best solution to this fear over the long run?{/i}\".
    
    And in my opinion, the answer to that question is no. A job is really a short-term solution to a long-term problem.
    """

    hide mike with dissolve
    
    show richDad unfocused at right 
    show kidMC thinking at left 
    with dissolve
    persistent.kidMC """
    {i}Huh... I was basically like this back then. I've worked for countless of hours, attended every office meeting, stood up late to cover for my colleagues, and more just to have a secured source of income{/i}.

    {i}I should probably ask him if this is the product of fear. But how would I ask him without blowing off my cover?{/i}

    {i}...{/i}
    """

    show kidMC surprised with dissolve
    persistent.kidMC "{i}Ah! I know! I'll just use my dad as an example.{/i}"
    
    show kidMC defaultEmotion at left with dissolve
    persistent.kidMC "But my dad is always saying \"{i}Stay in school and get good grades, so you can find a safe and secure job{/i}.\""

    show kidMC unfocused at left 
    show richDad smiling at right 
    with dissolve
    richDad """
    Yes, I understand why Alfred says that, most people recommend that, and it’s a good path for most people. But people make that recommendation primarily out of fear.
    
    He’s terrified that you won’t earn enough money and won’t fit into society. He wants the best for you.
    """
    richDad "{b}BUT{/b}, do not get me wrong as I believe that education and having a job is important." with vpunch
    richDad "However, it won’t handle the said {i}fear{/i} that causes him to be so fanatical about you going to school."
    

    show richDad unfocused at right 
    show kidMC confused at left 
    with dissolve
    persistent.kidMC "Ah, so what do you recommend we do?"

    show kidMC unfocused at left 
    show richDad smiling at right 
    with dissolve
    richDad "I want to teach you to master the power of money, instead of being afraid of it."
    richDad "They don’t teach that in school and, if you don’t learn it, you become a slave to money."

    show richDad unfocused at right 
    show kidMC smiling at left 
    with dissolve
    persistent.kidMC "Honestly, I did think of being able to afford new things for a moment."

    show kidMC unfocused at left 
    show richDad smiling at right 
    with dissolve
    richDad "By not giving in to your emotions, you were able to delay your reactions and think. We will always have emotions of fear and greed, it's in our nature, I wouldn't deny that."
    show richDad defaultEmotion at right with dissolve
    richDad "Most people live their lives chasing paychecks, pay raises and job security because of their e-"

    show richDad unfocused at right
    show kidMC smiling at left 
    with dissolve
    persistent.kidMC "Emotions. Like a donkey dragging a cart with it's owner dangling a carrot just in front of its nose."

    show kidMC unfocused at left 
    hide richDad 
    show mike smiling at right 
    with dissolve
    mike "The donkey's owner may be going where he wants to, but the donkey is chasing an illusion, right?"
    
    hide mike 
    hide kidMC 
    with dissolve

    show richDad surprised with dissolve
    richDad "..."
    show richDad smiling with dissolve
    richDad "Well, would you look at that?"
    richDad "You boys learn fast!"
    show richDad surprised with dissolve
    richDad "Look {b}[persistent.kidMC]{/b}, your dad's advice - I won't invalidate that. School is important, you get to learn a skill or profession to become a contributing member of society."
    richDad "Schools train and educate the young ones so society can thrive and flourish. But unfortunately, for many people, school is the end, not the beginning."

    show richDad unfocused at right with move
    show kidMC defaultEmotion at left with moveinleft
    persistent.kidMC "..."

    show kidMC unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad "And come to think of it, I really may have been cruel with my examples today, but I want you boys to always remember this talk. I want you to always think of Mrs. Martin and the donkey."
    show richDad sad at right with dissolve
    richDad "To spend your life living in fear, never exploring your dreams, is cruel."
    richDad "To work hard for money, thinking that it will buy you things that will make you happy is also cruel."
    richDad "To live a life dictated by the size of a paycheck is not really living a life."
    show richDad sad at right with dissolve
    richDad "I’ve seen how money runs people’s lives. Don’t let that happen to you. Please don’t let money run your life."
    
    hide richDad
    hide kidMC 
    with dissolve
    
    show richDad defaultEmotion with dissolve
    richDad "..."
    richDad "You know... when you boys mastered your emotions by agreeing to work for free, I knew there was hope."
    richDad "Especially when you again resisted your emotions when I tempted you with the ridiculous pay raise."

    show richDad unfocused at right with move
    show kidMC smiling at left with moveinleft
    persistent.kidMC "Honestly, I've thought of all the things I could possibly buy, but then I realized that if I were to take the bait -"
    hide richDad with dissolve

    show kidMC unfocused at left with dissolve
    show mike smiling at right with moveinright
    mike "All the things we've been doing such as getting ourselves away from the trap would've been for nothing."
    hide mike with dissolve

    show richDad smiling at right with dissolve
    richDad "Right, totally on point! Shall we head back to Mrs. Martin, boys?"
    hide richDad with dissolve

    show kidMC smiling at left 
    show mike smiling at right 
    with dissolve
    "Yup, let's do that!"
    stop music fadeout 0.5

    scene plainWhite with fade
    "As we headed back to the store, Mike's dad explained that the rich really did “make money” and that they did not work for it."

    scene backyard with fade
    "He also explained that when Mike and I were casting five-cent pieces out of lead - thinking that we were making money, that we were very {b}CLOSE{/b} to thinking the way the rich think."

    scene superetteCounter with fade
    play music "audio/bgm/quirkyShop.ogg" fadein 0.5 volume 0.25
    play sound "audio/sfx/openShopDoor.mp3" volume 0.5
    show richDad defaultEmotion with dissolve
    richDad "Aaaand, we're back."
    
    show richDad unfocused at right with move
    show mrsMartin smiling at left with moveinleft
    mrsMartin "Oh! Welcome back boys, did you have fun? Come on in and eat for now, my treat."

    show mrsMartin unfocused at left 
    show richDad smiling at right 
    with dissolve
    richDad "I'm afraid I would have to pass as I have to attend to some matters on my other superettes as well."
    richDad "But thank you for the kind invitation!"
    
    hide richDad 
    hide mrsMartin 
    with dissolve
    
    scene frontSuperette with fade
    show kidMC unfocused at left with moveinleft
    show richDad defaultEmotion at right with moveinright
    richDad "..."
    show richDad smiling at right with dissolve
    richDad "Boys! Keep working, but the sooner you forget about needing a paycheck, the easier your adult life will be."
    richDad "Keep using your brain, work for free, and soon your mind will show you ways of making money far beyond what I could ever pay you."
    richDad "The moment you see one opportunity, you'll see them for the rest of your life. The moment you do that, I'll teach you boys something else!"

    show kidMC smiling with dissolve
    persistent.kidMC "Yup, will do! Thank you so much!"
    
    hide richDad
    hide kidMC 
    with dissolve

    scene plainWhite with fade
    "Not long after did Mike and I picked up our things from the store and waved goodbye to Mrs. Martin."
    "Mike and I went to the same picnic park, sat down and spent several more hours thinking and talking."
    "We spent the next week at school thinking and talking too. For two more weeks, all we did was think, evaluate, and work for free."

    scene superetteCounter with fade
    "By the end of the second Saturday, I was again saying goodbye to Mrs. Martin, and looked at the comic-book stand with a longing gaze." 
    "Suddenly, I saw her do something I'd never seen her do before."
    play sound "audio/sfx/cuttingPaper.mp3" volume 0.5
    "Mrs. Martin was cutting up the front page of the comic book in half. She then kept the top half of the comic book cover and threw the rest of the book into a large cardboard box."

    show kidMC defaultEmotion with dissolve
    persistent.kidMC "Uhm, Mrs. Martin.. I have a question."

    show kidMC unfocused at left with move
    show mrsMartin smiling at right with moveinright
    mrsMartin "Oh, {b}[persistent.kidMC]{/b}! You're still here, ask away boy."

    show mrsMartin unfocused at right 
    show kidMC defaultEmotion at left 
    with dissolve
    menu:
        "What are you doing to the comic books?":
            call askMrsMartin
        "... No, nothing. Nevermind, sorry.":
            call doNotAsk
    
    play sound "audio/sfx/footSteps.ogg" volume 0.5
    queue sound "audio/sfx/openShopDoor.mp3" volume 0.5
    show mrsMartin smiling with dissolve
    mrsMartin "Welcome, come on in!"

    show mrsMartin unfocused at left with move
    show comicDistributor smiling at right with moveinright
    play sound "audio/sfx/loundThud.mp3" volume 0.5
    comicDistributor "Hello, here are the new batch of the comic books!"
    
    show comicDistributor unfocused at right with dissolve
    hide mrsMartin with dissolve
    show kidMC defaultEmotion at left with moveinleft
    persistent.kidMC "Uhmm, excuse me sir. Can we have those old comic books instead? I mean, if you're not going to use them anymore, and since it was already damaged anyways."

    show kidMC unfocused at left 
    show comicDistributor defaultEmotion at right 
    with dissolve
    comicDistributor "Hmm.."
    show comicDistributor smiling with dissolve
    comicDistributor "Alright, you can have them if you work for this store and do {b}NOT resell{/b} them."

    show comicDistributor unfocused at right 
    show kidMC surprised at left 
    with dissolve
    persistent.kidMC "{b}...!{/b}" with vpunch
    show kidMC smiling at left with dissolve
    persistent.kidMC "Mike... are you still willing to be my business partner?"
    persistent.kidMC "If so, then we're about to get busy."

    show kidMC unfocused at left with dissolve
    hide comicDistributor with dissolve
    show mike confused at right with moveinright
    mike "..."
    show mike smiling at right with dissolve
    mike "Ahh... I see I see. Let's try this out again, shall we?"

    scene plainWhite with fade
    "And with that, we revived our business partnership."
    stop music fadeout 0.5

    scene mikeBasement with fade
    play music "audio/bgm/jazzyShop.ogg" fadein 0.5 volume 0.25
    "Using Mike's basement, we began piling hundreds of comic books in that room. And soon, our comic book library was open to the public."
    play sound "audio/sfx/loundThud.mp3" volume 0.5
    queue sound "audio/sfx/newspaperFlip.mp3" volume 0.5
    "We also hired Mike's younger sister, who loved to study, as our head librarian. She charged each child 10 cents admission to the library which was open from 2:30pm to 4:30pm every weekdays."

    scene kidsReadingBooks with fade
    "The customers - the children of the neighbohood could read comics as much as they want in the span of two hours. That alone was enough to consider it as a bargain."
    play sound "audio/sfx/signingOnPaper.mp3" volume 0.5
    show logBook at truecenter with dissolve
    "Mike's sister would check the kids as they left to make sure they weren't borrowing any comic books. She also logs in how many kids showed up each day."
    hide logBook with dissolve
    "Mike and I averaged 9.50 dollars per week over a three-month period. Of course, we paid his sister one dollar a week."
    "We kept our agreement by working in the store every Saturday and collecting all the comic books from the different superettes owned by Mike's dad."
    "We also kept our agreement to the distributor by not selling any comic books. We burned them once they get too tattered."
    "And as time goes by, we wanted to open a branch office but we couldn't find someone as trustworthy and dedicated as Mike's sister."
    "Even I could not believe it, at an early age - we found out how hard it was to find good staffs."

    scene mikeBasement with fade
    "Three months after the library first opened, a fight broke out in the room as some bullies from another neighborhood pushed their way in."
    "Mike's dad suggested we shut it down, and we also stopped working on Saturdays at the superette."
    stop music fadeout 0.5

    scene plainWhite with fade
    "What had happened might made us sad, but in reality, we were excited as Mike's dad had new things he wanted to teach us. He was also happy because we had learned our first lesson so well."
    "{b}{i}Learn how to make money work for you{/i}{/b}. By not getting paid for our work at the superette, we were forced to use our imaginations to identify different opportunities to make money."
    "By starting the library business, not only were we in control of our own finances, it also generated money for us, even when we weren't physically there. Our money {b}WORKED{/b} for us."
    "Instead of Mike's dad paying us money, he had given us so much more, and I'd defnitely say that it was all worth it."

$ analytics.event("Chapter 1", "FINISHED")
$ persistent.ch01 = True
return