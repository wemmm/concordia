label scene2:

    show sebastian cheerful at left
    show concordia looking at right
    s "Anyway. Another day, another bitcoin."

    s "Let's check your website and see if anyone's made an enquiry."

    scene bg computeroff
    with pixellate

    s "What an antique."

    scene bg computeron
    with dissolve

    c "It works, though, doesn't it?"

    s "You have no flair."

    c "I can't afford flair."

    "You probably could afford to have flair if [seb_name] spent more time working and less time trading novelty sunglasses online."

    "Or if you had a real job."

    c "Hey, we have an email!"

    nvlNarrator "to: {color=#0FF}concordia.j@investigating4u.com{/color}\nfrom: {color=#0FF}mrvoctothorpe@neonsigns.biz{/color}"

    nvlNarrator "Dear Ms. Jones,"

    nvlNarrator "My name is Vasily Octothorpe and I am having a problem that appears to be of a paranormal nature."

    nvlNarrator "I found your card in an insalubrious phone box that I happened to be in last night."

    nvlNarrator "Please let me know your fees and we can arrange a meeting to discuss how to proceed."

    nvlNarrator "Vasily Octothorpe, esq."

    scene bg placeholder
    with pixellate

    show sebastian meh at left
    with easeinleft

    show concordia dubious at right
    with easeinright

    c "You've been putting the business cards in phone boxes?"

    s "You need all the help you can get."

    show sebastian cheerful at left

    s "And this guy seems to have a paranormal issue of some kind!"

    s "Isn't that supposed to be one of those things that you deal with?"

    show sebastian meh at left
    s "You know. For money."

    show concordia dubious at right
    c "You know I really don't think- {nw}"

    show sebastian cheerful at left
    s "GREAT WORK YOU'RE SO AMAZING THANK YOU SO MUCH YOU'RE SUCH A GREAT HELP AND A WONDERFUL SOCIAL MEDIA MANAGER/BRAND AWARENESS OFFICER I WILL RECOMMEND YOUR SERVICES TO A FRIEND A++++++ WOULD HIRE AGAIN MAYBE I OUGHT TO PAY YOU MORE OR AT ALL{nw}"

    s "So that's sorted. I'll email him back and find out what the deal is."

    "The situation might well be dubious, but potentially having something to investigate might not be a terrible thing."

    "But you don't really have any details yet."

    "So that means that you can let [seb_name] handle the situation, right?"

    menu:

        "Yeah, that's probably fine.":

            show concordia looking at right
            c "So..."

            c "You're handling this, right?"

            c "That means I can go out and... do something useful."

            show sebastian meh at left
            s "I guess."

            s "But I'm pretty sure you mean 'go and sulk in the park'."

            show concordia happy 1 at right
            "[seb_name] underestimates the sheer number of different places you like to sulk."

            show sebastian cheerful at left
            s "But..."

            s "Okay."

            s "Go and have an angsty inner monologue somewhere for a bit."

            s "Get it out of your system, then come back here and do some work."

            hide concordia happy 1 at right
            with easeoutright

            hide sebastian cheerful at left
            with easeoutleft

            jump scene3

        "...I'll email the guy back, [seb_name].":

            show sebastian meh at left
            s "I'm the social media manager, though."

            show sebastian cheerful at left
            s "On the other hand, it's nice to see you giving a crap about your ostensible business!"

            s "Just be polite and don't put him off, alright?"

            s "And tell him to use our hashtag."

            show sebastian smug at left
            s "{color=#0FF}#3eyeghostguy{/color}"

            c "I feel like that's potentially misleading because I'm not-{nw}"

            s "Shush."

            s "I'm going to go out and get us some coffee."

            show sebastian cheerful at left
            s "To help us {color=#04E762}W{/color}{color=#F5B700}O{/color}{color=#DC0073}R{/color}{color=#008BF8}K{/color}."

            hide sebastian cheerful at left
            with easeoutleft

            show concordia doubtful at right
            "How does he do that?"

            hide concordia doubtful at right
            with easeoutright

            jump scene3

    return
