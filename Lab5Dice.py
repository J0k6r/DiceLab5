"""
Program Name: Lab 5 - Craps Sim
Author: Kaleb Quinn
Purpose: Roll two dice.
Date: 2026-02-15
"""

import random


def get_term(d1, d2):
    total = d1 + d2
    pair = tuple(sorted((d1, d2)))  # makes (2,1) become (1,2), etc.

    # dice-value terms
    if pair == (1, 1):
        return "Snake Eyes"
    elif pair == (1, 2):
        return "Ace Caught a Deuce"
    elif pair == (2, 2):
        return "Little Joe from Kokomo"
    elif pair in ((1, 4), (2, 3)):
        return "Little Phoebe"
    elif pair == (3, 3):
        return "Jimmy Hicks from the Sticks"
    elif pair == (1, 6):
        return "Six Ace"
    elif pair == (4, 4):
        return "Eighter from Decatur"
    elif pair in ((3, 6), (4, 5)):
        return "Nina from Pasadena"
    elif pair == (5, 5):
        return "Puppy Paws"
    elif pair == (5, 6):
        return "Six Five no Jive"
    elif pair == (6, 6):
        return "Boxcars"

    # Fallback
    return f"Total {total}"


def roll_die():
    return random.randint(1, 6)


def main():
    print("Dice Rolling Terms (Option 1)")
    print("Rolling two dice...")

    while True:
        d1 = roll_die()
        d2 = roll_die()
        total = d1 + d2
        term = get_term(d1, d2)

        print(f"\nDie 1: {d1}")
        print(f"Die 2: {d2}")
        print(f"Total: {total}")
        print(f"Term: {term}")

        choice = input("\nRoll again? (y to continue, q to quit): ").strip().lower()
        if choice == "q":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
