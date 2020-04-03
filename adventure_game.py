import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("\nYou find yourself in a dark DUNGEON!"
                "It is DARK and COLD!!!")
    print_pause("You cannot remember, how you came here..")
    print_pause("You find a dagger on the floor and take it!\n")
    print_pause("There are two passageways in front of you.")


def door_opening(item, option):
    print_pause("\nWhich door do you want to open?\n")
    print_pause("Enter 1 to open the first door!\n"
                "Enter 2 to open the second door!\n")
    while True:
        door = input("(Please enter '1' or '2'.)\n")
        if door == "1":
            first_door(item, option)
            break
        elif door == "2":
            second_door(item, option)
            break


def first_door(item, option):
    print_pause("\nYou are opening the first door!")
    print_pause("Out of the door steps a giant " + option + ".")
    print_pause("The " + option + " attacks you!\n")
    print_pause("Do you want to (1) fight or (2) run away?\n")
    while True:
        task = input("(Please enter '1' or '2'.)\n")
        if task == '1':
            fight(item, option)
            break
        elif task == '2':
            run(item, option)
            break


def fight(item, option):
    if "weapon" in item:
        print_pause("\nThe " + option + " sees"
                    "your sword and runs in the desert!")
        print_pause("You are free!")
    else:
        print_pause("\nYou do your best...")
        print_pause("But your dagger is not enough!\n\n")
        print_pause("GAME OVER!\n\n")
    play_again()


def run(item, option):
    print_pause("\nYou close the door and are back in the DUNGEON!")
    door_opening(item, option)


def second_door(item, option):
    print_pause("\nYou are opening the second door!\n")
    if "weapon" in item:
        print_pause("You have been here before, and gotten all the"
                    "good stuff. It's just an empty room now.\n")
    else:
        print_pause("There is no one behind that door!")
        print_pause("But you can find a sword on the floor!")
        print_pause("You take the sword with you and discard your"
                    "silly old dagger!\n")
        item.append("weapon")
    print_pause("You leave the room and go back to the DUNGEON!")
    door_opening(item, option)


def play_again():
    play = input("Would you like to play again? (y/n)\n").lower()
    if play == "y":
        print_pause("\nGood luck for another game!\n")
        play_game()
    elif play == "n":
        print_pause("\nThanks for playing! See you next time.\n")
    else:
        play_again()


def play_game():
    item = []
    option = random.choice(["dragon", "pirate", "troll", "gorgon"])
    intro()
    door_opening(item, option)


play_game()
