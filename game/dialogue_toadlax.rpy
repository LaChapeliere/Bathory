label toadlax_intro:

    play sound "/audio/Frogs.mp3"
    show client toadlax beginning at client_pos with Dissolve(3)
    $ current_character = "tx"

    p "Welcome to... {w=1.0}Oh! Toadlax, long time not seen!"
    tx "Well, you know how hard it is to travel outside of festival time..."
    tx "I'd visit more often otherwise."
    p "Don't sweat, I understand!"
    p "How are you doing? Do you have plans to do some open mics this festival?"
    tx "I wish, but I actually got a pretty fancy job this year!"
    tx "I doubt I'll have any time in the evenings to go singing..."
    p "Too bad, I'd have come listen to you..."
    p "Your singing always lift my heart!"

    show client bored with Dissolve(0.3)

    tx "Yes, well, that wasn't the opinion of the temple masters, was it?"
    tx "A vulgar swamp frog like myself can't possibly grasp the subtlety of ceremonial singing..."
    pw "Oops, touchy topic..."
    p "It's their loss!"
    tx "Thanks."

    show client beginning with Dissolve(0.3)

    tx "I honestly love cooking as much as singing these days, but I still get bitter about their rejection whenever I think about it."
    p "I understand."
    p "What about that new job then? Not working for the Grand Final banquet anymore?"
    tx "No, not this year! My little specialty inn was pretty successful this year, so I nabbed the VIP catering gig."
    p "Wow, well done you!"
    tx "Yeah, they liked my little pitch about food satisfying the heart as much as the body."
    tx "I love the technical challenge of adapting my recipes to follow the nonsensical whims of the rich and famous..."
    tx "And I've got access to really high quality products!"

    show client bored with Dissolve(0.3)

    p "What with the long face? That sounds great, right?"
    tx "I guess I'm being oversensitive again..."
    tx "The job {b}is{/b} great. But some of that crowd..."
    tx "I'm just fed up with their well-meaning comments about how good my cooking is.{w=0.5}.{w=0.5}.{w=0.5} \"for a swamp frog\"."
    p "Seriously?"
    p "That sucks big time."
    p "I don't even have words..."
    tx "{cps=*0.5}It's not that bad...{/cps}"
    p "Oh, no, I'm stopping you right there!"
    p "You are not oversensitive, and it {b}is{/b} bad!"
    p "I know there's not much we can do against ordinary specism like this, at least not without you loosing your job."
    p "But we can still acknowledge that they are narrow-minded, entitled dung beetles, who wouldn't know respect if it bit them in the rear!"

    show client happy with Dissolve(0.3)

    tx "Haha, you always know what to say to make me laugh!"
    tx "I did consider putting a laxative in the iced maybugs..."
    tx "See how they like being the \"vulgar and dirty\" ones for a change."
    p "That'd sure knock them off their pedestal!"
    tx "Huhu. It wouldn't even be hard."

    show client beginning with Dissolve(0.3)

    tx "Anyway, what's up with you? The year treat you well?"
    p "Oh, well, you know, the usual..."
    p "The inn's always been rather quiet outside of the festival..."
    p "It's a good thing the closest temple is the region's healing centre, or we'd be stuck with only locals and the occasional traveller."
    tx "Meet anyone interesting recently?"
    p "Hum, let's see..."
    p "There was this shapeshifter who sought me out a few months ago. Wanted advice about becoming a healer against the wishes of their family..."
    p "And a family of eighteen siblings who came with their Pop for his birthday, and all of them were adopted."
    p "And the story of the people who come here for healing are always interesting, of course, but not really mine to tell..."
    tx "Right, of course!"
    tx "Do you have new ingredients for your bath balls?"
    p "They are called bath bombs, you know that!"
    tx "Yeah, well, they are round, so I'll call them balls if I want!"
    tx "Plus, most of them just melt or fizzle out, they don't actually explode, so I don't see why you insist on calling them bombs."
    p "It's all about their impact. They are too awesome to just be called balls!"
    tx "Sure, whatever you say."
    tx "How about you cook one up for me? I feel like a bath now."
    p "Sure, just give me a minute!"

    call craftingscene from _call_craftingscene

    p "Here it is, enjoy a good soak!"
    tx "Thanks! It'll give me an opportunity to fine-tune my laxative maybugs plan!"

    play sound "/audio/Frogs.mp3"
    hide client with Dissolve(3)

    pw "Wait, was she serious?"

    return

