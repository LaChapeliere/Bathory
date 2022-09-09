label croakma_intro:

    play sound "/audio/Frogs.mp3"
    show client croakma beginning at client_pos with Dissolve(3.0)
    $ current_character = "ca"
    $ stole_tadpoles = False

    p "Welcome to Bathory."
    ca "Hi. I only have one hour before I need to be off again, do you have a free bath right now?"
    p "Yes, absolutely."
    ca "Thank Heket, I don't know when I would have had the time otherwise!"
    p "The festival is keeping you busy?"
    ca "So, much, you can't even imagine!"
    ca "Well, to be honest, busy I could deal with."
    ca "But I had to go and lay eggs right before the festival, and now I'm stuck lugging those tadpoles around."
    menu:
        "I can see why that would tiring, especially if you have to run around a lot.":
            p "I can see why that would tiring, especially if you have to run around a lot."
            ca "Exactly! I'm lucky to my job isn't too demanding."
            ca "I take care of the crystals for the transportation portals..."
            ca "Not much to do once everything is setup, apart from being on call in case anything goes wrong."
            ca "But the festival is only once a year, and there's so many people to visit with!"
            ca "Distant cousins, children who had the fantastic idea to move half-a-world away..."
            ca "Not to mention friends from my time learning crystal crafting!"
            p "That's both the beauty and the difficulty of the festival."
            ca "Festival time is always hectic, but now I have to remember and stop to feed the rugrats every couple hours."
            ca "And that jar is heavier than expected, I swear I'm going to throw off my back..."
            p "It sounds like a lot of effort for animals who only have the potential to grow into spirits..."
            ca "Yes, well, I'm not even sure myself why I do it..."
        "Why are you keeping them, then?":
            p "Why are you keeping them, then?"
            ca "You know what, I've been asking myself the same question since coming onsite."
            ca "I feel like, you know, since I already went through all that trouble..."
            ca "Laying eggs, making sure no predator ate them, bringing the tads with me here..."
            ca "Sure, it's not like they are spirits yet, but it would still be wasted energy to abandon them now."
            ca "Isn't that a pigheaded thing, to stick to doing something that harms you because you've invested too much already?"
            ca "Anyway, while I was setting up I was able to just leave them in my toolshed."
            ca "But now that the portals are up and running, I only need to check on the crystal once a day."
            ca "The useless creatures can't go that long without beeing fed, so I have to carry them with me all over the place!"
            ca "Anyway..."

    show client upset with Dissolve(0.3)
    show tadpole_jar at jar_pos zorder 110 with Dissolve(0.3)

    ca "How about that bath then?"

    p "Give me a minute to prepare your bomb bath and you'll be all set."
    pw "I'm not sure it's healthy to resent your children that much..."

    call craftingscene from _call_craftingscene_2

    p "Here is your bath bomb, please enjoy your bath!"
    ca "Thanks! Hopefully it'll take my mind off things."

    play sound "/audio/Frogs.mp3"
    hide client with Dissolve(3.0)

    pw "She left her tadpole jar on the counter... Is it a sign?"
    pw "I could discreetly add them to my reserve of trippy tadpoles..."
    menu:
        "Leave the jar alone":
            pw "No, better not..."
        "Appropriate the tadpoles":
            pw "Here we go..."
            $ stole_tadpoles = True
            hide tadpole_jar with Dissolve(0.3)

    return

label croakma_postbath_fork:
    if bathball_results["ca"][1] > 0:
        # positive
        if stole_tadpoles:
            # stole the tadpoles
            $ endings.append(endgame_info["ca"]["mildlyupset"])
            jump croakma_postbath_mildlyupset
        else:
            #left the tadpoles
            $ endings.append(endgame_info["ca"]["thankyou"])
            jump croakma_postbath_thankyou
    else:
        # negative
        if stole_tadpoles:
            # stole the tadpoles
            $ endings.append(endgame_info["ca"]["forget"])
            jump croakma_postbath_forget
        else:
            #left the tadpoles
            $ endings.append(endgame_info["ca"]["burden"])
            jump croakma_postbath_burden


