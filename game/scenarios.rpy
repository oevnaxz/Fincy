#Chapter 0
#1ST USER INTERACTION MENU
label reason0:
    $ analytics.event("Introduction: Reason(Rich, Poor, Middle Class)", "0")

    show kidMC unfocused at left 
    show mc smiling at right 
    with dissolve
    alternateMC "No? Well, one main reason is because the subject of money is taught {b}AT{/b} home, not in school."
    alternateMC "Most of us learn about money from our parents. So what can poor parents tell their child about money?"

    show mc unfocused at right 
    show kidMC thinking at left 
    with dissolve
    menu:
        "I guess \"{i}Stay in school and study hard?{/i}\"":
            call studyHard
        "Hmm...":
            call tellThemToStudy

    show mc defaultEmotion with dissolve
    alternateMC "You see, schools would rather focus teaching their students scholastic and professional skills rather than financial skills."

return

label reason1:
    $ analytics.event("Introduction: Reason(Rich, Poor, Middle Class)", "1")

    show kidMC unfocused at left 
    show mc defaultEmotion at right 
    with dissolve
    alternateMC "And the reason is?"

    show mc unfocused at right 
    show kidMC thinking at left 
    with dissolve
    menu:
        "Hmm, the poor becomes poorer because they are in low-paying jobs in order to survive.":
            pass
        "Those who are rich puts more of their assets in high risk investments.":
            pass
        "Since people could not differentiate assets from liabilities?":
            pass

    show kidMC unfocused at left 
    show mc surprised at right 
    with dissolve
    alternateMC "Huh... if you knew it all along, then why didn't you-"
    show mc defaultEmotion at right with dissolve
    alternateMC "No, nevermind."

return

#2ND USER INTERACTION MENU FROM 1ST INTERACTION MENU
label studyHard:
    show kidMC unfocused at left 
    show mc smiling at right 
    with dissolve
    alternateMC "Right! But then the child may graduate with excellent grades, but with a poor person's financial programming and mindset as money management is not taught in schools."

return

label tellThemToStudy:
    show kidMC unfocused at left 
    show mc smiling at right 
    with dissolve
    alternateMC "Of course, to study hard and do their best - then tell them to look for a company to work for!"

return

#3RD USER INTERACTION MENU
label doNotRemember:
    show kidMC unfocused at left 
    show mc defaultEmotion at right 
    with dissolve
    alternateMC "Since I had two influential fathers, it's only natural that I learn from both of them."
    alternateMC "I had to think about each dad's advice, and in doing so, I gained valuable insight into the power and effect of one's thoughts on one's life."

    show mc unfocused at right 
    show kidMC defaultEmotion at left 
    with dissolve
    kidMC "Ah, so basically one lets you off the hook, and the other forces you to think?"

    show kidMC unfocused at left 
    show mc smiling at right 
    with dissolve
    alternateMC "Right!"

return

#4TH USER INTERACTION MENU
label thinkConstantly:
    show kidMC unfocused at left 
    show mc smiling at right 
    with dissolve
    alternateMC "Right! This analogy is not much different from a person who goes to the gym to exercise on a regular basis versus someone who basically sits on the couch and binge-watch any entertaining series."
        
return

label shutsBrain:
    show kidMC unfocused at left 
    show mc smiling at right 
    with dissolve
    play sound "audio/sfx/mouthClosedChuckle.mp3"
    alternateMC "Huh.. are you being sarcastic right now? Did you hit your head or something?"
    alternateMC"Well, regardless, the obvious answer is those who {b}CONSTANTLY{/b} thinks. This is not much different from a person who goes to the gym to train on a regular basis."

return

label changeName:
    show kidMC unfocused
    show mc smiling
    with dissolve
    alternateMC "What would you like to be called anyway? I mean on your upcoming new life?"
    show mc unfocused at right 
    show kidMC thinking at left 
    with dissolve
    python:
        persistent.kidMC = renpy.input("{b}Enter your desired name:{/b}", default="Robert")
        persistent.kidMC = persistent.kidMC.strip()
        persistent.mc = persistent.kidMC

        if persistent.kidMC == "":
            persistent.kidMC = "Robert"
            persistent.mc = "Robert"

    show kidMC unfocused with dissolve
return

#====================================================================================================================================================================================#

