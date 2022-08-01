label startPostGameSurvey:
    $ quick_menu = False

    scene kidMCSchool with fade
    show mc student smiling with dissolve
    persistent.mc "Now that you've finished all the chapters..."
    show mc student defaultEmotion with dissolve
    persistent.mc "I guess this is the perfect time to test your understanding in regards to what I've shared to you."
    show mc student smiling with dissolve
    persistent.mc "Do not worry, as this is relatively easy!"
    persistent.mc "However, be careful with your answers as you won't be able to roll back to change your answers!"

    show mc student smiling at left with moveinleft
    persistent.mc "Let's start, shall we?"
    show mc student defaultEmotion with dissolve
    persistent.mc "Here comes the first question..."
    
    ####################
    # Question 1
    ####################
    persistent.mc "Workers see their home as their biggest asset, yet in the story, it is actually seen as a liability. Why do you think so?"
    menu:
        "A. I beg to disagree. Properties {b}COULD{/b} also be an asset.":
            show mc student smiling with dissolve
            persistent.mc "You’re not wrong, yet you’re not right either."
            show mc student defaultEmotion with dissolve
            persistent.mc "Unfortunately, your primary residence is not really an asset. That's because you are living there and will be unable to realize any appreciation gains."
            persistent.mc "It only wouldn’t be a liability {b}IF{/b} and {b}only IF{/b}:"
            show mc student smiling with dissolve
            persistent.mc "1. It’s already paid off completely." 
            persistent.mc "And 2. If it was used or {b}transformed{/b} into a rental property that brings in money."
        
        "B. Because the home was “eating” them alive, in a sense where it cost them money every month.":
            $ persistent.totalSurveyScore += 1

            show mc student smiling with dissolve
            play sound "audio/sfx/correctAnswerPing.mp3"
            show 8bitCorrect at truecenter with dissolve
            persistent.mc "{b}Right!{/b}" with vpunch
            hide 8bitCorrect with dissolve
            show mc student defaultEmotion with dissolve
            show ancillaryExpenses at truecenter with dissolve
            persistent.mc "As you can see on the diagram above, every month, homeowners would have to pay for different fees such as..."
            persistent.mc "{i}Paying for your mortgage{/i}, {i}maintenance fees{/i}, {i}property taxes{/i}, as well as {i}utility expenses{/i}."
            hide ancillaryExpenses with dissolve
            persistent.mc "If you only have one source of income, a portion of it would directly go to your property’s management expenses."
    
    ####################
    # Question 2
    ####################
    show mc student smiling with dissolve
    persistent.mc "Okay, moving on, here comes the second question."
    show mc student defaultEmotion with dissolve
    persistent.mc "Why is that Mike’s dad stressed the importance of knowing the difference between assets and liabilities?"
    menu:
        "A. Because this can punctuate the future development of an individual’s personal finances.":
            $ persistent.totalSurveyScore += 1

            show mc student smiling with dissolve
            play sound "audio/sfx/correctAnswerPing.mp3"
            show 8bitCorrect at truecenter with dissolve
            persistent.mc "{b}Right!{/b}" with vpunch
            persistent.mc "Knowing the difference between an asset and liability is {b}INDEED{/b} the building foundation on achieving your personal financial freedom."
            hide 8bitCorrect with dissolve

        "B. No prior reason. Benedict (Mike’s dad) just decided it on a whim.":
            show mc defaultEmotion with dissolve
            play sound "audio/sfx/wrongAnswerPing.mp3"
            show 8bitWrong at truecenter with dissolve
            show mc student smiling with dissolve
            persistent.mc "{b}Oopsie{/b}, I’m afraid you’re wrong about that mate! The reason why rich dad stressed the importance of this topic is…" with vpunch
            persistent.mc "Because it would help you determine which things you should spend on such as {b}securities{/b}, {b}investments{/b}, {b}stocks{/b}, {b}commitments{/b}, and {b}obligations{/b}."
            persistent.mc "This concept is important as knowing it advises you to have as little debt load as possible because, in the end, having tons of liabilities {b}HINDERS{/b} the financial freedom you want to achieve."
            hide 8bitWrong with dissolve

    ####################
    # Question 3
    ####################
    show mc student smiling with dissolve
    persistent.mc "Okay, moving on, here comes the third question."
    show mc student defaultEmotion with dissolve
    persistent.mc "On the third lesson taught by my rich dad, what does he mean by “{i}Mind your own business{/i}”?"
    menu:
        "A. Build and keep your asset column.":
            $ persistent.totalSurveyScore += 1

            show mc student smiling with dissolve
            play sound "audio/sfx/correctAnswerPing.mp3"
            show 8bitCorrect at truecenter with dissolve
            persistent.mc "{b}Smart!{/b}" with vpunch
            persistent.mc "Once a dollar goes into it, never let it come out!"
            show mc student defaultEmotion with dissolve
            persistent.mc "Basically, look at your money as your employee. The best thing about money is that it works 24 hours a day and can work for generations."
            hide 8bitCorrect with dissolve

        "B. Do not take what others say into value.":
            show mc student defaultEmotion with dissolve
            play sound "audio/sfx/wrongAnswerPing.mp3"
            show 8bitWrong at truecenter with dissolve
            show mc student smiling with dissolve
            persistent.mc "{b}Nope!{/b} What Benedict meant by the said phrase was to keep building your asset column." with vpunch
            persistent.mc "But, nice try though! Keep trying!"
            hide 8bitWrong with dissolve

    ####################
    # Question 4
    ####################
    show mc student smiling with dissolve
    persistent.mc "Okay, moving on, here comes our second to the last question."
    show mc student defaultEmotion with dissolve
    persistent.mc "Choose which describes the phenomena rich dad calls “{i}The Rat Race{/i}”."
    menu:
        "A. It is the phenomenon in which an individual chases every opportunity without weighing and knowing it first.":
            show mc student defaultEmotion with dissolve
            play sound "audio/sfx/wrongAnswerPing.mp3"
            show 8bitWrong at truecenter with dissolve
            show mc student smiling with dissolve
            persistent.mc "{b}Nope!{/b} That’s just being reckless." with vpunch
            persistent.mc "Rat race, according to my rich dad, is actually the recurring pattern of getting up, going to work, and paying the bills…"
            persistent.mc "Which is a {b}VERY{/b} {i}exhausting{/i} and {i}rigorous{/i} routine for individuals who are trying to achieve financial freedom."
            persistent.mc "Not only is it limited to that, but a rat race could also refer to the life of individuals who work very hard in order to compete with others for money, status, and etc."
            hide 8bitWrong with dissolve

        "B. The recurring pattern of getting up, going to work, then paying the bills.":
            $ persistent.totalSurveyScore += 1

            show mc student smiling with dissolve
            play sound "audio/sfx/correctAnswerPing.mp3"
            show 8bitCorrect at truecenter with dissolve
            persistent.mc "{b}Right!{/b}" with vpunch
            persistent.mc "The Rat Race referred to by Mike's dad means a pointless pursuit."
            persistent.mc "Offer them more money and they continue the cycle by increasing the amount of money they spend."
            show mc student defaultEmotion with dissolve
            persistent.mc "Basically, once they get a few bucks in their hands, their emotions of joy, desire, and greed takes over. Those individuals stuck in this phenomena react first, instead of thinking."
            hide 8bitCorrect with dissolve

    ####################
    # Question 5
    ####################
    show mc student smiling with dissolve
    persistent.mc "And now, for our last question..."
    show mc student defaultEmotion with dissolve
    persistent.mc "Why was it that our rich dad made us work on his superette with little to no pay?"
    menu:
        "A. To help see the different opportunities that other people miss or can’t see.":
            $ persistent.totalSurveyScore += 1

            show mc student smiling with dissolve
            play sound "audio/sfx/correctAnswerPing.mp3"
            show 8bitCorrect at truecenter with dissolve
            persistent.mc "{b}Right!{/b}" with vpunch
            persistent.mc "Not only for that, but it was also to be aware of the rat race as early as possible."
            persistent.mc "It was also to help them remember that simply working hard isn’t the only way to achieve financial freedom."
            show mc student defaultEmotion with dissolve
            persistent.mc "It's sole purpose was to prevent the kids’ emotions from deciding things in regards to finance management."
            hide 8bitCorrect with dissolve

        "B. He saw you guys as an easy target and manipulated you to work for free.":
            show mc student defaultEmotion with dissolve
            play sound "audio/sfx/wrongAnswerPing.mp3"
            show 8bitWrong at truecenter with dissolve
            show mc student smiling with dissolve
            persistent.mc "Well, that may seem to be the case from other people’s point of view, however Benedict has no intention of doing that." with vpunch
            persistent.mc "He made his course like that so that we would be able to see the possible opportunities of making money that other people could and would not seize."
            hide 8bitWrong with dissolve

    #############################################
    # End of Questions & Score Computation
    #############################################
    $ persistent.scoreEvaluation = ["Very good", "Good", "Not Bad", "I think you should visit some of the chapters."]
    $ scorePercentage = 0.0

    $ persistent.totalSurveyScore += 0.0
    $ scorePercentage = (persistent.totalSurveyScore/5)*100

    show mc student smiling at center with move
    persistent.mc "Hmm, you got {b}{u}[persistent.totalSurveyScore]{/u}{/b} out of 5 questions..."

    if (scorePercentage > 0):
        #5/5
        if(scorePercentage >= 81 and scorePercentage <= 100):
            persistent.mc "{b}[persistent.scoreEvaluation[0]]{/b}, I'm impressed."
            persistent.mc "I'm sure you'll do well on your journey in achieving financial independency and freedom. I just know it!"
        #4/5
        if(scorePercentage >= 61 and scorePercentage <= 80):
            persistent.mc "{b}[persistent.scoreEvaluation[1]]{/b}, you did well buddy."
            persistent.mc "I'm sure you've discovered alot of things, I wish you luck on your journey!"
        #3/5
        if(scorePercentage >= 41 and scorePercentage <= 60):
            persistent.mc "{b}[persistent.scoreEvaluation[2]]{/b}, some minor re-learning here and there would do."
            persistent.mc "I hope you've learned a lot during your stay here!"
        #2/5 and 1/5
        if ((scorePercentage >= 21 and scorePercentage <= 40) or (scorePercentage >= 1 and scorePercentage <= 20)):
            persistent.mc "Honestly, {b}[persistent.scoreEvaluation[3]]{/b}."
            persistent.mc "I know you can do it! Don't lose confidence!"
        
        show mc student surprised with dissolve
        persistent.mc "{b}OH!{/b} Before I forget..." with vpunch
        show mc smiling with dissolve
        persistent.mc "Thank you for your time, user! Our connection might be short, but you can always come back to learn a thing or two from me."
        persistent.mc "Goodluck out there, buddy!"

        $ analytics.event("Post-Game Questionnaire", str(scorePercentage)+"%")
    
    else:
        persistent.mc "Hmm, I'm afraid you might have to retake the test."
        menu:
            "Retake the test.":
                persistent.mc "Alright then! Say no more, buddy. I gotcha!"
                jump startPostGameSurvey
            "Pass":
                persistent.mc "Sure, no problem!"
                persistent.mc "Thank you for your time, user! Our connection might be short, but you can always come back to learn a thing or two from me."
                persistent.mc "Goodluck out there, buddy!"
    
    scene plainBlack with fade
    window hide
    pause 1.5
    window auto
    
return