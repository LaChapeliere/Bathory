label fff_intro:

    show client fff hiden at client_pos with dissolve
    $ current_character = "fff"

    p "Welcome to Bathory"
    gn "Hel.. Hel.. Hello chief! We are her.. here to take a bath, we ain't no tadpoles but we love the pool."
    p "I believe it's your first visit to our place. Do you know how our baths work?"

    show client beginning with Dissolve(0.3)

    fie "*She's really in character!*"
    fwey "*Shhhht*"

    show client hiden with Dissolve(0.3)

    gn "That that would be a pr.. prec.. pr.. precious knowledge for my investigation."
    p "Oh, you're a detective? What brings you here?"

    show client beginning with Dissolve(0.3)

    fie "*Don't say too much you magpie eh!*"
    fey "*I know, believe in me! We prepared ourselves. Stay quiet.*"

    show client hiden with Dissolve(0.3)

    gn "I'm sear.. searching for a certain object. Some must say, a pr.. prec.. precious artifact."
    gn "It would appear to you simple, plain. But it could save the world!"
    gn "I'm her..e to retr... ret... retrieve it before it falls in the hands of Waetùl, the evil academician."
    gn "Or academinician would be more appropriate eheh."
    fie "*Shhhht!*"
    gn "Hmm anyway, civilians should stay away from this."
    p "Indeed, I understand. We civilians need to be protected from evil, and as a special detective you can't say much."
    p "You know, if you explain it to me some more, I could better help you."
    p "Our baths will influence you in ways that we cannot totally anticipate. We use special ingredients that will influence your emotions."

    show client beginning with Dissolve(0.3)

    fwey "*Oh damn! That's amazing! I've never heard of this!!*"
    fie "*We need to steal some of that.*"
    p "*Cute, but not happening.*"
    p "Are you prepared for this, detective? I mean, you looked like you can deal with the risk but maybe you need to think."
    fey "*What should we d... d... do?*"
    fie "*Ain't afraid of nothing!*"
    fwey "*I'm really really REALLY curious!!*"

    show client hiden with Dissolve(0.3)

    gn "Indeed my Mister, we are up for it. Our mission require secrecy but als... also inspir... ation."
    menu:
        "Don't worry, if I see a suspicious customer, I'll warn you and I will not mention our conversation.":
            p "Don't worry, if I see a suspicious customer, I'll warn you and I will not mention our conversation."
        "Do you not trust an honest and capable frog?":
            p "Do you not trust an honest and capable frog?"
    gn "You're ind... indeed a craopable lady!"

    show client beginning with Dissolve(0.3)

    fie "*Stop the jokes, you!*"
    fey "*Stay quiet.. t.. quiet.*"

    show client hiden with Dissolve(0.3)

    p "*I don't know what game they're playing, but it sounds very confusing.*"
    p "So, are you confident about your investigation so far?"
    gn "We never lose confidence. Our job is to keep a clear head."

    show client beginning with Dissolve(0.3)

    fie "*I'm wondering guys, is this place really the right one?*"
    fwey "*I mean, an artifact hidden into a secret spirit inn, seems legit to put it in here.*"
    fey "*I'm worried too, chief is nice but.. but.. but is she really an NPC?*"

    show client hiden with Dissolve(0.3)

    p "*A NPC? What's that supposed to be?*"
    gn "Hmm anyway, could we get a bath sir please?"
    p "Of course. I'll prepare your bathbomb right away! You can {b}all{/b} relax."
    fwey "*The artifact should be in the second bath of the first floor. Ask for this bath!!*"
    gn "Oh yes. Hmm, can I have the s.. sec.. second bath of the first floor please."
    p "This bath is free, so make yourself at home. Can I ask why this bath in particular?"
    gn "Spiritumental Secret Defense. SSD."
    fey "*Super Super Dope eheh.*"
    fie "*Shhhht!*"
    p "I understand, we civilians cannot understand the SSD ways."
    p "I will ask you to be calm and quiet during this process, we don't want to misplace ingredients in here. *wink*"

    call craftingscene

    p "And here it is! Enjoy your bath, and your search."

    hide client with dissolve

    return


label fff_postbath_fork:
    if bathball_results["fff"][1] > 0:
        # positive
        if bathball_results["fff"][0] > 0:
            # high
            jump fff_postbath_overpowered
        else:
            #low
            jump fff_postbath_satisfied
    else:
        #negative
        if bathball_results["fff"][0] > 0:
            # high
            jump fff_postbath_anger
        else:
            #low
            jump fff_postbath_tired


