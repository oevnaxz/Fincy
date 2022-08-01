label startChapter5:
    $save_name = "Chapter 05: The Rich Invent Money"
    scene plainWhite with fade

    #Flashing the Title Screen
    window hide
    show screen title_screen(_("{b}LESSON 5: THE RICH INVENT MONEY{/b}"))
    with dissolve
    pause 2
    hide screen title_screen
    with dissolve
    window auto

#MC House

    scene mcLivingRoom1 with fade

    show mc casual smiling with dissolve
    persistent.mc "Hey, Kim."
    show mc casual defaultEmotion with dissolve
    persistent.mc "Have you noticed something different?"

    show mc casual unfocused at left with move
    show Kim defaultEmotion at right with moveinright
    Kim "Hmm? What is it, {b}[persistent.mc]{/b}?"

    show Kim unfocused at right
    show mc casual smiling at left 
    with dissolve
    persistent.mc "Do you know that the economy right now is in a {b}horrible{/b} state?"
    persistent.mc "And we both know that this is the {b}PERFECT{/b} time to purchase property in the market!"

    show mc casual unfocused at left
    show Kim smiling at right 
    with dissolve
    Kim "Ohh come to think of it, it really is!" with vpunch
    show Kim defaultEmotion with dissolve
    Kim "How about we both go to our local real estate agents and check what properties are available? What do you think?"

    show Kim unfocused at right
    show mc casual surprised at left 
    with dissolve
    persistent.mc "Hmm, no. I don't think we should."
    show mc casual defaultEmotion with dissolve
    persistent.mc "I think we should visit a bankruptcy attorney's office instead."
    show mc casual smiling with dissolve
    persistent.mc "Because in these commercial centers, a $120,000 property may occasionally be purchased for $85,000 or less."
    persistent.mc "And if you ask me, that's definitely a steal!"

    show mc casual unfocused at left
    show Kim smiling at right 
    with dissolve
    Kim "Oh, I haven't heard of that!" 
    Kim "I can't wait to go there and see what properties they have for sale!"


    scene plainWhite with fade
    "With that, we've decided to go to our local bankruptcy attorney's office to check out their possible offers on different properties."
    "And hours later..."
#Office

    scene Office with fade
    play sound "audio/sfx/openDoor.mp3" volume 0.5
    show mc smiling with dissolve
    persistent.mc "Hi! Good day!"
    persistent.mc "May we take a look at some properties you offer?"

    show mc unfocused at left with move
    show Attorney smiling at right with moveinright
    Attorney "Hello dear clients! Sure thing!"
    Attorney "We actually have a lot of properties with varying prices for sale right now!"

    show Attorney unfocused at right
    show mc thinking at left
    with dissolve
    persistent.mc "Hmm..."
    persistent.mc "......"

    show mc unfocused at left
    show Attorney defaultEmotion
    with dissolve
    Attorney "If I may, I would like to recommend you this property." 
    play sound "audio/sfx/newspaperFlip.mp3"
    show mcReadInvitation at truecenter with dissolve #*Attorney hands him a paper showing picture of the property*
    Attorney "Apparently, this house is one of our cheapest properties. It would only cost you around $30,000."

    show Attorney unfocused at right
    show mc defaultEmotion at left
    with dissolve 
    persistent.mc "Hmm... I see."
    persistent.mc "{i}Interesting.{/i}"
    hide mcReadInvitation with dissolve
    show mc smiling at left with dissolve
    persistent.mc "Alright! I'll take this one!"

    show mc unfocused at left
    show Attorney smiling at right 
    with dissolve
    Attorney "Great! To continue our transaction, you would atleast need to make a down payment and that's it."
    Attorney "After that, the property will now be under your name."

    show Attorney unfocused at right
    show mc smiling at left 
    with dissolve
    persistent.mc "Ah! Of course, here's the cheque."

    hide mc
    hide Attorney
    with dissolve

    window hide
    play sound "audio/sfx/openCashRegister.mp3" volume 0.5
    pause 1.5
    window auto

    show mc unfocused at left
    show Attorney smiling at right 
    with dissolve
    Attorney "Aaaand... it's now settled." 
    Attorney "We'll update you after processing the property's documents."

    show Attorney unfocused at right
    show mc smiling at left
    with dissolve
    persistent.mc "Alright. Thank you!"

    scene plainWhite with fade
    play sound "audio/sfx/telephoneDialTone.mp3" volume 0.5
    "With the transaction being process, not long after did I received a phone call."
    stop sound fadeout 0.5
    play sound "audio/sfx/pickupTelephone.mp3" volume 0.5
    "It turns out that the caller is interested on the property I've put up on sale."
    "And of course... I wouldn't say no to them."
    "Hell, I didn't even bothered to bargain with them more, since I've easily gained profit from the property itself."

