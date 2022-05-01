# The script of the game goes in this file.
#FOR CUSTOM MAIN MENU -- WATCH: https://youtu.be/q5svrv2KN8g
define oldMC = Character("Old MC", color = "#FF0044")
define myst_alternateMC = Character("???", color = "#1DDCB3")
define alternateMC = Character("Alternate MC", color = "#1DDCB3")
define kidMC = Character("Kid MC")

image mcOnDeathBed_Aw = im.Scale("intro/MC_deathbed_awake.jpg", 1920, 1080)
image mcOnDeathBed_Aw2 = im.Scale("intro/MC_deathbed_awake_2.jpg", 1920, 1080)
image mcAcceptsDeath = im.Scale("intro/MC_deathbed_acceptance.jpg", 1920, 1080)

image plainWhite = im.Scale("transitions/whitescreen.jpg", 1920, 1080)
image plainBlack = im.Scale("transitions/blackscreen.jpg", 1920, 1080)

label start:
    #ROLL -- WHAT THE STORY IS ALL ABOUT
    scene plainWhite
    "INSERT ABSTRACT THROUGH NARRATION"
    with fade

    #ROLL -- MC ON DEATHBED REMINISCING HIS PAST
    play music "audio/introduction/farewell.mp3"
    scene mcOnDeathBed_Aw
    oldMC "*Reminiscing the old days*"
    oldMC "Ugh, what a waste.."

    #ROLL -- CONT. OF REMINISCING PAST -- SHOW IMAGES
    scene mcOnDeathBed_Aw2
    with fade
    play sound "audio/introduction/footsteps.ogg"
    queue sound "audio/introduction/door.4.ogg"

    "*Nurse leaving"
    oldMC "..."

    scene mcOnDeathBed_Aw
    with fade

    play sound "audio/introduction/maleGrunt.mp3"
    "*grunts"
    oldMC "INSERT MORE DIALOGUE"

    $ transitionCount = 1
    while(transitionCount < 3):
        show expression("intro/flashbacks/[transitionCount].png")
        with dissolve
        "Click to continue"
        $ transitionCount += 1
    "Click to continue"
    with dissolve

    #ROLL PRESENT MC ACCEPTING DEATH WITH REGRETS
    scene mcOnDeathBed_Aw
    with fade

    oldMC "Damn it.. I want to be able to give my family their needs and wants.."
    oldMC "Ah, I wish I could turn back time.."

    scene mcAcceptsDeath
    with fade
    oldMC "INSERT MORE DIALOGUE"
    play sound "audio/introduction/heartRateToFlatline.mp3" fadeout 1.0
    oldMC "I'd definitely make their lives easier.."
    #play sound "audio/introduction/heartRateToFlatline.mp3" fadeout 1.0

    scene plainBlack
    with fade
    "..."

    stop sound fadeout 1.0
    stop music fadeout 1.0

    #ROLL -- WHITE TRANSITION TO KID MC TALKING WITH ALTERNATE MC
    play music "audio/introduction/decision.mp3"
    scene plainWhite
    with fade

    show kidMC confused
    with dissolve
    kidMC "Huh.. w-what?"
    kidMC "Where am I?"
    myst_alternateMC "Hey, over here kiddo!"
    kidMC "Wait.. who? who's there? Where am I?"

    show alternateMC welcoming
    with dissolve
    alternateMC "Hey there! Unfortunately this is not heaven, but an empty space where we could talk about anything. And yes, you died - in case you're not aware."

    hide alternateMC
    show kidMC confused
    with dissolve
    kidMC "What empty space? Why am I in a kid's body? And more importantly, who are you?"

    hide kidMC
    show alternateMC welcoming
    with dissolve
    alternateMC "Apparently, that's actually '{i}you{/i}' as a kid back then."



    hide kidMC
    show alternateMC welcoming
    with dissolve
    alternateMC """
    And as for who I am, I am actually {i}you{/i} as well, {b}BUT{/b} from a different timeline.
    
    I am what you would call the successful version of you. I am the persona you've imagined and wanted to be before your last breath.
    """

    hide alternateMC
    show kidMC astonished
    with dissolve
    kidMC "Woah, lucky you. I wish I could be like you when I was still alive."

    hide kidMC
    show alternateMC laughing
    with dissolve
    #PLAY SOUND CHUCKLE
    alternateMC "I wouldn't really call myself lucky. This was merely the result of weighing out the options presented to me by my two fathers and then deciding for myself - unafraid of testing the waters, being different and many more!"
    
    alternateMC "This was all possible with the teachings and lessons given to me by my 'other' father."

    hide alternateMC
    show kidMC astonished
    with dissolve
    kidMC "Huh? Other father? Like your foster father or something?"

    hide kidMC
    show alternateMC
    with dissolve
    alternateMC "Not really, he was actually my best friend's father. I just referred him as my second father as he took us under his wing and guided us to our success."

    alternateMC """
    With that said I had two fathers - a rich one and a poor one. One finished his education, had a Ph.D., and went to multiple universities to do his advanced studies.

    The other father never finished his Junior High School.
    """
    alternateMC """
    {b}BUT!{/b} They were both successful in their careers, both earned substantial incomes yet one always struggled financially.

    One father became one of the richest men in the Philippines. He died leaving tens of millions of peso to his family, and charities.

    And the other one... left bills to be paid.
    """
    alternateMC """
    Do not get me wrong, both of them were strong, charismatic and influential. They both offered me advice, but they did not advise the same things.

    Both of my fathers believed strongly in education but did not recommend the same course of study.
    """
    alternateMC """
    If I had only one dad, I would have had to make or break with one's advice.

    But since I've had two dads, that alone offered me the choice of contrasting points of view:

    One of a rich man and one of a poor man.
    """
    hide alternateMC
    show kidMC
    with dissolve
    kidMC "..."

    hide kidMC
    show alternateMC
    with dissolve
    alternateMC """
    Instead of simply accepting or rejecting one idea or the other, I found myself to be... much more logical.

    As I weigh out and compare the options presented to me, I then choose for myself.
    """
    alternateMC """
    {b}However!{/b} The problem was that my 'rich' father was not rich yet, and my 'poor' father was not yet poor.

    Both were just starting out and of course --- both were struggling with money and families. Both had very different points of view about money.
    """

    hide alternateMC
    show kidMC
    with dissolve
    kidMC "Hmm.. how different are they?"

    hide kidMC
    show alternateMC
    with dissolve
    alternateMC "Curious aren't we, little one? Well, let me give you an example..."
    alternateMC """
    One dad would say, '{i}The love of money is {b}not{/b} the root of evil.{/i}'

    While the other would say '{i}The lack of money {b}is{/b} the root of all evil.{/i}'
    """
    alternateMC "Much of my precious time was spent on asking myself '{i}Why does he say that?{/i}'."

    hide alternateMC
    show kidMC
    with dissolve
    kidMC "Wouldn't it be easier for you to just agree on one's point of view and simply reject the latter?"

    hide kidMC
    show alternateMC
    with dissolve
    alternateMC """
    Here, let me ask you something.

    Do you know the reason why the rich get richer, the poor get poorer, and the middle class struggles in debt?
    """
    #1ST INTERACTION MENU
    menu:
        "...":
            call reason0
        "Yes":
            call reason1 #NO CONTINUATION YET

    alternateMC "You see, schools would rather focus teaching their students scholastic and professional skills rather than financial skills."
    alternateMC "Now, remember when I told you about deciding for yourself is important?"

    #3RD INTERACTION MENU
    menu:
        "Yes":
            alternateMC "Good, I hope you remember it well as you'll be using it everytime!"
            pass
        "No..":
            call doNotRemember

    alternateMC """
    Okay so, one dad had a habit of putting his brain to sleep when it came to finances, and other had a habit of exercising his brain.

    Now which do you think would grow stronger financially?
    """

    #4TH INTERACTION MENU
    menu:
        "The one who {b}thinks{/b} constantly?":
            call thinkConstantly
        "The one who {b}shuts{/b} his brain off ":
            call shutsBrain

    alternateMC """
    Anyways, here are some more examples on how different they think. 
    
    One of them encouraged talking about money and business at the dinner table, while the other forbade the subject of money to be discussed over a meal.
    """
    
    alternateMC """
    One said '{i}When it comes to money, play it {b}SAFE{/b}. Don't take risks{/i}.'. 
    
    While the other said, '{i}Learn to {b}MANAGE{/b} your financial risks effectively{/i}.'.
    """
    alternateMC """
    One believed '{i}Our home {b}IS{/b} our largest investment and our greatest asset{/i}.'. 
    
    Meanwhile, the other believed '{i}Our house {b}IS NOT{/b} an asset, but a liability. If your house is your largest investment, you're in trouble{/i}.'.
    """
    alternateMC """
    One dad taught me how to write an impressive resumé so I could {b}FIND and LAND{/b} a good job. 
    
    The other taught me how to write strong business and financial plans so I could {b}CREATE{/b} jobs.
    """

    alternateMC "See the difference between their mindset?"

    hide alternateMC
    show kidMC
    with dissolve
    kidMC "Yeah, but wouldn't you be morally confused as to who should you follow?"

    hide kidMC
    show alternateMC laughing
    with dissolve
    #PLAY SOUND CHUCKLE
    alternateMC "Well I did at first.. but how I balanced two contrasting points? That's for you to find out!"

    hide alternateMC
    show kidMC confused
    with dissolve
    kidMC "Why are you telling me all this anyway? Why am I even here? I'm pretty sure I died peacefully."

    hide kidMC
    show alternateMC
    with dissolve
    alternateMC "Remember being regretful about your financial decisions when you were alive?"

    #5TH INTERACTION MENU
    menu: 
        "Yes":
            pass
        "Not really..":
            call regretfulMemoriesFlashBack
    
    alternateMC """
    As to why I'm telling you this, basically, you would be alive again. But this time, you'll be able to be a better person and a father as well.
    
    You'll be experiencing my life. Now, it is up to you how you would walk this path. 
    """
    
    hide alternateMC
    show alternateMC laughing
    with dissolve
    #PLAY SOUND CHUCKLE
    alternateMC "Remember this very well: Money is one form of power. But what is more powerful is financial education."
    alternateMC "Money comes and goes, but if you have the education about how money works, you gain power over it and can begin building wealth."
    alternateMC "All these experiences and lessons you'll be acquiring aren't meant as answers, {b}but{/b} guideposts that will assist you and your children to grow wealthier no matter what happens in a world of increasing change and uncertainty."
    alternateMC "Lastly, good luck out there mini-me! Enjoy the second chance!"
    
    hide alternateMC
    show kidMC
    with dissolve
    kidMC "Wai-!"

    #PLAY SOUND WHOOSH
    scene plainBlack
    with fade
    "..."
    return


