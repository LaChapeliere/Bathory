label froxune_intro:

    play sound "/audio/Fox.mp3"
    show client froxune beginning at client_pos with Dissolve(3.0)
    $ current_character = "fe"

    fe "Hello Cr... Mister. I came here to rest before the festival tomorrow. It's always crowded and takes a lot of energy, am I right?"
    p "Hi, and welcome to our baths."
    p "The festival is famous among the spirits, even non frog ones. But we are a small place, and only few people know about us, you can relax about the crowd."
    fe "*gulp*"
    p "What brings you to the festival?"
    fe "Well, I'm a voyager you see. I travel from place to place, to learn more about frogs and their ways."
    fe "I mean, I mean, I mean, I know the ways of my lake spirit people, but not those of swamp frogs."
    menu:
        "That's great, we don't usually know how people from every other place do things.":
            p "That's great, we don't usually know how people from every other place do things."
        "That's an interesting goal, I hope you'll write a book or something after that!":
            p "That's an interesting goal, I hope you'll write a book or something after that!"
    fe "Oh yeah, yeah, yes."
    fe "Anyway, do you have maybe advice or something for the festival? I mean, hum, it's my first time around, I don't want to stand out."
    p "My advice is to do what makes you comfortable, but to try and leave some of your masks aside sometimes to let people know you truly."
    p "Us frogs like sincere people."
    p "Not all frogs, of course, but you could gain some true friends along the way."
    fe "Thanks, thanks, thanks for that! I'll try my best."
    menu:
        "I believe it's your first time here. Want some explanations?":
            p "I believe it's your first time here. Want some explanations?"
        "Do you need me to explain how the baths work?":
            p "Do you need me to explain how the baths work?"
    fe "I'll welcome your explanations, with pleasure!"
    fe "I'm passionate about spirits, mostly frog ones, but I haven't had the chance to come in and see y{cps=*0.3}...{/cps} {cps=*3}See, see, see this place.{/cps}"
    p "As you know, we love a lot of things, but here we selected ingredients that have an influence on your emotions."
    p "We have ginger bark, purple algae, arctic snake skin, trippy tadpoles, grey clay and dry guano."
    fe "Eeeeek! {w=1.0}Hm I mean, I mean, I mean, sounds lovely of course!"
    fe "How did you select these ingredients? I didn't know you had such powers!"
    p "{cps=*0.3}...{/cps}"
    pw "I think I know them..."
    fe "Hum I, I, I hum I mean you don't look like a frog that could do such things."
    p "It's my sister, we opened these baths together, she's really great at influencing people's emotions."
    p "We decided to create this place to help every frog sort through their issues and thoughts while having a good soak."
    fe "Oh okay, yeah you mentioned that... Hum, your sister, it's great to stay with our family sometimes."
    fe "Anyway, I think I should have that bath. I hope it'll give me strength for tomorrow!"
    p "I'll make you something nice, you'll see! *wink*"

    call craftingscene from _call_craftingscene_3

    p "Here it is! Enjoy your time in this \"lovely\" bath."

    play sound "/audio/Fox.mp3"
    hide client with Dissolve(3.0)

    return

label froxune_postbath_fork:
    if bathball_results["fe"][1] > 0:
        # positive
        if bathball_results["fe"][0] > 0:
            # high
            $ endings.append(endgame_info["fe"]["dreams"])
            jump froxune_postbath_dreams
        else:
            #low
            $ endings.append(endgame_info["fe"]["confident"])
            jump froxune_postbath_confident
    else:
        # negative
        $ endings.append(endgame_info["fe"]["depressed"])
        jump froxune_postbath_depressed