#Restaurant

    scene Restaurant with fade

    show Kim casual smiling with dissolve
    Kim "So honey, how was it? I mean the transaction?"
    Kim "Have you already bought a property?"
    
    show Kim casual unfocused at right with move
    show mc smiling at left with moveinleft
    persistent.mc "Yeah! And the price is cheaper just as I expected." 
    persistent.mc "I actually got it for only $30,000!"
    
    show mc unfocused at left
    show Kim casual smiling at right 
    with dissolve
    Kim "That's surprising!" with vpunch 
    Kim "By the way, how much will you sell it?"

    show Kim casual unfocused at right
    show mc smiling at left 
    with dissolve
    persistent.mc "While the purchase was being finalized..."
    play sound "audio/sfx/chuckle.mp3" volume 0.5
    persistent.mc "I actually placed an ad in the paper offering an $85,000 house for $70,000 with no money down."

    show mc unfocused at left
    show Kim casual smiling at right 
    with dissolve
    Kim "I'm really impressed with how your intelligence works!"

    show Kim casual unfocused at right
    show mc smiling at left 
    with dissolve
    persistent.mc "Maybe, you'll be more surprised if I say that I already have a client..."
    persistent.mc "And they've already agreed to buy the property."

    show mc unfocused at left
    show Kim casual defaultEmotion at right
    with dissolve
    Kim "Really? That fast?!" with vpunch
    show Kim casual defaultEmotion at right with dissolve
    Kim "Was it the person with whom you were on the phone call earlier?"

    show Kim casual unfocused at right
    show mc smiling at left 
    with dissolve
    persistent.mc "Yup! Plus, they're also easy to communicate with."
    persistent.mc "That alone helped me closed the deal with them in a short amount of time."

    show mc unfocused at left
    show Kim casual smiling at right 
    with dissolve
    Kim "{b}WAIT!{/b} Did you just earn $50,000 in a day?!" with sshake

    show Kim casual unfocused at right
    show mc smiling at left 
    with dissolve
    persistent.mc "Correction honey, it's only for 5 hours."

    show mc unfocused at left
    show Kim casual smiling at right 
    with dissolve
    Kim "Wow... just wow... I'm literally speechless."
    Kim "Is there anything else you can say that will make my jaw drop?"

    show Kim casual unfocused at right
    show mc smiling at left 
    with dissolve
    persistent.mc "Nah, I'm done impressing you for today, honey."
    persistent.mc "Anyways, let's eat. And since I closed a great transaction, the tab's on me."

    window hide
    scene plainBlack with fade
    pause 1.0
    play sound "audio/sfx/knifePutDownOnPlate.mp3" volume 0.5
    pause 1.0
    window auto