label croakma_postbath_mildlyupset:

    play sound "/audio/Frogs.mp3"
    show client croakma happy at client_pos with Dissolve(3.0)
    $ current_character = "ca"

    ca "Ah, this was nice!"
    p "I'm glad you enjoyed your bath!"
    ca "Hum... I thought I had left my tadpoles here?"

    show client worried with Dissolve(0.3)

    menu:
        "Err...":
            p "Err..."
            ca "Didn't I?"
            p "Yes, you did..."
            ca "Could I have them back, now? I really need to get going."
            p "About that..."
            pw "Did I badly misread the situation?"
            p "I'm afraid it's not going to be possible."
            p "I thought you had left them on purpose..."
            p "They are soaking peacefully in the back, turning in trippy tadpoles."
            p "I apologise deeply for misunderstanding..."
            show client upset with Dissolve(0.3)
            ca "What if you just scooped them out? They can't have been in there for long..."
            p "Even if we could pick them out in a tank full of tadpoles, I don't think it would be such a good idea."
            p "The preserve solution they are in is pretty potent. They wouldn't grow {w=1}{cps=*0.5}right...{/cps}"
            ca "Oh..."
            ca "And here I was, all refreshed, feeling like I could cope."
            ca "That's such a shame..."
        "I thought I'd do you a service and rid you of them.":
            p "I thought I'd do you a service and rid you of them."
            ca "What?"
            p "Honestly, you sounded so tired and overwhelmed..."
            p "I know you might feel like it's a waste of eggs, but you were going to run yourself into the ground."
            p "And I got the feeling you knew that but could not make the decision?"
            show client upset with Dissolve(0.3)
            ca "Maybe..."
            ca "Still, I didn't expect you to do that."
            ca "What did you do with them?"
            p "I put them to soak in trippy solution. I make my own trippy tadpoles preserves."
            ca "Not a total waste then, if you can make decent snacks out of them..."
            ca "I guess my days just lightened up."
            ca "Yay..."
            pw "She looks about as happy as a dried up clam..."
    ca "I'll just get on with my day then."
    p "Thank you for your patronage."

    play sound "/audio/Frogs.mp3"
    hide client with Dissolve(3.0)

    return

label croakma_postbath_thankyou:

    play sound "/audio/Frogs.mp3"
    show client croakma happy at client_pos with Dissolve(3.0)
    $ current_character = "ca"

    ca "Ah, this was nice!"
    ca "Oh, I had forgotten my taddies here..."
    ca "Thank you for keeping an eye on them!"

    hide tadpole_jar with Dissolve(0.3)

    show client happyjar with Dissolve(0.3)

    menu:
        "You're welcome.":
            p "You're welcome."
            ca "And thanks for the delightful bath bomb."
        "You're welcome. I think you should consider getting rid of them though.":
            p "You're welcome. I think you should consider getting rid of them though."
            ca "Oh, I can see why you would say that!"
            ca "I was a real mess earlier, wasn't I?"
            ca "But your bath bomb was perfectly on point, I feel much lighter now."
            ca "I'm sure I'll be okay!"
    p "I'm glad I could help!"
    p "I hope to see you next year, and in the meantime, please take care."
    ca "You do too! Goodbye."

    play sound "/audio/Frogs.mp3"
    hide client with Dissolve(3.0)

    return


label croakma_postbath_forget:

    play sound "/audio/Frogs.mp3"
    show client croakma thinking at client_pos with Dissolve(3.0)
    $ current_character = "ca"

    ca "Oh bother!"
    ca "I thought the bath would make me feel better."
    ca "But it's mostly forced my to think about the mess that my life is right now..."
    p "Hopefully you'll feel the benefits later..."
    ca "Yes, hopefully."
    ca "I feel like I'm forgetting something though..."
    p "..."
    pw "This is going to be awkward..."
    ca "Oh, well, no matter. It can't have been that important..."
    ca "Goodbye, then."
    p "Goodbye, take care."

    play sound "/audio/Frogs.mp3"
    hide client with Dissolve(3.0)

    pw "That went better than expected!"

    return


label croakma_postbath_burden:

    play sound "/audio/Frogs.mp3"
    show client croakma notsure at client_pos with Dissolve(3.0)
    $ current_character = "ca"

    ca "Oh bother!"
    ca "I thought the bath would make me feel better."
    ca "But it's mostly forced my to think about the mess that my life is right now..."
    ca "And my little burdens are here!"
    ca "Joy!"
    ca "I was wondering where I had left them..."
    pw "Oh, maybe I should have put them away then."
    pw "But then, it doesn't feel like a decision I should make for her..."

    hide tadpole_jar with Dissolve(0.3)
    show client sadjar with Dissolve(0.3)

    ca "Here I go then."

    pause 5

    menu:
        "Would you maybe like another bath?":
            p "Would you maybe like another bath?"
            ca "No, I really don't have time for that."
            ca "Bye."
        "I can still see you...":
            p "I can still see you..."
            ca "Yes, yes, I'm going...    "

    play sound "/audio/Frogs.mp3"
    hide client with Dissolve(3.0)

    return
