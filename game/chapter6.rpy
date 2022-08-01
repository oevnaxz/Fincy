label startChapter6:
     $save_name = "Chapter 06: Work to Learn, Don't work for Money"
#Going to garage
     scene plainWhite with fade
     "A few months later..."
     "After buying an auto and continuously using it for years, something went wrong with it as I've always anticipated."
     "Well, something's wrong with its engine or whatsoever, I really do not know the details myself so..."
     "With that, I've decided to go to an Auto Workshop and have it checked up on."

     scene autoWorkshop with fade
     show mc defaultEmotion with dissolve
     persistent.mc "Hi uhh, do you work here?"

     show mc unfocused at left with move
     show mechanic clean smiling at right with moveinright
     mechanic "{b}AH!{/b} Yes sir!" with vpunch
     mechanic "I am one of the car mechanics here. Why do you ask?"
    
     show mechanic clean unfocused at right
     show mc smiling at left 
     with dissolve
     persistent.mc "Oh great! Actually while I was driving earlier, and I noticed something wrong in my car, but I don't know what exactly the problem is..."
     persistent.mc "Would you be so kind to check it?"

     show mc unfocused at left
     show mechanic clean defaultEmotion at right 
     with dissolve
     mechanic "Sure thing! Let me just check some things to determine the problem real quick."

     show mechanic clean unfocused at right
     show mc smiling at left 
     with dissolve
     persistent.mc "Ah yes, please do so. Thank you very much!"
     
     play sound "audio/sfx/turnOnCarEngine.mp3" volume 0.5

     show mc unfocused at left
     show mechanic clean smiling at right 
     with dissolve
     mechanic "Ha-ha there it is! Now I see what's the problem."

     show mechanic clean unfocused at right
     show mc surprised at left 
     with dissolve
     persistent.mc "{b}Really?!{/b} That fast?!" with vpunch
     persistent.mc "Can you fix it?"

     show mc unfocused at left
     show mechanic clean smiling at right 
     with dissolve
     mechanic "Yup, I can fix it {b}very quick{/b}."
     
     hide mc
     hide mechanic
     with dissolve

     scene plainBlack with fade
     play sound "audio/sfx/setDownTools.mp3" volume 0.5
     queue sound "audio/sfx/rummageTools.mp3" volume 0.5
     pause 5.0

     scene autoWorkshop with fade
     show mechanic dirty defaultEmotion with dissolve
     mechanic "Welp, there you go!"
     mechanic "Your car's all fixed and she's ready to go!"

     show mechanic dirty unfocused at right with move
     show mc surprised at left with moveinleft
     mc "Wow! You really fixed my car in just few minutes. Thanks!"

     scene plainWhite with fade
     "I am constantly shocked at how little talented people earn. I have met brilliant, highly educated people who earn less than $20,000 a year."
     "A business consultant who specializes in the medical trade was telling me how many doctors, dentists, and chiropractors struggle financially." 
     "To be honest with you, all this time I thought that when they graduated, the dollars would pour in their pockets continuously."
     "The same business consultant gave me the phrase: “{i}They are one skill away from great wealth.{/i}”" 
     "I'm pretty sure what this phrase means is that most people earn and master one more skill and their income would jump exponentially."
     "Financial intelligence is a synergy of {b}accounting, investing, marketing,{/b} and {b}law{/b}. Combine these four technical skills and making money with money is easier than most people would believe."

     #Flashing the Title Screen
     window hide
     show screen title_screen(_("{b}LESSON 06: WORK TO LEARN, DON'T WORK FOR MONEY{/b}"))
     with dissolve
     pause 2
     hide screen title_screen
     with dissolve
     window auto

     #narration
     scene kidMCSchool with fade
     "In school and in the workplace, the popular opinion is the idea of specialization: that is, in order to make more money or get promoted, you need to {b}SPECIALIZE{/b} on something."
     "That is why for example, medical doctors immediately begin to seek a specialty such as orthopedics or pediatrics."
     "The same is also true for accountants, architects, lawyers, pilots, and other professions."
     "I remember my \"educated\" dad believes in the same idea of what the school and workplace thought us."
     "He always told me that..."

     scene kidMCLivingRoom with fade
     #Flashback 1
     show biologicalDad defaultEmotion with dissolve
     biologicalDad "{i}\"{b}Son{/b}... one road to being successful is that you need to be well-educated and have a specialization in your work to make more money and of course... to get promoted.\"{/i}"

     scene plainWhite with fade
     show mc defaultEmotion with dissolve
     persistent.mc "...while my \"rich\" dad, having a different point of view kept reminding me... "

     scene richDadLivingRoom with fade     
     show richDad smiling with dissolve
     richDad "{i}\"Well... you would want to know a little about a lot (of things).\"{/i}"
     
     scene plainWhite with fade
     "My rich dad told the exact opposite of what my educated dad beliefs when it comes to work."
     "That is why for years, I worked in different areas of my rich dad's companies and establishments when I was a kid."
     "For a while, I worked under his accounting department. Although I would probably never have been an accountant, he wanted me to learn things from him by experience."

     "That is why he also insisted that we sit-in on the meetings with his bankers, lawyers, accountants, as well as brokers." 
     "He basically wanted us to know a little about every aspect of his soon-to-be empire."
     
     scene officeCountryside with fade
     "In 19XX, I graduated from college. A local journalism outlet had hired me right after graudating from college here in the countryside."
     "I had a great career ahead of me, yet I resigned after some years with the company. I went to my hometown to discuss this with them."
     "And of course, my \"educated\" dad was devastated for my early resignation. However, Benedict whom I call my \"rich\" dad congratulated me."
     
     scene kidMCLivingRoom with fade
     show biologicalDad defaultEmotion with dissolve
     biologicalDad "Son, did you really quit?"
     
     show biologicalDad unfocused at right with move
     show mc casual defaultEmotion at left with moveinleft
     persistent.mc "..."
     show mc casual smiling with dissolve
     persistent.mc "Yeah, dad."
     
     show mc casual unfocused at left
     show biologicalDad defaultEmotion at right 
     with dissolve
     biologicalDad "But why? Isn't it too early?"
     
     show biologicalDad unfocused at right
     show mc casual defaultEmotion at left 
     with dissolve
     persistent.mc "Hmm... I spent six months on that company and I learned a lot from that job, but now I want to expand my wings and try you know... something new."
     
     show mc casual unfocused at left
     show biologicalDad defaultEmotion at right 
     with dissolve
     biologicalDad "But isn't too early for you to quit on the company?"
     biologicalDad "Why dont you spend a little more time working there, maybe you'll get promotion in the next few months."
     biologicalDad "After that your salary will increase, who knows what might happen? In my opinion, that would be the better route to take, son."   
     
     show biologicalDad unfocused at right
     show mc casual smiling at left 
     with dissolve
     persistent.mc "Dad... it's not about the promotion or the salary."
     persistent.mc "Just like I told you, I already had learned a lot from their company and now I want to experience new things on this field."
     
     show mc casual unfocused at left
     show biologicalDad defaultEmotion at right
     with dissolve
     biologicalDad "Hmm..."

     #narration
     hide biologicalDad
     hide mc
     with dissolve

     "My educated dad could not understand my decision to resign from a career that offered decent pay, great benefits, lots of time off, and opportunity for promotion."
     "Job security meant everything to my educated dad. Having a stable job meant everything to my rich dad."
     "And with that, I went to the city and worked on a publishing company situated on the city."

     #flash white screen
     scene plainWhite with fade
     "During the time I was in the second company, I've learnt alot and to be honest with you..."
     "I've actually remained to work there for four years as I was able to learn and experience new things."
     "And as you expected, I resigned again after that four years. And again... my dad could not understand my decisions."

     scene kidMCLivingRoom with fade
     show biologicalDad confused with dissolve
     biologicalDad "Son, why did you resign again?"
     show biologicalDad sad with dissolve
     biologicalDad "I'm afraid I don't quite understand what you're planning or aiming to do."

     show biologicalDad unfocused at right with move
     show mc casual smiling at left with moveinleft
     persistent.mc "Hmm... well, I believe I've already learned everything from that company, and now there are even new things I still want to learn."

     show mc casual unfocused at left
     show biologicalDad defaultEmotion at right 
     with dissolve
     biologicalDad "Hmm, what are you going to do now?"

     show biologicalDad unfocused at right
     show mc casual defaultEmotion at left 
     with dissolve
     persistent.mc "I found a job in Xerox Corp and yeah, I was hired already."

     show mc casual unfocused at left
     show biologicalDad surprised at right 
     with dissolve
     biologicalDad "Xerox Corp? That's a big company..."
     show biologicalDad confused with dissolve
     biologicalDad "You {b}REALLY{/b} want to work at Xerox Corp right after your sudden resignations from two companies?"
     biologicalDad "{b}PLUS!{/b} It's totally unrelated the specialization course you took in college!" with vpunch

     show biologicalDad unfocused at right
     show mc casual smiling at left with dissolve
     persistent.mc "Yeah, and actually dad, I'll be starting to work there next week."

     show mc casual unfocused at left
     show biologicalDad smiling at right 
     with dissolve
     biologicalDad "Well, it seems like you've already made up your mind. That's great then, do what you want, but always take care, alright?"

     hide biologicalDad
     hide mc
     with dissolve

     scene plainWhite with fade
     "I joined in Xerox Corp for one reason, and it was not for the benefits."
     "I was a shy person, and the thought of selling was the most frightening subject in the world for me." 
     "Also, Xerox has one of the best sales-training programs in the country."
     "For the first month, I trained in the company while learning the skills I need to have for my work."
     "The training includes how to sell and the proper way of communicating and dealing with different clients."
     "Well, the training didn't last long, and within a month of continuous training, I am now starting to work under them."

     scene xeroxNeighborhood with fade
     show mc student smiling with dissolve
     persistent.mc "{i}Whew... being here in front of someone's door makes me feel nervous.{/i}"

     label choices1:
          show mc student confused at left with move
          persistent.mc "{i}Hmm... should I ring their doorbell to sell them my product?{/i}"
     menu:
          "Yes.":
               jump ch6Yes1
          "No.":
               jump ch6No1

     #MENU1 YES1
     label ch6Yes1:
          show mc student defaultEmotion with dissolve
          persistent.mc "{i}Alright, I definitely have to if I want to be able to sell these.{/i}"
          persistent.mc "{i}Whew! You can do this, {b}[persistent.mc]{/b}!{/i}"
          
          jump press

     #MENU1 NO1
     label ch6No1:
          show mc student confused with dissolve
          persistent.mc "{i}But, if i don't do this i won't be able to sell our product.{/i}"
          show mc student defaultEmotion with dissolve
          persistent.mc "{i}It would be better if I do this now...{/i}"
          
          jump press

     #press the doorbell
     label press:
          show mc student defaultEmotion with dissolve
          play sound "audio/sfx/doorbellChime.mp3" volume 0.5
          pause 2.0
          play sound "audio/sfx/openDoor.mp3" volume 0.5

          show mc student unfocused at left with dissolve
          show teacher defaultEmotion at right with moveinright
          neighbor "Hmm?"
          neighbor "Oh! Hello, how may I uhh... help ya?"

          show teacher unfocused
          show mc student smiling at left 
          with dissolve
          persistent.mc "Hi there!"

          show teacher unfocused at right
          show mc student smiling at left 
          with dissolve
          persistent.mc "Uhmm... I uhh... I'm actually selling some---"

          show mc student unfocused at left
          show teacher defaultEmotion at right 
          with dissolve
          neighbor "Sorry, but I'm really busy right now, and I don't have time to listen or know what you're selling."

          hide teacher 
          hide mc
          with dissolve

          "I was rejected before I could even finish my sentence."
          "Even though I was nervous, I still kept on knocking every single door of house I ran into and try to sell the product."
          
          scene plainWhite with fade
          "I kept doing this for a year."
          "Working in Xerox Corp I know that I am making a progress for myself. I can say that because I noticed that I was slowly getting comfortable into talking to people."
          "Thus, I continued to working in the company to further improve my skill in selling."

          "And of course, after a few years of continuous door-to-door selling."
          "I have now overcame my fear of being rejected. I'm consistently on the top five of the company's overall top sales."
          "With that, I again resigned and moved on, leaving behind a great career on an excellent company."
          
          "Since Mike and I were both groomed by Benedict, we're able to learn the importance of managing cashflow, the assets, investing, and how to work and handle a company." 
          "So now, I think it's time I form one and put all my experiences together."
          
          show mc smiling with dissolve
          "In 19XX, I formed my first company. My product is the Nylon-and-Velcro wallet, it was manufactured in the Far East and shipped to a warehouse in Manila, near where I had completed my formal education."
          "And of course, managing a business is really hard. There were a lot of hurdles." 
          "However, I persevered through them with the help of my close one's advices, especially rich dad's."
          "After few years, my business became sucessfull and now I still do business internationally."
          "And as my rich dad encouraged me to do, I kept seeking the emerging nations."
          
          hide mc with dissolve

          "After my business and investments become sucessful, the money automatically poured in and now I've become one of richest individuals in the country."
          "And today, I was invited to be interviewed by a newspaper writer in Singapore. I'll be speaking on \"{b}The Secrets of the Rich\"{/b}."

     scene interviewOffice with fade
     "The young female reporter and writer was on time, and the interview got under way immediately."
     "While in the interview the female writer suddenly mentioned that she wanted to be a best-selling author."

     show writer smiling at center with dissolve
     writer "Good day, Mr. {b}[persistent.mc]{/b}."
     show writer defaultEmotion with dissolve
     writer "Wow, you know I uhh..." 
     writer "I'd like to be a best-selling author someday."

     show writer unfocused at right with move
     show mc smiling at left with moveinleft
     persistent.mc "You know what... I had seen some of articles you have written and... I was realy impressed."
     persistent.mc "You have a tough and clear style of writing and your articles catches the reader's interest."
     show mc confused with dissolve
     persistent.mc "But, I was wondering what holds you back from achieveing your dream?"

     show mc unfocused at left
     show writer defaultEmotion at right 
     with dissolve
     writer "Hmm, my work does not seem to go anywhere. Everyone says that my novels are excellent, but nothing happens."
     show writer smiling with dissolve
     writer "So... I keep my job with the paper. At least it pays the bills."
     show writer defaultEmotion with dissolve
     writer "Do you have any suggestions for me on how can I become a best-selling author?"

     show writer unfocused at right
     show mc smiling at left 
     with dissolve
     persistent.mc "I'm glad you asked! Honestly, I {b}DO{/b} have a suggestion for you."
     persistent.mc "I have a friend here in Singapore who runs a school that trains people to {i}sell{/i}."
     persistent.mc "He runs sales-training courses for many of the top corporations here in Singapore."
     persistent.mc "I think attending one of his courses would greatly enhance your career."

     show mc unfocused at left
     show writer confused at right 
     with dissolve
     writer "Are you saying that I should go to school to learn how to... sell?"

     show writer unfocused at right
     show mc surprised at left 
     with dissolve
     persistent.mc "Yes!"

     show mc unfocused at left
     show writer confused at right 
     with dissolve
     writer "Huh...? I have a master’s degree in English Literature."
     writer "Why would I go to school to learn to be a salesperson?"
     show writer defaultEmotion with dissolve
     writer "I am a professional. I went to school to be trained in a profession..."
     writer "... and I hate salespeople, no offense. All they want is money. So tell me why I {b}SHOULD{/b} go out of my way and study sales?"

     show writer unfocused at right
     show mc defaultEmotion at left 
     with dissolve
     persistent.mc "Well, you said you wanted to be a best-selling author, right?"

     show mc unfocused at left
     show writer defaultEmotion at right 
     with dissolve
     writer "Yes, I'm aware I did."

     show writer unfocused at right
     show mc smiling at left 
     with dissolve
     persistent.mc "Look... Just like you said it's \"best-{b}selling{/b} author\", not \"best-{b}writing{/b} author\"."

     show mc unfocused at left
     show writer confused at right 
     with dissolve
     writer "What are you talking about? I'm afraid I was not able to catch up."

     show writer unfocused at right
     show mc defaultEmotion at left 
     with dissolve
     persistent.mc "Well... you are already a great writer but your lack of knowledge on selling is preventing you to become a best-selling author."

     show mc unfocused at left
     show writer confused at right 
     with dissolve
     writer "So you're {b}IMPLYING{/b} that I should learn how to sell?"

     show writer unfocused at right
     show mc smiling at left 
     with dissolve
     persistent.mc "Basically, yes."

     show mc unfocused at left
     show writer defaultEmotion at right 
     with dissolve
     writer "You know that I dont like being a salesperson. And I'll never go as far as learning how to sell and become one of them."
     writer "People like them have no business in writing. Plus, I am a professionally trained writer not a salesman. Why would I even study sales?"

     show writer unfocused at right
     show mc smiling at left 
     with dissolve
     persistent.mc "I understand your feelings right now, I wouldn't invalidate that."
     show mc defaultEmotion with dissolve
     persistent.mc "But, if you really want to be a best-selling author maybe you should consider and think about the things that I suggested for you to do."

     hide writer with dissolve

     label ch6Choices2:
          show mc defaultEmotion at center with move
          persistent.mc "{i}Why do you think I keep suggesting her to study sales?{/i}"
     menu:
          "Hmm... maybe you just wanted to piss her off?":
               jump ch6Choice1
          "Because if she studied sales, then she would be able to market her novels to the right audience?":
               jump ch6Choice2
          
     #MENU2 CHOICE1
     label ch6Choice1:
          show mc smiling with dissolve
          play sound "audio/sfx/chuckle.mp3" volume 0.5
          persistent.mc "Hahaha you're funny one. However, that was not my intention..."
          persistent.mc "... and I clearly have no reason to do that."

          show mc defaultEmotion with dissolve
          persistent.mc "Okay, listen as I will tell you the reason."

          jump reason

     label ch6Choice2:
          show mc smiling with dissolve
          persistent.mc "You're right about that."
          persistent.mc "Since she is already a great writer, learning sales would possibly make her the best-selling author as well as best-writing author."

          jump reason

     #reason
     label reason:
          show mc defaultEmotion with dissolve
          persistent.mc "If she diligently learned the skills of sales and marketing, her income would jump dramatically." 
          persistent.mc "If I were her, I would take some courses in {b}advertising{/b}, {b}copywriting{/b} as well as {b}sales{/b}."
          show mc smiling with dissolve
          persistent.mc "Then, instead of working at the newspaper, she could seek a job at an advertising agency to learn how to communicate in short-cuts that are used in successful advertising."
          persistent.mc "She also would spend time learning public relations, an important skill. She would learn how to get millions in free publicity."

     hide mc with dissolve

     scene plainWhite with fade
     "The female writer cooled down after a few seconds and the interview was continued."

     scene interviewOffice with fade

     show writer defaultEmotion at left with moveinleft
     writer "Does anyone have questions for Mr. {b}[persistent.mc]{/b}?"

     show writer unfocused with dissolve
     show jake defaultEmotion at right with moveinright
     jake "Me, I have a question."

     show jake unfocused
     show writer smiling 
     with dissolve
     writer "What is your name, sir?"

     show writer unfocused
     show jake smiling 
     with dissolve
     jake "Ah! It's Jake, ma'am."
     
     show jake unfocused
     show writer smiling 
     with dissolve
     writer "Okay, Jake. Well, what is your question?"

     hide writer with dissolve
     show mc unfocused at left with moveinleft
     show jake smiling at right with dissolve
     jake "I'll be straight to the point, what do you think I should do to earn more?"
     show jake defaultEmotion with dissolve
     jake "I'm completely at loss on what to do and what not to do."

     show jake unfocused at right
     show mc surprised at left 
     with dissolve
     persistent.mc "Hmm..."
     show mc smiling with dissolve
     persistent.mc "Well, Jake. What is your current job?"

     show mc unfocused
     show jake defaultEmotion at right 
     with dissolve
     jake "I am currently a professional tattoo artist and the salary was just fine. But... I want to earn more."

     show jake unfocused at right
     show mc defaultEmotion at left 
     with dissolve
     persistent.mc "You said that your salary is fine, then why do you want to earn more?"

     show mc unfocused at left
     show jake defaultEmotion at right 
     with dissolve
     jake "You know, there are things I want to buy... but I can't right now because my salary is just enough to pay for my bills."

     show jake unfocused at right
     show mc smiling at left 
     with dissolve
     persistent.mc "If that was the case, then why don't you quit and look for another job that will pay you higher?"

     show mc unfocused at left
     show jake defaultEmotion at right 
     with dissolve
     jake "I can't really do that, I couldn't afford to lose my only source of income, because I have bills to pay. That's why I keep my work."
     show jake smiling with dissolve
     jake "Also, this is really the job I've fallen in love with."
     
     show jake unfocused at right
     show mc defaultEmotion at left 
     with dissolve
     persistent.mc "Let me share you this management theory."
     show mc smiling with dissolve
     persistent.mc "\"Workers work hard enough to not be fired, and owners pay just enough so that workers won’t quit.\""
     persistent.mc "Do you know what that means?"

     show mc unfocused
     show jake defaultEmotion at right 
     with dissolve
     jake "No, not really..."

     show jake unfocused at right
     show mc defaultEmotion at left 
     with dissolve
     persistent.mc "Okay. Well, workers do what they think is right, and that is to get a secure job." 
     persistent.mc "And most workers focus on working for wage and benefits that rewards them in the short term, but are often disastrous in the long run."

     show mc unfocused
     show jake defaultEmotion at right 
     with dissolve
     jake "..."

     show jake unfocused at right
     show mc defaultEmotion at left 
     with dissolve
     persistent.mc "Listen Jake. Instead of simply working for the money or job security, which I admit is also very important."
     persistent.mc "It is better for you take a second job that will teach you a second skill that is not related to your current work."

     show mc unfocused
     show jake defaultEmotion at right 
     with dissolve
     jake "Ohh! I think that is to much hassle for me!"

     show jake unfocused at right
     show mc confused at left 
     with dissolve
     persistent.mc "So you would rather work all your life giving fifty percent of what you earn to the government?"

     show mc unfocused
     show jake defaultEmotion at right 
     with dissolve
     jake "But, I only do what I am interested in."
     
     show jake unfocused at right
     show mc defaultEmotion at left 
     with dissolve
     persistent.mc "It seems like you haven't understood what I'm trying to tell you." 
     persistent.mc "Okay, I'll tell you an example of what I am implying."
     persistent.mc "I am not interested in going to the gym, but I go because I want to feel better and live longer..."
     persistent.mc "... life is much like going to the gym. The most painful part is deciding to go. Once you get past that, it’s easy."
     persistent.mc "There have been many days I have dreaded going to the gym, but once I am there and in motion, it is a pleasure. After the workout is over, I am always glad I talked myself into going."

     show mc unfocused
     show jake defaultEmotion at right 
     with dissolve
     jake "..."

     show jake unfocused at right
     show mc defaultEmotion at left 
     with dissolve
     persistent.mc "Now, do you get my point, Jake?"

     show mc unfocused
     show jake defaultEmotion at right 
     with dissolve
     jake "Yeah, but is it bad if i only want to specialize in one profession?"

     show jake unfocused at right
     show mc smiling at left 
     with dissolve
     persistent.mc "Being technically specialized has its strengths as well as its weaknesses."
     show mc defaultEmotion with dissolve
     persistent.mc "Imagine if you were a professional athlete who suddenly got injured or are too old to play, your once high-paying position is gone, and now you have only limited skills to fall back on."
     persistent.mc "If you really want to earn more. I suggest that you find a second job that will teach you a second skill so that you can have another option and to not to rely too much on your specialized work."
     persistent.mc "I hope you learned something from me."

     show mc unfocused
     show jake smiling at right 
     with dissolve
     jake "..."
     jake "Come to think of it, thinking about your explanation you made me realize that learning other skills is important." 
     jake "Thank you for making me understand that. I really appreciate it."

     show jake unfocused at right
     show mc smiling at left 
     with dissolve
     persistent.mc "You're welcome! Glad I was able to help ya!"

     hide mc 
     hide jake
     with dissolve

     scene plainWhite with fade
     "Soon after answering all Jake's question, the interview was over."
     "After a long day I can now finally take some rest at home."

     scene mcBedroomNight with fade
     show mc casual smiling with dissolve
     persistent.mc "Whew! Finally I can take a rest now."
     show mc casual surprised with dissolve
     persistent.mc "Looking back, when I was still living my old life, I was just curious on how to get rich. However, I didn't expect that I will be this rich."
     show mc casual smiling with dissolve
     persistent.mc "I am really glad that I was able to meet my second dad. His teachings helped me on every financial decisons I made in my life."
     persistent.mc "Now one part of me is a hard-core capitalist who loves the game of money making money."
     persistent.mc "The other part is a socially responsible teacher who is deeply concerned with this everwidening gap between the haves and have-nots."
     persistent.mc "At the end of the day I'm always thankful that I had met my alternate self and was able to live a life I dreamt of."
     
     play sound "audio/sfx/turnSwitchOff.mp3" volume 0.5

     scene mcBedroomNoLights with fade
     play sound "audio/sfx/layInBed.mp3" volume 0.5
     pause 2.0
     
     scene plainWhite with fade
     window hide
     show screen title_screen(_("{b}The End.{/b}"))
     with dissolve
     pause 2
     hide screen title_screen
     with dissolve
     window auto

     $ analytics.event("Chapter 6", "FINISHED")
     $ persistent.ch06 = True
     return