#House2

    scene mcBedroomNight with fade
    #Narration
    #Mc talking to users

    show mc casual defaultEmotion with dissolve
    persistent.mc "So... that's one of the examples on how you can create money."
    persistent.mc "But, before you spend your money on an investment..."
    show mc casual smiling with dissolve
    persistent.mc "Do make sure that you understand what you're getting into, alright?"
    persistent.mc "Come to think of it, I've been a professional teacher for years now."
    show mc casual defaultEmotion with dissolve
    persistent.mc "I've taught hundreds of people, and there's one thing that all of us, including myself, have in common."
    persistent.mc "We all have immense potential and are endowed with special abilities." 
    persistent.mc "Self-doubt, on the other hand, is the one thing that holds us all back."
    persistent.mc "And one thing I have realized when it comes to the subject of money is that everyone would rather play it safe."
    show mc casual smiling with dissolve
    persistent.mc "But for you, the one who's reading this, I... have a question for you."

    label choice1:
        persistent.mc "Do you consider yourself as a risk taker?"

    menu:

        "Yes.":
            $ analytics.event("Chapter 5: Risk Taker?", "1")
            jump RiskTaker

        "No.":
            $ analytics.event("Chapter 5: Risk Taker?", "0")
            jump NotRiskTaker


    label RiskTaker:
        show mc casual smiling with dissolve
        persistent.mc "I admire how brave you are."
        persistent.mc "The majority of people your age are frightened of taking risks."
        show mc casual defaultEmotion with dissolve
        persistent.mc "However, we must always remember that taking risks allows us to grow and become more tough and confident..."
        persistent.mc "... regardless of its outcome."

        show mc casual smiling with dissolve
        persistent.mc "You're the only one who can make decisions on what to do with your assets when it comes to growing your money."
        persistent.mc "Hell, nobody even knows if you taking the said risk will pay off in the end." 
        persistent.mc "Nobody does, not even your friend or your fiance, but you alone."
        show mc casual defaultEmotion with dissolve
        persistent.mc "This should not, however, prevent you from taking risks."
        persistent.mc "Risks are important if you want your money to grow."
        persistent.mc "You should ponder what may possibly happen if you had taken the risk of jumping."
        jump AfterAnswering

    label NotRiskTaker:
        show mc casual defaultEmotion with dissolve
        persistent.mc "It's easy to stay in your comfort zone and do what you've always done"
        persistent.mc "But if you want to advance in your life..."
        persistent.mc "You must break free from the things that hold you back."
        show mc casual smiling with dissolve
        persistent.mc "Yes, I know that you didn't come here for life lessons and realizations."
        persistent.mc "But my point is that, taking risks - like managing it, knowing when to take it, and etc. is really important when it comes to building your wealth."
        jump AfterAnswering


    label AfterAnswering:

        show mc casual defaultEmotion with dissolve
        persistent.mc "And now that I know whether or not you're a risk taker..."
        persistent.mc "I want to tell you about something I did on a property located in Portland, Oregon back then, and let's see whether it's worth taking a risk."

#Park

    scene park with fade
    play ambient "audio/sfx/parkAmbience.mp3" volume 0.75
    #Mc jogging

    show mc casual smiling with dissolve
    persistent.mc "Ha... what a beautiful setting."
    persistent.mc "I've always longed to own property here in Oregon."
    show mc casual smiling at left with move

    scene plainWhite with fade
    play sound "audio/sfx/jogging.wav" volume 0.5
    "As usual, I did my roadwork around the neighborhood."
    "And as I was about to complete one lap, I suddenly saw a house listed for sale."

    scene signSaleNeighborhood with fade
    show mc casual defaultEmotion at right with dissolve
    stop sound fadeout 0.5
    persistent.mc "{i}Huh... wait, is that perhaps a sale sign of a property?{/i}"
    show mc casual unfocused with dissolve

    window hide
    play sound "audio/sfx/footSteps.ogg" volume 0.5
    pause 1.0
    window auto

    scene closeSignSaleNeighborhood with fade
    show mc casual defaultEmotion with dissolve
    persistent.mc "{i}I'm curious as to how much this cost.{/i}"
    persistent.mc "{i}I suppose I'll approach the owner.{/i}"

    scene closeSignSaleNeighborhood with fade
    show mc casual smiling with dissolve
    persistent.mc "Hi! Uhh... are you perhaps the owner of this house?"

    show mc casual unfocused at left with move
    show Sean smiling at right with moveinright
    Sean "{b}AH!{/b} Yes, I am the owner of this house." with vpunch
    show Sean defaultEmotion with dissolve
    Sean "I uhh, I've been selling this for quite some time now, actually."
    Sean "Oregon's real estate is currently in a slump, many people simply walk past the house without going inside."

    show Sean unfocused at right
    show mc casual smiling at left 
    with dissolve
    persistent.mc "Hmm I see. Well, the house looks beautiful outside in my opinion."
    window hide
    show mc casual smiling with dissolve
    pause 1.5
    window auto
    show mc casual smiling with dissolve
    persistent.mc "... Alright Mr., I'd like to take a look at this house of yours."

    show mc casual unfocused at left
    show Sean smiling at right 
    with dissolve
    Sean "{b}Really?!{/b}" with vpunch
    Sean "Heavens! I'm going to show you around, come follow me."

    stop ambient fadeout 0.5

