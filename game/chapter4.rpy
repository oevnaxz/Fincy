label startChapter4:
    $save_name = "Chapter 04: The History of Taxes and the Power of Corporations"
    scene plainWhite with fade

    #Flashing the Title Screen
    window hide
    show screen title_screen(_("{b}LESSON 4: THE HISTORY OF TAXES AND THE POWER OF CORPORATIONS{/b}"))
    with dissolve
    pause 2
    hide screen title_screen
    with dissolve
    window auto

    "A few years back..."

    scene mcLivingRoom with fade
    show mc casual sad with dissolve
    persistent.mc "{i}It was a nightmare.{/i}"
    persistent.mc "{i}It was like every week of my life was on a sad, predictable loop...{/i}"
    persistent.mc "{i}Work, parties, hangovers, and hookups, you name it.{/i}"
    persistent.mc "{i}And the worst part was, I didn’t know how to break out of it. I was trapped in a toxic cycle that dragged me penniless.{/i}"
    show mc casual tearyEyed with dissolve
    persistent.mc "{i}How did I even end up here?{/i}"

#flashback College graduation day. 
    scene CollegeGraduation with fade

    show mc student smiling with dissolve
    show mc student smiling at right with move
    show mc student unfocused at right

    show richDad smiling at left with dissolve
    richDad "Congrats, Robert. We’ve been looking forward to this day. All your hard work has finally paid off."
    richDad "You’re going to be a journalist traveling the world. I am so proud of you!"

    show richDad unfocused at left
    show mc student smiling at right 
    with dissolve
    persistent.mc "Thanks, Benedict. We’ve still got a lot of surprises further ahead though."

#present time
    scene mcLivingRoom with fade

    show mc casual tearyEyed with dissolve
    persistent.mc "{i}Little did I know that one of the surprises would lead me to breaking down on the sticky floor of my apartment{/i}"
    persistent.mc "{i}Where... I would be kicked out of in a few days, by the way.{/i}"
    show mc casual sad with dissolve
    persistent.mc "{i}My life wasn’t always like this.{/i}"
    persistent.mc "{i}I was a star student from the day I learned how to read and write.{/i}"
    persistent.mc "{i}I sacrificed so much... dating, parties, and getaway weekends.{/i}"
    persistent.mc "{i}I barely had friends and I spent more time with my books than with actual people.{/i}"
    persistent.mc "{i}I had stable younger years, but I regret most of them.{/i}"

#Flashback Last day of high school.
    scene kidMCSchool with fade
    show PopularGirl smiling with dissolve
    PopularGirl "Hey {b}[persistent.mc]{/b}, I’m throwing a party at my house to celebrate finishing high school!" 
    PopularGirl "I know you don’t go out much and you probably don’t even know me, but I’d really like you to be there. See ya!"

    #Invited in party
    label ch4Choices1:
        show PopularGirl unfocused at left with move 
        show mc student surprised at right with moveinright
        persistent.mc "{i}Huh... should I go to the party?{/i}"
    menu:
        "Yeah, why not.":
            jump YesParty

        "I'll have to pass, sorry.":
            jump PassParty

    label YesParty:
        show mc student smiling at right with dissolve
        persistent.mc "I would love to. What time should I drop by?"
        
        show mc student unfocused at right
        show PopularGirl smiling at left 
        with dissolve
        PopularGirl "{b}Really?{/b} Great! See you at 8PM!" with vpunch

        scene mcBedroomNight with fade
        show mc student smiling with dissolve
        play sound "audio/sfx/openCloset.mp3" volume 0.5
        persistent.mc "{i}I should get ready and put on the best clothes I could find.{/i}"
        play sound "audio/sfx/rummageWardrobe.mp3" volume 0.5
        persistent.mc "{i}This is my first party after all.{/i}"
        stop sound fadeout 0.5

        window hide
        scene plainBlack with fade
        play sound "audio/sfx/perfumeSpray.mp3" volume 0.5
        pause 1.5
        window auto

        scene neighborhoodNight with fade
        play ambient "audio/sfx/neighboroodAmbience.mp3"
        persistent.mc "{i}As I walk through the rich neighborhood...{/i}"
        scene mansionNight with fade
        persistent.mc "{i}I found a mansion scattered with teenagers.{/i}"
        persistent.mc "{i}I think this is the right one.{/i}"
        play sound "audio/sfx/openDoor.mp3" volume 0.5

        scene frontDoorMansion with fade
        play ambient "audio/sfx/upbeatMusicAmbience.mp3" volume 0.25
        persistent.mc "{i}I was shocked at the sight beyond the front door.{/i}"
        persistent.mc "{i}I knew parties were loud, but not as chaotic as this.{/i}"
        persistent.mc "{i}I felt a knot in my stomach and walked back out before someone recognizes me.{/i}"
        persistent.mc "{i}This isn’t what I should be doing.{/i}"
        persistent.mc "{i}I should keep my focus on studying.{/i}"
        stop ambient fadeout 1
        scene mansionNight with fade
        persistent.mc "{i}I quickly run out the mansion’s pavement and walked back home.{/i}"
        
        scene neighborhoodNight with fade
        persistent.mc "{i}Ha... well, at least I tried.{/i}"

        jump PresentTime


    label PassParty:
        show mc student surprised at right with moveinright
        persistent.mc "Thanks for the invite, but uhh... I’ll be busy with my college preparation tonight."
        show mc student smiling with dissolve
        persistent.mc "I plan to get there earlier in the summer for the orientations and workshops."

        show mc unfocused at right 
        show PopularGirl defaultEmotion at left 
        with dissolve
        PopularGirl "Oh, okay. It was worth a shot trying to get you to come along. Hehe."

        jump PresentTime

