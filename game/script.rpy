init python:
    renpy.music.register_channel("longvoice", "voice", False)

# Effects

define uncensored = True


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define syl = Character("Unknown Girl", who_color="#B4F8C8")

define tob = Character("Unknow Man", who_color="#964B00")

define me = Character("Narrator")

define um = Character("Unknow Man", who_color="#FFFFFF")

define ol = Character("Unknow Man", who_color="#FFFFFF")

define nivi = Character("?", image="nivi shadow", who_color="#771b22")

define nf = Character("Nivi\'s Father")

define city_name = "Yomall" # iomallach Scottish Gaelic

define inn_name = "Forpaw" # Quatrepatte en anglais

define hero_name = "Fynn"

define hero_longname = "Sceite" # Irish

define city_capital_name = "Mioja" # Centre en Icelandic


# The game starts here.

label start:

    # TEST STARTER

    jump chapter1_flashback_ol_leaving

    #jump prologue
    
return


# REDUIRE TAILLE DU JEU