#Chapter 1
label dadPeeksOperation:
    #FLASH ANIMATION boilingPot
    play sound "audio/sfx/burning.mp3"
    show kidMC unfocused
    show biologicalDad thinking 
    with dissolve
    biologicalDad "..."
    stop sound fadeout 0.5
    #FLASH ANIMATION pourIntoPlasterMold
    #play sound liquidDropping
    show biologicalDad defaultEmotion at right with dissolve
    biologicalDad "Hmm..."
    
return

label explainOperation:
    show kidMC smiling at left with dissolve
    persistent.kidMC "{i}Hmm, I really don't want to explain something that's not my idea...{/i}"
    persistent.kidMC "Mike, explain it to dad! This was your idea in the first place. This was all you."
    hide kidMC with moveoutleft
    show mike smiling at left with moveinleft
    mike "Right. So, these toothpaste tubes are made from {i}lead{/i} instead of the usual which is {i}plastic{/i}."
    mike "And there's this science book I've read.. basically we'll be melting these toothpaste tubes."
    #FLASH ANIMATION boilingPot
    play sound "audio/sfx/burning.mp3"
    mike "After they've turned into a liquid state, we'll be pouring it on our plaster molds."
    #FLASH ANIMATION pourIntoPlasterMold
    play sound "audio/sfx/liquidDropping.mp3"
    queue sound "audio/sfx/liquidDropping2.mp3"
    mike "And that's basically it!"
    hide mike with dissolve

return

label dadExplains:
    show kidMC unfocused at left 
    show biologicalDad flustered at right 
    with dissolve
    play sound "audio/sfx/oldManCoughing.mp3"
    biologicalDad "Ehem.. Because I chose to be a school teacher. School teachers really don't think about being rich. We just like to teach."
    show biologicalDad defaultEmotion at right with dissolve
    biologicalDad "I wish I could help you boys, but honestly, I really don't know how to make money and grow it out."

return

label opportunitiesComeAndGo:
    show kidMC unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad "If you can’t make up your mind decisively, then you’ll never learn to make money anyway."
    richDad "Opportunities {b}come{/b} and {b}go{/b}, {b}[persistent.kidMC]{/b}. Being able to know when to make quick decisions is an important skill.You have the opportunity that you asked for."
    show richDad smiling at right with dissolve
    richDad "School is beginning, or it's over in 10 seconds."
    play sound "audio/sfx/clockTicking.mp3"
    
    show richDad unfocused at right 
    show kidMC serious at left 
    with dissolve
    menu:
        "Take it.":
            stop sound fadeout 0.5
            pass

    hide richDad with moveoutright
    show kidMC unfocused at left with dissolve
    
return

label treatedBetter:
    show kidMC unfocused at left
    show richDad smiling at right 
    with dissolve
    play sound "audio/sfx/mouthClosedChuckle.mp3"
    richDad "Not bad... in less than a month, you sound like most of my employees."

    show richDad unfocused at right 
    show kidMC confused at left 
    with dissolve
    persistent.kidMC "What?"
    persistent.kidMC "I thought you were going to keep your end of the bargain and teach me. Instead you want to torture me? What a letdown."

return

label agreeOnTeachingTalking:
    show kidMC unfocused at left 
    show richDad smiling at right 
    with dissolve
    richDad "That's how they teach you in school. That's not how life teaches you, {b}[persistent.kidMC]{/b}."
    richDad "Most of the time, life does not talk to you. It just sort of pushes you around."
    show richDad defaultEmotion at right with dissolve
    richDad "Think of each {i}push{/i} of life saying: {i}\"Wake up, there's something I want you to learn.\"{/i}"

    show richDad unfocused at right 
    show kidMC confused at left 
    with dissolve
    persistent.kidMC "Huh? I'm pretty sure I asked you to teach us how to make money, I did not wish to learn values and philosophy in life!"

    show kidMC unfocused at left 
    show richDad smiling at right 
    with dissolve
    play sound "audio/sfx/chuckle.mp3"
    richDad "Haha, this cheeky bra-"
    show richDad defaultEmotion at right with dissolve
    play sound "audio/sfx/oldManCoughing.mp3"
    richDad "Ehem. Atleast let me finish talking first."

return

