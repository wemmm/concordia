label scene3:

    show concordia dubious at right
    with easeinright
    c "Okay. I can totally write a business email."

    c "Like a regular email, only boring."

    c "So..."

    label emailChoice:

menu:

    "Let's get to it, then."

    "How did Sebastian say I should write it?"

    "Politely. {i}Professionally.{/i}":

        c "Yeah, that sounds like a good idea."

        c "This is a business, after all."

        menu:

            "Keep it profesh.":

                c "Okay."

                c "I guess."

                jump emailChosen

            "Nah.":

                c "On the other hand..."

                jump emailChoice

    "...hashtagily?":

        c "Ugh."

        c "But I'm not a social media manager. I'm the talent."

        c "So..."

        menu:

            "{color=#0FF}#3eyeghostguy{/color}":

                c "I'm not-"

                c "...it's quite catchy."

                jump emailChosen

            "Nope. Nope. Can't do it.":

                c "It is an inaccurate hashtag at best."

                jump emailChoice

    "There is nothing wrong with how I would usually write an email.":

        c "I see no reason to make any particular effort here."

        menu:

            "Yeah! [seb_name] doesn't get me.":

                c "I should be my authentic self. Even when it's incongruous with our social media presence."

                c "{i}Especially{/i} when it's incongruous with our social media presence."

                jump emailChosen

            "Actually, this may not be a great idea.":

                c "'Be yourself' isn't actually good advice."

                jump emailChoice

        label emailChosen:

          c "lol placeholder"

return
