import random


def get_valid_guess(min_value: int, max_value: int) -> int:
    """
    Ask the player for a guess and keep asking until they enter a valid integer.

    Returns:
        int: The player's guess between min_value and max_value (inclusive).
    """
    while True:
        raw = input(f"Enter your guess ({min_value}-{max_value}): ").strip()
        if not raw:
            print("Please type a number, not an empty answer.")
            continue

        if not raw.isdigit():
            print("That doesn't look like a whole number. Try again.")
            continue

        guess = int(raw)
        if guess < min_value or guess > max_value:
            print(f"Your guess must be between {min_value} and {max_value}.")
            continue

        return guess


def play_round(min_value: int = 1, max_value: int = 100, max_attempts: int = 10) -> None:
    """
    Play a single round of the guessing game.

    The computer chooses a random number and the player has a limited
    number of attempts to guess it. After each guess, the player is told
    whether the guess was too high or too low, and how many attempts remain.
    """
    secret = random.randint(min_value, max_value)
    attempts_used = 0

    print("\nI'm thinking of a number between "
          f"{min_value} and {max_value}.")
    print(f"You have {max_attempts} attempts to find it.\n")

    while attempts_used < max_attempts:
        remaining = max_attempts - attempts_used
        print(f"Attempt {attempts_used + 1} of {max_attempts} "
              f"(you have {remaining} attempt(s) left).")

        guess = get_valid_guess(min_value, max_value)
        attempts_used += 1

        if guess == secret:
            print(f"\n🎉 Correct! The number was {secret}.")
            print(f"You found it in {attempts_used} attempt(s).\n")
            return
        elif guess < secret:
            print("Too low!\n")
        else:
            print("Too high!\n")

    # If we reach here, the player has run out of attempts
    print("❌ You've used all your attempts.")
    print(f"The correct number was {secret}.\n")


def ask_play_again() -> bool:
    """
    Ask the player if they want to play another round.

    Returns:
        bool: True if the player wants to play again, False otherwise.
    """
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer with 'y' or 'n'.")


def main() -> None:
    """
    Entry point for the Guess the Number game.

    Repeats rounds until the player chooses to stop.
    """
    print("🎲 Welcome to the Guess the Number Game! 🎲")

    while True:
        play_round()

        if not ask_play_again():
            print("\nThanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()

