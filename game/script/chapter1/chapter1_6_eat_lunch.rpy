label chapter1_eat_lunch:

    "..."
    
    "After laying down for some time, I get up and walk down the stairs."

    play music "audio/ambient/Boiling Water.ogg" volume 0.1 fadein 10.0

    scene bg inn mainroom
    with Fade(0.5, 1.0, 0.5)

    "Nobody's at the counter but I heard some sounds in the kitchen."

    "Looking in, I see a man cooking."

    "His greying hair betrayed his age."

    me "Hello."

    define nf = Character("?", who_color="#0516af")

    show theodore shadow
    with Dissolve(0.1)

    nf "Hello, sir. Are you Fynn Sceite, the new client ?"

    me "I am."

    "He give his hand and we shake hands."

    define nf = Character("Theodore", who_color="#0516af")

    nf "I am Theodore, the father of the girl you saw."

    nf "She talked to me about your long stay here."

    me "Oh yeah... About that..."

    nf "Don't worry."

    nf "There is no problem with that, you can stay however long you want."

    me "Really ?"

    me "Don't you close sometimes ?"

    nf "Not in the foreseable future."

    nf "Where would we go anyway ?"

    me "Hum..."

    "Out of this city maybe ?"

    "But yeah...{w} He probably can't even think about that."

    me "True." 

    nf "As you can see, there is you dinner."

    "Looking in, I see a big marmite of soup cooking above a fire."

    nf "I put all we had left in here."

    nf "It's a bit rustic but to be honest, we didn't expect someone to come."

    me "Didn't expect someone to come ?"

    nf "Well no one come in the fall."

    nf "It's already rare to fill 2 rooms at the same in normal times..."

    me "So am I the only client here ?"

    nf "Indeed and probably will be for a long time."

    nf "But regularly we lend rooms for people in the city when they are in need."

    me "I see..."

    nf "About the food..."

    nf "We'll buy some more tomorrow but..."

    me "It's fine, I need a lightweight lunch anyway after not eating for days."

    nf "For days ?!"

    nf "Are you okay ?"

    me "Uh... Yeah."
    
    me "Don't worry, I'm used to fasting for long periods."

    me "And this one was pretty short so no need to worry."

    nf "Oh...{w} That's good then."

    stop music fadeout 3.0

    "[nf] served me a bowl of soup."

    nf "That's for you."

    me "Thanks"

    nf "Take any seat you want, when you're finished, just leave the bowl on the table."

    nf "I'll take care of it."

    nf "Bon appetit !"

    hide theodore shadow
    with Dissolve(0.5)

    play music "audio/ambient/Crackling Fireplace.ogg" volume 0.2 fadein 5.0

    "I nodded and took the seat closest to the fire."

    "The meal was good but I wasn't the most objective in my condition."

    "Still, it felt good to eat again."

    "After finishing the dinner, I left the bowl on the table."

    "On my way back to my room, Theodore stopped me."

    show theodore shadow
    with Dissolve(0.5)

    nf "Sorry to hold you, I know you must be really sleepy..."
    
    nf "But I wanted to tell you to wait for us tomorrow morning."

    nf "We'll have something to offer you."

    nf "I can't tell you the details right now because I didn't talk yet with my daughter."

    me "Something to offer me ?"

    nf "A service yes."

    nf "I don't want to bother you."
    
    nf "I'm just telling you to wait for us tomorrow if we're not up yet."

    "I wonder what kind of service it is..."

    me "Sure then, I'll wait."

    nf "Wonderful !"

    nf "Have a good night !"

    me "Thanks."

    stop music fadeout 3.0

    scene bg bedroom inn night
    with Fade(0.5, 1.0, 0.5)

    "..."

    "Theodore said I must be really sleepy but..."

    "As usual I do not feel it."

    "I never do."

    "..."

    "But what else to do anyway ?"

    "I can't go outside."

    "Not on the first night."

    "I need a break anyway."

    "..."

    "I guess I'll force myself into sleep."

    "I took off my clothes, lay down in the bed and closed my eyes."

    "Let's go through an another dreamless night."

    show bg black screen
    with Fade(3.0, 4.0, 0.0)

    $ renpy.movie_cutscene("gui/opening.webm")