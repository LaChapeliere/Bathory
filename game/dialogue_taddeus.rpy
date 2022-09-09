label taddeus_intro:

    show client taddeus beginning at client_pos with dissolve
    $ current_character = "ts"

    p "Welcome to Bathory."
    ts "Thank you, my good friend."
    ts "I was told one could bring their worries to your establishment, and leave their bath with clearer thoughts?"
    menu:
        "We try our best.":
            p "We try our best."
            ts "Well, I suppose a good soak will be relaxing, in any case."
        "Yes, our emotional bath-bombs are a treasured family secret.":
            p "Yes, our emotional bath-bombs are a treasured family secret."
            ts "Oh, bath bombs? Can I pick the flavour?"
            p "I will be the one selecting the ingredients for you, actually."
            p "Building the right composition to induce the desired emotion requires experience..."
            ts "Ah, my apologies, I did not mean to underestimate your skill."
            p "No harm done."
    p "Was there any specific reason you were visiting our baths today?"
    ts "Oh, dear me, yes!"
    ts "I am looking for some peace from the swarm of fans that seem to hunt me."
    ts "I cannot leap between one festival stand to another without some stranger bothering me with a request to design this or that building."
    ts "I do not want to be obnoxious, but..."
    ts "I'm rather famous, Taddeus Pole, architect?"
    menu:
        "Hum, are you the toad who built the Aquadiva Opera?":
            p "Hum, are you the toad who built the Aquadiva Opera?"
            ts "Yes, it is one of my better known works, with the One-Thousand Palace and the modular Underfloating compexes..."
            ts "How refreshing to meet someone who have barely heard of me!"
        "Of course. Making a fuss when we recognise a famous or infamous client is simply against our policy.":
            p "Of course. Making a fuss when we recognise a famous or infamous client is simply against our policy."
            p "We welcome all spirit-frogs equally, and with respect for their privacy."
            ts "Much appreciated... Much appreciated..."
    ts "It is not my first rodeo as a Very Important Spirit, but I feel like every year it gets worse!"
    ts "Why, just this morning, I learnt that some mindless sycophants have created a club to keep track of my tastes."
    ts "Music, holiday spots, coitus positions..."
    ts "They dissect my every move!"
    ts "How is one supposed to relax in that situation?!?"
    ts "I cannot even indulge in some trippy tadpoles to relax, because I am afraid word of it will get back to my homeforest."
    ts "The little bits are a treat, but they really aren't the done thing where I'm from..."
    p "It sounds like an unpleasant situation..."
    ts "That's one way to word it!"
    ts "If at least I still enjoyed my work..."
    p "You don't?"
    ts "I am not sure anymore."
    ts "I had this philosophy you know."
    ts "Buildings should enable collaborative work while protecting individuals."
    ts "And I still believe in that..."
    ts "But these days, I feel like people expect my buildings to do all the work for them!"
    ts "I can design spaces to foster collaboration, but I cannot force people to communicate or care for each other!"
    ts "Do not get me wrong, I am very happy about people liking my work. But all this hero-worshipping is ridiculous! And tedious!"
    p "I understand your frustration."
    ts "I am this close to accepting my cousin's offer to join her on her tea farm!"
    ts "A quiet glade in a far away forest, the daily challenge of life, a strong tie to the earth..."
    ts "Sounds like heaven right now..."
    p "Maybe things will be clearer after a bath?"
    ts "Maybe... I hope so..."
    p "Please give me a minute to prepare your bath bomb."

    call craftingscene from _call_craftingscene_4

    p "Here it is, please enjoy your bath!"
    ts "Thank you kindly."

    hide client with dissolve

    return


label taddeus_postbath_fork:
    if bathball_results["ts"][0] > 0:
        # high
        if bathball_results["ts"][1] > 0:
            # positive
            $ endings.append(endgame_info["ts"]["teafarm"])
            jump taddeus_postbath_teafarm
        else:
            # negative
            $ endings.append(endgame_info["ts"]["revenge"])
            jump taddeus_postbath_revenge
    else:
        # low
        $ endings.append(endgame_info["ts"]["priceoffame"])
        jump taddeus_postbath_priceoffame


