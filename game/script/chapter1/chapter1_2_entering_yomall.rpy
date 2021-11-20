label chapter1_entering_yomall:

    "..."
    
    play music "audio/ambient/Forest.ogg"

    scene bg forest twilight
    with Dissolve(3.0)
    

    "I finally see the wall of the city."

    "I reached my destination."
    
    "Nice."

    "All this walking for days..."
    
    "Not a single event to distract me..."
    
    "I shall now enjoy the warmth of a fresh bed."

    "The sun is almost down. It was about time."

    stop music fadeout 5.0

    scene bg gate twilight
    with dissolve

    "At the gate, I am stopped by a guard. I let him check the stuff in my bag and he let me pass."

    "Weird.{w} Even though the city is completly lost in the middle of the mountains, they still are that vigilant huh?"

    "And those walls..."

    "What are they protecting the city from ?"
    
    "Well...{w} Seems nice to be a citizen here."

    play music "audio/ambient/Bustling Town Ambience.ogg" fadein 3.0 volume 0.5

    scene bg city twilight
    with dissolve
    
    "Entering in the city, I am immediately lost. I try to remember the sayings of my 'old friend."

    define ol = Character("Old Friend", who_color="#964B00")

    ol "{i}The inn is next to the gate. You have to take the street to your right then the second to your left.{/i}"

    "I hope, I remember well enough."

    "..."

    "He was right, I see the sign. This should be \"{i}The [inn_name]{/i}\"."

    stop music fadeout 2.0

    "I push the door."

    play sound "audio/sfx/Door Open.ogg"

    jump chapter1_flashback_ol_grave