#House-Interior

    scene HouseInterior with fade

    show Sean smiling at right with dissolve
    Sean "You know, this house has..."

    scene plainWhite with fade
    "Sean showed me around the house he's selling. And I gotta say, it looks really nice on the inside."
    "And after a few minutes of him showing me the different rooms and areas of the house..."
    "I've decided to buy it from him right away."

    scene HouseInterior with fade
    show Sean unfocused at right
    show mc casual smiling at left 
    with dissolve
    persistent.mc "You know what Sean, I love it. I actually do."
    persistent.mc "I’ll buy this. How much does your house cost in total?"

    show mc casual unfocused at left
    show Sean defaultEmotion at right 
    with dissolve
    Sean "!!!" with sshake
    show Sean smiling with dissolve
    Sean "It approximately costs $45,000 and after renovations, I'm sure it will look good again!"

    show Sean unfocused at right
    show mc casual surprised at left 
    with dissolve
    persistent.mc "Hmm, I don't have a lot of that cash..." 
    persistent.mc "I\'ll pay $20,000 for it. How about that?"

    show mc casual unfocused at left
    show Sean defaultEmotion at right 
    with dissolve
    Sean "Hmm..."
    show Sean smiling with dissolve
    Sean "Okay, I guess that will do. Deal."

    show Sean unfocused at right
    show mc casual smiling at left 
    with dissolve
    persistent.mc "Great! I’ll be handing you down $5,000 as down payment."

    window hide
    show mcShakeHands with dissolve
    pause 1.5
    hide mcShakeHands with dissolve 
    window auto

    show mc casual unfocused at left
    show Sean smiling at right 
    with dissolve
    Sean "Finally, it has been purchased."

#Restaurant

    scene Restaurant with fade
    play ambient "audio/sfx/restaurantAmbience.mp3" volume 0.75
    show Kim defaultEmotion with dissolve
    Kim "So, how did it go with your Oregon property?"
    Kim "Also, have you found a tenant?"

    show Kim unfocused at right with move
    show mc smiling at left with moveinleft
    mc "Yeah. He moved in last week."

    show mc unfocused at left
    show Kim smiling at right 
    with dissolve
    Kim "So... how much money is left to you after paying mortgage, expenses, and management fees?"

    show Kim unfocused at right
    show mc smiling at left 
    with dissolve
    mc "Eh... I put a little less than $40 in my pocket at the end of each month."

    show mc unfocused at left
    show Kim smiling at right 
    with dissolve
    Kim "Oh! $40 a month isn't so awful!"
    Kim "I'm sure that the market in Oregon will recover after some years. Give it some time, honey."
    Kim "I'm confident you'll sell the property for three times what you paid for it!"

    show Kim unfocused at right
    show mc smiling at left with dissolve
    mc "Thanks honey, and yeah, the state's recovery is indeed certain to happen."
    
    stop ambient fadeout 0.5

