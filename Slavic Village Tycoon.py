import math
import random

time = 22
day = 0
villagers = 2
houses = 1
wood = 0
rating = 0
tools = True
location = "Village"
water = 16
food = 9
is_running = True


def leshy():
    global rating, location, wood

    print("\nYou are in the forest. A Leshy stands before you.")
    print("1. Give meat")
    print("2. Chop wood")
    print("3. Leave bread and milk")
    print("4. Ask for directions")

    choice = input(">> ")

    if choice == "3":
        print("The Leshy nods and guides you through a hidden path.")
        rating += 1
        wood += 5
    elif choice == "4":
        print("Leshy: 'Where is your gift?' You get lost in the mist.")
        rating -= 1
    elif choice == "1":
        print("Leshy: 'I am not a beast!' Wolves attack you. You lose supplies.")
        rating -= 1
    elif choice == "2":
        print("The forest reacts angrily. You lose your way and tools.")
        rating -= 1

    location = "Village"


def domovoy():
    global rating, tools

    print("\nYou enter a dark house. The Domovoy is here.")
    print("1. Leave porridge")
    print("2. Argue")
    print("3. Hide an item")
    print("4. Sweep the floor")

    choice = input(">> ")

    if choice == "1":
        print("The Domovoy is pleased and protects the house.")
        rating += 1
    elif choice == "4":
        print("He approves: 'I like order.'")
        rating += 1
    elif choice == "2":
        print("He gets angry. Tools stop working for 2 days.")
        rating -= 1
        tools = False
    elif choice == "3":
        print("The Domovoy is offended. You lose the item.")
        rating -= 1


def vodyanoy():
    global rating, water, food

    print("\nAt the river. The Water Spirit rises.")
    print("1. Make noise")
    print("2. Throw a coin")
    print("3. Walk away")
    print("4. Ask for fish")

    choice = input(">> ")

    if choice == "2":
        print("He accepts the coin and gives you fish.")
        rating += 1
        water += 5
        food += 3
    elif choice == "1":
        print("He creates waves. You fall into the water.")
        rating -= 1
        water = max(0, water - 3)
    elif choice == "4":
        print("He ignores your request.")
        rating -= 1


def baba_yaga():
    global rating, location

    print("\nA hut on chicken legs. Baba Yaga stands nearby.")
    print("1. Bring herbs")
    print("2. Ask for a potion")
    print("3. Run away")
    print("4. Boast about strength")

    choice = input(">> ")

    if choice == "1":
        print("She accepts and gives you a potion.")
        rating += 1
    elif choice == "2":
        print("Baba Yaga: 'Where is the payment?' She disappears.")
        rating -= 1
    elif choice == "3":
        print("You escape. The hut watches you leave.")
    elif choice == "4":
        print("She laughs: 'Strong ones burn best.' You get hurt.")
        rating -= 1

    location = "Village"


def bannik():
    global rating, location

    print("\nYou enter the bathhouse. The Bannik is here.")
    print("1. Sit on the edge shelf")
    print("2. Splash water in the corner")
    print("3. Leave soap")
    print("4. Laugh")

    choice = input(">> ")

    if choice == "3":
        print("The Bannik approves. The steam feels pleasant.")
        rating += 1
    elif choice == "1":
        print("Bannik: 'That is my place!' The steam burns you.")
        rating -= 1
    elif choice == "2":
        print("A quiet laugh is heard...")
    elif choice == "4":
        print("The steam becomes suffocating.")
        rating -= 1

    location = "Village"


def poludnitsa():
    global rating, location

    print("\nNoon in the field. The Field Spirit appears with a sickle.")
    print("1. Keep working")
    print("2. Bow and step away")
    print("3. Ask about harvest")
    print("4. Ignore her")

    choice = input(">> ")

    if choice == "2":
        print("She disappears. You are safe.")
        rating += 1
    elif choice == "1":
        print("She is angry: 'Time to rest!' You collapse.")
        rating -= 1
    elif choice == "4":
        print("Fog surrounds you. You get lost.")
        rating -= 1

    location = "Village"


def firebird():
    global rating, location

    print("\nA glowing light in the forest — the Firebird.")
    print("1. Try to catch it")
    print("2. Offer an apple")
    print("3. Just watch")
    print("4. Bow")

    choice = input(">> ")

    if choice == "4":
        print("The Firebird gives you a feather. Luck increases.")
        rating += 1
    elif choice == "2":
        print("It accepts your gift. Happiness grows in the village.")
        rating += 1
    elif choice == "1":
        print("You get burned. The bird escapes.")
        rating -= 1
    elif choice == "3":
        print("It stares back at you silently.")

    location = "Village"


def game_loop():
    print(f"\nDay {day}, {time:02d}:00 | Location: {location}")
    print(f"Villagers: {villagers}, Houses: {houses}, Wood: {wood}, Water: {water}, Food: {food}, Rating: {rating}")


def forest():
    global wood
    if random.randint(1, 9) == 1:
        leshy()
    elif random.randint(1, 9) == 2:
        baba_yaga()
    elif random.randint(1, 9) == 3:
        firebird()
    else:
        print("\nYou collected 5 wood.")
        wood += 5


def river():
    global water, food
    if random.randint(1, 5) == 1:
        vodyanoy()
    else:
        print("\nYou collected water and fish.")
        water += 5
        food += 3


def field():
    global food
    if time == 12:
        poludnitsa()
    else:
        print("\nYou collected grain.")
        food += 3


def build_house():
    global wood, houses

    if wood >= 10 and tools:
        wood -= 10
        houses += 1
        print("\nYou built a new house!")
    else:
        print("\nNot enough wood (need 10).")


def village():
    global location

    if random.randint(1, 8) == 1:
        domovoy()
    elif random.randint(1, 8) == 2:
        bannik()
    else:
        print("\n1. Go to forest")
        print("2. Go to river")
        print("3. Work in field")
        print("4. Rest")
        print("5. Build house")

        choice = input(">> ")

        if choice == "1":
            location = "Forest"
        elif choice == "2":
            location = "River"
        elif choice == "3":
            location = "Field"
        elif choice == "5":
            build_house()


while is_running:

    if time == 22:
        day += 1
        time = 7

        food -= villagers
        water -= villagers * 2

        if food < 0 or water < 0:
            print("\nYou ran out of resources. You lost.")
            is_running = False
            break
    else:
        time += 5

    if day == 30:
        if rating >= 10 and villagers >= 30:
            print("\nYou survived 1 month — YOU WIN!")
        else:
            print("\nYou survived 1 month but failed the spirits — YOU LOSE!")
        break

    if day % 3 == 0 and time == 7:
        villagers += math.floor(villagers / 2)
        print(f"\nPopulation grows! Now: {villagers}")

    if villagers / 4 > houses:
        if day % 3 == 1:
            loss = villagers - houses * 4
            villagers -= loss
            print(f"\nPeople left due to lack of houses: -{loss}")

    game_loop()

    if location == "Forest":
        forest()
        location = "Village"
    elif location == "River":
        river()
        location = "Village"
    elif location == "Field":
        field()
        location = "Village"
    elif location == "Village":
        village()

print("\nGame over. Thanks for playing!")