label taddeus_postbath_revenge:

    show client taddeus happy at client_pos with dissolve
    $ current_character = "ts"

    ts "This bath was very illuminating indeed!"
    ts "Those fools refuse to stop pestering me and respect my privacy, no matter how many times I ask them to leave alone."
    ts "Well, the time for letting them walk all over me is over!"
    ts "I will have my revenge, and no one will ever dare bother me again!"
    menu:
        "Revenge?":
            p "Revenge?"
            ts "Worry not, friend!"
            ts "I cannot go into details, for I would not want to ruin the surprise."
            ts "But it will be grandiose, one of my chef-d'oeuvre!"
            p "Wait..."
            hide client with dissolve
            pw "He's gone already... Oh dear!"
        "Sounds good. Go get them!":
            p "Sounds good. Go get them!"
            ts "Thank you for your support!"
            ts "If you ever want to come to one of my unveiling events, you will be most welcome."
            p "That is nice of you."
            ts "Well, except the next one. No, that would be terribly ungrateful of me."
            pw "What??"
            ts "In any case, I will make sure to visit during our next festival!"
            p "We would be honoured by your continued patronage."
            p "Please take care."
            hide client with dissolve

    return



label taddeus_postbath_teafarm:

    show client taddeus thinking at client_pos with dissolve
    $ current_character = "ts"

    ts "Aaaah..."
    p "How did you enjoy your bath?"
    ts "It was most refreshing!"
    ts "I had not enjoyed such peace and quiet for a long time!"
    ts "If a short soak in a tranquil place leaves me energised again, maybe it is a sign."
    p "A sign?"
    ts "Yes, a sign that it's high time I left the hubbub of architect life behind me."
    ts "I think I shall write to my cousin immediately."
    menu:
        "I wish you luck on the tea farm then.":
            p "I wish you luck on the tea farm then."
            ts "I do not think luck has much to do with it."
            ts "Hard work, skill, and experience, more likely."
            ts "But your well-wishes are appreciated all the same!"
        "When are you planning to move?":
            p "When are you planning to move?"
            ts "Well... I should probably wait for my cousin's answer, to ensure his offer is still relevant."
            ts "But I will want to take advantage of the portals that have been set up for the festival."
            p "I suppose there's no sense in dawdling if you have made your decision."
    ts "Farewell, spirit-witch of the energising bath-bombs."
    pw "Wow, I like that new title. Very fancy!"
    p "Goodbye, take care."

    hide client with dissolve

    return



label taddeus_postbath_priceoffame:

    show client taddeus bored at client_pos with dissolve
    $ current_character = "ts"

    ts "Well..."
    menu:
        "Is something wrong?":
            p "Is something wrong?"
            ts "Not as such, no."
            ts "I am simply..."
            ts "...underwhelmed. Yes, underwhelmed, that is the perfect word!"
        "You look thoughtful.":
            p "You look thoughtful."
            ts "Do I ?"
            ts "I do not feel thoughtful. More... disheartened."
    p "Was something wrong with your bath?"
    ts "Oh no, no, the bath was perfectly fine."
    ts "I can even say that it exceeded my expectations! My path is much clearer now."
    ts "Only..."
    p "Yes?"
    ts "My way forward is clear, but I do not like it much."
    p "Oh."
    ts "It occurred to me that I have nothing to complain about."
    ts "My work is my passion, I am lauded for it, and my future is secure."
    ts "Minor drawbacks are to be expected, are they not?"
    ts "It is the price of fame..."
    menu:
        "I guess so...":
            p "I guess so..."
            ts "I had best be on my way, before words spread that I am your patron."
            ts "I would hate for my fans to descend upon your establishment like a locust swarm..."
            p "I'm sure it wouldn't be that bad!"
            pw "What a dramatic frog!"
            ts "Good bye. My thanks for the bath."
            p "You're welcome. Take care, and don't hesitate to come back if things aren't looking up."
            hide client with dissolve
        "You can still decide whether that price is reasonable or not.":
            p "You can still decide whether that price is reasonable or not."
            ts "And if I decide it is not?"
            p "Well, then you can think about changing your life around?"
            p "You mentionned your cousin's invited you to work on their tea farm..."
            ts "It is a nice thought, but one must remain realistic."
            ts "I cannot run away from my responsibilities."
            ts "And if I want to get away from it all for a few hours, I can come back here, can I not?"
            p "You will always be welcome."
            ts "Until my next visit, then."
            hide client with dissolve

    return
