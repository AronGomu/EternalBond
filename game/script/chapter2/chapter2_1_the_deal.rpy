label chapter2_1_the_deal:

    play music "audio/music/First Steps.mp3" fadein 3.0 fadeout 3.0 volume 0.5

    window hide
    scene bg chapter1 with Fade(0.5, 0, 5)
    window show
    
    scene  bg bedroom inn day with Fade(1, 0, 3)

    "..."

    "Judging by the light, the sun has already been up for a while now."

    "It's probably late in the morning."

    "I didn't think I would sleep that much."

    "Like always, it felt like I just closed my eyes seconds ago."

    "An another dreamless night..."

    "..."

    stop music fadeout 3.0

    "Or was it ?"

    scene bg inn mainroom
    with Fade(2.0, 0.0, 2.0)

    "When entering the room I see 2 pair of eyes looking at me."

    image theodoreSepia = im.Sepia(Image("images/character sets/theodore/theodore shadow.png"))

    image niviSepia = im.Sepia(Image("images/character sets/nivi/nivi maid basic28 brows3 eyes8 mouth7 closed mouth open eyes.png"))
    

    show theodoreSepia
    with Dissolve(0.5)
    
    show niviSepia at right
    with Dissolve(0.5)
    
    

    "Nivi and Theodore..."

    "Oh... {w}True."

    play music "audio/music/Stony Stony Brooke.mp3" fadein 10.0

    "They wanted me to offer something."

    me "Hi."

    show theodore shadow

    nf "Hi Fynn."

    nf "We were waiting for you."

    me "Ah ? How long ?"

    nf "Don't worry !"
    
    nf "We didn't stand here still for hours waiting for you."

    nf "You can sleep as much as you want, you're a client afterall !"

    me "..."

    menu:
        "How to respond ?"

        "Sure.":
            me "Sure."

        "Just a client ?":
            me "Just a client ?"

            nf "Hum..."

            nf "A long term one !"

            me "..."
        
        "It doesn't mean that making you wait for me is good.":
            me "It doesn't mean that making you wait for me is good."

            nf "Listen."

            nf "It's fine."
            
            nf "Don't worry."

            me "..."

            me "Ok."

    me "So ? What's the deal ?"

    nf "Well you see my daugter have some free time in her hands."

    nf "What do you think about having a guide for your first tour in the city ?"
    
    nf "And that service for only 4 coins !"

    me "Hum..."

    nf "You seems like a nice guy and you'll be staying here for a long time as you said yourself."

    nf "It would be a nice way to kill 2 birds with one stone right ?"

    me "Birds ?"

    me "How's that ?"

    nf "Well..."

    nf "If you'll live here for that long..."
    
    nf "You'll basically become like a new member of the family !"

    nf "And this is an opportunity to know the city and Nivi at the same time."

    nf "And for Nivi to know you."

    "He winked at Nivi with a smile."

    "No response."

    nf "Hopefully it kickstarts our relations in a good way."

    "Hum..."

    "The \"like\" is the most important word here."

    "Because making a family member pay their bedroom isn't what I call \"family\"."

    "Although I understand the concept."

    "But why only his daughter ?"

    "If I'm the only client, he too doesn't have much work to do."

    nf "You know..."

    nf "I would have loved coming with you but I have much work to do."

    nf "I need to help Robert with his harvesting."

    "Ok."
    
    "I got the answer."

    nf "But even if I was there, I wouldn't be much help compared to my daughter."

    nf "She knows the entire history of this city."

    nf "All the secrets and stuff."

    nf "You cannot hope for a better guide honestly."

    "..."

    nf "So what do you think ?"

    "I looked at Nivi."

    "During the entire discussion she stayed silent, looking at me."

    me "Four coins ?"

    nf "Yes."

    me "And what's the exact deal exactly ?"

    hide theodore shadow
    show theodoreSepia
    hide niviSepia
    show nivi maid basic28 brows3 eyes8 mouth7 closed mouth open eyes at right

    nivi "Until the sun is down, I'll accompany you and serve as a guide for you."

    hide theodoreSepia
    show theodore shadow
    hide nivi
    show niviSepia at right

    nf "Don't worry, she has already done this several time."

    "She nodded."

    "Hum..."

    "I often don't take shortcuts because I know I have all the time in the world."

    "But if they force themselves to me, there are no reasons to not take them."

    "I'm not crazy.{w} Not anymore."

    me "Sure then."

    me "I accept."

    me "Here the money."

    "I hand the money to Theodore.."

    nf "Perfect !"

    nf "Have fun kiddos !"

    stop music fadeout 3.0

    jump chapter2_2_the_tour