label noAnswerTeachingTalking:
    show kidMC unfocused at left 
    show richDad slyGrin at right 
    with dissolve
    richDad "How I teach is different from the method you boys are familiar with."
    richDad "I prefer to teach things indirectly, I at least want you boys to experience it firsthand."
    show richDad smiling at right with dissolve
    richDad "In that way, I believe you'll be able to remember the lessons I'll be teaching you as long as you have that fire within you to earn and make money."

return

label whatsTheLesson:
    show kidMC unfocused at left 
    show richDad smiling at right 
    with dissolve
    richDad "Of course I'm not telling it to you blatantly."
    richDad "Let me give you a hint, change your point of view. Know which one is the problem."

    show richDad unfocused at right 
    show kidMC confused at left 
    with dissolve
    persistent.kidMC "I don't really understand."

    show kidMC unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad "Let's put it this way. If you think I’m the problem here, then you have to change me. If you realize that you’re the problem, then you can change yourself, learn something, and grow wiser."
    richDad "Don't push the blame on anyone for your problems."

    show richDad unfocused at right with dissolve
    show kidMC defaultEmotion at left with dissolve
    persistent.kidMC "So, what should I do? Do I just take this measly 10 cents an hour and move on?"

return

label cheapAndExploit:
    show kidMC unfocused at left 
    show richDad smiling at right 
    with dissolve
    richDad "Well, how am I cheap?"

    show richDad unfocused at right 
    show kidMC serious at left 
    with dissolve
    persistent.kidMC "I keep telling you. You only pay me 10 cents in which I think I do not clearly deserve!"

    show kidMC unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad "So, you think I {b}AM{/b} the problem?"
    
    show richDad unfocused at right 
    show kidMC serious at left 
    with dissolve
    persistent.kidMC "Yes, you are!"

    show kidMC unfocused at left 
    show richDad smiling at right 
    with dissolve
    richDad "Well, keep that attitude and you’ll learn nothing. Keep the attitude that I’m the problem and what choices do you have?"

    show richDad unfocused at right 
    show kidMC serious at left 
    with dissolve
    persistent.kidMC "Well, if you don’t pay me more or show me more respect and teach me, I’ll quit."

    show kidMC unfocused at left 
    show richDad smiling at right 
    with dissolve
    richDad "Well put, and that's exactly what most people do."
    richDad "They quit and go look for another job, a better opportunity, and higher pay - actually thinking that this will solve the problem."

    show richDad unfocused at right 
    show kidMC thinking at left 
    with dissolve
    persistent.kidMC "So, what should I do? Do I just take this measly 10 cents an hour and move on?"

return

label moneyWontSolveProblem:
    show kidMC unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad "Well, just look at your dad. He makes a lot of money by working as a teacher, and yet he still can’t pay his bills."
    richDad "Basically, most people who are given more money, only gets into more debt."

    show richDad unfocused at right 
    show kidMC thinking at left 
    with dissolve
    persistent.kidMC "Huh, hence why the 10 cent per hour rate..."

    show kidMC unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad "Right, let's use your dad as an example. He graduated with good grades, was able to land on a high-paying job, but how come he still encounter money problems?"

    show richDad unfocused at right 
    show kidMC thinking at left 
    with dissolve
    persistent.kidMC "Huh.. I suddenly feel lucky to be coached by someone who knows their way about managing finance."

    show kidMC unfocused at left 
    show richDad smiling at right 
    with dissolve
    play sound "audio/sfx/mouthClosedChuckle.mp3"
    richDad "Haha, I'm glad you understand what I'm trying to tell you."

return