#House2

    scene mcBedroomNight with fade
    #*Narration*
    #*Mc talking to users*

    show mc casual smiling with dissolve
    persistent.mc "So, the poor Oregon real estate market had began to improve a year later."
    show mc casual defaultEmotion with dissolve
    persistent.mc "Kim was right. You know what they say \"{b}{i}What comes down, goes back up{/i}{/b}.\""
    persistent.mc "And... I was able to sell the said property that I purchased for $20,000 for $95,000."

    show mc casual smiling with dissolve
    play sound "audio/sfx/chuckle.mp3" volume 0.5
    persistent.mc "I sold it to a young couple who, amusingly, believe that the price I offered them was bargained!"

    show mc casual smiling with dissolve
    persistent.mc "The purpose of this example is to demonstrate how I risked a small amount of money can grow into a significant sum of money."
    persistent.mc "However, as I previously stated, the stock trades in which I personally engaged were {b}HIGHLY HIGH-RISK{/b} for the majority of individuals."
    show mc casual defaultEmotion with dissolve
    persistent.mc "If the Oregon real estate market does not recover, then... I lost my $20,000 investment. Nothing I could do about it, really."
    show mc casual smiling with dissolve
    persistent.mc "{b}However!{/b} I've been playing this game for quite some time now so, I am able to manage the risks I'll be taking." with vpunch
    persistent.mc "If you re-read why these investments are high-risk for most people, well..."
    persistent.mc "You might be able to build your life up in such a way that the ability to turn $25,000 into let's say... $1 million in a year is low-risk for you."
    show mc casual defaultEmotion with dissolve
    persistent.mc "Financial literacy will {b}ASSIST{/b} you in managing your money and growing it."
    persistent.mc "But first, by choosing from these options, I'd want to learn more about your personality."
    show mc casual smiling with dissolve
    persistent.mc "This can be used to determine the type of life you wish to live in the future."
    persistent.mc "So, given enough circumstances, what will be your course of action to grow your wealth?"
    
    menu:

        "Work hard. Pay for necessities (Bills, food etc), save what is left, then store it in a bank account.":
            $ analytics.event("Chapter 5: Action to Grow Wealth", "Work Hard")
            jump WorkHard

        "Take the time to develop your financial intelligence, and understand the different relationships of columns in the financial statement.":
            $ analytics.event("Chapter 5: Action to Grow Wealth", "Develop Financial Intelligence")
            jump TakeTime

#WorkHard

    label WorkHard:
        show mc casual smiling with dissolve
        persistent.mc "Following the norm, I suppose, is never a bad idea."
        persistent.mc "{i}Let’s see what will happen to our money with this kind of lifestyle, alright?"
        
        show mc casual thinking with dissolve
        persistent.mc "Let’s see, if you’re working a full time job and working 8 hours a day with a pay of $10 per hour you’ll be earning $80 a day and that will be $1,600 for a month."
        persistent.mc "And of course, you would have to pay your monthly bills, you know, the necessities, taxes, and other expenses."
        persistent.mc "Let's say this is \'your\' scenario. After paying your {b}$300{/b} monthly mortgage, {b}$600{/b} in bills, food, and other expenses. How much money do you have left?"

    menu:
        "$500.00":
            jump FiveAndEight

        "$700.00":
            jump Seven

        "$800.00":
            jump FiveAndEight

#FiveAndEight

    label FiveAndEight:
        show mc casual defaultEmotion with dissolve
        persistent.mc "I suppose that is not the right answer."
        show mc casual smiling with dissolve
        persistent.mc "However the total amount will be left on you is {b}$700{/b}."
        show mc casual defaultEmotion with dissolve
        persistent.mc "Do you think that having $700 monthly will be enough for you to get rich?"

    menu:

        "Yes.":
            jump YesFiveAndEight

        "No.":
            jump NoFiveAndEight

#YesFiveAndEight

    label YesFiveAndEight:
        show mc casual defaultEmotion with dissolve
        persistent.mc "I would have to completely disagree with you, as that’s not how money works."
        persistent.mc "Yes, you will be consistently saving $700 in your account, and don't get me wrong, $700 is alot already alot if you're just starting out."
        persistent.mc "{b}HOWEVER{/b}, it will take you a really long time to save enough money for yourself." with vpunch
        show mc casual smiling with dissolve
        persistent.mc "So I please you not to settle with this process."
        persistent.mc "I'm not saying that you should overwork yourself, but my point is that building enough foundation to fully grasp the ins and out of how money works..."
        show mc casual defaultEmotion with dissolve
        persistent.mc "Is better than working multiple jobs at the same time for long term."
        jump EndQuestions

