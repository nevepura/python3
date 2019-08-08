print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == '1':
    print("I don't really wanna do this game anymore. Quitting")

elif door == '2':
    print("You found the Magic Rabbit. He wants something from you. What do you give him?")
    print('(carrots | gold | dick)')
    gift = input("> ")
    if gift == 'carrots':
        print('How many carrots will you give him?')
        carrots = int(input('> '))
        if carrots in range(0,3):
            print("The rabbit is still hungry. He cryes.")
        elif carrots in range(3,10):
            print("The rabbit eats greedily. He looks satisfied.")
        elif carrots > 10:
            print("Too many carrots. He eats only a few.")

    elif gift == 'gold':
        print("The rabbit is rich now. He doesn't need to do magic.")
    elif gift == 'dick':
        print("The rabbit isn't interested in interracial.")
    else:
        print("You probably mispelled. The rabbit gets angry and kills you.")

else:
    print("There is only 2 door. You stupidity is neverending.")