#=============================================================================================================#

#1ST USER INTERACTION MENU
label reason0:
    alternateMC """
    No? Well, because the subject of money is taught {b}AT{/b} home, not in school.

    Most of us learn about money from our parents. So what can poor parents tell their child about money?
    """

    menu:
        "I guess '{i}Stay in school and study hard?{/i}'":
            call studyHard
        "Hmm..":
            call tellThemToStudy

    return

label reason1: #ANDIE WILL PROVIDE ANSWER AS SHE HAS PRIOR KNOWLEDGE WHEN IT COMES TO FINANCE
    alternateMC "And the reason is?"
    menu:
        "CHOICE 1":
            pass
        "CHOICE 2":
            pass

    return

#2ND USER INTERACTION MENU FROM 1ST INTERACTION MENU
label studyHard:
    alternateMC "Right! But then the child may graduate with excellent grades, but with a poor person's financial programming and mindset as money management is not taught in schools."

    return

label tellThemToStudy:
    alternateMC "Of course, to study hard and do their best - then tell them to look for a company to work for!"

    return

#3RD USER INTERACTION MENU
label doNotRemember:
    alternateMC """
    Since I had two influential fathers, it's only natural that I learn from both of them.

    I had to think about each dad's advice, and in doing so, I gained valuable insight into the power and effect of one's thoughts on one's life.
    """

    hide alternateMC
    show kidMC
    with dissolve
    kidMC "Ah, so basically one lets you off the hook, and the other forces you to think?"

    hide kidMC
    show alternateMC
    with dissolve
    alternateMC "Right!"

    return

#4TH USER INTERACTION MENU
label thinkConstantly:
    alternateMC "Right! This analogy is not much different from a person who goes to the gym to exercise on a regular basis versus someone who basically sits on the couch and binge-watch any entertaining series."
    
    return

label shutsBrain:
    #PLAY SOUND CHUCKLE
    alternateMC """
    Huh.. are you being sarcastic right now? Did you hit your head or something?
    
    Well, regardless, the obvious answer is those who {b}CONSTANTLY{/b} thinks. This is not much different from a person who goes to the gym to train on a regular basis.
    """

    return

#5TH USER INTERACTION MENU
label regretfulMemoriesFlashBack:
    alternateMC "Don't hate me on this, mini-me!"
    $ transitionCount = 1
    while(transitionCount < 3):
        show expression("intro/flashbacks/[transitionCount].png")
        with dissolve
        "Click to continue"
        $ transitionCount += 1
    "Click to continue"
    with dissolve

    scene plainWhite
    with fade

    show kidMC confused
    with dissolve
    kidMC "..."

    show alternateMC
    with dissolve
    return