```

▄▄▄█████▓ ██░ ██ ▓█████     ██░ ██  ▄▄▄       █    ██  ███▄    █ ▄▄▄█████▓▓█████ ▓█████▄
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓██░ ██▒▒████▄     ██  ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▒██▀ ██▌
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒██▀▀██░▒██  ▀█▄  ▓██  ▒██░▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ░██   █▌
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ░▓█ ░██ ░██▄▄▄▄██ ▓▓█  ░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ░▓█▄   ▌
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░▓█▒░██▓ ▓█   ▓██▒▒▒█████▓ ▒██░   ▓██░  ▒██▒ ░ ░▒████▒░▒████▓
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░    ▒ ░░▒░▒ ▒▒   ▓▒█░░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░ ▒▒▓  ▒
    ░     ▒ ░▒░ ░ ░ ░  ░    ▒ ░▒░ ░  ▒   ▒▒ ░░░▒░ ░ ░ ░ ░░   ░ ▒░    ░     ░ ░  ░ ░ ▒  ▒
  ░       ░  ░░ ░   ░       ░  ░░ ░  ░   ▒    ░░░ ░ ░    ░   ░ ░   ░         ░    ░ ░  ░
          ░  ░  ░   ░  ░    ░  ░  ░      ░  ░   ░              ░             ░  ░   ░    

                            █████▒██▓    ▄▄▄     ▄▄▄█████▓
                            ▓██   ▒▓██▒   ▒████▄   ▓  ██▒ ▓▒
                            ▒████ ░▒██░   ▒██  ▀█▄ ▒ ▓██░ ▒░
                            ░▓█▒  ░▒██░   ░██▄▄▄▄██░ ▓██▓ ░
                            ░▒█░   ░██████▒▓█   ▓██▒ ▒██▒ ░
                            ▒ ░   ░ ▒░▓  ░▒▒   ▓▒█░ ▒ ░░   
                            ░     ░ ░ ▒  ░ ▒   ▒▒ ░   ░    
                            ░ ░     ░ ░    ░   ▒    ░      
                            ░  ░     ░  ░        

```

## What is it now Jenny?

This is a text-based adventure game that uses [TheBroox's](https://github.com/TheBroox) [Text Adventure](https://github.com/TheBroox/TextAdventure.js) engine.

The Haunted Flat refers to chapter seven of [The Master and Margarita](https://en.wikipedia.org/wiki/The_Master_and_Margarita) by [Mikhail Bulgakov](https://en.wikipedia.org/wiki/Mikhail_Bulgakov), which I am trying to adapt into a text adventure format because that's what I feel like doing apparently. It's a really good book but this specific chapter is a decently enclosed 'scene' and I think it's probably best to start small. It's also geographically easy to grasp - as you might be able to tell from the title, it's (almost) all set inside a flat.

## How does it work?

Clone this repo and:
```
npm install
npm start
```
Then in the text box you'll see in your browser:
```
load haunted_flat
```

![intro](https://github.com/wemmm/the-haunted-flat/blob/master/intro.png)

## Okay how do I play it?

You type commands into the text parser (the lined-off section at the bottom of the window) and hope that I've been insightful enough to write a response to them.

More specifically, you'll mainly be typing verbs and objects. For example: ```look at bed``` or ```take bread```. Here's a list of verbs:

| Verb        | Usage           | Notes  |
| ------------- |:-------------|:-----|
| Look      | "look at [object]" | Works on inventory items and environmental things. |
| Take      | "take [item]"      |   Adds item to inventory. |
| Use | "use [item or object]"      | Attempts to use target. |
| Talk | "talk to [character]"   | Returns dialogue if the target has anything to say. |
| Drop | "drop [item]"  |  Removes target item from inventory. Can be picked up again. |
| Eat  | "eat [item]"      |  Attempts to eat item. Only for inventory items that seem to be food. |
| Drink  | "drink [item]"   |   Attempts to drink item. Only for inventory items that seem to be beverages. |
| Go | "go to [destination]"  | Go to the specified area. |

You can also use the command ```help``` to see this list in-game, and the command ```inventory``` to return a list of items you've picked up.

Most items referred to in the text can be looked at for further information, and in many situations you can ```look at room``` to see a list of things that can be inspected. Words that are capitalised suggest actions that will progress the scene.

## Tech:

* Node
* Express
* Javascript
* npm text-adventure

![intro](https://github.com/wemmm/the-haunted-flat/blob/master/cover.JPG)
