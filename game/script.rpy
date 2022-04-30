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

    show kidMC confused
    with dissolve
    kidMC "Huh.. w-what?"
    kidMC "Where am I?"
    myst_alternateMC "Hey, over here kiddo!"
    kidMC "Wait.. who? who's there? Where am I?"

    show alternateMC welcoming
    with dissolve
    alternateMC "INSERT MORE DIALOGUE"

    hide alternateMC
    show kidMC confused
    with dissolve
    kidMC "INSERT MORE DIALOGUE"

    hide kidMC
    show alternateMC welcoming
    with dissolve
    alternateMC "INSERT MORE DIALOGUE"
    alternateMC """
    I had two fathers, a rich one and a poor one. One finished his education, had a Ph.D., and went to multiple universities to do his advanced studies.

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
    alternateMC "Much of my precious time was spent on asking myself 'Why does he say that?'."

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

    alternateMC "See? Schools would rather focus teaching their students scholastic and professional skills rather than financial skills."
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
            pass
        "The one who {b}shuts{/b} his brain off ":
            pass

    "end"
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

label reason1:
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
    alternateMC "Of course, to study hard and do their best -- look for a company to work for!"

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
