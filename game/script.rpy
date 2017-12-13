define c = Character("Concordia")
define s = DynamicCharacter("seb_name")
define nvlNarrator = Character(None, kind=nvl, what_xalign=0.5, window_xalign=0.5, what_italic=True)

init:
    style nvl_vbox:
        xfill True


# The game starts here.

label start:

    $ seb_name = "???"

    scene bg placeholder

    "You are Concordia Jones."

    scene bg cityscape
    with pixellate

    "You live in the glorious neon retro future/past."

    "The Neon District is your home."

    "The rent's pretty low on account of the fact that it's always uncomfortably brightly lit."

    "Which works well for you as you don't exactly make a huge amount of money as a paranormal detective."

    "(Or a detective who is paranormal.)"

    scene bg placeholder
    with pixellate

    show concordia pensive at right
    with dissolve

    c "Another day of solving mysteries on the mean streets of the Neon District..."

    show concordia happy 1 at right

    c "Is definitely what I would say if I had any mysteries to solve."

    show sebastian cheerful at left
    with easeinleft

    show concordia looking at right

    s "What in the name of all that is sweet and savoury?"

    s "It's already ten o'clock, Concordia. At least open the curtains or something."

    # Office background goes here when I actually have one (fade in)

    "This is your social media manager and/or brand awareness officer. He's a mostly ordinary cat, save for the fact that he's had human arms grafted on to his body."

    menu:

        "You call him..."

        "Sebastian":

            $ seb_name = "Sebastian"

            c "Hey, Sebastian."

            show sebastian meh at left
            s "It's {color=#0FF}@magical_pitchforque_1989{/color} to you. But I guess I can't expect you to remember that."

            show concordia doubtful at right
            "You have no intention of referring to him by his Chitter handle."

            jump scene2

        "Mr. Pitchforqué":

            $ seb_name = "Mr. Pitchforqué"

            c "Good morning, Mr. Pitchforqué."

            show sebastian smug at left
            s "So formal! I like it. Very on-brand."

            jump scene2

    return
