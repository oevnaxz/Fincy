label startChapter2:
    $ save_name = "Chapter 02: Why Teach Financial Literacy?"
    scene plainWhite with fade
    play sound "audio/sfx/clockTicking.mp3" volume 0.5
    "As Mike's Dad continue to teach us different things in regards to investment, cashflow, risks assessment and such, it wasn't long until I saw him as my second father."
    stop sound fadeout 0.5
    "And of course, since {i}our{/i} rich father (Mike's Dad) continuously taught us things that would help us become financially secured for years..." 
    "It was destined for Mike to take over his dad's empire soon after. And as much as unsurprising at this is, he's actually doing a {b}better{/b} job than our father did."
    "Over the years, Mike married someone and they're wealthier than you could imagine."
    "They're able to live on a nice house, they are also able to buy the things they need and want anytime." 
    "Basically they're living the life we all dreamt of."
    "Do not fret as the empire left by our father to Mike is definitely in great hands, and I am confident that Mike will do everything he can to protect it."
    #FLASH ANIMATION mikeTalkingToSon
    "And soon after, Mike is now grooming his son to take his place, as his dad had groomed us."
    show signingADocument at truecenter with fade
    play sound "audio/sfx/signingOnPaper.mp3" volume 0.5
    "As for me however, I retired at the age of 47, I also got married to my wife, Kim."
    hide signingADocument with fade
    "I'm currently enjoying the {i}second{/i} life I've been granted, and I couldn't ask for more." 
    "I really am thankful."

    #Flashing the Title Screen
    window hide
    show screen title_screen(_("{b}LESSON 2: WHY TEACH FINANCIAL LITERACY?{/b}"))
    with dissolve
    pause 2
    hide screen title_screen
    with dissolve
    window auto

#Going to party
    scene mcLivingRoom with fade
    show mc casual defaultEmotion with dissolve
    show mc casual defaultEmotion at left with move
    show envelope at truecenter with dissolve
    persistent.mc "Hmm..."
    play sound "audio/sfx/openInvitation.mp3" volume 0.5
    hide envelope with dissolve

    show mc casual defaultEmotion with dissolve
    show casual readInvitation at truecenter with dissolve
    persistent.mc "An invitation to a party huh.."

    show mc casual unfocused at left with dissolve
    show Kim smiling at right with moveinright 
    Kim "Oh honey, what's that paper you're holding?"

    show Kim unfocused at right with dissolve
    show mc casual defaultEmotion at left with dissolve
    persistent.mc "Ah, it's from a friend of mine."
    persistent.mc "He's inviting me for the party this evening."
    hide casual readInvitation with dissolve

    show mc casual unfocused at left with dissolve
    show Kim defaultEmotion at right with dissolve
    Kim "Ah I see..."
    show Kim smiling at right with dissolve
    Kim "Well, are you going?"

    show Kim unfocused at right with dissolve
    show mc casual surprised at left with dissolve
    persistent.mc "Hmm, I don't really know to be honest."

    label ch2Choices1:
        show mc casual sad with dissolve
        persistent.mc "{i}Should I even attend the party?{/i}"
    menu:
        "Yes.":
            jump yes1

        "No.":
            jump no1

    #MENU1_YES
    label yes1:
        show mc casual smiling at left with dissolve
        persistent.mc "Yup, I better get ready."
        jump go

    #MENU1_NO
    label no1:
        show mc casual defaultEmotion at left with dissolve
        persistent.mc "Eh... I don't really feel like it."
        show mc casual sad at left with dissolve
        persistent.mc "But, I probably would disappoint my friend."

        show mc casual unfocused at left with dissolve
        show Kim defaultEmotion at right with dissolve
        Kim "You should definitely go, {b}[persistent.mc]{/b}."
        show Kim unfocused at right with dissolve

    menu:
    
        "Alright, I'll go.":
            jump go
        
        "Yeah, I think I should go. But I'll only be there for a few hours.":
            jump going

    label go:
        show mc casual smiling at left with dissolve
        persistent.mc "Would you like to come with me?"

        show mc casual unfocused at left with dissolve
        show Kim smiling at right with dissolve
        Kim "I would love to, but... I kinda want to stay indoors tonight."
        show Kim defaultEmotion with dissolve
        Kim "Go on without me and have fun, okay?"

        show Kim unfocused at right with dissolve
        show mc casual smiling at left with dissolve
        persistent.mc "Okay sure, I'll keep that in mind!"

        jump picking

    label going:
        show mc casual unfocused at left
        show Kim defaultEmotion at right
        with dissolve
        Kim "Alright, go get ready for the party."

        hide mc
        hide Kim
        with dissolve

        jump picking


#picking suit
    label picking:
        scene mcBedroom with fade
        show mc casual sad with dissolve
        play sound "audio/sfx/openCloset.mp3" volume 0.5
        persistent.mc "Hmm, I wonder what I should wear..."
        show mc casual defaultEmotion with dissolve
        play sound "audio/sfx/rummageWardrobe.mp3" volume 0.5
        persistent.mc "..."
        show mc casual smiling with dissolve
        persistent.mc "Eh... Let's just go with my favorite suit."
        hide mc with dissolve
        stop sound fadeout 0.5
        play sound "audio/sfx/perfumeSpray.mp3" volume 0.5
        pause 3.0
        show mc smiling with dissolve
        persistent.mc "And, all set."

        scene mcLivingRoom with fade
        show mc unfocused at left with moveinleft
        show Kim smiling at right with moveinright
        Kim "Oh, someone looks handsome."

        show Kim unfocused at right
        show mc smiling at left 
        with dissolve
        play sound "audio/sfx/chuckle.mp3" volume 0.5
        persistent.mc "Haha, thanks sweetie."

        scene mcLivingRoom1 with fade
        show mc defaultEmotion with dissolve
        persistent.mc "Alright, I'm going to have to go now, honey. See ya later."

        show mc unfocused at left with move
        show Kim defaultEmotion at right with moveinright
        Kim "Okay, take care. I love you!"

        show Kim unfocused at right
        show mc smiling at left
        with dissolve
        persistent.mc "I love you too, honey."

        hide mc 
        hide Kim 
        with dissolve

        jump party