#Present Time
    label PresentTime:

    scene mcLivingRoom with fade
    show mc casual tearyEyed with dissolve
    persistent.mc "{i}I wish I said yes.{/i}"
    persistent.mc "{i}I wish I went to all the events I passed up on.{/i}"
    persistent.mc "{i}Sure, I’d have less time studying and probably ended up in some random girl’s room{/i}"
    show mc casual sad with dissolve
    persistent.mc "{i}But looking back... that would’ve been better than where I am now.{/i}"
    persistent.mc "{i}I was so deprived that the moment I had my own money, I went all out.{/i}"
    persistent.mc "{i}I tried everything with everyone.{/i}"
    persistent.mc "{i}And by the end of the night...{/i}"
    persistent.mc "{i}The only thing left in my wallet would be a receipt for mints from the convenience store.{/i}"
    
#Flashback Laying on the couch, swiping through a dating app.
    scene mcLivingRoom1 with fade
    show mc casual defaultEmotion with dissolve
    play sound "audio/sfx/phoneTap.mp3" volume 0.5
    persistent.mc "Left."
    play sound "audio/sfx/phoneTap.mp3" volume 0.5
    persistent.mc "Left."
    play sound "audio/sfx/phoneTap.mp3" volume 0.5
    persistent.mc "Left!"
    play sound "audio/sfx/phoneTap.mp3" volume 0.5
    show mc casual confused with dissolve
    persistent.mc "Hmmm, cute, but way too young, left!"
    play sound "audio/sfx/phoneTap.mp3" volume 0.5
    show mc casual flustered with dissolve
    persistent.mc "Oh, she seems okay."

    label ch4Choices2:
    menu:
        "Swipe left":
            jump Swipeleft

        "Swipe right":
            jump Swiperight

    label Swipeleft:
        play sound "audio/sfx/swipedLeft.mp3" volume 0.5
        "{b}You missed a match!{/b}" with sshake
        show mc casual flustered with dissolve
        persistent.mc "{i}Ah... I should have swiped right.{/i}."
        show mc casual sad with dissolve
        persistent.mc "{i}I suddenly feel... lonely.{/i}"
        show mc casual defaultEmotion with dissolve
        persistent.mc "Eh... I’ll just try to sleep this feeling off, but I feel... restless."
        hide mc with dissolve

        scene plainWhite with fade
        "I washed my face and walked out the door."
        play sound "audio/sfx/openDoor.mp3" volume 0.5
        "I walked around aimlessly and stumbled upon a sort of cheap nightclub or some sort."
        "I entered the nightclub and not long after did I find myself by the bar with two girls."
        "And, the rest of the night was a blur."

        jump PresentTime2

    label Swiperight:
        play sound "audio/sfx/swipedRight.mp3" volume 0.5
        "{b}It’s a match!{/b}" with sshake

        show mc casual defaultEmotion:
            ease 0.5 xalign 0.7 
        
        nvl_narrator "It's a match! Now, both of you shoot your shots!"
        show mc casual smiling
        girl_nvl "Hi there, {b}[persistent.mc]{/b}! What are you up to?"
        mc_nvl "Nothing much. How about you?"
        show mc casual defaultEmotion
        girl_nvl "Actually, me and a few friends of mine are going out tonight."
        girl_nvl "Would you like to join us?"
        girl_nvl "{image=locationEmoji.png} {i}shared her current location.{/i}"
        show mc casual smiling 
        mc_nvl "Ah! Yeah sure, I'm down."
        show mc casual defaultEmotion
        mc_nvl "Are you going to pick me up?"
        mc_nvl "{image=locationEmoji.png} {i}shared your current location.{/i}"
        show mc casual smiling
        girl_nvl "Sure! See ya later, {b}[persistent.mc]{/b}!"

        window hide
        scene plainBlack with fade
        pause 2.0
        window auto

        jump PresentTime2

