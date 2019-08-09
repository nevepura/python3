from sys import exit


def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input('> ')
    
    if '0' in choice or '1' in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print('Not greedy, you win.')
        exit(0)
    else:
        dead('You took too much money, and you die overburdened.')
    
def bear_room():
    print('''
    There is a bear here.
    He's got a lot of money.
    The fatbear is in front of another door.
    How are you going to move the bear?
    ''')

    bear_moved = False

    while True:
        print("(take honey | taunt bear | open door)")
        choice = input('> ')

        if choice == "take honey":
            dead("The bear looks at ou and eats you instead")
        elif choice == 'taunt bear' and not bear_moved:
            print("The bear has moved from the door, you can go trough it now")
            bear_moved = True
        elif choice == 'taunt bear' and bear_moved:
            dead("The bear gets pissed and eats you")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("what are you talkin about?")
def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    print("(flee | head )")
    choice = input("> ")

    if "flee" in choice:
        start()

    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()   

def dead (reason):
    print(reason, "Good job")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()