label reasonFor10Cents:
    show kidMC unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad "Right, you see, your dad went to school and got an excellent education so he could get a high-paying job. But, the thing is that he still has money problems."
    richDad "Because he never learned anything about money in school. And on top of that, he believes in working {b}FOR{/b} money."

    show richDad unfocused at right 
    show kidMC defaultEmotion at left 
    with dissolve
    persistent.kidMC "And you don't?"

    show kidMC unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad "No, not really."
    richDad "If you want to learn to work for money, then stay in school. That is a great place to learn to do that. But if you want to learn how to have money work for you, then I will teach you that."

    show richDad unfocused at right 
    show kidMC defaultEmotion at left 
    with dissolve
    persistent.kidMC "Huh.. wouldn't everyone want to learn that?"

    show kidMC unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad "No, simply because it's easier to learn to work for money, especially if fear is your primary emotion when the subject of money is discussed."
    richDad "Just know that it's fear that keeps most people working at a job: "
    richDad """
    {i}The fear of not paying their bills{/i}. 
    
    {i}The fear of being fired{/i}.
    
    {i}The fear of not having enough money{/i}.
    
    {i}And lastly, the fear of starting over{/i}.
    """

    show richDad unfocused at right 
    show kidMC thinking at left 
    with dissolve
    persistent.kidMC "..."

    show kidMC unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad "That’s the price of studying to learn a profession or trade, and then working for money."
    show richDad smiling at right with dissolve
    richDad "Most people become a slave to money - and then get angry at their boss."

return

label happyBeingPoor:
    show kidMC unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad "No, I don't think so."
    show richDad surprised with dissolve
    richDad "The avoidance of money is just as psychotic as being attached to money."
    
    hide richDad
    hide kidMC 
    with dissolve
    
    play sound "audio/sfx/rummageTrashcan.mp3"
    "As if on cue, a town derelict went past our table, stopping by the large rubbish can and rummaging around in it."
    "The three of us watched him with great interest, when before we probably would have just ignored him."

    show kidMC defaultEmotion at left with moveinleft
    show mike defaultEmotion at right with moveinright
    "..."
    hide mike with dissolve
    show kidMC unfocused at left with dissolve
    show richDad defaultEmotion at right with moveinright
    richDad "Watch."

    hide richDad 
    hide kidMC 
    with dissolve
    
    play sound "audio/sfx/getMoneyFromWallet.mp3"
    "Mike's dad pulled a dollar out of his wallet and gestured to the older man."
    "Seeing the money, the derelict came over immediately, took the bill, thanked Mike's dad profusely and hurried off, ecstatic with his good fortune."

    show richDad defaultEmotion with dissolve
    richDad "He’s not much different from most of my employees. I've met so many people who say \"{i}Oh, I'm not so interested in money{/i}.\", yet they'll work at a job for eight hours a day."
    richDad "If they weren’t interested in money, then why are they working? That kind of thinking is probably more psychotic than a person who hoards money."

    show richDad unfocused at right with move
    show kidMC thinking at left with moveinleft
    persistent.kidMC "Huh.. come to think of it, I've heard my father say that he's not interested in money, and whenever I bring up the topic regarding money, he's been covering himself by saying \"{i}I work because I love my job.{/i}\""
    
return

label notWorkForMoney:
    show kidMC unfocused at left 
    show richDad defaultEmotion at right 
    with dissolve
    richDad "No, that would be a waste of time. Emotions are what make us human."
    show richDad surprised with dissolve
    richDad "Be truthful about your emotions and use your mind and emotions in your favor, not against yourself."
    hide kidMC with dissolve

    show richDad unfocused at right 
    show mike surprised at left 
    with dissolve
    mike "Oh.."
    hide mike with dissolve
    
return

label askMrsMartin:
    show kidMC unfocused at left 
    show mrsMartin defaultEmotion at right 
    with dissolve
    mrsMartin "Oh, this?"
    show mrsMartin smiling at right with dissolve
    play sound "audio/sfx/womanLaughing.mp3"
    mrsMartin "I throw them away. I give the top half of the cover back to the comic book distributor for credit when he brings in the new batch of comics."
    mrsMartin "Mr. Comic distributor is coming in an hour by the way, come say hi if you want!"

    show mrsMartin unfocused at right 
    show kidMC surprised at left 
    with dissolve
    persistent.kidMC "..."
    show kidMC defaultEmotion at left with dissolve
    persistent.kidMC "Ohh, I see I see. Thanks, Mrs. Martin!"

    scene superette with fade
    "I talked to Mike about it and we've decided waited for an hour. And not long after did the comic distributor arrived."
    scene superetteCounter with fade
return

label doNotAsk:
    scene superette with fade
    "For some reason, I couldn't really leave the superette, not until I see what Mrs. Martin would do to those comic books."
    "I just have a feeling that I should stay here and watch what's about to happen."
    "After waiting for an hour or so, a mysterious man showed up at the superette."

return