# The script of the game goes in this file.
#FOR CUSTOM MAIN MENU -- WATCH: https://youtu.be/q5svrv2KN8g
init:
    python:
        import math
        class Shaker(object):
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move, time, child, add_sizes=True, **properties)

        Shake = renpy.curry(_Shake)
    #   
        #GENERATE ID - AUTO INCREMENT
        #CREATE A PERSISTENT VARIABLE FOR TOTAL NUMBER OF PLAYS
        #AND ANOTHER PERSISTENT VARIABLE FOR ID (ID = totalNumberOfPlays + 1)
        #THEN ASSIGN TO A .JSON FILE
#
init:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=10)
    $ renpy.music.register_channel("ambient","sfx",loop=True,tight=True)

$ persistent.ch00 = False
$ persistent.ch01 = False
$ persistent.ch02 = False
$ persistent.ch03 = False
$ persistent.ch04 = False
$ persistent.ch05 = False
$ persistent.ch06 = False
$ persistent.totalSurveyScore = 0
$ persistent.scorePercentage = 0
$ persistent.kidMC = "Robert"
default persistent.mc = "Robert"

label splashscreen:
    scene black
    with Pause(1)

    play sound "audio/sfx/ping.mp3" volume 0.25
    show splash at truecenter with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)
return

label start:
    $ _quit_slot = "quitsave"
    $ persistent.totalSurveyScore = 0

    if persistent.analytics is None:
        menu:
            "Welcome! This game supports analytics. Enabling it will help us on our research requirements, and will send data to Google Analytics and the developers. Do you want to enable analytics?"

            "Yes.":
                $ persistent.analytics = True
                "Thank you."

            "No.":
                $ persistent.analytics = False
                "No problem!"

    call startChapter0
    call startChapter1
    call startChapter2
    call startChapter3
    call startChapter4
    call startChapter5
    call startChapter6
    
    if(persistent.totalSurveyScore == 0):
        call startPostGameSurvey

return

label end:
    #UPLOAD .json FILE TO mongoDB Atlas
    $ renpy.unlink_save("quitsave")
    $ _quit_slot = None
return