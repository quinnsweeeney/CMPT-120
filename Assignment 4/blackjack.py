#if you don't know how to play blackjack, tbh not super important but look it up anyway LOL
#this script is going to require some googling: I want you to practice using your resources with this one. But of course if you get stuck, reach out :)
'''instructions: randomly generate three values between 1 and 11. in the function bust: add these three numbers together. if they add up to or less than 21, return the sum. If it's over 21, return 0. If it's over 21 BUT there's an 11 as one of the values, return the sum - 10. '''

import random
def bust():

    x = random.randint(1, 11)
    y = random.randint(1, 11)
    z = random.randint(1, 11)

    total = x + y + z

    if total <= 21:
        return total

        # If the total is over 21, check if there is an 11 and adjust the total accordingly
    if total > 21:
        if x == 11 or y == 11 or z == 11:
            return total - 10
        else:
            return 0


def main():

    main()