#NoFiveAndEight

    label NoFiveAndEight:
        show mc casual smiling with dissolve
        persistent.mc "{b}Indeed!{/b} This method of saving is not advisable." with vpunch
        persistent.mc "Also, I recommend that you check into some more other options that will {b}ALLOW{/b} you to make your money work for you,, rather than the other way around."
        jump EndQuestions

#Seven

    label Seven:
        show mc casual defaultEmotion with dissolve
        persistent.mc "Right!"
        persistent.mc "Only $700 will be left. Do you think it will be enough for you to get rich?"

    menu:
        "Yes.":
            jump YesRich

        "No.":
            jump NoRich

#YesRich

    label YesRich:
        show mc casual defaultEmotion with dissolve
        persistent.mc "Hmmm, I would have to disagree with you here, buddy. That’s because that's not how money works."
        persistent.mc "You will be consistently saving $700 in your account."
        persistent.mc "And it will take you a long time to save enough money for yourself."
        show mc casual smiling with dissolve
        persistent.mc "So I please you not to settle with this process."
        jump EndQuestions

#NoRich

    label NoRich:
        show mc casual smiling with dissolve
        persistent.mc "{b}Indeed!{/b} This method of saving is not advisable." with vpunch
        persistent.mc "Also, I recommend that you check into some more other options that will {b}ALLOW{/b} you to make your money work for you,, rather than the other way around."
        jump EndQuestions

#TakeTime

    label TakeTime:
        show mc casual smiling with dissolve
        persistent.mc "Wise decision, bud."
        persistent.mc "I've always known you to be the type of person who will invest time in learning anything that can benefit your financial status!"
        show mc casual defaultEmotion with dissolve
        persistent.mc "With that said, I have another question for you."
        show mc casual smiling with dissolve
        persistent.mc "Do you know why we should bother developing your financial intelligence?"

    menu:
        "Yes.":
            jump YesDeveloping

        "Not really.":
            jump NoDeveloping

#YesDeveloping

    label YesDeveloping:
        show mc casual smiling with dissolve
        persistent.mc "That’s good to hear!" with vpunch
        show mc casual defaultEmotion with dissolve
        persistent.mc "Money as well as debt management, in particular, will definitely assist you in achieving your financial goals."
        show mc casual smiling with dissolve
        persistent.mc "Not only that, it will also reduce your expenses with the help of your improved regulation."
        persistent.mc "And this is the result of having enough financial literacy."
        jump EndQuestions

#NoDeveloping

    label NoDeveloping:
        show mc casual defaultEmotion with dissolve
        persistent.mc "It's fine if you hadn't considered it."
        persistent.mc "As for me, however, I understand why I should continue to study and continuously test the waters."
        show mc casual smiling with dissolve
        persistent.mc "I do it because I am aware that things will change."
        show mc casual defaultEmotion with dissolve
        persistent.mc "I wish to keep improving my financial knowledge because, some folks will be on their knees begging for their jobs at each market shift."
        persistent.mc "We all get {i}life{/i} lemons from time to time, I wouldn't deny that. Sure we can be resilient, however other people will transform those lemons that life throws at them into opportunities..."
        persistent.mc "And possibly turn it into millions, who knows? Anything could happen anyways."
        persistent.mc "That my friend, is business intelligence."
        jump EndQuestions

