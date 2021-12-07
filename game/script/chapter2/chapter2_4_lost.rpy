label chapter2_4_lost:

    scene bg city
    with Fade(0.5, 0.5, 1.5)

    play music "audio/ambient/Bustling Town Ambience.ogg" fadein 3.0 volume 0.5

    "After our lunch, the visit continued."

    "The pace got faster."

    "A bit too fast."

    "Honestly, it was barely enjoyable."

    "I mean...{w} I'm not in a race against time."

    "I'm staying here for days anyway."

    "I just wanted to enjoy the views..."

    "So yeah..."
    
    "I looked away for a instant."

    "Ok ok..."

    "Maybe more than an instant."

    "The result is that I'm lost."

    "Lost like a child."

    "In the biggest street of the city."

    "The thoroughfare coming from the farms in the south to the merchants in the north-west."

    "What was my first reaction ?"

    "I smiled."

    "I'm free right ?"

    "Free to walk at my own pace."

    "She'll see soon that I'm missing and will search for me."
    
    "Or maybe she'll wait for me at the end."

    "Until then."

    "Free time !"

    stop music fadeout 1.0

    scene bg gate
    with Fade(0.5, 0.5, 1.5)

    play music "audio/ambient/Bustling Town Ambience.ogg" fadein 3.0 volume 0.5

    "I'm now passed through the gate."

    "If I continue forward, I'll go to the mountains."

    "Clearly not the correct path to take."

    "..."

    "I did not saw her."

    "I'm starting to worry."

    "But maybe there is a way to turn this into my advantage."

    "It was time to be pissed."

    "But before getting pissed, I need to find her."

    "And decide how to do it."

    menu:

        "What should I do ?"

        "Go back and search for Nivi.":
            jump chapter2_4_choice1_goback

        "Stay here and wait for Nivi":
            jump chapter2_4_choice1_stay
    

    # CHOICES LINES

label chapter2_post_menu1:

    show nivi maid basic28 brows3 eyes8 mouth7 closed mouth closed eyes with Dissolve(0.1)

    nivi "..."

    me "You're alright ?"

    show nivi maid basic28 brows14 eyes9 mouth16 closed mouth open eyes with Dissolve(0.1)

    nivi "What is that question ?"

    me "Is it that weird ?"

    me "You ran a lot didn't you ?"

    show nivi maid basic28 brows3 eyes8 mouth7 closed mouth closed eyes with Dissolve(0.1)

    nivi "..."

    show nivi maid basic28 brows3 eyes8 mouth7 closed mouth open eyes with Dissolve(0.1)

    nivi "No."

    nivi "Not the question itself but the context."

    show nivi maid basic28 brows3 eyes8 mouth7 closed mouth closed eyes with Dissolve(0.1)

    nivi "..."

    show nivi maid basic28 brows3 eyes8 mouth7 closed mouth open eyes with Dissolve(0.1)

    nivi "I feel like you aren't really upset about this."

    nivi "That you just wanted a drink."

    me "..."

    "It's not really about the drink though..."

    "But I'm not gonna tell her that."

    me "Not too tired ?"

    nivi "..."

    show nivi maid basic28 brows6 eyes0 mouth6 closed mouth open eyes with Dissolve(0.1)

    nivi "No we can continue the visit if it's what you're worrying about."

    me "You're mistaken."

    me "I'm worrying about you, not the tour."

    show nivi maid basic28 brows14 eyes9 mouth16 closed mouth open eyes with Dissolve(0.1)

    nivi "But mostly about your drink..."

    nivi "I'm fine."
    
    nivi "Let's continue."

    hide nivi with Dissolve(0.5)

    "She starts walking."

    "Tough type."

    "At least I got a free drink."

    show nivi maid basic28 brows14 eyes9 mouth16 closed mouth open eyes with Dissolve(0.1)

    nivi "Hey !"
    
    nivi "Start moving !"

    nivi "I'm not paying you 2 drinks !"

    jump chapter2_5_the_incident