#Party start here.
    label party: 
    play music "audio/bgm/thejazzpiano.mp3" fadein 0.5 volume 0.25
    scene mansionParty with fade
    play ambient "audio/sfx/laughingChitchat.mp3" volume 0.75
    show mc defaultEmotion with dissolve
    persistent.mc "{i}Hmm... I wonder where's John at?{/i}"
    persistent.mc "..."
    #end sound laughing and chitchat

    show mc smiling with dissolve
    persistent.mc "Ah! There he is!"
    play sound "audio/sfx/footSteps.ogg" volume 0.5

    show mc unfocused at left with move
    show john smiling at right with dissolve
    john "Oh, {b}[persistent.mc]{/b}! My man, thank you for attending the party!" with sshake

    window hide
    show mcShakeHands at truecenter with dissolve
    pause 1.5
    hide mcShakeHands with dissolve
    window auto

    show john unfocused at right
    show mc smiling at left 
    with dissolve
    persistent.mc "Man, your loudness never deteriorates does it?"
    persistent.mc "But hey, it's been what? 3 years since we've last seen each other? Glad to see you again, Johnny."

    show mc unfocused at left
    show john smiling at right 
    with dissolve
    john "Yeah, life got busy. I had no time to attend some of our yearly reunion."
    john "Anyways {b}[persistent.mc]{/b}, how are you?"

    show john unfocused at right
    show mc defaultEmotion at left 
    with dissolve
    persistent.mc "I'm doing good actually, I uhh..."
    show mc smiling with dissolve
    persistent.mc "I'm actually retired now, but not really like the {i}retired{/i} retired."

    show mc unfocused at left
    show john smiling at right
    with dissolve
    john "Yeah? Wait, what? Isn't your retirement way too early?"

    show john unfocused at right
    show mc smiling at left 
    with dissolve
    persistent.mc "Hmm... let's say that I just want to enjoy life."
    persistent.mc "Plus, I have savings and assets that {b}WOULD GENERATE{/b} money regardless if I work or not." 
    persistent.mc "And that's basically it, I decided to free myself from stress from managing businesses."

    show mc unfocused at left
    show john smiling at right 
    with dissolve
    john "Well, if you say so. I'm happy for you, man."

    hide mc
    hide john 
    with dissolve

    show butler defaultEmotion with dissolve
    play sound "audio/sfx/footSteps.ogg" volume 0.5
    butler "Excuse me, sirs."
    butler "Sir John, you have a phone call."

    show butler unfocused at right with move
    show john defaultEmotion at left with moveinleft
    john "Oh okay, I'll answer it in a sec."
    hide butler with dissolve

    show john smiling at right with move
    show mc unfocused at left with moveinleft
    with dissolve
    john "I'm sorry, {b}[persistent.mc]{/b}, but I have to take this call."
    john "Let's talk again later! See ya!"

    show john unfocused at right
    show mc smiling at left 
    with dissolve
    persistent.mc "Sure, no worries!"

    hide mc
    hide john
    with dissolve

    "And with that, John left to answer his phone call."
    "Meanwhile, I went looking for some people I could hang out with."

    scene mansionParty with fade
    show mc smiling with dissolve
    persistent.mc "How are you guys?"
    
    show mc unfocused at left with move
    show Liam smiling at right with moveinright
    Liam "Hey! Here's the millionaire guy."
    hide Liam with dissolve
    show Oliver smiling at right with dissolve
    Oliver "Oh hey, it's {b}[persistent.mc]{/b}! You're friends with Mike, right?"

    show Oliver unfocused at right
    show mc smiling at left 
    with dissolve
    play sound "audio/sfx/chuckle.mp3" volume 0.5
    persistent.mc "Haha, yeah."

    show mc unfocused at left with dissolve
    show Oliver defaultEmotion at right with dissolve
    Oliver "{b}[persistent.mc]{/b}, I know that this may be too sudden, but uh..."
    show Oliver smiling with dissolve
    Oliver "Could you pray tell the secret to you and Mike's success?"
    hide Oliver with dissolve
    show William smiling at right with moveinright
    William "Yeah, how do I actually make millions?"

    show William unfocused at right with dissolve
    show mc flustered at left with dissolve
    persistent.mc "Ahh..."
    hide William with dissolve

    show mc unfocused at left with dissolve
    show Liam smiling at right with moveinright
    Liam "How do I get started on becoming a millionaire??"
    hide Liam with dissolve
    show Oliver defaultEmotion at right with moveinright
    Oliver "Is there a book you would recommend?"
    hide Oliver with dissolve
    show Liam smiling at right with moveinright
    Liam "Hey {b}[persistent.mc]{/b}, what should I do to fund my children up until college?"

    show Liam unfocused at right
    show mc smiling at left 
    with dissolve
    persistent.mc "You guys bombarded me with lots of questions, whew."
    persistent.mc "Don't worry, I'll tell you guys my {i}secret{/i}."
    persistent.mc "Listen carefully, alright?"

    #==============================================================================================================================================================
    #
    # Be mindful of grammar and punctuation.
    # Be mindful of the characters used, see characters.rpy kung sino sino sila doon.
    # Pag monologue:
    #   don't use MCMonologue na character, use mc. 
    #   remove the (), use italic: {i}type text here{/i}.
    # Change the mc sa mga dialogue into persistent.mc katulad nung mga nasa itaas.
    # Be mindful rin kung saan mo ipapakita yung character, di pwedeng parehas nasa right yung dalawa.
    # I removed gop/groupOfPeople since redundant siya, decided to go with individual spamming ng questions sa isang scene sa taas.
    # And lastly, kindly check yung magiging transition ng characters, medyo inconsistent kasi:
    #       Kunwari pag galing sa gitna yung speaker tas gusto mong ipunta sa left side: show [character] at left with move 
    #       Pag nag move ka from center to left, dapat yung second speaker mo rin ay gagamit ng move transition like: show [2ndCharacter] at right with moveinright
    #
    # Overall, it's good naman, just need to refactor it pa, do PM me pag may questions ka or need ng clarifications.
    # 
    #==============================================================================================================================================================

    hide Liam with moveoutright
    show mc defaultEmotion at center with move
    persistent.mc "It's a story about the richest businessmen and tycoons..."
    persistent.mc "A group of our country's most powerful leaders and wealthiest businesses met in a specific year at the Canon Maharlika hotel in the Philippines."
    show mc sad with dissolve
    persistent.mc """But twenty-five years later, nine of those titans ended their lives due to certain reasons.

        Most of them lived their years on borrowed money, some went insane, and some even committed suicide."""
    show mc thinking with dissolve
    persistent.mc "I'm not sure whether anyone knows what happened to these folks."
    show mc defaultEmotion with dissolve
    persistent.mc "But it was in their time that the stock market crash and the {i}Great Depression{/i} happened."
    persistent.mc "And I believe that those events made a significant impact on their lives."
    show mc thinking with dissolve
    persistent.mc "{i}I'm afraid that too many people are obsessed with money rather than their most valuable asset, their education{/i}."
    show mc smiling with dissolve
    persistent.mc "If people believe that money would solve problems, well... they're in for a bumpy road."
    show mc defaultEmotion with dissolve
    persistent.mc "Intelligence is used to solve issues and of course, create income."
    persistent.mc "Obviously, money is quickly spent {b}without{/b} financial understanding."
    show mc smiling with dissolve
    persistent.mc "Most individuals are unaware that it is {b}NOT{/b} about how much money you make in life. It's all about how much money you save."
    persistent.mc "I am glad some people have become richer and richer but..."
    persistent.mc "I caution them that in the long run, it is not how much money you make that really matters." 
    persistent.mc "It's about how much you keep and how long you keep it for."
    
    show mc unfocused at left with move
    show Liam defaultEmotion at right with moveinright
    Liam "Ah, I see..."
    Liam "Well uhh... how do I get started then?"
    hide Liam with dissolve
    show Oliver smiling at right with moveinright
    Oliver "Enough with the stories Mr. Millionaire. Tell me how to get rich quick!"

    show Oliver unfocused at right
    show mc smiling at left 
    with dissolve
    persistent.mc "Alright, if you say so. Hmm..."
    persistent.mc "I remember my {i}rich{/i} dad telling me this back then."

    hide mc
    hide Oliver
    with dissolve

