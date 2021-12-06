label chapter1_nivi_discussion_1:

    play sound "audio/sfx/Door Close.ogg"
    play music "audio/ambient/Crackling Fireplace.ogg" volume 0.2 fadein 15.0

    scene bg inn mainroom
    with Fade(0.5, 1.0, 0.5, color="#FFFFFF")

    "..."

    "The interior is lightly lighted by a few torchs. It's a wide space with some tables and a counter. And at that counter..."

    $ nivi = Character("Unknow Female Voice", who_color="#771b22")

    nivi "Can I help you ?"

    show nivi maid basic7 brows0 eyes0 mouth0 closed mouth open eyes
    with Dissolve(0.1)

    $ nivi = Character("Unkown Young Women", who_color="#771b22")

    "She was looking straight into my eyes, inquisitive."

    menu:
        "Hum..."

        "Going straight to the point.":

            me "I'm looking for a room to stay."

        "Asking about her.":
            me "Are you the innkeeper ?"

            nivi "Yes."

            me "Hum... Okay."

            me "I'm looking for a room to stay."


    nivi "How long ?"

    me "I don't know."

    show nivi maid basic7 brows2 eyes4 mouth14 closed mouth open eyes
    with Dissolve(0.1)

    nivi "You don't know..."

    "..."

    nivi "At least for this night right ?"

    me "Yeah, sure."

    show nivi maid sad2 brows4 eyes20 mouth16 closed mouth closed eyes
    with Dissolve(0.7)

    nivi "..."

    me "Is there anything troubling you ?"

    show nivi maid basic7 brows0 eyes0 mouth0 closed mouth open eyes
    with Dissolve(0.3)

    nivi "No nothing..."

    show nivi maid sad2 brows4 eyes20 mouth16 closed mouth closed eyes
    with Dissolve(0.4)

    nivi "Hum..."

    "Is she making fun of me ?"

    menu:
        "Do I ask what's happening ?"

        "Yes.":

            me "Are there anything troubling you ?"

            nivi "..."

            show nivi maid basic7 brows2 eyes4 mouth14 closed mouth open eyes
            with Dissolve(1.0)

            nivi "Actually yes."

        "No let's wait...":

            nivi "..."

            show nivi maid basic7 brows2 eyes4 mouth14 closed mouth open eyes
            with Dissolve(1.0)

            nivi "No, actually, there is a thing."

    nivi "Why don't you know how long ?"

    me "..."

    me "Ah..."

    nivi "You don't need to answer, it's not important..."

    nivi "I'm just curious..."

    me "Oh no don't worry."

    me "I'm here to get some... vacation sort of..."

    nivi "Vacation ?"

    show nivi maid basic7 brows0 eyes0 mouth0 closed mouth open eyes
    with Dissolve(0.1)
    
    nivi "Seems nice !"

    nivi "You're the first to come here for leisure purposes !"

    me "Really ?"

    me "Well there is a first time for everything."

    show nivi maid basic7 brows2 eyes4 mouth14 closed mouth open eyes
    with Dissolve(0.1)

    nivi "But sir...{w} Can you estimate the duration of your vacation here ?"

    me "Hum...{w} I already told you."

    me "No idea."

    nivi "Give me a scale at least."

    me "Hum..."

    me "Between several months and several years ?"
    
    play sound "audio/sfx/Thunder Explosion.ogg" volume 0.2

    show nivi maid surprise2 brows12 eyes22 mouth14 open mouth open eyes
    with Dissolve(0.1)
    with hpunch

    nivi "{b}SEVERAL YEARS !{/b}"

    show nivi maid surprise2 brows11 eyes4 mouth14 closed mouth open eyes
    with Dissolve(0.1)
    
    nivi "Wait..."
    
    nivi "Did you buy a piece of land here ?"

    me "A piece of land ? For what ?"

    nivi "Where are you gonna live ?"

    me "Here I guess. You stay open all year right ?"

    show nivi maid basic28 brows2 eyes0 mouth0 closed mouth closed eyes
    with Dissolve(0.1)

    nivi "I..."

    show nivi maid basic28 brows2 eyes0 mouth0 closed mouth open eyes
    with Dissolve(0.1)

    nivi "I guess but..."
    
    nivi "Is it really convenient for you ?"

    me "Why ? Is there a problem for staying that long ?"

    show nivi maid basic7 brows0 eyes0 mouth0 closed mouth open eyes
    with Dissolve(0.1)

    nivi "No, of course we are open for you..."
    
    nivi "And we would be really happy to host you..."

    show nivi maid basic7 brows11 eyes4 mouth14 closed mouth open eyes
    with Dissolve(0.1)
    
    nivi "It's just that it never happened."
    
    nivi "The longuest a host stayed was about two weeks."
    
    show nivi maid basic7 brows2 eyes4 mouth14 closed mouth open eyes
    with Dissolve(0.1)
    
    nivi "But a full year..."

    show nivi maid sad2 brows4 eyes20 mouth16 closed mouth closed eyes
    with Dissolve(1.0)

    nivi "{i}A full year...{/i}"

    me "Hum ?..."

    show nivi maid basic7 brows0 eyes0 mouth0 closed mouth open eyes
    with Dissolve(0.1)

    nivi "That's fine, we'll make it happen, no problems here..."

    show nivi maid basic7 brows0 eyes0 avert mouth0 closed mouth open eyes
    with Dissolve(0.1)

    nivi "No problems at all..."

    me "..."

    me "Sure..."

    me "By the way, excuse me for not presenting myself yet."

    define me = Character("Fynn")

    me "I am Fynn Sceite."

    show nivi maid basic7 brows2 eyes4 mouth14 closed mouth open eyes
    with Dissolve(0.1)

    me "I am a traveller that often gets in others troubles."

    me "And you are ?"

    nivi "..."

    show nivi maid basic7 brows0 eyes0 mouth0 closed mouth open eyes
    with Dissolve(0.1)

    $ nivi = Character("Nivi", who_color="#771b22")

    nivi "I'm Nivi."

    "Nivi ? Huh..."

    "This name's weird..."

    "I'll ask about that later."

    me "Are you managing the inn alone ?"

    nivi "No."
    
    nivi "We're managing the inn with my father."

    nivi "So me and my father."

    me "I see, familial establishment ?"

    nivi "Sort of..."

    nivi "We manage the inn but don't own it."

    nivi "The city does."

    me "Oh...{w} That's weird..."

    nivi "It's not the first time a client find that weird."

    nivi "The organisation in this city seems quite different from the outside world."

    show nivi maid basic7 brows0 eyes0 avert mouth0 closed mouth open eyes
    with Dissolve(0.1)

    nivi "Not that I know anything about the outside world."

    show nivi maid basic7 brows0 eyes0 mouth0 closed mouth open eyes
    with Dissolve(0.1)

    nivi "Only the sayings of the few travellers passing here."

    nivi "But if you stay here for long enough, you'll get used too."

    show nivi maid basic7 brows0 eyes0 avert mouth0 closed mouth open eyes
    with Dissolve(0.1)

    nivi "Like I did..."

    me "..."

    me "Of course."

    me "No problem with that, I get used to strange things all the time."

    "..."

    show nivi maid basic7 brows2 eyes4 mouth14 closed mouth open eyes

    nivi "I have a question."

    nivi "How will you pay ?"

    nivi "I don't think your bag can hold enough coins for 3 months."

    me "I'll work."

    me "I can make myself useful."

    me "Never had a problem with money so far."

    nivi "Didn't you say you were on vacation ?"

    me "Yeah..."

    me "That's why I added the {i}\"sort of\"{/i}..."

    me "But honestly...{w} comparing working here sometimes and what I lived through those last years..."

    me "This will truly be a vacation."

    nivi "I see you had rough times."

    me "You can say so."

    "..."

    me "About the services..."

    me "Lunch and stuff..."

    show nivi maid basic23 brows15 eyes0 mouth10 open mouth open eyes

    nivi "Oh ! Yes !"

    show nivi maid basic7 brows0 eyes0 mouth0 closed mouth open eyes

    nivi "We serve only the dinner."

    nivi "By the way, after taking your room, you can come in 1 hour for the dinner."

    nivi "I'll tell my dad to cook it for you."

    nivi "For the price, it's 2 coins per day."

    me "It's cheap !"

    nivi "We and the city try its best to make the inn affordable to everyone."

    me "That's cool."

    show nivi maid basic28 brows0 eyes0 mouth0 closed mouth closed eyes

    nivi "I don't think there is anything more..."

    show nivi maid basic23 brows15 eyes0 mouth10 open mouth open eyes

    nivi "Yes there is !"

    show nivi maid basic7 brows0 eyes0 mouth0 closed mouth open eyes
    
    nivi "We clean the rooms once every 3 days."

    me "Perfect."

    nivi "Your room is the frog one."

    me "The frog one ?"

    nivi "You'll understand."

    show nivi maid basic3 brows0 eyes9 mouth37 closed mouth open eyes

    nivi "I let you the surprise."

    show nivi maid basic7 brows0 eyes0 mouth0 closed mouth open eyes

    me "Well then..."

    me "See you later."

    #hide nivi maid basic7 brows0 eyes0 mouth0 closed mouth open eyes

    show nivi maid wave
    with Dissolve(0.1)

    nivi "Later !"

    hide nivi maid wave
    with Dissolve(0.5)

    jump chapter1_going_to_bedroom