#Present Time 
    #Present time, Sitting in a cleaner room
    label PresentTime2:
    scene mcLivingRoom with fade
    show mc casual defaultEmotion with dissolve
    persistent.mc "{i}Well... I’m glad that phase was over.{/i}"
    persistent.mc "{i}I could’ve ended up on a Netflix murder documentary with how carelessly I would go along with girls that I just met.{/i}"
    show mc casual smiling with dissolve
    persistent.mc "{i}I didn’t willingly get off Tinder though.{/i}"
    persistent.mc "{i}My account got banned. Someone I rejected was probably still on there and reported my profile.{/i}"

    label choices2:
        show mc casual surprised with dissolve
        persistent.mc "{i}Now, what should I do today?{/i}"

    menu:
        "Sleep in.":
            jump Sleep

        "Workout.":
            jump Workout

    label Sleep:
        show mc casual defaultEmotion with dissolve
        persistent.mc "{i}Ehh... I have no energy to do anything today.{/i}"
        persistent.mc "{i}I'll just grab last night’s frozen dinner out of my fridge and stick it into the microwave.{/i}"
        
        show mc casual unfocused at left with move
        window hide
        show oven at truecenter with dissolve
        play sound "audio/sfx/microwaveOpenClose.mp3" volume 0.5
        
        hide mc with dissolve
        pause 2.5
        hide oven with dissolve

        window auto

        play sound "audio/sfx/slidLaundryToSide.mp3" volume 0.5
        persistent.mc "{i}I then hid all of my laundry in the corner of my room and prepared for a day of... doing nothing, again.{/i}"
        play sound "audio/sfx/microwaveOperating.mp3" fadein 0.5
        persistent.mc "{i}Then I heard the microwave ring and bring my not-so-acceptable first meal...{/i}"
        persistent.mc "{i}and lay down endlessly in my bed accompanied by the subtle sounds of the television.{/i}"
        jump nextday

    label Workout:
        hide mc with dissolve
        play sound "audio/sfx/knifePutDownOnPlate.mp3" volume 0.5
        persistent.mc "{i}I proceeded to drag myself into my kitchen and whipped up a reasonable breakfast.{/i}"
        persistent.mc "{i}I decided to workout to get my mind off things.{/i}"
        play sound "audio/sfx/pourWaterToTumbler.mp3" volume 0.5
        persistent.mc "{i}I filled up my tumbler with water and took the elevator up a few floors.{/i}"
        play sound "audio/sfx/elevatorBell.mp3"

        scene gymComplex with fade
        persistent.mc "{i}I walked into the gym of my complex.{/i}"
        play sound "audio/sfx/treadmill.mp3" volume 0.5
        persistent.mc "{i}I put on my earphones and started with the treadmill.{/i}"
        persistent.mc "{i}This is going to be a long session.{/i}"
        jump nextday

    label nextday:
        scene plainWhite with fade
        "The next day..."
        show mc casual defaultEmotion with dissolve
        persistent.mc "Ah... my body is now physically incapable of producing more tears."
        persistent.mc "No matter how hard I try, my eyes remain dry."
        show mc casual smiling with dissolve
        persistent.mc "I guess I should take this as a sign to get my life together... enough with the moping."
        persistent.mc "Younger me would’ve wanted me to act on my problems as soon as I can, but first..."
        persistent.mc "I should call Benedict and say hi."
        play sound "audio/sfx/telephoneDialTone.mp3" volume 0.5
        pause 1.0

        scene mcLivingRoomRichDadLivingRoom with fade
        play sound "audio/sfx/pickupTelephone.mp3" volume 0.5
        show mc casual unfocused at left
        show richDad smiling at right 
        with dissolve
        richDad "Hi there, {b}[persistent.mc]{/b}. How are you?"

        show richDad unfocused
        show mc casual defaultEmotion 
        with dissolve
        persistent.mc "Hi uhh... I think I’m good. I just really needed to you know... talk to you."
        persistent.mc "I know I’ve been avoiding your calls and I’m really sorry for that."
        
        show mc casual unfocused 
        show richDad smiling
        with dissolve
        richDad "It’s fine. I know you’re a busy boy now and that you have your own life."
        show richDad defaultEmotion with dissolve
        richDad "Do you need anything?"

        show richDad unfocused
        show mc casual defaultEmotion 
        with dissolve
        persistent.mc "I really need your advice."
        show mc casual sad with dissolve
        persistent.mc "I uh... barely have any savings right now."
        persistent.mc "I have articles overdue for my job."
        show mc casual tearyEyed with dissolve
        persistent.mc "I am about to get kicked out of my apartment and I am so lost..."
        persistent.mc "Really lost that... I was really ashamed to call you all these months and admit it."
        
        show mc casual unfocused 
        show richDad defaultEmotion
        with dissolve
        richDad "I understand, {b}[persistent.mc]{/b}"
        show richDad smiling with dissolve
        richDad "You do know that you can move back here in the countryside anytime." 
        richDad "My family and your family can still support you while you try and get back on your feet."
        richDad "We’d be more than willing to help you."

        show richDad unfocused 
        show mc casual sad
        with dissolve
        persistent.mc "Benedict, to be honest... I think that’s one of the factors that led me here right now."
        persistent.mc "Knowing that you’d catch me after any failure allowed me to never weigh down the consequences of my actions."
        show mc casual defaultEmotion with dissolve
        persistent.mc "I’m an adult now, and as much as possible. I uhhh... I really do not want to rely on anyone anymore."
        persistent.mc "I love you, but don’t you think it’s time that I figure things out on my own?"
        
        show mc casual unfocused
        show richDad smiling 
        with dissolve
        richDad "Well to me, it sounds like you already know what you’re supposed to do before you called."
        richDad "Boy, you don’t really need my advice, don’t you?"

        show richDad unfocused 
        show mc casual smiling 
        with dissolve
        play sound "audio/sfx/chuckle.mp3" volume 0.5
        persistent.mc "Hahaha. I guess I just needed to hear your voice for some reassurance."
        
        show mc casual unfocused 
        show richDad smiling
        with dissolve
        richDad "Well, I believe in you, {b}[persistent.mc]{/b}. I always will be. I’ll be one call away, alright?"

        show richDad unfocused
        show mc casual smiling 
        with dissolve
        persistent.mc "Thanks, Benedict. Bye."
        play sound "audio/sfx/pickupTelephone.mp3" volume 0.5

        scene mcLivingRoom with fade
        show mc casual smiling with dissolve
        persistent.mc "Yeah, I’ve had the best support system."
        show mc casual defaultEmotion with dissolve
        persistent.mc "I didn’t need to take out student loans."
        persistent.mc "I didn’t worry about where I had to live in order to get to school on time."
        persistent.mc "I admit, I’ve been living with privilege that most people didn’t have and unfortunately, I took that all for granted."
        persistent.mc "I was so secure that it was my own decisions that led me into this instability."

