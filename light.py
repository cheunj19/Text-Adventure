print("\n")
print("     *Light in the Dark*")
print("  (a text-based adventure)")
print("\n")

def Cave ():
    print ("\n")
    print ("You have walked through the snow to the cave.")
    print ("As you walk in through its mouth, a big bear appears! You have unknowingly wandered into its den.")
    print ("It chases you out of the cave. When you are finally able to distance yourself, you find yourself in a valley.")
    print ("At the end of the valley is a forest.")
    vat = int (input ("Press 1 to continue."))
    if (vat == 1):
        Dragon ()

def Dragon ():
    print ("\n")
    print ("You are now travelling through the forest.")
    print ("Things are going smoothly until suddenly...")
    print ("A huge dragon appears!")
    vam = int (input("Press 1 to fight. Press 2 to try to make peace."))
    if (vam == 1):
        print ("\n")
        print ("You try to fight the dragon,")
        print ("but you die because you are a mere weak mortal.")
        print ("GAME OVER")
      #BARGAIN WITH DRAGON
    if (vam == 2):
        Success ()

def Success ():
        print ("\n")
        print ("You tell the dragon that you are wearing an old family necklace.")
        print ("The necklace has a big, valuable, pretty gem.")
        print ("You offer this necklace in exchange for the dragon's help.")
        print ("The dragon accepts and reveals that it knows where the orb of Light is.")
        print ("It flies you to the remote island with the orb.")
        print ("Congratulations! You have saved the day!")







start = True
while(start == True):
    #character selection
    print("Choose your character!")
    print("(1) Knight  (2) Sorceress  (3) Princess")
    num = int(input("Enter the number of your choice:"))
    name = input("Name your character:")
    print("\n")

    #character names
    if(num == 1):
        char = "Knight " + str(name)
    if(num == 2):
        char = "Sorceress " + str(name)
    if(num == 3):
        char = "Princess " + str(name)



        #backstory
    print("Your kingdom is in danger!")
    print("The Dark is poised to consume everything and everyone you love.")
    print("However, your land does not despair, for there is still hope!")
    print("Legend tells of an enchanted orb, the weapon capable of vanquishing the Dark with Light.")
    print("It is up to you, " + char + ", to retrieve the Light and save your realm!")
    vap = int(input ("Press 1 to continue."))
    if (vap == 1):
        print ("\n")
        print ("You have begun your journey!")
        print ("Oh no. There is a fork in the road. Which way will you go?")
        print ("The left path leads to the mountains.")
        print ("The right path leads to the forest.")

        choice = int (input("Press 1 for left. Press 2 for right."))
        #MOUNTAINS
        if (choice == 1):
            print ("\n")
            print ("You are now travelling through the mountains.")
            print ("After walking for 2 days, a blizzard makes continuing impossible.")
            print ("You need to find shelter!")
            print ("You see a small hut in the distance, and a cave in the other direction.")
            val = int (input("Press 1 for the hut. Press 2 for the cave."))
            #HUT
            if (val == 1):
                print ("\n")
                print ("You have walked through the snow to the hut.")
                print ("Living in the hut is a man who lets you stay.")
                print ("You are given a nasty surprise when he tries to attack you at night! ")
                print ("You manage to escape and resort to hiding in the cave.")
                Cave ()
                break
            if (val == 2):
                Cave ()
                break
        		#FOREST
        elif (choice == 2):
            Dragon ()
            restart = str (input("Return to start? (Enter 'y' or 'n')"))
            if (restart == "y"):
                start = True
            if (restart == "n"):
                break
