label chapter2_3_the_discussion:

    play sound "audio/sfx/Door Close.ogg"

    scene bg restaurant
    with Fade(0.5, 0.5, 1.5)
    
    me "Nice place."

    show nivi maid basic28 brows14 eyes9 mouth16 closed mouth open eyes
    with Dissolve(0.5)

    nivi "..."

    show nivi maid basic28 brows14 eyes9 mouth16 closed mouth open eyes:
        xpos 650
    with moveinleft
    show francis shadow:
        xpos 1100 ypos 200
    with Dissolve(0.5)

    define francis = Character("Probably a Nivi acquaintance", who_color="#ebd2ca")

    play music "audio/music/Mega_Man_3_Rock_My_Socket_OC_ReMix.mp3" fadein 3.0 volume 0.1

    francis "Yo Nivi !"

    francis "Long time no see !"

    nivi "..."

    "He was an almost young man."

    "Probably in his late 20's."

    $ francis = Character("Probably an unwanted Nivi acquaintance", who_color="#ebd2ca")

    francis "Hum."

    francis "I see..."
    
    francis "Still cold as ever huh ?"

    francis "What brings you here ?"

    nivi "We need a table."

    francis "For two ?"

    nivi "Yes."

    francis "Okay."

    $ francis = Character("A Questionner", who_color="#ebd2ca")

    francis "Who's this young man ?"

    nivi "A client."

    $ francis = Character("An annoying Questionner ?", who_color="#ebd2ca")

    francis "What are you doing with a client here ?"

    me "She's my guide for today."

    "I lend my hand for a shake."

    me "I'm Fynn, nice to meet you."

    $ francis = Character("Nah... just a nice guy.", who_color="#ebd2ca")

    francis "Me too."

    francis "So ?"

    francis "A visit of the city..."

    francis "I see, I see..."

    $ francis = Character("Just annoying.", who_color="#ebd2ca")

    francis "Make sense."

    $ francis = Character("Finally !", who_color="#ebd2ca")

    francis "Take any table you want."

    francis "I serve only the meal of the day at lunch."

    $ francis = Character("Better this way.", who_color="#ebd2ca")

    francis "No choice but at least you'll be served fast haha!"

    hide francis shadow
    with Dissolve(0.5)

    show nivi maid basic28 brows14 eyes9 mouth16 closed mouth open eyes at center
    with moveinright

    "Looking at Nivi, she still did not show any sign of amusement."

    "In fact, she didn't since entering to the restaurant."

    "It seems I'm missing some parts of a story untold story."

    "I turn to Nivi."

    me "You know we can go to another..."

    nivi "This is the only one."

    me "We don't need to go to a restaurant to eat..."

    nivi "You wanted to go to one."

    "..."

    me "I see how it is."

    "We sat at the nearest table."

    "..."

    me "Hum..." 

    me "Who's this guy anyway ?"

    nivi "It's better for you that I don't present him."

    me "What do you mean ?"

    nivi "Do you really think I'm capable to give you an objective portrait of him ?"

    "Wow a cold anger."

    "It's rare to see one."

    "She's still capable of rational thinking even though she seems to just hate the guy."

    me "You have a point."

    "..."

    "Yeah."

    "I don't really want to have her stare me like that for the entire lunch."

    "I need to find something."

    "..."
    
    me "Why do you wear this maid's uniform ?"

    show nivi maid basic28 brows6 eyes0 mouth6 closed mouth open eyes with Dissolve(0.1)

    nivi "Maid ?"

    nivi "Those are my work clothes."

    "Hah ?"

    me "Yeah but your father said you had nothing to work on today."

    me "Wouldn't it be more comfortable to have more casual clothes on ?"

    show nivi maid basic28 brows3 eyes8 mouth7 closed mouth closed eyes with Dissolve(0.1)

    nivi "..."

    show nivi maid basic28 brows6 eyes0 mouth6 closed mouth open eyes with Dissolve(0.1)

    nivi "Why do you ask that ?"

    "Oof..."

    "I guess I'm gonna be honest."

    me "I don't know...{w} just trying to have a discussion going I guess."

    show nivi maid basic28 brows3 eyes8 mouth7 closed mouth closed eyes with Dissolve(0.1)

    nivi "Hum..."

    nivi "..."

    show nivi maid basic28 brows2 eyes0 mouth0 closed mouth open eyes with Dissolve(0.1)

    nivi "I...{w} I don't really have casual clothes."

    me "Really ?"

    show nivi maid angry1 brows8 eyes9 mouth8 open mouth open eyes with Dissolve(0.1)

    nivi "I'm the innkeeper !"

    show nivi maid pose1 brows14 eyes8 mouth10 open mouth open eyes with Dissolve(0.1)
    
    nivi "That's who I am !"

    "Bingo !"

    "Let's proceed to this emotionnaly driven discussion now !"

    show nivi maid pose1 brows14 eyes8 mouth10 closed mouth open eyes with Dissolve(0.1)

    me "That's not really a answer."

    me "So does it means you wear this maid costume everyday ?"

    show nivi maid angry1 brows8 eyes9 mouth8 open mouth open eyes with Dissolve(0.1)

    nivi "Why do you call it a maid costume anyway ?"

    me "From where I comme this ressembles a maid costume."

    me "A bit too colorful though..."

    show nivi maid basic28 brows14 eyes9 mouth16 closed mouth open eyes with Dissolve(0.1)

    nivi "Well I'm not a maid."

    me "Aren't you ?"

    show nivi maid basic28 brows15 eyes8 mouth6 closed mouth open eyes with Dissolve(0.1)

    nivi "How's that ?"

    $ renpy.music.set_volume(0.2, delay=0, channel='music')
    play sound "audio/sfx/Swoosh.mp3" volume 0.3
    show francis shadow #with Dissolve(0.1)
    show nivi maid surprise2 brows12 eyes22 mouth14 open mouth open eyes at left #with moveinleft
    with Fade(.25, 0, .75, color="#fff")

    $ francis = Character("WOW ! What the fuck man ?!", who_color="#ebd2ca")

    francis "Dinner served !"

    $ renpy.music.set_volume(1.0, delay=0, channel='music')

    "We each received a plate with some meat and vegetables."

    $ francis = Character("Yeah yeah, leave fast please", who_color="#ebd2ca")

    francis "Bon appetit !"

    hide francis shadow
    with Dissolve(0.5)

    "He left as fast as he came."

    show nivi maid basic28 brows6 eyes9 mouth6 closed mouth closed eyes at center with Dissolve(1)

    "..."

    nivi "{size=-10}{i}I hate this fucking guy...{/i}{/size}"

    me "..."

    "Yeah."

    "Like if I ever needed more proof..."

    show nivi maid basic28 brows3 eyes8 mouth7 closed mouth open eyes with Dissolve(0.1)

    me "So."

    me "About the maid stuff..."

    me "You prepare beds, foods and take care of the house."

    me "You do the same work than a maid right ?"

    me "The only difference is that you don't have one master but severals."

    show nivi maid basic28 brows3 eyes8 mouth7 closed mouth closed eyes
    with Dissolve(0.1)

    nivi "..."

    show nivi maid basic28 brows3 eyes8 mouth7 closed mouth open eyes with Dissolve(0.1)

    nivi "So there is a difference."

    me "I never said you were a maid."

    show nivi maid basic28 brows6 eyes0 mouth6 closed mouth open eyes with Dissolve(0.1)

    nivi "Really ?"

    me "It was only rhetorical."

    show nivi maid basic28 brows3 eyes8 mouth7 closed mouth open eyes with Dissolve(0.1)

    nivi "Sure."

    nivi "But if I follow your logic I'm doing the same work."

    me "Same work but not for the same reasons."

    me "And that changes everything."

    me "Like..."

    me "A slave could do your work too..."

    show nivi maid basic28 brows3 eyes8 mouth7 closed mouth closed eyes
    with Dissolve(0.1)

    nivi "Hum..."

    show nivi maid basic28 brows3 eyes8 mouth7 closed mouth open eyes
    with Dissolve(0.1)

    nivi "I think I understand yes."

    nivi "We could say that my job is giving bedrooms and doing the job of a maid."

    nivi "But what's your point ?"

    me "My point ?"

    menu:
        "Hum..."

        "Making fun of her.":

            me "I'm just making fun of you."

            show nivi maid angry1 brows8 eyes9 mouth8 open mouth open eyes with Dissolve(0.1)

            nivi "WHAT ?!"

            nivi "You dumbass !"

            me "Haha !"

            show nivi maid basic28 brows6 eyes9 mouth6 closed mouth closed eyes with Dissolve(0.1)

            nivi "..."

            show nivi maid basic28 brows6 eyes0 mouth6 closed mouth open eyes with Dissolve(0.1)

            nivi "{cps=2}.  .  .{/cps}"

            me "What ?"

            nivi "Explain me the point."

            me "{cps=25}I told you it wa-{/cps}{nw}"

            show nivi maid angry1 brows8 eyes9 mouth8 open mouth open eyes with Dissolve(0.1)

            nivi "That's not the real reason !"

            me "..."

            me "Okey."

            me "I'll explain it."

            show nivi maid basic28 brows6 eyes0 mouth6 closed mouth open eyes with Dissolve(0.1)

            me "My point is that being a maid or an innkeeper is the same work."

            me "So having similar clothes is logical."

            show nivi maid basic28 brows15 eyes8 mouth6 closed mouth open eyes with Dissolve(0.1)

            nivi "So you weren't making fun of me ?"

            me "..."

            show nivi maid basic28 brows3 eyes8 mouth7 closed mouth open eyes with Dissolve(0.1)

            nivi "You're weird sometimes."

            "Because you aren't ?"

            show nivi maid basic28 brows4 eyes2 mouth3 closed mouth open eyes with Dissolve(0.1)

            nivi "But I don't mind."

        "Explaining it clearly":

            me "My point is that being a maid or an innkeeper is the same work."

            me "So having similar clothes is logical."

            show nivi maid basic28 brows12 eyes17 mouth10 open mouth open eyes with Dissolve(0.1)

            nivi "Oh !"

            show nivi maid basic28 brows4 eyes2 mouth3 closed mouth open eyes with Dissolve(0.1)

            nivi "I see..."

        "Telling her she's dumb to not understand it.":

            me "Is it that hard to grasp ?"

            show nivi maid basic28 brows6 eyes9 mouth6 closed mouth open eyes with Dissolve(0.1)

            nivi "Yes ?"

            me "..."

            me "I cannot do anything with you I guess..."

            show nivi maid angry1 brows8 eyes9 mouth8 open mouth open eyes with Dissolve(0.1)

            nivi "What are you talking about !?"

            me "Whatever."

            me "Forget it."

            nivi "No !"

            show nivi maid pose1 brows14 eyes8 mouth10 open mouth open eyes with Dissolve(0.1)

            nivi "Explain it to me !"

            nivi "Clearly !"

            me "..."

            me "Okey."

            me "My point is that being a maid or an innkeeper is the same work."

            me "So having similar clothes is logical."

            show nivi maid basic28 brows12 eyes17 mouth10 open mouth open eyes with Dissolve(0.1)

            nivi "Ah !"

            show nivi maid basic28 brows3 eyes8 mouth7 closed mouth open eyes with Dissolve(0.1)

            nivi "Thank you for the clear and concise explanation !"

            nivi "It feels nice to be treated as a sentient being."

            "Sentient ?"

            "If by that she means emotionnal, she's right."

    show nivi maid basic33 brows0 eyes0 mouth0 closed mouth open eyes with Dissolve(0.1)

    nivi "But now that I'm thinking about it."

    show nivi maid basic3 brows0 eyes9 mouth37 closed mouth open eyes with Dissolve(0.1)

    nivi "I'm basically your personnal maid right now since you're the only client."

    me "Uh yeah..."

    me "You can say that..."

    me "Then what do you think about being a maid ?"

    show nivi maid basic33 brows0 eyes0 mouth0 closed mouth open eyes with Dissolve(0.1)

    nivi "What do I think about it ?"

    me "How does it feels ?"

    show nivi maid basic33 brows0 eyes0 mouth0 closed mouth closed eyes with Dissolve(0.1)

    nivi "I mean..."

    show nivi maid basic28 brows3 eyes8 mouth7 closed mouth open eyes with Dissolve(0.1)

    nivi "It's fine I guess."

    me "Do you like your work ?"

    show nivi maid basic28 brows15 eyes8 mouth6 closed mouth open eyes with Dissolve(0.1)

    nivi "Why those weird questions ?"

    me "I just try to keep the flow of the discussion, that's all."

    show nivi maid basic28 brows3 eyes8 mouth7 closed mouth closed eyes with Dissolve(0.1)

    nivi "Hum..."

    show nivi maid basic28 brows3 eyes8 mouth7 closed mouth open eyes with Dissolve(0.1)

    nivi "My life is being the daughter of the innkeeper."

    nivi "So asking me how I feel about my work is basically asking how I feel in my life."

    nivi "It's very personnal."

    me "Sure..."

    me "I understand."

    me "..."

    me "No need to answer."

    nivi "..."

    "She could have simply answer : \"I feel good\"."

    "But she didn't..."

    "..."

    hide nivi maid basic28 brows3 eyes8 mouth7 closed mouth open eyes with Dissolve(0.5)

    stop music fadeout 3.0

    "Being lost in my thoughts, we ended the lunch without talking."

    jump chapter2_4_lost