"""
Name: Alex Perez
Last updated: 06/17/2026
Description: This program is to write your own story and choose your own adventure!
"""

def adventure():
    """ This function runs one session of a choose your own adventure.
        Arguments: None
        Returns: None (Printed text is not returned)
    """

    print()

    print("Welcome, worthy adventurer, to The Swamp,")
    print("home to Ally the Golden Gator and sourdough bread!")

    print()

    player_name, player_class = create_player()

    print()
    
    while player_class not in ("Warrior", "Mage"): 
        player_class = input("I don't recognize that class. Please choose either Warrior or Mage. ")

    if player_class == "Warrior":
        health = 100
        mana = 50
        print("A brave warrior, ready to confront any challenge.")
    else:
        health = 50
        mana = 100
        print("A cunning mage, capable of outwitting the strongest foe.")

    print()

    print("Here are your beginning stats:")
    print("Health: {}".format(health))
    print("Mana: {}".format(mana))

    print()

    print(player_name, "your quest is to rescue Ally from the Spartans")
    print("who hold her captive.")
    print("Let us begin...")

    print()

    # Add branches to the adventure here!
    while True:
           print()
           print("You face to 2 paths one is a forest and the other is a village")
           print()
           decision1 = input("Which path do you want to take? [Forest / Village]")
           #Decision1 is the first decision the player makes to choose what path they take.
           while decision1 not in ("Forest", "Village"): #Creates a loop to ensure the player chooses a valid path.
               decision1 = input("Choose a valid path. [Forest / Village]")

           #Decison 1: Forest
           if decision1 == "Forest": 
               print()
               print("You enter the forest and you see a wild bear! Do you want to fight it or run away?")
               print()
               decision2 = input("What do you want to do? [Fight / Run]")
               #Descision2 determines what the player decides to do
               while decision2 not in ("Fight", "Run"): #Creates a loop to ensure the player chooses a valid path.
                   decision2 = input("Choose a valid path. [Fight / Run]")
               if decision2 == "Fight":
                    if player_class == "Warrior":
                       print()
                       print("You bravely fight the bear and defeat it! But you lost mana and health.")
                       health -=20
                       mana -=10
                    else: 
                        print()
                        print("You cast a spell and defeat the bear!. But you almost lost all your mana and health.")
                        health -=40
                        mana -=80

                    print()
                    print("Your current health is {} and your current mana is {}".format(health, mana))
                    print()
                    print("You continue on your journey and find Ally!. You win!")
                    return 1

               else:
                    print("You run away you escaped cowardly you. Game over!")
                    return 0
            #Decision 1: Village
           elif decision1 == "Village":
               print()
               print("You enter the village and you see a house with a wide open door. Enter or keep walking?")
               print()
               decision3 = input("What do you want to do? [Enter / Keep Walking]")
               #Decision3 Player dicides to enter the house or keep walking
               while decision3 not in ("Enter", "Keep Walking"): #Creates a loop to ensure the player chooses a valid path.
                   decision3 = input("Choose a valid path. [Enter / Keep Walking]")
               if decision3 == "Enter":
                    print()
                    print("You Enter the house and find Ally! You win!")
                    print()
                    return 1
               elif decision3 == "Keep Walking":
                   print()
                   print("You keep walking and got lost in the village. Game over!)")
                   return 0
                    
                       
    return 0


def create_player():
    """ Prompts the user for their name and class.
        Arguments: None
        Returns:
            - player_name (string): Name of the player
            - player_class (string): Class of the player
    """

    player_name = input("Before we begin, what should I call you? ")
    player_class = input("What is your specialty? [Warrior / Mage] ")

    return player_name, player_class

win = 0
while win == 0:
    win = adventure()