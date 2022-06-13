"""
File: assignment5and6.py
Author: Joshua Ellis

Purpose: Text based adventure game.

# Above and Beyond completed.
"""
def gametext(words):
    print(f"\n\n\n{words}\n\n\n")
def display(health, mana, gold):
    print(f"Health:{health:^6d} Mana:{mana:^6d} Gold:{gold:^6d}")

    # Set terminal height to 12 lines for the best experience.


def game(health, mana, gold):


    gametext("\n\nWelcome to the newest Adventure Game!\n\n")
    name = input(f"What name will you give your character? ")
    display(health,mana,gold)
    gametext(f"Welcome to the game {name}!\nYou are a Dwarf who is trying to find treasure inside of a cave.\nYou come upon a branch in the caves. Two options are present,\nLeft and Right?")
    option1 = input(f"What is your decision? Left or Right? ")
    if option1.lower() == "left":
        health = health-1
        display(health,mana,gold)
        gametext(f"You decided to go left. Little did you know there was a spider in this direction, and you HATE spiders.\nYou lose 1 health because you jump away from the spider and hit the wall.\n\nYou see a splitting path, Your options are Up, centeral, or down.")
        loop1 = input(f"Which do you choose? ")
        if loop1.lower() == "up":
            display(health,mana,gold)
            gametext(f"\nYou decide to go up! When you do, you end up just climbing out of the dungeon completely.\nSomeone sees you and you are dranded a coward all your days. That really sucks.\n")
            return 0
        elif loop1.lower() == "central":
            display(health,mana,gold)
            gametext(f"\nYou decide to pursue the central path! When you do, You find a papers. What is on them? Oh no!\nIt is a homework assignment and you forgot to study! You rush home and forget\nthat you were supposed to finish the dungeon in the cave.")
            return 0
        elif loop1.lower() == "down":
            display(health,mana,gold)
            gametext(f"\nYou decide to go down! When you do, You find a skeleton! How will you decide to take it on? Will you\npunch it, or use your battleaxe?\n")
            loop2 = input(f"Your choice (punch or battleaxe)? ")
            if loop2.lower() == "punch":
                display(health,mana,gold)
                gametext(f"You decide to punch the thing in the freaking face! You wind up your arm and filng it forward.\nNot such a bright idea becaues the skeleton is made of some pretty hard bone. You feel\nyour hand crunch and wonder why its bone beat your bone in this wierd rock paper scissors.\nSadly, you black out and wake up at home, having been saved by someone else.")
                return 0
            elif loop2.lower() == "battleaxe":
                display(health,mana,gold)
                gametext(f"You decide to use your battleaxe!(Like a true Dwarf) You wind up and swing it forward and slam it into the skull of the skeleton and hear\nthe cracking and breaking of bones. You stand triumphant and continue, stepping over some useless paper as you climb from the hole, realizing you\nback at the beginning, you now head right down the original path. Will you use magic to light the way?")
            else:
                gametext(f"Sorry, but that was not a choice! You lose!")
                return 0
        else:
            gametext(f"Sorry, but that was not a choice! You lose!")
            return 0
    elif option1.lower() == "right":
        gold = gold + 10
        display(health,mana,gold)
        gametext(f"You decided to go right. Upon walking a few feet you get tired and lean against the wall.\nThe wall moves, having been a pressure plate, and opens a hole in the wall, Revealing 10 gold!\n You hurridly take it and put it in your pouch. The path ahead is dark. Will you use magic to light the way?\n")
    else:
        gametext(f"Sorry, but that was not a choice! You lose!")
        return 0
    option2 = input(f"Yes or no? ")
    if option2.lower() == "yes":
        mana = mana - 1
        gold = gold + 10
        display(health,mana,gold)
        gametext(f"With a flicker of sparks, a flame comes forth from your hand and you see that directly in front of you\nis a large hole. Imagine what could have happened had you chosen to not use magic! You walk forward\nand see the 10 gold on the ground! A little ahead, There is an Ogre in front of you. Will you blast it away with magic,\nor use your words?")
    elif option2.lower() == "no":
        health = health - 1
        display(health,mana,gold)
        gametext(f"You choose to save your mana and walk forward. Instantly you regret your decision as you fail to feel\nany solid ground under your foot as you put all your weight behind it. You get up and brush off\nthe dirt from your scraped knee and walk forward. You continue, squinting and slowly progressing through the darkness,\nwhen you happen to bump into an ogre. Will you use magic to put this Ogre in it's place, or will you insult it with your superior words?")
    else:
        gametext(f"Sorry, but that was not a choice! You lose!")
        return 0
    option3 = input(f"Words or Magic? ")
    if (option1.lower() == "right") and (option2.lower() == "yes") and (option3.lower() == "words"):
        gold = gold - 20
        health = health - 4
        display(health,mana,gold)
        gametext(f"You try to use your words... Bad choice! (it is an ogre after all) The Ogre listens for about three\nseconds and then charges you, knocking you back. As you hit the ground, you hear your coins fly from\nyour pocket, and You run from the cave, not wanting to stay longer.\n")
    elif (option1.lower() == "right") and (option2.lower() == "yes") and (option3.lower() == "magic"):
        gold = gold - 10
        mana = mana - 2
        display(health,mana,gold)
        gametext(f"You decide to use Magic. You have been on a roll today, You are 20 gold coins up and you feel GOOD.\nYou cast a lightening spell on the Ogre, who then brushes it off and throws a stone at your unprotected face.\n You fall back and hear coins fall from your pouch as you get up and sprint from the dungeon with a bloody nose.\n")
    elif (option1.lower() == "right") and (option2.lower() == "no") and (option3.lower() == "words"):
        display(health,mana,gold)
        gametext(f"You try to use your words... Nice! After having a kinda bad day scraping your knee, you complain and\ngrumble, which the Ogre seems to understand. He lets you pass without hurting you, and you leave the\n dungeon.\n")
    elif (option1.lower() == "right") and (option2.lower() == "no") and (option3.lower() == "magic"):
        mana = mana - 3
        display(health,mana,gold)
        gametext(f"You do not wish for this day to be any worse, so you decide to use magic on the Ogre. You summon the\nmagic within you and blast the Ogre with a supercharged frost spell, which leaves it frozen in place.\n You walk past the Ogre as it is helpless to do anything but watch as you leave the dungeon victorious.\n")
    elif (option1.lower() == "left") and (option2.lower() == "no") and (option3.lower() == "words"):
        gold = gold + 400
        display(health,mana,gold)
        gametext(f"You. Are. Done. You have had it with stupid stuff happening today. You tell the ogre all you wanted to do was impress\nyour father (the nobleman) and prove to him that you were more a man than he was (He could never complete\nthe dungeon) The Ogre lowers his rock and you see him puch on a secret portion of the wall. Inside is a mountain\nof gold from other adventurers and he tells you to take it all and rub it in your fathers face. Today was an absolute win!!!")

    else:
        health = 0
        mana = 0
        gold = 0
        display(health,mana,gold)
        gametext(f"\nLong story short... You kinda died. That spider combined with seeing an ogre just kinda killed you. The ogre took everythign you\nhad (even your shoes).")







health = 5
mana = 3
gold = 0
game(health, mana, gold)