label fff_postbath_overpowered:

    show client fff hiden at client_pos with dissolve
    $ current_character = "fff"

    gn "My dear dear d.. deer chief, what a formidable invest..igation! Your bath are quite the thing."

    show client confident with Dissolve(0.3)

    fie "*That was powerful as heck!! I'll need to find some for home...*"
    fwey "*We will go to the human realm, have so much power with this suit and save all the worlds in the world!!*"
    fey "*Quiet, it was am.. amazing but we have to stay in character.*"

    show client hiden with Dissolve(0.3)

    p "My bath seemed to help!"
    menu:
        "So, how did the investigation go?":
            p "So, how did the investigation go?"
        "I'm happy that you feel great now! What's next?":
            p "I'm happy that you feel great now! What's next?"
    gn "After all these pr.. precious adventures, we gained no artifact but I can fe..feel the power in me right now."
    gn "I believe that's what the rid.. rid.. riddle wanted us hmm me to find."

    show client confident with Dissolve(0.3)

    fie "*SO MUCH POWER! We'll take over the entire world tomorrow!*"
    fwey "*We'll help the entire world, don't forget we're a great spy-detective-adventurer-hero, Froggie*"
    fey "*T.. true. Frogwey you said that \"fr..iendship is p..ower\" in the human world, bath is p..power here. Haha*"
    menu:
        "You grew up in no time in this bath! Hope your power will be a good fit for tomorrow!":
            p "You grew up in no time in this bath! Hope your power will be a good fit for tomorrow!"
        "Great job finding what your riddle meant! I hope you'll have a great festival Mr. Gordon":
            p "Great job finding what your riddle meant! I hope you'll have a great festival Mr. Gordon"
    gn "Bye you beaut.. ti.. tiful Sir!"

    hide client with dissolve

    return


label fff_postbath_satisfied:

    show client fff hiden at client_pos with dissolve
    $ current_character = "fff"

    gn "Exqu..isite! That was so soft and p...pleasing."

    show client blush with Dissolve(0.3)

    fie "*Hell yeah! Like being in a fluffy animal.*"
    fwey "*Too bad we found nothing, but Frogey you did a great job. We got into the bath and now we feel sooooo goood. yawn*"
    fey "*Thanks but quiet, or chief will understand.*"

    show client hiden with Dissolve(0.3)

    p "I'm happy to hear this. You seemed stressed, I gave you a happy and relaxing bath. Like a soft water massage you could say."
    gn "A massage delivering a message, indeed."

    show client blush with Dissolve(0.3)

    fey "D.. damn I'm too t..ired. Thanks."
    fie "*Hey you! You've lost character.*"
    fey "*I know but..but I don't think that mat..mat..matter anymore.*"
    fwey "*frown It matters a little...*"
    fie "Oh come on! We had a great time and we will tomorrow, too! Remember how we started this game?"
    fey "Yeah. We went to.. to the see great Felune, and met Platyss."
    fwey "And she was so out of place among frogs! But lead us to our first interspirit LARP!!"
    fie "I can't wait to see their faces tomorrow, we'll tell them about this BATH OF POWER."
    fey "Keep c.. calm *yaaaawn*"

    hide client with dissolve

    p "They were quite a trio, these three little fellas!"

    return


label fff_postbath_anger:

    show client fff angry at client_pos with dissolve
    $ current_character = "fff"

    fie "OMG! We searched for SO LONG!"
    fwey "Far too long..."
    fey "We found nothing, n... nothing."
    menu:
        "Oh no, I'm sorry to hear this. Can I do anything to help?":
            p "Oh no, I'm sorry to hear this. Can I do anything to help?"
        "You were searching for something special? You know, you could have asked.":
            p "You were searching for something special? You know, you could have asked."
    fie "Oh don't mock us m'aam! You KNEW, we will tell the organizers."
    fey "Hey calm down, it's not his fault..."
    fwey "We talked about our investigation, why she didn't stop us?!"
    p "You know, I just wanted for you to have a nice moment."
    p "*I'm really not good at handling children...*"
    fie "We LOST precious time! I swear I'll kick every organizer."
    fwey "She's right, they produced poor game design and here we are. I HATE THAT! I WANTED TO SAVE THE WORLD CRAAAAAA"
    p "Calm down."
    fey "Thanks but we d... don...'t want to. We n.. need t.. to.. to tell them."

    hide client with dissolve

    p "**sigh* Have a nice festival...*"

    return


label fff_postbath_tired:

    show client fff tired at client_pos with dissolve
    $ current_character = "fff"

    fwey "*yawn* Daaaaamn, this is really hard work, human documentation doesn't lie."
    fey "Yeah, we s.. searched everywhe..re and n.. no..w *yaaaaaawn*"
    fie "Hey pals, we need to stay in character. *yawn*"

    show client hiden with Dissolve(0.3)

    p "So, how was this investigation?"
    gn "It was exq.. exqu.. great, but I'm afraid we didn't find anything for our quest euhm case."

    show client tired with Dissolve(0.3)

    fwey "Too tired to be sad, we searched well."
    menu:
        "I'm happy to know that you're not too bummed out!":
            p "I'm happy to know that you're not too bummed out!"
        "I'm sorry to hear that, but yeah you did a great job.":
            p "I'm sorry to hear that, but yeah you did a great job."
    fie "Happen' sometimes, at least we've made quite the memory heh."
    fwey "Yeah, the last puzzle, that pointed us here, it was thrilling even if it was badly designed!"
    fey "We took long to guess it, maybe it.. it was too difficult but remember the first day when we decid.. deci... ded to play FFF?"
    fie "Yeah it's quite a character this one, and how we made Crokella search into the whole camp for..."

    hide client with Dissolve(1)

    return