#flashback_2
    #sound clock ticking
    scene plainWhite with fade

    show richDad slyGrin with dissolve
    richDad "“{i}If you want to be rich, you need to be financially literate{/i}.”"
#flashback_2 end

    scene mansionParty with fade
    show mc thinking with dissolve
    persistent.mc "{i}They looked greatly disappointed with my answer{/i}..."
    show mc smiling with dissolve
    persistent.mc "{i}Well, that's to be expected, even I got disappointed when he just told me that phrase{/i}."

    show mc unfocused at left with move
    show Oliver defaultEmotion at right with moveinright
    Oliver "Ahh... I was so looking forward to rich quickly."
    hide Oliver with dissolve
    show Liam defaultEmotion at right with moveinright
    Liam "Honestly {b}[persistent.mc]{/b}, your answer did not... you know, live up to my expectations."
    Liam "I honestly thought there was something more, like a big secret or something."

    show Liam unfocused at right
    show mc smiling at left 
    with dissolve
    persistent.mc "Yeah, I get it. Disappointing right?" 
    persistent.mc "Well, my rich dad created a basic method of teaching me back then."

    show mc unfocused at left
    show Liam defaultEmotion at right 
    with dissolve
    Liam "..."

    show Liam unfocused at right
    show mc smiling at left 
    with dissolve
    persistent.mc "You know what, I'll let you in on something important, let me just take a piece of paper and a pen."
    persistent.mc "I'll give you the same simple line drawings Mike’s dad created for us."
    play sound "audio/sfx/drawOnPaper.mp3" volume 0.5

    show mc unfocused at left
    show Liam smiling at right 
    with dissolve
    Liam "Ohh! That's what I'm talking about!" 
    hide Liam with dissolve
    show Oliver smiling at right with moveinright
    Oliver "Yeah sure, take your time!"

    show Oliver unfocused at right
    show mc smiling at left
    with dissolve
    persistent.mc "Though basic, these drawings helped guide two little boys in building great sums of wealth on a solid and deep foundation."
    show mc defaultEmotion with dissolve
    persistent.mc "Rule #1: You {b}MUST{/b} know the difference between an asset and a liability."
    persistent.mc "Once you get past that level, you then buy assets."
    show mc smiling with dissolve
    persistent.mc "Most people struggle financially because they do not know the difference between those two."

#flashback_3
    scene richDadLivingRoom with fade
    show richDad surprised with dissolve
    richDad "Rich people acquire assets."
    richDad "And the poor and middle class acquire liabilities that they {b}THINK{/b} are assets."
    show richDad unfocused at left with move

    #*We believed Rich Dad was joking when he told Mike and me this.*

    show kidMC thinking at right with moveinright
    persistent.kidMC "Hmm..."
    hide kidMC with dissolve
    show mike defaultEmotion at right with moveinright
    mike "Uhmm... if I may ask a question."
    mike "What exactly is an asset and liability?"

    show mike unfocused at right
    show richDad smiling at left 
    with dissolve
    richDad "Assets... these are the things that would help you generate money in the long run, even if you're not working."
    richDad "In simpler terms, it puts money {b}IN{/b} my pocket."
    richDad "On the other hand, a liability takes money {b}OUT{/b} of my pocket."
    richDad "Anyways, don’t worry about it right now. Just let the idea sink in."
    show richDad defaultEmotion with dissolve
    richDad "If you can comprehend its simplicity, your life will have a plan and be financially easy."
    hide mike with dissolve
    show kidMC thinking at right with moveinright
    persistent.kidMC "So you're saying that..."
    show kidMC surprised with dissolve
    persistent.kidMC "All we need to know is what an asset is, acquire them, and we’ll be rich?"
    show kidMC defaultEmotion with dissolve
    persistent.kidMC "Is that what you mean?"

    show kidMC unfocused at right
    show richDad smiling at left 
    with dissolve
    richDad "Yes, it’s actually that simple."

    show richDad unfocused at left
    show kidMC thinking at right 
    with dissolve
    persistent.kidMC "..."
    show kidMC thinking at right with dissolve
    persistent.kidMC "Then if it’s that simple, how come everyone is not... rich?"

    show kidMC unfocused at right
    show richDad smiling at left 
    with dissolve
    richDad "Well, believe it or not, the reason is actually simple as well."
    show richDad defaultEmotion at left with dissolve
    richDad "It's because they simply do not know the difference between the two."
    
    show richDad unfocused at left
    show kidMC defaultEmotion at right 
    with dissolve
    persistent.kidMC "..."
    show kidMC thinking at right with dissolve
    persistent.kidMC "{i}How could adults be so misguided?{/i}"
    persistent.kidMC "{i}If it is that simple and at the same time important...{/i}"
    show kidMC sad with dissolve
    persistent.kidMC "{i}How come everyone hasn't figured this out?{/i}"
    
    show kidMC unfocused at right
    show richDad smiling at left 
    with dissolve
    richDad "Look boys, to us businessmen..."
    richDad "What defines an asset are not words, but numbers."
    richDad "If you want to be rich, you’ve got to {b}READ{/b} and {b}UNDERSTAND{/b} numbers."

    show richDad unfocused at left
    show kidMC thinking at right
    with dissolve
    persistent.kidMC "..."

    show kidMC unfocused at right
    show richDad smiling at left
    with dissolve
    richDad "Just remember this boys, “{i}The rich acquire assets, and the poor and middle class acquire liabilities.{/i}”"
    
