﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character()
define c = Character("Stranger", screen="csay", what_style="csay_text") # Add ctc for click-to-continue
define fey = Character("Frogey", kind=c)
define fwey = Character("Frogwey", kind=c)
define fie = Character("Froggie", kind=c)
define tx = Character("Toadlax", kind=c)
define fe = Character("Froxune", kind=c)
define ca = Character("Croakma", kind=c)
define ts = Character("Taddeus", kind=c)

transform client_pos:
    zoom 0.9
    xalign 0.55
    yalign 0


# The game starts here.

label start:

    # Set default game menu to the Preferences screen
    $ _game_menu_screen = "preferences"


    jump testscene

    return

label testscene:

    scene bg inside

    show client toadlax beginning at client_pos

    show counter

    tx "Hello my friend, welcome to the bath bubble bubble. This is a good place to be. Don't you think so? The bubble extend to about 160 characters."

    show client happy at client_pos behind counter

    tx "Again"
