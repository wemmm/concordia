# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Concordia")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg placeholder

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show concordia

    # These display lines of dialogue.

    "You are Concordia Jones."

    scene bg cityscape
    with fade

    "You live in the glorious neon retro future/past."

    "The neon district is your home."

    "The rent's pretty low on account of the fact that it's always uncomfortably brightly lit."

    "Which works well for you as you don't exactly make a huge amount of money as a paranormal detective."

    "(Or a detective who is paranormal.)"

    scene bg placeholder
    with fade

    show concordia pensive

    c "Another day of solving mysteries on the mean streets of the Neon District..."

    show concordia happy 1

    c "Is definitely what I would say if I had any mysteries to solve."

    return
