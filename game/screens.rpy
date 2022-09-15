################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")
    activate_sound "/audio/button.mp3"

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screens ##################################################################
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen csay(who, what, tint, whisper=False):
    style_prefix "csay"

    fixed:
        frame:
            at Transform(matrixcolor=TintMatrix(tint)) # Tint the box
            id "namebox"
            style "namebox"
            text who id "who"

        frame:
            at Transform(matrixcolor=TintMatrix(tint)) # Tint the box
            if whisper:
                foreground Transform(im.FactorScale("/images/props/icon whisper.png", 0.3), xpos=38, ypos=36)
                window:
                    top_padding 33
                    text what id "what"
            else:
                text what id "what"

screen psay(who, what, whisper=False):
    style_prefix "psay"

    fixed:

        frame:
            at Transform(matrixcolor=TintMatrix(gui.player_tint)) # Tint the box
            if whisper:
                foreground Transform(im.FactorScale("/images/props/icon whisper.png", 0.3), xpos=38, ypos=36)
                window:
                    top_padding 33
                    text what id "what"
            else:
                text what id "what"

## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style namebox is default

style namebox:
    # What pixel of the frame is used to position the frame
    anchor gui.name_anchor

    # position
    xpos gui.name_xpos
    ypos gui.name_ypos

    # These are the distance between the text area and frame outer edge
    padding gui.textbox_padding

    minimum (gui.namebox_width, gui.textbox_min_height)
    maximum (gui.textbox_width, gui.textbox_max_height)

    background Frame("gui/textbox_client.png", gui.textbox_borders)

    # Text styling
    xalign gui.name_xalign
    yalign gui.name_yalign

style say_label:
    # Style the text in the namebox
    size gui.name_text_size

style csay_frame:
    # our background picture
    background Frame("gui/textbox_client.png", gui.textbox_borders)

    # What pixel of the frame is used to position the frame
    anchor (1.0, 1.0)
    # position
    xpos 840
    ypos 480
    # size
    minimum (gui.textbox_width, gui.textbox_min_height)
    maximum (gui.textbox_width, gui.textbox_max_height)

    # These are the distance between the text area and frame outer edge
    padding gui.textbox_padding

style psay_frame:
    # our background picture
    background Frame("gui/textbox_player.png", gui.textbox_borders)

    # What pixel of the frame is used to position the frame
    anchor (0.0, 1.0)
    # position
    xpos 1080
    ypos 1060
    #size
    minimum (gui.textbox_width, gui.textbox_min_height)
    maximum (gui.textbox_width, gui.textbox_max_height)

    # These are the distance between the text area and frame outer edge
    padding gui.textbox_padding

style say_text:
    xsize None # needed - otherwise it uses a gui setting
    align (0,0) # also likely needed

    # Text styling
    font gui.text_font
    color gui.text_color
    size gui.text_size

style whisper_text is say_text
## If this is modified, remember to also update the hard coded style in add_to_bathball()
style whisper_text:
    first_indent 75
    color gui.whisper_text_color

## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    fixed:

        frame:
            at Transform(matrixcolor=TintMatrix(gui.player_tint)) # Tint the box

            vbox:
                for i in items:
                    button:
                        action i.action
                        idle_background im.FactorScale("/gui/button/continue_idle.png", gui.arrow_zoom)
                        hover_background im.FactorScale("/gui/button/continue_hover.png", gui.arrow_zoom)
                        text i.caption


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True

style choice_frame is psay_frame
style choice_vbox is vbox
style choice_button is button
style choice_text is button_text

style choice_frame:
    ymaximum gui.choicebox_max_height

style choice_vbox:
    xalign 0.0
    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    background None
    top_padding 5
    left_padding 65
    activate_sound "/audio/button.mp3"

style choice_text is default:
    properties gui.button_text_properties("choice_button")

################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        vbox:
            xalign 0.5

            text "[config.name!t]":
                style "navigation_title"

            text "[config.version]":
                style "navigation_version"

        if main_menu:

            textbutton _("Start") action Start() background "../gui/button/menu_green_pad.png" xysize (412,238) text_size 64

        else:

            textbutton _("Continue") action Return() background "../gui/button/menu_green_pad.png" xysize (412,238) text_size 64


        textbutton _("Settings") action ShowMenu("preferences") background "../gui/button/menu_blue_pad.png" xysize (362,179)


        textbutton _("Content warning") action ShowMenu("about") background "../gui/button/menu_darkgreen_pad.png" xysize (509, 131)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    xalign 0.5
    activate_sound "/audio/button.mp3"

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