#flashback_3_end
    scene mansionParty with fade
    show mc smiling with dissolve
    persistent.mc "I have trouble discussing this subject to other people as an adult as well."
    persistent.mc "Not because the lesson is complex or anything, but because we were taught... differently." 
    persistent.mc "They know the complexity in and out, yet they miss how simple the concept is."
    show mc defaultEmotion with dissolve
    persistent.mc "And I know I know, you gentlemen want things to be further explained, so..."
    persistent.mc "Here is how to tell the difference between an asset and a liability."
    persistent.mc "Most accountants and financial professionals do not agree with the so-called \"{i}standard{/i}\" definition of it. However the idea is really just the same."

    play sound "audio/sfx/drawOnPaper.mp3" volume 0.5
    persistent.mc "Let me just draw it for y'all."
    show mc smiling at left with move
    show cashflowAsset at truecenter with dissolve
    persistent.mc "This is how a cashflow pattern of an asset."
    persistent.mc "It's that simple, really."
    persistent.mc "The top part of the diagram is an {b}Income Statement{/b}." 
    persistent.mc "In some field, it is often called {b}Profit-and-Loss Statement{/b}."
    show mc defaultEmotion at left with dissolve
    persistent.mc "Basically, it measures your income and expenses."
    persistent.mc "Then, the lower part of the diagram is called a {b}Balance Sheet{/b}."
    persistent.mc "It’s called that because it’s supposed to balance assets against liabilities."
    persistent.mc "Many financial novices do not know the relationship between the Income Statement and the Balance Sheet, and it is vital to understand that relationship."
    hide cashflowAsset with dissolve

    show mc smiling at center with move
    persistent.mc "To give more light to the difference of asset and liability, let me draw another cashflow-pattern."
    
    window hide
    show mc defaultEmotion with dissolve
    play sound "audio/sfx/drawOnPaper.mp3" volume 0.5
    pause 1.0
    window auto
    
    show mc defaultEmotion at left with move
    show cashflowLiability at truecenter with dissolve
    persistent.mc "This, my friends, is what a cashflow-pattern of a liability looks like."
    persistent.mc "Any thing that takes money out of your pocket is a liability."
    show mc smiling at left with dissolve
    persistent.mc "See? Do not complicate things, simplify it and trust me, you'll do better on the long run."
    hide cashflowLiability with dissolve
    show mc smiling at center with move
    persistent.mc "So, what should you remember?"
    persistent.mc "Well, just remember what my {i}rich{/i} dad said."
    persistent.mc "An asset is something that puts money {b}IN{/b} your pocket, and a liability is something that takes money {b}OUT{/b} of your pocket."
    show mc defaultEmotion with dissolve
    persistent.mc "If you want to be rich, you could simply spend your life buying assets."
    persistent.mc "If you want to be poor or middle class, then... spend your life buying liabilities."

    show mc unfocused at left with move
    show Liam smiling at right with moveinright
    Liam "Ohh, I see. Now that we know the difference..."
    Liam "Could you atleast show us the cashflow-pattern of the three classes? Mainly the poor's, middle class', and the rich's?"

    show Liam unfocused at right
    show mc smiling at left
    with dissolve
    persistent.mc "Yeah, sure thing. Let me just draw them up real quick."
    hide mc
    hide Liam
    with dissolve
    
    window hide
    play sound "audio/sfx/drawOnPaper.mp3" volume 0.5
    pause 2.0
    window auto

#The arrows in the diagrams represent the “cash flow.”.
    show mc defaultEmotion at left with moveinleft
    show cashflowPoor at truecenter with moveinbottom
    persistent.mc "This is an example of a cashflow pattern of those who are poor."
    hide cashflowPoor with dissolve
    show cashflowMiddleClass at truecenter with moveinbottom
    persistent.mc "And, here's for those who are in the middle class."
    hide cashflowMiddleClass with dissolve
    show cashflowRich at truecenter with moveinbottom
    persistent.mc "And lastly, here's a cashflow-pattern of those who are rich."
    hide cashflowRich with dissolve
    
    show mc smiling at center with move
    persistent.mc "As you can see, all of these diagrams are obviously oversimplified."
    persistent.mc "Everyone has living expenses, the need for food, shelter, and clothing."
    persistent.mc "If your pattern is to spend everything you get, then most likely an increase in cash will just result in an increase in spending."
    show mc defaultEmotion with dissolve
    persistent.mc "Therefore I could say, that people are clueless as to how and why they struggle financially."
    persistent.mc "It's certainly because they don’t understand cash flow."
    show mc thinking with dissolve

#Choice_3
    label ch2Choices2:
        persistent.mc "{i}Anyways... should I tell them another story?{/i}"
        persistent.mc "{i}Just so that they could understand things more clearly?{/i}"
    menu:
        "Yes":
            jump yes2

        "No":
            jump no2

#MENU3_YES
    label yes2:
        show mc defaultEmotion with dissolve
        persistent.mc "{i}Eh, I prolly should{/i}."
        persistent.mc "Alright, I hope that didn't bore you, gentlemen."
        show mc smiling with dissolve
        persistent.mc "As I... have another story to tell you."
        jump WifeHusbandStory

#MENU3_NO
    label no2:
        show mc defaultEmotion at left with move
        persistent.mc "..."

        show mc unfocused at left with dissolve
        show William defaultEmotion at right with moveinright
        William "Aw, come on {b}[persistent.mc]{/b}. Tell us another story!"
        show William smiling with dissolve
        William "You never know, we might learn a thing or two from it!"

        show William unfocused at right
        show mc thinking at left 
        with dissolve
        persistent.mc "Hmm, let me think about it."

#Choice Menu 4
    menu:
        "Tell another story?":
            jump WifeHusbandStory
        "Pass.":
            jump NoStory

