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

                $ email = "profesh"

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

                $ email = "hashtag"

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

                $ email = "authentic?"

                jump emailChosen

            "Actually, this may not be a great idea.":

                c "'Be yourself' isn't actually good advice."

                jump emailChoice

        label emailChosen:

            show concordia happy 1 at right

            c "Hah."

            c "Totally did some work."

            if email == "profesh":

                c "In a suitably professional manner."

                c "Because I'm a young and dynamic entepreneur!"

                show concordia dubious at right
                c "..."

            if email == "hashtag":

                c "In a... like... on-brand way?"

                c "{color=#0FF}#3eyeghostguy{/color}!"

                c "I should be an internet raconteur."

                "You wonder if you can get paid to be witty on the internet."

                show concordia dubious at right
                c "Is that how [seb_name] makes a living?"

                "Basically, yes."

            if email == "authentic?":

                c "I'm living my truth!"

                c "It probably isn't a good idea!"

                c "Whatever!"

            c "So that's that done."

            "You wonder if there's any other work-like stuff you could do."

            "Sebastian probably won't be back for a little while on account of his extremely complicated coffee order."

            menu:

                "Well...":

                    c "It's not that I'm suspicious, but..."

                    c "I mean, we don't really get emails very often."

                    "You don't really get much business at all, actually, so it's probably a reasonable thing to be suspicious of."

                    c "I think I should probably look this guy up."

                    c "I'm a detective, after all!"

                    c "Not an internet detective, but still. Growth mindset."

                    jump googling

                "No.":

                    c "Nope."

                    c "I did something already."

                    c "So now I'm going to lie down on the sofa."

                    jump procrastinating

            label googling:

                scene bg computeron
                with pixellate

                c "Vasily Octothorpe, huh?"

                c "Not much here... is it a real name?"

                c "...a poetry website?"

                c "Ew."

                $ whoIsVasily = "beat poet"

                jump scene8

            label procrastinating:

                "You lie down on the sofa."

                "It's been quite a challenging day. You need to gather your strength."

                $ whoIsVasily = "a mystery"

                jump scene8

return
