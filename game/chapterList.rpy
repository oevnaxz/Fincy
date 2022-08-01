screen chapter_list:
    tag menu 

    # This is the background image.
    add "ui/ch_bg.png" 

    frame:
        style "game_menu_outer_frame"

    # I'd rather not bother making navigation buttons again, so I called the navigation buttons I already had. 
    use game_menu(_("Chapters"), scroll="viewport"):
        style_prefix "chapter_list"

        vbox:
            imagemap:
                ground "ui/ch_ground_3.png"
                idle "ui/ch_idle.png"
                hover "ui/ch_hover.png"
       
                # Because my buttons all have transparency. 
                alpha False

                if persistent.ch00:
                    hotspot (0, 10, 293, 188) action Jump("startChapter0") activate_sound "audio/sfx/click.mp3"
                if persistent.ch01:
                    hotspot (456, 8, 300, 192) action Jump("startChapter1") activate_sound "audio/sfx/click.mp3"
                if persistent.ch02:
                    hotspot (920, 12, 292, 189) action Jump("startChapter2") activate_sound "audio/sfx/click.mp3"
                if persistent.ch03:
                    hotspot (0, 255, 294, 183) action Jump("startChapter3") activate_sound "audio/sfx/click.mp3"
                if persistent.ch04:
                    hotspot (458, 253, 297, 185) action Jump("startChapter4") activate_sound "audio/sfx/click.mp3"
                if persistent.ch05:
                    hotspot (919, 251, 293, 188) action Jump("startChapter5") activate_sound "audio/sfx/click.mp3"
                if persistent.ch06:
                    hotspot (458, 493, 297, 183) action Jump("startChapter6") activate_sound "audio/sfx/click.mp3"
        

init -2 python:
    style.gm_nav_button.size_group = "gm_nav" 
    #For some reason, it doesn't work right if this isn't here. 