#Bookstore 
        scene Bookstore with fade

        "So, I now opt to deal with my problems the way any boy in a quarter life crisis would:"
        "Buy a self-help book and pretentiously read it while drinking overpriced coffee in a café with the tiniest tables."

    label choices3:
        show mc casual confused with dissolve
        persistent.mc "What book should I get?"

    menu:
        "Crazy Rich Me":
            jump Crazy

        "Where to keep your Gold":
            jump Gold

    label Crazy:
        scene Bookstore with fade
        "I skimmed through the book's introduction and found interesting topics."
        "The reviews at the back of the cover seem convincing."
        "I held onto it and proceeded to the cashier."

        window hide
        play sound "audio/sfx/getMoneyFromWallet.mp3" volume 0.5
        queue sound "audio/sfx/openCashRegister.mp3" volume 0.5
        pause 3.0
        window auto
        
        jump outsideBookstore

    label Gold:
        scene Bookstore with fade
        "I browsed the book's table of contents and saw that the subject of financial literacy is definitely broad."
        "The book even gives me the trusting feeling that I’d be a millionaire as soon as I finished reading it."
        "Hell, I even kept imagining my future as I walk towards the counter to pay for it."
        
        window hide
        play sound "audio/sfx/getMoneyFromWallet.mp3" volume 0.5
        queue sound "audio/sfx/openCashRegister.mp3" volume 0.5
        pause 3.0
        window auto

        jump outsideBookstore

