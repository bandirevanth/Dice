import random


# We'll track counts of roll outcomes in a 13-element list.
# The first two indices (0 & 1) are ignored, leaving just
# the indices that match the roll values (2 through 12).
freq = [0] * 13


# Display intro text
print("\n                   Dice")
print("Creative Computing  Morristown, New Jersey")
print("\n\n")
# "Danny Freidus"
print("This program simulates the rolling of a")
print("pair of dice.")
print("You enter the number of times you want the computer to")
print("'roll' the dice.   Watch out, very large numbers take")
print("a long time.  In particular, numbers over 5000.")

still_playing = True
while still_playing:
    print("")
    n = int(input("How many rolls? "))

    # Roll the dice n times
    for i in range(n):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_total = die1 + die2
        freq[roll_total] += 1

    # Display final results
    print("\nTotal Spots   Number of Times")
    for i in range(2, 13):
        print(" %-14d%d" % (i, freq[i]))

    # Keep playing?
    print("")
    response = input("Try again? ")
    if len(response) > 0 and response.upper()[0] == 'Y':
        # Clear out the frequency list
        freq = [0]*13
    else:
        # Exit the game loop
        still_playing = False