#wife and husband story
    label WifeHusbandStory:

    show mc defaultEmotion with dissolve
    persistent.mc "Here is a classic story of two hardworking people who has basically set a pattern in terms of how they spend their hard-earned money."

    show mc unfocused at left with move
    show William smiling at right with moveinright
    William "Ohhh!" with vpunch

    show William unfocused at right
    show mc defaultEmotion at left 
    with dissolve
    persistent.mc "Alright, here goes..."
    persistent.mc "The recently married, happy, and highly educated young couple moved into one of their small rented apartments."
    
    stop music fadeout 1
    stop ambient fadeout 0.5

    hide mc 
    hide William
    with dissolve

    scene apartmentLivingRoom with fade
    play music "audio/bgm/dreamHouse.ogg" fadein 0.5 volume 0.25
    #scene Wife opening door of the new apartment
    play sound "audio/sfx/openDoor.mp3" volume 0.5
    show wife focused with dissolve
    wife "Hon, this apartment looks great!"

    show husband focused with dissolve
    #picture of husband hugging wife from the back
    husband "Yeah... we'll finally be together, honey."

    hide wife
    hide husband 
    with dissolve

    "As months passed by, they realized that they are saving money as the two of them can live as cheaply as one."

    show husband focused with dissolve
    husband "Hey, uhh look honey..."

    show wife focused with dissolve
    wife "Hmm?"
    hide wife focused with dissolve

    husband "I think we can save enough money to buy our dream house and you know... have kids."

    show wife focused with dissolve
    wife "{b}..!{/b}" with vpunch
    wife "But honey, isn't it too {i}early{/i} for us to buy a house?"

    hide wife with dissolve
    husband "No, I don't think so. Plus, we have two income streams, we could definitely buy one."

    show wife focused with dissolve
    wife "I really like the idea of having our own house, but..." 
    wife "But then our expenses will rise."
    hide wife with dissolve

    husband "Well... if we save money from living in this small apartment, then why not buy our dream house? it could be our {i}biggest{/i} asset."
    
    show wife focused with dissolve
    wife "Okay, honey... if you say so then let's do that, alright?"

    hide wife
    hide husband
    with dissolve

    "They focused on their career to increase their incomes but as their incomes go up... their expenses go up as well."
    "And as a result of their incomes increasing, they decided to buy the house of their dreams."
    "And once they get that house built, they then have a new tax (property tax), which is another expense to pay for."

    scene dreamHouseLivingRoom with fade
    show wife focused with dissolve
    wife "Honey! Our dream house looks great!"

    show husband focused with dissolve
    husband "Yeah, it totally looks great."
    husband "You know, this wouldn't happen without you."
    hide husband with dissolve

    wife "Aww, you're such a tease!"

    show husband focused with dissolve
    husband "Now that we're here, how about we buy the necessary furnitures and appliances?"
    hide husband with dissolve

    wife "Yeah, I think we should do that."

    scene applianceStore with fade
    show wife focused with dissolve
    wife "Look hon! With this TV, we can finally binge-watch those series on the big screen!"
    wife "We could even pair it with the sofa set we saw on the other store awhile ago!"

    show husband focused with dissolve
    husband "Well, say no more! Let's get both of it then."
    play sound "audio/sfx/openCashRegister.mp3" volume 0.5

    hide wife
    hide husband
    with dissolve

    scene plainWhite with fade
    "And a few months later..."

    scene dreamHouseDiningRoom with fade 
    play sound "audio/sfx/knifePutDownOnPlate.mp3" volume 0.5
    show husband solo at left with moveinleft
    show wife solo unfocused at right with moveinright
    husband "Hmm... I think we need to buy a car so that we won't have to commute to work everyday."
    
    show husband solo unfocused
    show wife solo
    with dissolve
    wife "And also, we can go wherever and whenever we want to go."
    wife "But, do we have enough money to buy a new one?"

    show wife solo unfocused
    show husband solo
    with dissolve
    husband "Don't worry about the money, we could put it under a loan."

    show husband solo unfocused
    show wife solo 
    with dissolve
    wife "Well, if you say so."

    scene carShop with fade
    show salesman smiling with dissolve
    salesman "Good day ma'am and sir, how may I help you today?"

    show salesman unfocused at right with move
    show husband focused at left with moveinleft
    husband "Hello, I'm actually looking for a car."
    husband "A car not too large, yet not too small - something perfect for me and my wife."

    show husbandwife unfocused at left
    show salesman smiling at right 
    with dissolve
    salesman "Ahh I see. I think I have the perfect car for you."

    hide salesman
    hide husband
    hide husbandwife
    with dissolve 

    show salesman smiling at left with moveinleft
    salesman "This car looks great for you and your wife. It's a 4-seater car, so if you ever have a plan on having kids, then..."
    salesman "This would definitely be a safe purchase on your end."

    show salesman unfocused at right with move
    show husband focused at left with moveinleft
    husband "{i}Hmm, come to think of it, having it 4-seater would be the safest bet...{/i}"
    husband "Alright, we'll get this one."

    show husbandwife unfocused at left
    show salesman smiling at right
    with dissolve
    salesman "Glad to be of service. Well then..."
    salesman "Let's settle the payment and papers over there."
    play sound "audio/sfx/signingOnPaper.mp3" volume 0.5
    pause 1.0
    play sound "audio/sfx/openCashRegister.mp3" volume 0.5

    scene mansionParty with fade
    show mc defaultEmotion with dissolve 
    persistent.mc "They didn't realize that their liabilities column was full of mortgage and credit card debt. Their liabilities went up like there's no tomorrow."
    persistent.mc "Pretty soon, a baby comes along... and they worked even harder."
    persistent.mc "And as they work harder, they get their salaries raised."
    show mc smiling with dissolve
    persistent.mc "Sure, a raise is definitely nice, but it also comes with increased taxes."
    show mc sad with dissolve
    persistent.mc "When they were able to get a credit card, they used it and maxed it out to buy different things that they clearly do {b}NOT{/b} need."
    persistent.mc "After a few months, a loan company called and told them that their greatest \"asset,\" their home, has appreciated in value because their credit score is so good."
    persistent.mc "The company then offers them a {b}{i}Debt Consolidation Loan{/i}{/b}, telling them that the intelligent thing to do is to avail this to pay off their credit cards."
    show mc defaultEmotion with dissolve
    persistent.mc "With the Debt Consolidation Loan, that alone should pay off their high-interest consumer debt."
    persistent.mc "They went and secured for it - paying off those high-interest credit cards."
    persistent.mc "And with that, they’ve now folded their consumer debt into their home mortgage."
    persistent.mc "The amount of debt they would pay timely went down because they extended their debt over 30 years as it is the {i}smartest{/i} thing to do in their current predicament."

    scene dreamHouseKitchen with fade
    play sound "audio/sfx/telephoneRinging.mp3" volume 0.5
    queue sound "audio/sfx/pickupTelephone.mp3" volume 0.5
    show wife solo with dissolve
    wife "Hello?"

    show wife solo unfocused with dissolve
    neighbor "Hello Mrs. X! I just wanted to ask if you'd want to come shopping with us?"

    show wife solo with dissolve
    wife "Ah! Hello! Uhmm, why exactly are we gonna go shopping?"

    show wife solo unfocused with dissolve
    neighbor "The Memorial Day Sale is on!"
    
    show wife solo with dissolve
    wife "Oh, I see..."
    wife "Wait a minute, I'll call you back, alright?"
    play sound "audio/sfx/hangupTelephone.mp3" volume 0.5

    scene dreamHouseLivingRoom with fade
    show wife solo with dissolve 
    wife "Honey, our neighbor just called and asked if we would want to go shopping because apparently... it's the Memorial Day Sale today."
    wife "We could definitely save money if we were to buy the things we need right now."

    show wife solo unfocused at right with move
    show husband solo at left with moveinleft
    husband "Sure, let's go. But we'll just be window shopping first, alright?"
    
    show husband solo unfocused at left
    show wife solo at right 
    with dissolve 
    wife "Only window shopping... but may we bring our credit cards? Just in case?"
    wife "Please...?"
    
    show wife solo unfocused at right
    show husband solo at left 
    with dissolve
    husband "Hmmm..."
    husband "Alright."

    show husband solo unfocused at left
    show wife solo at right 
    with dissolve
    wife "{b}...!{/b}" with vpunch
    wife "Thank you, honey!"

    scene dreamHouseKitchen with fade
    play sound "audio/sfx/dialTelephone.mp3" volume 0.5
    queue sound "audio/sfx/telephoneDialTone.mp3" volume 0.5
    show wife solo with dissolve
    wife "..."
    play sound "audio/sfx/pickupTelephone.mp3" volume 0.5
    show wife solo unfocused with dissolve
    neighbor "Hello...?"
    show wife solo with dissolve
    wife "Hi! I got my husband's go signal! Let's meet there at 2PM in the afternoon!"
    show wife solo unfocused with dissolve
    neighbor "Oh! Absolutely!"
    play sound "audio/sfx/hangupTelephone.mp3" volume 0.5
    
    play music "audio/bgm/thejazzpiano.mp3" fadein 0.5 volume 0.25
    scene mansionParty with fade
    play ambient "audio/sfx/laughingChitchat.mp3"
    show mc defaultEmotion with dissolve
    persistent.mc "And with that, they don't realize that their problems result from how they spend the money they have."
    persistent.mc "As long as they continue being like that, they would never escape the thing my {i}rich{/i} dad call \"{b}{i}Rat Race{/i}{/b}\""
    persistent.mc "Now that the topic at hand is about debt, I suddenly remembered what my friend usually say to those who are in the same predicament..."
    persistent.mc "Apparently, it goes something like this, “{i}If you found out that you've dug yourself into a hole, stop digging{/i}.”"
    
    show mc unfocused at left with move
    show William defaultEmotion at right with moveinright
    William "Ohh..."
    William "Man, those young couple are easily blinded by their wants."

    show William unfocused at right with dissolve
    show mc smiling at left with dissolve
    persistent.mc "Yeah, I totally agree with you."
    show mc defaultEmotion at left with dissolve
    persistent.mc "Well, moving on..."
    jump sword

    label NoStory:
    scene mansionParty with fade
    show mc smiling at left with dissolve
    persistent.mc "Let me tell you this instead."

    jump sword

    label sword:
    show mc defaultEmotion at left with dissolve
    persistent.mc "As a child, my dad often told us that the Japanese were aware of three powers: "
    persistent.mc "The Power of the Sword, the Jewel, and the Mirror."
    persistent.mc "The Sword symbolizes the power of... weapons, obviously."
    persistent.mc "The Jewel symbolizes the power of money."
    persistent.mc "And lastly, the Mirror symbolizes the power of self-knowledge."
    persistent.mc "This self knowledge, the mirror... according to them, was the most treasured out of the three categories."
    persistent.mc "And that is why the Japanese valued it the most."
    persistent.mc "The fear of ostracism... the fear of being singled out and criticized that causes people to conform to, and not to ask questions."
    persistent.mc "With that, people easily and commonly accepted opinions as well as popular trends like: "
    persistent.mc "“{i}Your home is an asset.{/i}”, “{i}Work harder.{/i}”, “{i}Get a promotion.{/i}”, “{i}Save money.{/i}”, “{i}When I get a raise, I’ll buy us a bigger house.{/i}” and the like."
    persistent.mc "Many financial problems are caused by trying to keep up with the Joneses by buying expensive cars and clothes that they don't really need, and at the same time they can't even afford."
    
    show mc unfocused at left with dissolve
    show William defaultEmotion at right with dissolve
    William "Ohh, I see..."
    William "Yeah, I totally get that one as I was also a victim of those trends."
    William "I believe it's an event called FOMO, or Fear of Missing Out, and man, when I realized it..."
    William "I immediately knew I wasted money just for satisfaction in a short amount of time."

    show mc smiling at left with dissolve
    persistent.mc "Well, atleast you've learnt something. I'm sure that's what's important."
    persistent.mc "You know, honestly..."

    show mc defaultEmotion at left with dissolve
    persistent.mc "I really am not the type of a business-oriented person, like someone who has vast knowledge of managing businesses or the likes."
    persistent.mc "I often spent hours at work just sitting at a table while holding meetings together with my bankers, attorneys, accountants, brokers, investors, managers, and employees."
    persistent.mc "I remember my {i}rich{/i} dad kept me telling this over and over again: "

    scene richDadOffice with fade
    show richDad slyGrin with dissolve
    richDad "“An intelligent person hires people who are more intelligent than he is.”" 

    scene mansionParty with fade
    show mc smiling with dissolve
    persistent.mc "And so I did it, I hired people to do something I'm not familiar with, sure it might be contradicting to what I said earlier by obtaining assets."
    show mc defaultEmotion with dissolve
    persistent.mc "But personally, I see my employees as assets. Yes, I give them their due money, but without them I wouldn't gain money in my pocket automatically."
    persistent.mc "And, it's also fine to stray away from the norm."

    show mc unfocused at left with move
    show Liam defaultEmotion at right with moveinright
    Liam "Hmm, what norm exactly?"

    show Liam unfocused at right
    show mc smiling at left
    with dissolve
    persistent.mc "Hmm..."
    persistent.mc "Something like disagreeing with the standard dogma my teachers preached."

    scene kidMCSchool with fade
    show teacher defaultEmotion with dissolve
    teacher "Class! If you don’t get good grades, I assure you, you won’t do well in the real world."
    
    show teacher unfocused at right with move
    show kidMC thinking at left with moveinleft
    persistent.kidMC "{i}Hmm...{/i}"
    persistent.kidMC "{i}I started to understand why rich dad told us that schools were designed to produce good employees, instead of employers{/i}."
    persistent.kidMC "{i}They only teach how we could apply the things we learnt in the real world, yet alone how money works."
    persistent.kidMC "{i}Even to manage it? Nah, it's likely impossible they teach this unless you enrolled in a specialization class regarding the subject of business or the likes{/i}."
    
    show kidMC unfocused at left
    show teacher defaultEmotion at right 
    with dissolve
    teacher "My point is, the subject of money is not important, {b}FOR{/b} if you excelled in education, money would follow you."

    show teacher unfocused at right
    show kidMC confused at left
    with dissolve
    persistent.kidMC "{i}Hmm, yeah-nope{/i}."
    show kidMC defaultEmotion with dissolve
    persistent.kidMC "{i}Yes, excelling on your specialization is really great and would help you land a job. "
    persistent.kidMC "Having a job at first would definitely help you build your foundation but then after that, now what?"
    show kidMC sad with dissolve
    persistent.kidMC "You might even get stuck in the {b}{i}Rat Race{/i}{/b} if you're not careful."

    hide teacher
    hide kidMC 
    with dissolve

    "From that day onwards, I became distant to the teachers and some of my classmates who blindly agreed to her point of view and opinion."

    scene plainWhite with fade
    "And the next day."

    scene kidMCLivingRoom with fade
    show biologicalDad defaultEmotion with dissolve
    biologicalDad "You know son, our house is my most valuable investment."
    
    show biologicalDad unfocused at right with move
    show kidMC confused at left with moveinleft
    persistent.kidMC "Eh, I don't think so, dad."
    
    show kidMC unfocused at left
    show biologicalDad smiling at right 
    with dissolve
    play sound "audio/sfx/newspaperFlip.mp3" volume 0.5
    biologicalDad "Why do you think so, young man?"
    show biologicalDad defaultEmotion with dissolve
    biologicalDad "You haven't even taken a specialization in managing finance and investments..."
    biologicalDad "Yet how could you confidently say that? Hm?"

    show biologicalDad unfocused at right
    show kidMC defaultEmotion at left 
    with dissolve
    persistent.kidMC "Well Dad... this is why I thought that buying a house is not a good investment nor an asset."
    play sound "audio/sfx/drawOnPaper.mp3" volume 0.5
    show kidMC surprised at left with dissolve
    show ancillaryExpenses at truecenter with moveinbottom
    persistent.kidMC "Look dad, a bigger home equates to bigger expenses, and as you can see, the cash flow kept going out through the expense column."
    
    show kidMC unfocused at left
    show biologicalDad defaultEmotion at right
    with dissolve
    biologicalDad "Hmm..."
    show biologicalDad flustered with dissolve
    biologicalDad "I see..."

    scene mansionParty with fade
    show mc defaultEmotion with dissolve 
    persistent.mc "You know... emotions plays a big role when it comes to your financial decisions."
    persistent.mc "I could boldly state that as I've already been there. Money has a way of making every decision emotional."
    show mc flustered with dissolve
    persistent.mc "Now, I am not saying that you shouldn't buy a house, a car, clothing or whatsoever."
    show mc surprised with dissolve
    persistent.mc "What I want to point out is that you should understand the difference between an asset and a liability."
    show mc defaultEmotion with dissolve
    persistent.mc "For example, when I want a bigger house... I first buy assets that will {b}GENERATE{/b} the cash flow to {b}PAY{/b} for the house."
    show mc sad with dissolve
    persistent.mc "And believe it or not, my \"highly-educated\" dad’s personal financial statement best demonstrates the life of someone caught in the {b}{i}Rat Race{/i}{/b}."
    persistent.mc "His expenses matches his income, never allowing him to have any amount of money left to invest in assets. And as a result..."
    persistent.mc "His liabilities are larger than his assets."
    show mc smiling with dissolve
    persistent.mc "To give a better idea of how different are my fathers' cash flows are, let me show you their cashflow-pattern."
    play sound "audio/sfx/drawOnPaper.mp3" volume 0.5
    show mc smiling at left with move
    show poorDadCashFlow at truecenter with moveinbottom
    persistent.mc "This one belongs to my real dad, it shows that his income and expenses are equal while his liabilities are larger than his assets."
    hide poorDadCashFlow with dissolve
    show richDadCashFlow at truecenter with moveinbottom
    persistent.mc "And this one belongs to my {i}rich{/i} dad. It's pretty much self explanatory."
    persistent.mc "It reflects the results of a life dedicated to investing and minimizing liabilities."
    hide richDadCashFlow with dissolve
    
    show mc defaultEmotion with dissolve
    persistent.mc "So, why does the rich get richer?"
    play sound "audio/sfx/drawOnPaper.mp3" volume 0.5
    show richGetRicher at truecenter with moveinbottom
    persistent.mc "Their asset column provides enough money to cover their expenses, and with the remaining balance, they reinvest it on other assets."
    show mc smiling with dissolve
    persistent.mc "Therefore, their asset column continuously grow and thus, the income it produces grows with it."
    persistent.mc "It might be simple, but that really is the most logical thing to do with your money if ever you want to keep your money flowing."
    hide richGetRicher with dissolve
    
    show mc defaultEmotion with dissolve
    persistent.mc "Moving on, why do those who are in the middle class struggle then?"
    play sound "audio/sfx/drawOnPaper.mp3" volume 0.5
    show middleClassStruggles at truecenter with moveinbottom
    persistent.mc "As you can see on the diagram, their salary is their primary source of income, and as their salaries increase, so do their taxes."
    show mc sad with dissolve
    persistent.mc "They use their home as their primary \"asset\", rather than investing in income-producing assets."
    persistent.mc "Also, in most cases, their spending tends to increase in proportion to their pay increase, hence getting stuck in the {b}{i}Rat Race{/i}{/b}."
    show mc defaultEmotion with dissolve
    persistent.mc "This pattern of treating your home as an investment, a pay raise that makes you spend more is the foundation of today’s debt-ridden society."
    persistent.mc "Increased spending throws a lot of families into greater debt and into more financial uncertainty."
    hide middleClassStruggles with dissolve

    show mc unfocused at left with dissolve
    show Liam smiling at right with moveinright
    Liam "So, you're saying that I need to invest in something that will generate money for me."
    Liam "And not in something that will cost my money in the long run?"
    
    show Liam unfocused at right with dissolve
    show mc smiling at left with dissolve
    persistent.mc "Exactly! If I want to increase my expenses, then I first have to increase my cash flow to {b}MAINTAIN{/b} this level of wealth."
    persistent.mc "If I quit my job today, I would be able to cover my monthly expenses with the cash flow from my assets."
    show mc defaultEmotion with dissolve
    persistent.mc "The more money that goes into my asset column, the more my asset column grows."
    persistent.mc "My cash flow increases as my assets increase, and as long as I keep my expenses lower than the cash flow from these assets such as investments, stocks, and etc."
    show mc smiling with dissolve
    persistent.mc "Then I grow richer with more and more income from different sources other than my current job or occupation."
    
    show mc unfocused at left
    hide Liam
    with dissolve

    show William defaultEmotion at right with moveinright 
    William "Ah I see. I totally get it now! Thank you for your advice, {b}[persistent.mc]{/b}."
    William "Even though I thought differently, I get your point on how to get rich."

    show William unfocused at right with dissolve
    show mc surprised at left with dissolve
    play sound "audio/sfx/telephoneDialTone.mp3" volume 0.5
    persistent.mc "{b}...!{/b}" with vpunch
    persistent.mc "Oh, excuse me for a sec, gentlemen."
    show mc smiling with dissolve
    persistent.mc "Wife's calling, gotta take this call, sorry."
    
    show mc unfocused at left
    show William smiling at right 
    with dissolve
    William "Ah! No worries! Take your time, {b}[persistent.mc]{/b}." 
    hide William with dissolve

    show mc smiling at center with move
    play sound "audio/sfx/pickupTelephone.mp3" volume 0.5
    persistent.mc "Hi honey! I just finished talking to some people here."
    show mc unfocused with dissolve
    Kim "Hi uhh, it's kinda getting late already, what time will you come home?"
    show mc defaultEmotion with dissolve
    persistent.mc "Hmm, why?"
    show mc unfocused with dissolve
    Kim "Nothing much, it's just that I'll be waiting for you to come home."
    show mc defaultEmotion with dissolve
    persistent.mc "Ah I see, well it is getting late indeed."
    persistent.mc "... Okay, I'll just bid farewell to these gents and I'll be on my way home, alright?"
    show mc unfocused with dissolve
    Kim "Okay, take care on your way home! I'll be waiting for you."
    show mc smiling with dissolve
    persistent.mc "Yup I will, I love you!"
    show mc unfocused with dissolve
    Kim "I love you too, you take care alright?"

    show mc unfocused at left with move
    play sound "audio/sfx/footSteps.ogg" volume 0.5
    show john smiling at right with moveinright
    john "Hey guys, ya'll having fun so far? Hm?"

    show john unfocused at right
    show mc smiling at left 
    with dissolve
    persistent.mc "Hey there, John. Welcome back, man."
    show mc defaultEmotion with dissolve
    persistent.mc "Ah, I was talking to these gents for a little while."
    show mc smiling with dissolve
    persistent.mc "And uhh... yeah, they're fun to be with!"

    show mc unfocused at left
    show john smiling at right 
    with dissolve
    john "Ah I see. That's great, man! Appreciate it."
    john "So, are you enjoying the party so far?"

    show john unfocused at right
    show mc smiling at left 
    with dissolve
    persistent.mc "Absolutely! But uhh..."
    show mc defaultEmotion at left with dissolve
    persistent.mc "I kinda need to go now, man."

    show mc unfocused at left with dissolve
    show john sad at right with dissolve
    john "Aww, come on {b}[persistent.mc]{/b}!"
    show john smiling with dissolve
    john "Have a drink or two with us first before going!"

    show john unfocused at right
    show mc defaultEmotion at left 
    with dissolve
    persistent.mc "Ah, as much as I want to John, I'm really sorry but I can't." 
    show mc smiling with dissolve
    persistent.mc "But, don't worry. I'll make it up to you next time, alright?"

    show mc unfocused at left
    show john smiling at right 
    with dissolve
    john "If you say so, {b}[persistent.mc]{/b}. Feel free to call me if you need anything, okay?"

    show john unfocused at right
    show mc defaultEmotion at left 
    with dissolve
    persistent.mc "Yeah, absolutely."
    persistent.mc "Anyways, I'll be taking my leave now."
    show mc smiling with dissolve
    persistent.mc "Oh! Also tell those gents over there that I enjoyed our little get-along together. Thanks!"

    show mc unfocused at left
    show john smiling at right with dissolve
    john "Sure sure, no problem! I got you!"
    john "Take care on your way home, {b}[persistent.mc]{/b}!"
    hide john with dissolve

    show Liam smiling at right with moveinright
    Liam "Hey {b}[persistent.mc]{/b}!" with vpunch
    Liam "Thank you for sharing us some of your {i}secrets{/i} on how to get rich! I'll forever remember them!"

    show Liam unfocused at right
    show mc smiling at left 
    with dissolve
    play sound "audio/sfx/chuckle.mp3"  volume 0.5
    persistent.mc "Hahaha, alright Liam."
    show mc smiling with dissolve
    persistent.mc "See ya, gents!"

    hide Liam with dissolve
    hide mc with dissolve

    stop ambient fadeout 0.5
    stop music fadeout 0.5
    
    #scene mc drivinghome

    scene mcLivingRoom1 with fade
    play music "audio/bgm/kidMCHouse.ogg" fadein 0.5 volume 0.25
    play sound "audio/sfx/openDoor.mp3" volume 0.5
    show mc smiling at right with moveinright
    persistent.mc "Hi! I'm home."

    show mc unfocused at right with dissolve
    show Kim smiling at left with moveinleft
    Kim "Welcome home, {b}[persistent.mc]{/b}."
    Kim "Take a half bath and change your clothes."
    show Kim defaultEmotion with dissolve
    Kim "After that, eat the meal I've prepared beforehand if you feel hungry alright?"

    show Kim unfocused
    show mc smiling
    with dissolve
    persistent.mc "Yup. Will do, honey!"

    window hide
    scene plainBlack with fade
    play sound "audio/sfx/showerSound.mp3" volume 0.5
    pause 2.0
    stop sound fadeout 0.5
    queue sound "audio/sfx/openShowerDoor.mp3" volume 0.5
    pause 1.0
    window auto

    scene mcLivingRoom with fade
    show mc casual smiling at left with dissolve
    persistent.mc "Welp, feeling fresh already."

    show mc casual unfocused at left with dissolve
    show Kim defaultEmotion at right with moveinright
    Kim "I'll go ahead alright? I'm kinda sleepy already."
    show Kim smiling with dissolve
    Kim "Wash the dishes after you eat. And make sure to turn off every lights and appliances before you go up, okay?"
    
    show Kim unfocused at right 
    show mc casual smiling at left 
    with dissolve
    persistent.mc "Yup! Don't worry, honey. I know."
    stop music fadeout 0.5

    $ analytics.event("Chapter 2", "FINISHED")
    $ persistent.ch02 = True
    return
#=============================================================================================================================#