#OutsideBookstore
    label outsideBookstore:
        scene outsideBookstore with fade
        "I bought a book that’s basically “Financial Literacy for Dummies,” but with a fancier title."
        "I went around and saw a cafe nearby, and I've decided to read the book there."
        play sound "audio/sfx/openShopDoor.mp3" volume 0.5
        
        scene Restaurant with fade
        "As soon as I get a table, I immediately wrote down my savings, expenses, and organized what I needed to do for work."
        play sound "audio/sfx/signingOnPaper.mp3" volume 0.5
        show mc casual confused with dissolve
        persistent.mc "Huh... I have enough savings to pay the apartment rent for half a year, which would then allow me to get more than enough writing done to keep my job..."
        hide mc with dissolve
        "The good thing about being a published writer is that people would completely understand me having a burnout and writer’s block,"
        "...but to be honest with you, I’m done with using those as excuses."
        
        scene outsideCafe with fade
        "I found a cozy park outside and put my things down on the wooden bench."
        "I took a sip of my coffee and opened the book that just reeks of {i}crypto, real estate, stocks,{/i} and {i}market trends.{/i}"
        play sound "audio/sfx/newspaperFlip.mp3" volume 0.5
        "Then, lo and behold, a finance girl, the embodiment of the book that I just purchased, sits across me and strikes up a conversation."

        show Kim casual smiling with dissolve
        Kim "Hi! That’s a good book. I’ve read it before."

        show Kim casual unfocused at right with move
        show mc casual defaultEmotion at left with moveinleft
        persistent.mc "Ah, I see... thanks."

        show mc casual unfocused at left
        show Kim casual defaultEmotion at right
        with dissolve
        Kim "Hmph, not much of a talker are ya?"

        show Kim casual unfocused at right
        show mc casual defaultEmotion at left 
        with dissolve
        persistent.mc "Well... now I choose to be a reader."

        show mc casual unfocused at left
        show Kim casual defaultEmotion at right 
        with dissolve
        Kim "Sure. I guess most of the time you’re... a writer?"

        show Kim casual unfocused at right
        show mc casual defaultEmotion at left 
        with dissolve
        persistent.mc "{i}Did she peeked at my company ID lace hanging on my bag?{/i}"

        show mc casual defaultEmotion with dissolve
        persistent.mc "Ah! Yeah yeah... I've wrote a few pieces. Are you perhaps familiar with the website?"
        persistent.mc "{i}Wait, why am I even asking her these questions?{/i}"

        show mc casual unfocused at left
        show Kim casual smiling at right 
        with dissolve
        Kim "Well, who isn’t?"
        Kim "Ever since the pandemic, online magazines and newsletters have been all the rage."
        show Kim casual defaultEmotion with dissolve
        Kim "That website you’re working for has been booming and I don’t see things getting stagnant any time soon."

        show Kim casual unfocused at right
        show mc casual defaultEmotion at left 
        with dissolve
        persistent.mc "How do you know so much?"

        show mc casual unfocused at left
        show Kim casual smiling at right 
        with dissolve
        Kim "I’m a stock broker. Basically, I watch the trends."

        show Kim casual unfocused
        show mc casual defaultEmotion 
        with dissolve
        persistent.mc "{i}Stupid question, self. It was obvious from the fancy watch and perfectly tailored dress.{/i}"

        show mc casual defaultEmotion at left with dissolve
        persistent.mc "Hmm okay. Good for you, I guess."
        persistent.mc "{i}Haaa... when will this conversation even end? I just wanna read this book in peace.{/i}"

        show mc casual unfocused at left
        show Kim casual smiling at right 
        with dissolve
        Kim "You know, getting advice from a pretty girl would be better than reading that boring book of yours."

        show Kim casual unfocused at right
        show mc casual smiling at left with dissolve
        persistent.mc "{i}Ah...{/i}"
        show mc casual surprised at left with dissolve
        persistent.mc "{i}Finance girls are so determined, but she is right.{/i}"
        show mc casual flustered at left with dissolve
        persistent.mc "{i}There’s a pair of hazel brown eyes hidden behind her glasses.{/i}"
        persistent.mc "{i}Her hair is effortlessly styled, and she has a smile that definitely could sell.{/i}"
        persistent.mc "{i}And guess what? I caved in.{/i}"
        play sound "audio/sfx/sipDrink.mp3" volume 0.25

        show mc casual smiling with dissolve
        persistent.mc "Okay, Ms. Stock Broker. What do you have to teach me?"

        show mc casual unfocused at left
        show Kim casual smiling at right 
        with dissolve
        Kim "Well, first... the government {b}IS{/b} exploiting us."

        show Kim casual unfocused at right
        show mc casual defaultEmotion at left 
        with dissolve
        persistent.mc "Whew, really? Ain't that a surprise?.   {i}(I said sarcastically.){/i}"

        show mc casual unfocused at left
        show Kim casual defaultEmotion at right 
        with dissolve
        Kim "Wait, let me explain."

        show Kim casual unfocused at right
        show mc casual defaultEmotion at left 
        with dissolve
        persistent.mc "Yeah, by all means, go."

        show mc casual unfocused at left
        show Kim casual defaultEmotion at right 
        with dissolve
        Kim "The rich stay rich because they’ve found the loopholes for getting taxed."
        Kim "And as for us everyday employees, we are yet to strike gold."
        Kim "You work 5 to 6 days in a week and I’m guessing you don’t plan to stop, even when things get... extremely tiring."

        show Kim casual unfocused at right
        show mc casual flustered at left 
        with dissolve
        persistent.mc "Stop staring at the bags under my eyes. I know they’re a dead giveaway."

        show mc casual unfocused at left
        show Kim casual smiling at right 
        with dissolve
        Kim "I can't help it as you do have pretty eyes above them."

        show Kim casual unfocused at right
        show mc casual smiling at left 
        with dissolve
        persistent.mc "{b}Continue.{/b} This is supposed to be a professional conversation, Ms. Stock Broker."

        show mc casual unfocused at left
        show Kim casual defaultEmotion at right 
        with dissolve
        Kim "{b}AH!{/b} Yeah, my bad." with vpunch
        Kim "Well... you'd have to invest some \"{i}parts{/i}\" of your salary."

        show Kim casual unfocused at right
        show mc casual defaultEmotion at left 
        with dissolve
        persistent.mc "Wait, is this the part where you try to... you know, sell me something?"

        show mc casual unfocused at left
        show Kim casual smiling at right 
        with dissolve
        Kim "Well, for now, I’m only trying to pitch you myself."

        show Kim casual unfocused at right
        show mc casual smiling at left 
        with dissolve
        persistent.mc "{i}Tsk. She’s too smooth. Annoyingly smooth.{/i}"
        show mc casual defaultEmotion with dissolve
        persistent.mc "Go on --"
        persistent.mc "With how I’m supposed to handle my money, I mean."

        show mc casual unfocused at left
        show Kim casual smiling at right 
        with dissolve
        Kim "Alright then!"
        show Kim casual defaultEmotion with dissolve
        Kim "The rich understand the power of company structures and the tax code. So they use every {b}LEGAL{/b} means they can to minimize their tax burden."
        Kim "And, when someone sues a wealthy individual, they are often met with layers upon layers of legal protection..."
        Kim "And often find that... the wealthy person actually owns nothing in their own name."
        Kim "They control everything, but personally own nothing."

        show Kim casual unfocused at right
        show mc casual defaultEmotion at left 
        with dissolve
        persistent.mc "Well, they’ve always had the upper hand."

        show mc casual unfocused at left
        show Kim casual smiling at right 
        with dissolve
        Kim "Exactly."
        Kim "That’s why we should learn from them."
        Kim "The rich put their money {b}INTO{/b} a corporation."
        show Kim casual defaultEmotion with dissolve
        Kim "Their asset puts income into their corporation, and then corporate income can be used as income for their personal income statement."
        Kim "And the expenses from their personal income statement can go into the expenses for the corporation."
        Kim "Even though the masses continuously try to find ways to tax the rich, the rich consistently outsmart them."
        show Kim casual smiling with dissolve
        Kim "Something to remember about the government, is that if they don’t spend their allotted funds..."
        Kim "They’ll risk losing money when the next budget is announced."
        show Kim casual defaultEmotion with dissolve
        Kim "They aren’t rewarded for being efficient spenders."
        Kim "Yet, entrepreneurs are rewarded for financial efficiency."
        Kim "The mindsets between the two are polar opposite."
        show Kim casual smiling with dissolve
        Kim "The rich look for legal loopholes to avoid paying taxes."
        Kim "That’s why they often hire the smartest accountants and attorneys."

        show Kim casual unfocused at right
        show mc casual defaultEmotion at left 
        with dissolve
        persistent.mc "Well, I’m no accountant nor an attorney so..."

        show mc casual unfocused at left
        show Kim casual defaultEmotion at right 
        with dissolve
        Kim "No, but you do have money to invest with."

        show Kim casual unfocused at right
        show mc casual confused at left 
        with dissolve
        persistent.mc "Okay uhh... so is this the part where you sell me something?"

        show mc casual unfocused at left
        show Kim casual smiling at right 
        with dissolve
        Kim "Nope, but how about... a dinner this Friday?"

        show Kim casual unfocused at right
        show mc casual smiling at left with dissolve
        persistent.mc "Thanks for the advice, Ms. Stock Broker. I have to go now."

        show mc casual unfocused at left
        show Kim casual smiling at right 
        with dissolve
        Kim "The name’s {b}Kim{/b} by the way, and... you’re welcome."
        show Kim casual defaultEmotion at right with dissolve
        Kim "Come to think of it, I haven't got your name yet. What’s your name?"

        show Kim casual unfocused at right
        show mc casual smiling  at left 
        with dissolve
        persistent.mc "Ah I see, okay."
        persistent.mc "Bye, {b}Kim{/b}."

        play sound "audio/sfx/footSteps.ogg" volume 0.5
        pause 1.0
        hide mc
        hide Kim 
        with dissolve

        scene mcLivingRoom1 with fade
        #in front of laptop

        show mc casual defaultEmotion at left 
        show handsOnLaptop at truecenter
        with dissolve
        play sound "audio/sfx/laptopTyping.mp3" volume 0.5
        persistent.mc "I’ve pondered on everything that I’ve learned today."
        persistent.mc "{i}I’m keeping my job, this apartment, but not my bad habits.{/i}"
        show mc casual surprised with dissolve
        persistent.mc "I’ll be setting up a long-term savings bank account, as well as an account for investing."
        show mc casual smiling at left with dissolve
        persistent.mc "{i}If I keep this up, in a few years, I may be able to find the “loophole” Ms. Stock Broker was talking about.{/i}"

    label choices4:
        show mc casual confused with dissolve
        persistent.mc "{i}But, what should be my first step?{/i}"

    menu:
        "Go to the bank.":
            jump bank

        "Go to work.":
            jump work

    label bank:
        scene bank with fade
        "I walked towards the counter by the entrance and told the customer service person about the predicament I'm in."
        "He then guides me to a table in the corner of the bank."

        show mc casual unfocused at left with moveinleft
        show CustomerService defaultEmotion at right with moveinright 
        CustomerService "Please wait here, dear customer."

        show CustomerService unfocused at right
        show mc casual defaultEmotion at left 
        with dissolve
        persistent.mc "Okay, thanks."

        hide CustomerService with dissolve

        persistent.mc "I fidgeted things as I patiently stare at the pile of papers on the table."
        play sound "audio/sfx/footSteps.ogg" volume 0.5
        pause 1.0
        persistent.mc "I am then greeted by a young employee holding a clipboard or some sort."

        show mc casual unfocused at left 
        show Employee smiling at right 
        with dissolve
        Employee "Hi, I am Luke. I’m this bank’s financial employee. Nice to meet you."

        show Employee unfocused at right
        show mc casual smiling at left 
        with dissolve
        persistent.mc "Ah! Hello, nice to meet you as well."

        hide Employee 
        hide mc
        with dissolve

        "The financial advisor sat down across from me and we basically started brainstorming about how I can {b}keep{/b} and {b}grow{/b} my savings."
        "And... it was a long afternoon."
        "A very long afternoon."

        scene plainWhite with fade
        "And three years later..."

        jump city

    label work:
        scene mcLivingRoom with fade
        show mc casual defaultEmotion with dissolve
        persistent.mc "{i}I better call my assistant and tell her I’ll be going to work today.{/i}"

        show mc casual smiling with dissolve
        persistent.mc "Hey uhh, it’s me. I’ll be there in a few minutes. Thank you!"
        play sound "audio/sfx/pickupTelephone.mp3" volume 0.5

        hide mc with dissolve
        
        scene outsideBookstore with fade
        "I quickly headed towards my company’s building with my laptop in my bag."
        
        scene mcWorkOffice with fade
        "I walked in and greeted our office's receptionist."
        "Not long after did I go to my cubicle and prepared my workstation."
        play sound "audio/sfx/laptopTyping.mp3" volume 0.5
        "I started to email my supervisor and my team members."
        "I immediately apologized to them for the delay of my articles and asked them when would be the earliest possible time for all of us to meet in the conference room."
        "While doing all this, I felt a wave of inspiration coming in."
        
        scene plainWhite with fade
        "And three years later..."