label froxune_postbath_dreams:

    play sound "/audio/Fox.mp3"
    show client froxune dreamy at client_pos with Dissolve(3.0)
    $ current_character = "fe"

    fe "Oh wow that was amazing!"
    p "I told you it would be."
    fe "Yeah, but that was really something my friend!"
    fe "You got me! I never imagined this could feel so wonderful!"
    p "And you didn't tell me it was you when you came in..."

    show client happy with Dissolve(0.3)

    fe "Don't act like you didn't know when I came in."
    menu:
        "I knew, but you've gotten better at mimicking us.":
            p "I knew, but you've gotten better at mimicking us."
        "Hmmm, I was suspicious but not entirely sure.":
            p "Hmmm, I was suspicious but not entirely sure."
    fe "Eheh, that means tomorrow will go great for sure."

    show client dreamy with Dissolve(0.3)

    fe "I can already see my life with all of you, now..."
    fe "Having my own place, meeting all the spirits I can, living freely with everyone."
    fe "It's all thanks to you!"
    p "Oh, I just gave you a little boost, my foxy friend! The rest is all yours!"

    show client normal with Dissolve(0.3)

    fe "You did so much more than that. Remember when we were kids?"
    p "You were so cute back then!"
    fe "Eh! That was not what I was going to say."
    p "I know, I know, I love messing with you."
    fe "You've changed too, you know? You're much more lively."
    fe "Anyway, as I was saying, before you interrupted..."
    fe "You talked to me at this holiday camp. Even if the others were afraid."
    fe "You told me to believe in my dream. You told me that you liked me."
    fe "And I think this is the first time you helped me, and it lead us here."
    fe "You are truly amazing, my friend."
    menu:
        "Thanks. You are too!":
            p "Thanks. You are too!"
        "I know, I know!":
            p "I know, I know!"

    show client dreamy with Dissolve(0.3)

    fe "*sigh* Alright! Let's go ace that festival, shall we?!"
    p "You're going to rock it, I'm sure!"
    fe "See you soon!"

    play sound "/audio/Fox.mp3"
    hide client with Dissolve(3.0)

    return

label froxune_postbath_confident:

    play sound "/audio/Fox.mp3"
    show client froxune happy at client_pos with Dissolve(3.0)
    $ current_character = "fe"

    fe "That was comforting."
    fe "I'm glad I came here before the festival."
    p "And I'm glad you came here too!"
    p "Was the bath great for you?"
    fe "My friend, it was relaxing and I feel better."

    show client normal with Dissolve(0.3)

    fe "I'm still a little worried that it might not go well tomorrow."
    fe "Yet, I'm confident. I will stay under the radar and..."
    menu:
        "Be yourself?":
            p "Be yourself?"
        "Be the best fox in town?":
            p "Be the best fox in town?"
    fe "Be myself, yeah, but also stay under the radar."
    fe "I'll be a modest but blunt frog with fortune telling powers."
    p "I see, but you know, I think you can go as yourself this time."
    p "Times sure changed and you could start something new for all of us."
    fe "I'm not that good you know. Anyway, I'll stay true to myself."
    few "And to my dream."
    p "I'm sure it'll be alright! Cheer up!"
    fe "Yes yes, I'll cheer up after a nap."
    p "I hope to see you again soon this time, and not in forty years!"
    fe "I promise I'll come see you more often from now on."
    p "You better!"
    fe "Anyway, let's get ready for tomorrow."
    fe "Goodbye and see you soon!"
    p "Good luck!"

    play sound "/audio/Fox.mp3"
    hide client with Dissolve(3.0)

    return


label froxune_postbath_depressed:

    play sound "/audio/Fox.mp3"
    show client froxune sad at client_pos with Dissolve(3.0)
    $ current_character = "fe"

    few "Frogs have weird tendencies for their bath... I'll never be one of them..."
    fe "Well hum, this was... an, hum, experience."
    menu:
        "A great one or...?":
            p "A great one or...?"
        "Experiences make life exciting!":
            p "Experiences make life exciting!"
    fe "Eh you know me, I'm not so good with new things. I didn't realise frogs loved that sort of things so much!"
    p "Oh yeah, it's you, Froxune! I almost didn't recognize you, you grew up so much!"
    p "I was suspicious before your bath... So you finally came to the frog realm for the big festival!"
    fe "It was quite my big dream for life, as you know."
    p "Was?"
    fe "Eh, I'm not sure I'll go tomorrow. I'm sure you're the only frog I can get along with."
    fe "All the others will be afraid of me, or hate me. It can't be otherwise."
    p "*sigh* You know, when we were children, I wasn't afraid of you. My parent, they told me stories about big bad foxes and how they treat every other spirits."
    p "But I saw that you're not like this. You're kind, you're thoughtful, you have a lot of empathy."
    p "I'm sure other frogs can keep an open mind about this and welcome you within our realm."
    fe "I'm worried you know. My fortune telling powers have put me through hard times before."
    p "Your fortune telling skills or your bluntness? *lil laugh*"
    p "I'm joking. I like this about you."
    fe "You're the only one... *sigh in despair*"
    p "C'mon, you can do it! And if you have problem, come here and talk to me this time. It's been too long since we were able to see each other like this."
    fe "Thanks."

    play sound "/audio/Fox.mp3"
    hide client with Dissolve(3.0)

    return