#EndQuestions

    label EndQuestions:
        show mc casual smiling with dissolve
        persistent.mc "{b}Oh, wait!{/b}" with vpunch
        persistent.mc "I forgot to mention that after speaking with you."
        persistent.mc "These two types of investors come to mind."
        persistent.mc "Can you decide which one is best for you?"
        
    menu:
        "1. An investor who purchases packaged investments. They make a purchase from a retail shop such as a real estate firm, a stockbroker, or a financial planner.":
            jump click1


        "2. An investor who makes investments. These are the types who knows how to apply opportunities together.":
            jump click2

    label click1:
        show mc casual smiling with dissolve
        persistent.mc "Ah, I see. As I previously stated, that is a clean and straightforward method of investing, so I suppose it can never go wrong if you are this type of investor."
        show mc casual defaultEmotion with dissolve
        persistent.mc "To further understand the concept, let's use the example of buying a computer off the shelf in a computer store" 
        persistent.mc "That alone could be a waste of money, mainly because you're paying for the things you CLEARLY do not want or need. You didn't have freedom to choose the parts yourself."
        persistent.mc "Thus, whatever's in it, then... you'd have no choice but to deal with it."
        show mc casual smiling with dissolve
        persistent.mc "However, if you buy the parts separately, you have the freedom to choose the parts you want."
        persistent.mc "This alone can definitely save you money, because you can set your own pricing range."
        jump investor

    label click2:
        show mc casual smiling with dissolve
        persistent.mc "Ah... the more professional investor is the second sort of investor."
        persistent.mc "Where we should learn how to put the parts together, since that is where the big successes happen." 
        persistent.mc "This is an investment that I strongly advise you to make." 
        persistent.mc "Because you will learn a variety of money-making tactics here."        
        jump investor

    label investor:
        persistent.mc "{i}Are you sure about what kind of investor you are? Can you pick the investor you want to be.{/i}"


    menu:
        "Investor 1":
            $ analytics.event("Chapter 5: Type of Investor", "1, Buy Packaged Investments")
            jump investor1

        "Investor 2":
            $ analytics.event("Chapter 5: Type of Investor", "2, Make Investments")
            jump investor2

    label investor1:
        show mc casual smiling with dissolve
        persistent.mc "Okay, I guess you preferred to buy a pre-packaged investment."
        show mc casual defaultEmotion with dissolve
        persistent.mc "Although this will certainly save you time, I do not advocate this investment." 
        persistent.mc "But don't worry, you can learn something from this even if it doesn't work for you."
        show mc casual smiling with dissolve 
        persistent.mc "It's never too late to learn more about investing and making the best selections." 
        jump LastPart

    label investor2:
        show mc casual smiling with dissolve
        persistent.mc "That’s great! I never doubted your choices."
        show mc casual defaultEmotion with dissolve
        persistent.mc "Since you’ve chosen this investment I want you to develop three main skills." 
        show mc casual smiling with dissolve
        persistent.mc "First, you should find an opportunity that everyone else {b}missed{/b}." 
        persistent.mc "Second, raise money." 
        persistent.mc "And lastly... hire and organize smart people to help you."        
        jump LastPart

    label LastPart:
        show mc casual smiling with dissolve
        persistent.mc "One last word from me, if you know what you're doing, then it's never considered as gambling."
        persistent.mc "If you're merely throwing money at a deal and hoping for the best, then that itself is gambling."
        show mc casual defaultEmotion with dissolve
        persistent.mc "The aim is to use your technical knowledge, judgment, and passion for the \'game\' to reduce the odds and lessen the danger in every situation."
        persistent.mc "Of course, there is always the possibility of danger."
        persistent.mc "However, financial intelligence enhances your chances of getting past over those hurdles."
        show mc casual smiling with dissolve
        persistent.mc "And as a result, what is risky for one individual may be less risky for another."
        persistent.mc "That is why I always advise people to put more money into their financial education rather than stocks, real estate, or other markets."
        persistent.mc "The more intelligent you are, the higher your chances of beating the odds are."
        show mc casual defaultEmotion with dissolve
        persistent.mc "Every day of your life, the world presents you with once-in-a-lifetime possibilities, but we all too often miss them."
        show mc casual smiling with dissolve
        persistent.mc "They are, nonetheless, present. For me, the more the world and technology develop, the more options will be for you and your family to be financially secure for future generations."
    


    $ analytics.event("Chapter 5", "FINISHED")
    $ persistent.ch05 = True
    return