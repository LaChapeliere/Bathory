# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character(screen="psay", what_style="say_text")
define c = Character("Stranger", screen="csay", what_style="say_text", show_tint="#ffffff") # Add ctc for click-to-continue
define fey = Character("Frogey", kind=c, show_tint="#62CBEE")
define fwey = Character("Frogwey", kind=c, show_tint="#795349")
define fie = Character("Froggie", kind=c, show_tint="#9CC151")
define tx = Character("Toadlax", kind=c, show_tint="#939070")
define fe = Character("Froxune", kind=c, show_tint="#E29C6A")
define ca = Character("Croakma", kind=c, show_tint="#469BE2")
define ts = Character("Taddeus", kind=c, show_tint="#E0A92A")
$ current_character = ""

transform client_pos:
    zoom 0.9
    xalign 0.55
    yalign 0

# Info for the ingredients
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


# The game starts here.

label start:

    # Set default game menu to the Preferences screen
    $ _game_menu_screen = "preferences"

    # Show button to access menu
    show screen access_menu
    show screen ingredients


    jump testscene

    return

label testscene:

    scene bg inside

    show client toadlax beginning at client_pos
    $ current_character = "tx"

    show counter

    p "I'm going to make you a bathball!"

    jump craftingscene


label craftingscene:

    # Disable ctc
    $ _skipping = False
    $ config.keymap['dismiss'] = []
    $ config.keymap["rollforward"] = []

    p "I need to add three ingredients from the shelf."

    $ crafting_session = True

    show screen bathball

    while len(bathball_info) < 3:
        $ renpy.pause(0.1)

    $ crafting_session = False
    $ bathball_info = []

    # Enable ctc
    $ _skipping = True
    $ config.keymap['dismiss'] = [ 'mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT' ]
    $ config.keymap["rollforward"] = [ 'mousedown_5', 'K_PAGEDOWN', 'repeat_K_PAGEDOWN' ]

    jump testscene


label testmenu:

    scene bg inside

    show client toadlax beginning at client_pos

    show counter

    tx "Hello"

    menu:
        "Should I say this? It's a really good choice I think. In my humble opinion. Let's make that box too big, yooohoooo!":
            p "This"

        "Or that":
            p "That"

        "Or something else entirely":
            p "Boop"

    tx "Hello my friend, welcome to the bath bubble bubble. This is a good place to be. Don't you think so? The bubble extend to about 160 characters."

    show client happy at client_pos behind counter

    tx "Again"

    p "Narrator speech"