label toadlax_postbath_fork:
    if bathball_results["tx"][1] > 0:
        # positive
        if bathball_results["tx"][0] > 0:
            # high
            $ endings.append(endgame_info["tx"]["revenge"])
            jump toadlax_postbath_revenge
        else:
            #low
            $ endings.append(endgame_info["tx"]["mellow"])
            jump toadlax_postbath_mellow
    else:
        #negative
        $ endings.append(endgame_info["tx"]["laxative"])
        jump toadlax_postbath_laxative


label toadlax_postbath_revenge:

    play sound "/audio/Frogs.mp3"
    show client toadlax revenge at client_pos with Dissolve(3)
    $ current_character = "tx"

    tx "I had a much better idea!"
    menu:
        "Oh dear!":
            p "Oh dear!"
            tx "Don't be a monkey! It's really better!"
        "What about?":
            p "What about?"
            tx "Getting back at the VIP who made comments about me coming from the swamps."
            tx "Do keep up!"
    p "Alright, alright, what's the idea, then?"
    tx "Hum, you know what, I don't think I should tell you..."
    p "Now I'm worried. Are you going to kill anyone?"
    tx "Of course not! I'm not going to kill them, maim them, or anything like that!"
    tx "I'll just be in a lot of trouble if it doesn't work."
    tx "And they can't blame you if you didn't know about it. Plausible deniability and all that..."
    p "{cps=*0.2}Ooo-kayyy...{/cps}"
    tx "I'd better scram, though, if I want to get everything ready on time."
    tx "Thanks for the very inspiring bath!"
    p "You're welcome?"
    tx "See you around!"
    p "See you soon. Take care!"

    play sound "/audio/Frogs.mp3"
    hide client with Dissolve(3)

    return

label toadlax_postbath_mellow:

    play sound "/audio/Frogs.mp3"
    show client toadlax happy at client_pos with Dissolve(3)
    $ current_character = "tx"

    tx "Best bath ever..."
    p "I'm glad you liked it so much!"
    tx "Yes, I feel all mellow and satisfied."
    tx "I think you saved a few VIPs from a laxative attack, haha."
    tx "I hadn't realise I was so tense, I would probably have ended up poisoning the next dryfrog who made a speciesist comment."
    p "They'd have deserved it, but I'd have been sad if it had cost you your job..."

    show client beginning with Dissolve(0.3)

    tx "I have to go back to my kitchen, but I'll try to visit again before the end of the festival."
    p "It'd be really nice! Come whenever you want!"
    tx "Cheers pal!"

    play sound "/audio/Frogs.mp3"
    hide client with Dissolve(3)

    return


label toadlax_postbath_laxative:

    play sound "/audio/Frogs.mp3"
    show client toadlax interrogative at client_pos with Dissolve(3)
    $ current_character = "tx"

    tx "Hum, which do you think would work best frozen?"
    tx "Cascara bark or sulfurous powder?"
    p "Err..."
    tx "As a laxative?"
    menu:
        "The bark.":
            p "The bark."
        "The powder.":
            p "The powder."
        "I really wouldn't know.":
            p "I really wouldn't know."
    tx "'k. I need to research some more, but it can probably work..."
    pw "It sounds like she's really going to put laxative in the VIP food..."
    p "Are you sure that's a good idea?"
    tx "Probably not. But I'm just sick of everyone looking down on me because of my species."
    tx "I just want them to get what's coming to them for once..."
    tx "Anyway, I'll see you around."

    play sound "/audio/Frogs.mp3"
    hide client with Dissolve(3)

    pw "I hope she doesn't get into too much trouble."

    return