style navigation_title:
    properties gui.text_properties("title")
    xalign 0.5

style navigation_version:
    properties gui.text_properties("version")
    xalign 0.8

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    text _("A game by Kit, LaChapeliere, Marsheleene and Sweetberry") style "main_menu_text"

style main_menu_text is gui_text

style main_menu_text:
    properties gui.text_properties("main_menu")
    yalign 0.94



## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

                ## Reserve space for the navigation section.
                frame:
                    style "game_menu_navigation_frame"

    use navigation

    # Only add the Return button if in the main menu, else use "Continue"
    if main_menu:
        textbutton _("Return"):
            style "return_button"

            action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize gui.navigation_xpos - 80

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    xalign 1.0
    yalign 1.0
    yoffset -45

## About screen ################################################################
##
## This screen gives content warning information.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Content warning"), scroll="viewport"):

        style_prefix "about"

        if gui.about:
            text "[gui.about!t]\n"


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        button:
                            action Preference("display", "window")
                            text _("Window")
                        button:
                            action Preference("display", "fullscreen")
                            text _("Fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                    text "" # To force spacing with sound parameters if box wrap

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    left_padding 45
    idle_background "/gui/button/check_idle.png"
    hover_background "/gui/button/check_hover.png"
    selected_idle_background "/gui/button/check_selected_idle.png"
    selected_hover_background "/gui/button/check_selected_hover.png"
    activate_sound "/audio/button.mp3"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    left_padding 45
    idle_background "/gui/button/check_idle.png"
    hover_background "/gui/button/check_hover.png"
    selected_idle_background "/gui/button/check_selected_idle.png"
    selected_hover_background "/gui/button/check_selected_hover.png"
    activate_sound "/audio/button.mp3"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675

################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/textbox_client.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")
    activate_sound "/audio/button.mp3"

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Quick buttons ###############################################################
##
## Two simple buttons at the top-right of the screen to access the game menu (by default the parameters) and quit the game

screen quick_buttons():
    hbox:
        anchor (1.0, 0.0)
        align (0.995, 0.01)

        imagebutton:
            at Transform(zoom=0.3)
            idle "/gui/button/pause_idle.png"
            hover "/gui/button/pause_hover.png"
            action ShowMenu("preferences")
            activate_sound "/audio/button.mp3"

        imagebutton:
            at Transform(zoom=0.3)
            idle "/gui/button/quit_idle.png"
            hover "/gui/button/quit_hover.png"
            action Quit(confirm=True)
            activate_sound "/audio/button.mp3"

## Ingredients screens ###############################################################
##
## Imagebuttons for the ingredients, inactive but visible during dialogue

init python:

    def compute_result():
        global bathball_info
        global ingredient_info

        energy = 0
        pleasure = 0

        for i in bathball_info:
            energy += ingredient_info[i]["energy_modifyer"]
            pleasure += ingredient_info[i]["pleasure_modifyer"]

        return (energy, pleasure)

    def add_to_bathball(ingredient):
        global bathball_info
        global bathball_color
        global current_character
        global bathball_results

        # Store info
        bathball_info.append(ingredient)

        # Update visual
        bathball_color = bathball_color * TintMatrix(ingredient_info[ingredient]["colour"])

        # Next step
        if len(bathball_info) == 1:
            renpy.show_screen("psay", who="", what=_("One down, two to go!"), whisper=True, _widget_properties={"what": {"first_indent": 75,
            "color": gui.whisper_text_color}}) ## Whisper mode
        elif len(bathball_info) == 2:
            renpy.show_screen("psay", who="", what=_("Just one more ingredient..."), whisper=True, _widget_properties={"what": {"first_indent": 75,
            "color": gui.whisper_text_color}}) ## Whisper mode
        elif len(bathball_info) == 3:
            renpy.show_screen("psay", who="", what=_("And one bathbomb to go!"), whisper=True, _widget_properties={"what": {"first_indent": 75,
            "color": gui.whisper_text_color}}) ## Whisper mode
            bathball_results[current_character] = compute_result()
            renpy.hide_screen("bathball")
        else:
            renpy.show_screen("psay", who="", what=_("Something went wrong, please contact costumer service!"))

screen ingredients():
    style_prefix "ingredients"
    hbox:
        for i in ingredient_info.keys():
            imagebutton:
                idle ["/images/props/ingredient " + i + " idle.png"]
                hover ["/images/props/ingredient " + i + " hover.png"]
                insensitive ["/images/props/ingredient " + i + " insensitive.png"]
                action [SensitiveIf(crafting_session),
                    Hide("csay"), # Shouldn't be necessary, just in case
                    Hide("choice"), # Shouldn't be necessary, just in case
                    Hide("psay"),
                    Show("ingredient_confirm", ingredient = i)]
                activate_sound "/audio/button.mp3"
                yalign 1.0


## Confirm the selected ingredient
screen ingredient_confirm(ingredient):
    style_prefix "ingredient_confirm"

    fixed:

        frame:
            has vbox
            at Transform(matrixcolor=TintMatrix(gui.player_tint)) # Tint the box
            text ingredient_info[ingredient]["name"] style "ingredient_name"
            text ingredient_info[ingredient]["description"]
            button:
                action [Function(add_to_bathball, ingredient=ingredient), Hide("ingredient_confirm")]
                idle_background im.FactorScale("/gui/button/continue_idle.png", gui.arrow_zoom)
                hover_background im.FactorScale("/gui/button/continue_hover.png", gui.arrow_zoom)
                text _("Add")
                activate_sound "/audio/ingredient.mp3"
            button:
                action Hide("ingredient_confirm")
                idle_background im.FactorScale("/gui/button/continue_idle.png", gui.arrow_zoom)
                hover_background im.FactorScale("/gui/button/continue_hover.png", gui.arrow_zoom)
                text _("Put back")
                activate_sound "/audio/button.mp3"

## Display the bathball
screen bathball():
    style_prefix "bathball"

    hbox:
        at bathball_dissolve
        image "/images/props/bathBall.png":
            at Transform(matrixcolor=bathball_color)



style ingredients_hbox:
    # Position
    xpos 60
    ypos 820
    spacing 60

style ingredient_confirm_frame is psay_frame

style ingredient_confirm_frame:
    ymaximum gui.choicebox_max_height

style ingredient_confirm_vbox:
    xalign 0.0
    spacing 15

style ingredient_name:
    color gui.accent_color
    size gui.name_text_size

style ingredient_confirm_hbox is choice_hbox
style ingredient_confirm_button is choice_button
style ingredient_confirm_text is choice_text

style bathball_hbox:
    xalign 0.43
    ypos 680

transform bathball_dissolve:
    on hide:
        alpha 1.0
        linear .25 alpha 0



## End game ###############################################################
##
## Article screens with various layouts

screen article(title, content, pic):
    style_prefix "article"

    hbox:
        if pic:
            image Transform(pic, xsize=600, ysize=600)
        vbox:
            if title:
                text title style_prefix "article_title"
            if content:
                text content

style article_hbox:
    xalign 0.5

style article_title_text is main_menu_text
style article_title_text:
    font gui.bold_text_font
    size 42

style article_vbox:
    yalign 0.5
    spacing 50

style article_text is default
style article_text:
    justify True

screen final_credits():

    vbox:

        text _("Credits") style_prefix "article_title"

        hbox:
            xalign 0.5
            spacing 30
            image "/gui/window_icon.png"
            text endgame_in_credits style "article_text" line_spacing 20

        hbox:
            xalign 0.5
            spacing 30
            image "/images/props/icon whisper.png" yalign 0.5
            text endgame_out_credits style "article_text" line_spacing 20 size gui.notify_text_size

screen newspaper(articles):
    style_prefix "newspaper"

    viewport:
        mousewheel True
        scrollbars "vertical"

        vbox:
            null height 30

            for a in articles:
                use article(a["title"], a["text"], a["image"])
                image Transform("/gui/scrollbar/horizontal_idle_bar.png", xsize=800, ysize=3, xcenter=0.5)

            use final_credits

            null height 100

style newspaper_viewport:
    xpos 150
    xsize 1500
    ypos 320
    ysize 780

style newspaper_vscrollbar:
    #anchor(1.0, 0.0)
    xpos 300
    ypos 350
    ysize 700

style newspaper_vbox:
    spacing 80
