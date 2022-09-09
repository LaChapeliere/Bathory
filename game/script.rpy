# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character(screen="psay", what_style="say_text")
define pw = Character(screen="psay", what_style="whisper_text", show_whisper=True)
define c = Character("Stranger", screen="csay", what_style="say_text", show_tint="#ffffff") # Add ctc for click-to-continue
define fey = Character("Frogey", kind=c, show_tint="#62CBEE")
define feyw = Character(kind=fey, what_style="whisper_text", show_whisper=True)
define fwey = Character("Frogwey", kind=c, show_tint="#795349")
define fweyw = Character(kind=fwey, what_style="whisper_text", show_whisper=True)
define fie = Character("Froggie", kind=c, show_tint="#9CC151")
define fiew = Character(kind=fie, what_style="whisper_text", show_whisper=True)
define gn = Character("\"Gordon\"", kind=c, show_tint="#D8D0B2")
define tx = Character("Toadlax", kind=c, show_tint="#939070")
define txw = Character(kind=tx, what_style="whisper_text", show_whisper=True)
define fe = Character("Froxune", kind=c, show_tint="#E29C6A")
define few = Character(kind=fe, what_style="whisper_text", show_whisper=True)
define ca = Character("Croakma", kind=c, show_tint="#469BE2")
define caw = Character(kind=ca, what_style="whisper_text", show_whisper=True)
define ts = Character("Taddeus Pole", kind=c, show_tint="#E0A92A")
define tsw = Character(kind=ts, what_style="whisper_text", show_whisper=True)
$ current_character = ""

transform client_pos:
    zoom 0.9
    xalign 0.55
    yalign 0

image tadpole_jar = "/images/props/jarcroakma.png"

transform jar_pos:
    xalign 0.5
    yalign 0.6

# Info for the ingredients and crafting
init python:
    crafting_session = False

    ingredient_info = {
        "algae": {
            "name": "Purple algae",
            "description": "Infuse their spirit with light-hearted colours",
            "energy_modifyer": 1,
            "pleasure_modifyer": 2,
            "colour": u'D079EF'
        },
        "ginger": {
            "name": "Ginger bark",
            "description": "Zap and zing, straight to their veins, kind of nice",
            "energy_modifyer": 3,
            "pleasure_modifyer": 1,
            "colour": u'FFEE89'
        },
        "clay": {
            "name": "Grey clay",
            "description": "A good dampening base, to slow them down",
            "energy_modifyer": -1.99,
            "pleasure_modifyer": 0.1,
            "colour": u'CFD7D3'
        },
        "snake": {
            "name": "Artic snake skin",
            "description": "The cold is gross, but sometimes they need to cool down",
            "energy_modifyer": -1,
            "pleasure_modifyer": -2,
            "colour": u'EBE7CE'
        },
        "tadpoles": {
            "name": "Trippy tadpoles",
            "description": "Melt them into a happy puddle with these special snacks",
            "energy_modifyer": -3,
            "pleasure_modifyer": 2,
            "colour": u'88C78E'
        },
        "guano": {
            "name": "Dry guano",
            "description": "It's sticky and smelly, plain gross, but will wake them up right away",
            "energy_modifyer": 1.98,
            "pleasure_modifyer": -2.99,
            "colour": u'D9D3B1'
        }
    }

    bathball_info = []
    bathball_color = TintMatrix("#ffffff")
    bathball_results = {"fff": (0,0), "tx": (0,0), "fe": (0,0), "ca": (0,0), "ts": (0,0)}

    def debug_result(tuple):
        string = "The result of this bathball is "
        if tuple[0] > 0:
            string += "high"
        else:
            string += "low"
        string += " energy and "
        if tuple[1] > 0:
            string += "high"
        else:
            string += "low"
        string += " pleasure."
        return string

# The game starts here.

label start:

    # Set default game menu to the Preferences screen
    $ _game_menu_screen = "preferences"

    # Show button to access menu
    show screen quick_buttons
    show screen ingredients

    scene bg inside
    show counter zorder 100

    call toadlax_intro from _call_toadlax_intro

    call fff_intro from _call_fff_intro

    call toadlax_postbath_fork from _call_toadlax_postbath_fork

    call froxune_intro from _call_froxune_intro

    call croakma_intro from _call_croakma_intro

    call froxune_postbath_fork from _call_froxune_postbath_fork

    call taddeus_intro from _call_taddeus_intro

    call fff_postbath_fork from _call_fff_postbath_fork

    call croakma_postbath_fork from _call_croakma_postbath_fork

    call taddeus_postbath_fork from _call_taddeus_postbath_fork

    return

label testscene:

    scene bg paper

    $test_article = endgame_info["tx"]["revenge"]
    call screen article(test_article["title"], test_article["text"], test_article["image"])


    return


label craftingscene:

    # Disable ctc
    $ _skipping = False
    $ config.keymap['dismiss'] = []
    $ config.keymap["rollforward"] = []

    pw "I need to add three ingredients from the shelf."

    $ crafting_session = True

    show screen bathball

    while len(bathball_info) < 3:
        $ renpy.pause(0.1)

    # Reset bathball info
    $ crafting_session = False
    $ bathball_info = []
    $ bathball_color = TintMatrix("#ffffff")

    # Enable ctc
    $ _skipping = True
    $ config.keymap['dismiss'] = [ 'mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT' ]
    $ config.keymap["rollforward"] = [ 'mousedown_5', 'K_PAGEDOWN', 'repeat_K_PAGEDOWN' ]

    $ temp = debug_result(bathball_results[current_character])
    pw "[temp]"

    return
