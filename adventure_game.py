import time
import random


def start():
    item_character = []
    character = ''
    item_character = ["Priate", "Troll", "Gorgon"]
    i = random.randint(0, 2)
    character = item_character[i]
    print_pause("You find yourself standing in an")
    print_pause("open field, filled with grass",)
    print_pause("and yellow wildflowers.")
    print_pause("Rumor has it that a " + character + " is")
    print_pause("somewhere around here,")
    print_pause("and has been terrifying the nearby.")
    print_pause("village. In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty")
    print_pause("(but not very effective) dagger.")

    main(character)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def win_lose():
    print_pause("GAME OVER")


def play_again():
    response = input("Would you like to play again?(y/n)")
    if response == "y":
        print("Excellent! Restarting the game ...")
        items.clear()
        start()
    elif response == "n":
        print_pause("Ok Goodbye!")
    else:
        print_pause("Please enter (y/n)")
        play_again()


def fight(character):
    # Things that happen when the player fights
    if "sword" in items:
        print_pause("As the " + character + "moves to attack,")
        print_pause("you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in")
        print_pause("your hand as you brace yourself for the attack.")
        print_pause("But the " + character + "takes one look")
        print_pause("at your shiny new toy and runs away!")
        print_pause("You have rid the town of " + character + ".")
        print_pause("You are victorious!")
        win_lose()
        play_again()

    elif "sword" not in items:
        print_pause("The " + character + " attacks you!")
        print_pause("You feel a bit under-prepared for this,")
        print_pause("with only having a tiny dagger.")
        play_game(character)
        win_lose()
        play_again()


def cave(character):
    # Things that happen to the player goes in the cave
    if "sword" not in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and")
        print_pause("take the sword with you.")
        items.append("sword")
        field(character)
    elif "sword" in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and")
        print_pause("gotten all the good stuff. It's just an empty cave now.")
        field(character)


def field(character):
    # Things that happen when the player runs back to the field
    print_pause("You go back to the field.")
    main(character)


def house(character):
    # Things that happen to the player in the house
    print_pause("You approach the  " + character + "'s door of the house.")
    print_pause("You are about to knock when the door")
    print_pause("opens and out steps a " + character + ".")
    print_pause("Eep! This is the " + character + "'s house!")
    fight(character)


def main(character):
    print_pause("Enter 1 to knock on the door of the house.\n")
    print_pause("Enter 2 to peer into the cave.\n")
    choice = input("Please enter 1 or 2")
    if choice == "1":
        house(character)
    elif choice == "2":
        cave(character)
    else:
        print_pause("(Please enter 1 or 2)")
        main(character)


def play_game(character):
    print_pause("Would you like to (1) fight or (2) run away?")
    choice = input("Please enter 1 or 2")
    if choice == "1":
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the " + character + ".")
        print_pause("You have been defeated!")

    elif choice == "2":
        field(character)

    else:
        print_pause("Please enter 1 or 2")
        play_game(character)


items = []
start()
