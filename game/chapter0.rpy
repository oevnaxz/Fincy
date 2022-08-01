default kidMC = "Robert"
default mc = "Robert"
label startChapter0:
    $ save_name = "Introduction: The Beginning"
    #ROLL -- WHAT THE STORY IS ALL ABOUT
    scene plainWhite with fade
    "The story focuses on Robert's journey to become a successful person he always dreamt of." 
    "However, his actions and poor decisions has lead him to a life he hates, thus having lots and lots of regret."
    "Upon losing consciousness in the hospital bed, he was able to meet an alternate version of him, offering him a second chance at life."
    "And thus, Robert's journey to change the outcome of his life begins..."
    
    #ROLL -- MC ON DEATHBED REMINISCING HIS PAST
    scene mcOnDeathBed_Aw with fade
    play music "audio/bgm/farewell.mp3"
    oldMC "..."
    oldMC "Ugh, what a waste.."

    #ROLL -- CONT. OF REMINISCING PAST -- SHOW IMAGES
    scene mcOnDeathBed_Aw2 with fade
    play sound "audio/sfx/nurseFootsteps.ogg"
    queue sound "audio/sfx/door.4.ogg"
    "{i}Nurse leaving the room{/i}."
    oldMC "..."

    scene mcOnDeathBed_Aw with fade
    play sound "audio/sfx/maleGrunt.mp3"
    "*grunts*"
    oldMC "Hmm..."
    oldMC "Looking back, it seems that I've lived my life full of regrets.."

    window hide
    scene mcAcceptsDeath with fade
    pause 2.0
    window auto

    #ROLL PRESENT MC ACCEPTING DEATH WITH REGRETS
    scene mcOnDeathBed_Aw with fade
    oldMC "Damn it... I want to be able to give my family their needs and wants.."
    oldMC "Ah, I wish I could turn back time.."

    scene mcAcceptsDeath with fade
    oldMC "If... if only I studied how to properly manage my net worth and do safe financial decisions..."
    oldMC "I could've saved up more money to buy and invest on assets to leave something to my family..."
    play sound "audio/sfx/heartRateToFlatline.mp3" fadeout 1.0
    oldMC "That would definitely make their lives easier..."

    scene plainBlack with fade
    window hide
    pause 5.0
    window auto

    stop sound fadeout 1.0
    stop music fadeout 1.0

    #ROLL -- WHITE TRANSITION TO KID MC TALKING WITH ALTERNATE MC
    scene plainWhite with fade
    play music "audio/bgm/decision.mp3"
    show kidMC confused with dissolve
    kidMC "Huh.. w-what?"
    kidMC "Where am I?"
    myst_alternateMC "Hey, over here kiddo!"
    kidMC "Wait.. who? who's there?! Where am I?!" with vpunch

    show kidMC unfocused at left with move
    show mc mysterious at right with moveinright
    alternateMC "Hey there! Unfortunately this is not heaven, but an empty space where we could talk about anything."
    alternateMC "And yes, you really did {i}die{/i}, in case you're not aware."

    show mc mysterious at right 
    show kidMC defaultEmotion at left 
    with dissolve
    kidMC "What? Why am I in a kid's body? And more importantly, who are you?"

    show kidMC unfocused at left 
    show mc smiling at right 
    with dissolve
    alternateMC "Apparently, that's actually \"{i}you{/i}\" as a kid back then."
    show mc defaultEmotion with dissolve
    alternateMC """
    And as for who I am, I am actually \"{i}you{/i}\" as well, {b}BUT{/b} from a different timeline.
        
    I am what you would call the successful version of you. I am the persona you've imagined and wanted to be before your last breath.
    """

    show mc unfocused at right 
    show kidMC confused at left 
    with dissolve
    kidMC "Uhhh... lucky you, I guess?"

    show kidMC unfocused at left 
    show mc smiling at right 
    with dissolve
    play sound "audio/sfx/chuckle.mp3"
    alternateMC "I wouldn't really call myself {i}lucky{/i}. This was merely the result of weighing out the options presented to me by my two fathers and then deciding for myself."
    show mc defaultEmotion at right with dissolve
    alternateMC "This was all possible with the teachings and lessons given to me by my \"{i}other{/i}\" father."

    show mc unfocused at right 
    show kidMC confused at left
    with dissolve
    kidMC "Huh? Other father? Like your foster father or something?"

    show kidMC unfocused at left 
    show mc smiling at right 
    with dissolve
    alternateMC "Not really, he was actually my best friend's father. I just referred him as my second father as he took us under his wing and guided us to our success."
    show mc defaultEmotion at right with dissolve
    alternateMC """
    With that said I had two fathers - a rich one and a poor one. One finished his education, had a Ph.D., and went to multiple universities to do his advanced studies.

    The other father never finished his Junior High School.
    """
    show mc smiling at right with dissolve
    alternateMC """
    {b}BUT!{/b} They were both successful in their careers, both earned substantial incomes yet one always struggled financially.
    
    One father became one of the richest men in the Philippines. He died leaving tens of millions of peso to his family, and charities.

    And the other one... well, he left bills to be paid.
    """
    alternateMC """
    Do not get me wrong, both of them were strong, charismatic and influential. They both offered me advice, but they did not advise the same things.

    Both of my fathers believed strongly in education but did not recommend the same course of study.
    """
    show mc defaultEmotion at right with dissolve
    alternateMC """
    If I had only one dad, I would have had to make or break with one's advice.

    But since I've had two dads, that alone offered me the choice of contrasting points of view:

    One of a rich man and one of a poor man.
    """
    show mc unfocused at right 
    show kidMC thinking at left 
    with dissolve
    kidMC "..."

    show kidMC unfocused at left 
    show mc smiling at right 
    with dissolve
    alternateMC """
    Instead of simply accepting or rejecting one idea or the other, I found myself to be... much more logical.

    As I weigh out and compare the options presented to me, I then choose for myself.
    """
    show mc defaultEmotion at right with dissolve
    alternateMC "{b}However!{/b} The problem was that my \"rich\" father was not rich yet, and my \"poor\" father was not yet poor." with vpunch
    alternateMC "Both were just starting out and of course - both were struggling with money and families. Both had very different points of view about money."

    show mc unfocused at right 
    show kidMC defaultEmotion at left 
    with dissolve
    kidMC "Hmm... How different are they?"

    show kidMC unfocused at left 
    show mc smiling at right 
    with dissolve
    alternateMC "Curious aren't we, little one? Well, let me give you an example..."
    show mc defaultEmotion at right with dissolve
    alternateMC """
    One dad would say, \"{i}The love of money is {b}not{/b} the root of evil.{/i}\"

    While the other would say \"{i}The lack of money {b}is{/b} the root of all evil.{/i}\"
    """
    alternateMC "And to be honest with you, much of my precious time was spent on asking myself why does he say that?"

    show mc unfocused at right 
    show kidMC confused at left 
    with dissolve
    kidMC "Wouldn't it be easier for you to just agree on one's point of view and simply reject the latter?"

    show kidMC unfocused at left 
    show mc smiling at right 
    with dissolve
    alternateMC """
    Hmmm well... let me ask you something.

    Do you know the reason why the rich get richer, the poor get poorer, and the middle class struggles in debt?
    """
    #1ST INTERACTION MENU
    show mc unfocused at right 
    show kidMC thinking at left 
    with dissolve
    menu:
        "...":
            call reason0
        "Yes.":
            call reason1 

    alternateMC "Anyways, remember when I told you about deciding for yourself is important?"

    #3RD INTERACTION MENU
    show mc unfocused at right 
    show kidMC thinking at left 
    with dissolve
    menu:
        "Yeah.":
            show kidMC unfocused at left 
            show mc smiling at right 
            with dissolve
            alternateMC "Good, I hope you remember it well as you'll be using it everytime!"
            pass
        "Hmm... sorry, but no.":
            call doNotRemember

    alternateMC """
    Okay so, one dad had a habit of putting his brain to sleep when it came to finances, and other had a habit of exercising his brain.

    Now which do you think would grow stronger financially?
    """

    #4TH INTERACTION MENU
    show mc unfocused at right 
    show kidMC thinking at left 
    with dissolve
    menu:
        "The one who {b}thinks{/b} constantly?":
            call thinkConstantly
        "The one who {b}shuts{/b} his brain off?":
            call shutsBrain

    show mc defaultEmotion at right with dissolve
    alternateMC """
    Anyways, here are some more examples on how different they think. 
        
    One of them encouraged talking about money and business at the dinner table, while the other forbade the subject of money to be discussed over a meal.
    """
        
    alternateMC """
    One said \"{i}When it comes to money, play it {b}SAFE{/b}. Don't take risks{/i}.\" 
        
    While the other said, \"{i}Learn to {b}MANAGE{/b} your financial risks effectively{/i}.\"
    """
    alternateMC """
    One believed \"{i}Our home {b}IS{/b} our largest investment and our greatest asset{/i}.\"
        
    Meanwhile, the other believed \"{i}Our house {b}IS NOT{/b} an asset, but a liability. If your house is your largest investment, you're in trouble{/i}.\"
    """
    alternateMC """
    One dad taught me how to write an impressive resumé so I could {b}FIND and LAND{/b} a good job. 
        
    The other taught me how to write strong business and financial plans so I could {b}CREATE{/b} jobs.
    """
    show mc smiling at right with dissolve
    alternateMC "See the difference between their mindset?"

    show mc unfocused at right 
    show kidMC confused at left 
    with dissolve
    kidMC "Yeah, but wouldn't you be morally confused as to who should you follow?"

    show kidMC unfocused at left 
    show mc smiling at right 
    with dissolve
    play sound "audio/sfx/mouthClosedChuckle.mp3"
    alternateMC "Well I did at first... but how I balanced two contrasting points? That's for you to find out!"

    show mc unfocused at right 
    show kidMC confused at left 
    with dissolve
    kidMC "Why are you telling me all this anyway? Why am I even here? I'm pretty sure I died {i}peacefully{/i}."
    
    show kidMC unfocused at left
    show mc defaultEmotion at right
    with dissolve
    alternateMC """
    As to why I'm telling you this, basically, you would be {i}alive{/i} again. But this time, you'll be able to be a better person and a father as well.
        
    You'll be experiencing {i}my{/i} life. Now, it is up to you how you would walk this path.

    Anyways, would you like to change your name? This may be irrelevant, but since you'll be alive once again, I thought you might want to change your name.
    """
    
    show mc unfocused at right 
    show kidMC thinking at left 
    with dissolve
    menu:
        "I would like to change my name.":
            call changeName
        "No. I'd like to retain my original name, thanks.":
            $ persistent.kidMC = "Robert"
            $ persistent.mc = "Robert"
            pass

    show kidMC unfocused
    show mc smiling
    with dissolve
    play sound "audio/sfx/chuckle.mp3"
    alternateMC "Alright, remember this very well, {b}[persistent.kidMC]{/b}: \"{i}Money is one form of power. But what is more powerful is financial education{/i}.\""
    show mc defaultEmotion at right with dissolve
    alternateMC "Money comes and goes, but if you have the education about how money works, you gain power over it and can begin building wealth."
    alternateMC "All these experiences and lessons you'll be acquiring aren't meant as answers..." 
    alternateMC "{b}BUT{/b} guideposts that will assist you and your children to grow wealthier no matter what happens in a world of increasing change and uncertainty."
    show mc smiling at right with dissolve
    alternateMC "Lastly, good luck out there mini-me! Enjoy the second chance!"
        
    show mc unfocused at right 
    show kidMC surprised at left 
    with dissolve
    persistent.kidMC "{b}Wai-!{/b}" with vpunch
    stop music fadeout 0.5

$ analytics.event("Introduction", "FINISHED")
$ persistent.ch00 = True
return