#Three years pass by, walking in the city
    label city:
        scene outsideBookstore with fade
        "I... got promoted."
        show mc defaultEmotion with dissolve
        "I’m writing more serious pieces now and the company now allows me to travel for my articles..."
        "I was also able to stay on my spacious apartment situated on the busiest part of the city, which in my opinion is really great."
        "I also have multiple investments on the side and I was able to turn my bad spending as well as shopping habits into money-making habits."
        "I have a few Birkins safely stored in my closet that I plan to sell when their prices further appreciate."
        
        "Looking back..."
        "I never thought that I’d ever be here if I didn’t jump out of that toxic cycle and recognized the opportunities in front of me once again."

        "I also try to meet up and talk to my financial advisor as much as possible."
        "I meet her at least twice a month to discuss things."
        
        "And as I enter my FA's building, I've decided to take the elevator just so that I would get on his office faster."

        scene buildingElevator with fade
        play sound "audio/sfx/elevatorBell.mp3" volume 0.5
        "As the elevator’s doors were closing..."
        "I heard someone say “{b}Wait!{/b}”"
        "So as a good gesture, I pressed and held the \"door\" button."
        "And to my surprise, it’s a familiar face who recognizes me as well."

        show mc unfocused at left with moveinleft 
        show Kim smiling at right with moveinright
        Kim "Hey there. Thanks!"

        show Kim unfocused at right
        show mc smiling at left 
        with dissolve
        persistent.mc "Hi, Kim."

        show mc unfocused at left 
        show Kim smiling at right 
        with dissolve
        Kim "{b}...!!!{/b}" with vpunch
        Kim "I'm surprised you still remember my name."
        Kim "Now, how's about that date?"

        scene plainWhite with fade
        "And with that, we started hitting it off, Kim and I."
        "After a few years of dating, we've decided to be in a relationship with each other."
        
        $ analytics.event("Chapter 4", "FINISHED")
        $persistent.ch04 = True
        return