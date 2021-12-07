label chapter2_4_choice1_goback:
    
    "I turn around and go back on my steps."

    stop music fadeout 1.0

    scene bg city
    with Fade(0.5, 0.5, 1.5)

    play music "audio/ambient/Bustling Town Ambience.ogg" fadein 3.0 volume 1.2

    "..."

    "Lots of people."

    "I hope she didn't go too far."

    "..."

    #$ renpy.music.set_volume(0.1, 0, channel="music")
    stop music fadeout 1.0

    play sound "audio/sfx/Swoosh.mp3" volume 0.3

    scene bg city
    with Fade(.25, 0, .75, color="#fff")

    "I feel something grabing my shoulder."

    show nivi maid running2 brows2 eyes0 mouth10 open mouth open eyes with Dissolve(0.1)

    nivi "{cps=15}FYNN !!!!!{/cps}"

    play longvoice "audio/sfx/voice/nivi/nivi after climax.ogg" fadein 10.0

    play music "audio/music/Lurking Around.mp3" fadein 3.0 volume 0.8

    show nivi maid h-caressing standing afterglow with Dissolve(0.1)

    nivi "{i}*Catches her breath.*{/i}"

    show nivi maid h-caressing standing afterglow headup brows2 eyes0 mouth10 open mouth open eyes with Dissolve(0.1)

    nivi "God ! You're there !"

    nivi "I though I lost you."

    stop longvoice fadeout 2.0

    me "Hum..."

    me "It's not a thought, you did in fact lost me."

    nivi "..."

    show nivi maid happy2 brows0 eyes17 mouth1 closed mouth open eyes with Dissolve(0.1)

    nivi "But you're there so it's fine !"

    me "We lost some time on the visit though."

    show nivi maid happy2 brows2 eyes15 mouth6 closed mouth open eyes with Dissolve(0.1)

    nivi "Uuuh... yeah..."

    me "I'm quite upset you know ?"

    me "How are you gonna compensate ?"

    show nivi maid basic10 brows6 eyes8 mouth6 closed mouth open eyes with Dissolve(0.1)

    nivi "What ?"

    nivi "What are you talking about ?"
    
    me "The deal was that you'll be my guide until the evening."

    me "I understand that it was an error but the facts are :"

    me "\"You did not guide me for quite a time now.\""

    show nivi maid basic10 brows1 eyes9 mouth6 closed mouth open eyes with Dissolve(0.1)

    nivi "So what ?"

    nivi "You want your money back ?"

    me "No."

    me "Just pay me a drink before going back to the inn."

    show nivi maid surprise2 brows12 eyes22 mouth14 open mouth open eyes with Dissolve(0.1)

    nivi "Huuuh ???"

    me "That would be enough."

    me "This bar you showed me earlier seemed quite nice."

    show nivi maid surprise2 brows11 eyes4 mouth14 closed mouth open eyes with Dissolve(0.1)

    nivi "A-"

    nivi "A drink ?"

    me "Exact."

    show nivi maid basic28 brows3 eyes8 mouth7 closed mouth closed eyes with Dissolve(0.1)

    nivi "..."

    show nivi maid basic28 brows3 eyes8 mouth7 closed mouth open eyes with Dissolve(0.1)

    nivi "Sure."

    jump chapter2_post_menu1