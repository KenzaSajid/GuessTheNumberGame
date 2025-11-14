import random


def ask_int(prompt: str, min_value: int | None = None, max_value: int | None = None) -> int:
    """
    Ask the user for an integer, repeating until a valid number is entered.

    Optionally enforces minimum and/or maximum allowed values.
    """
    while True:
        raw = input(prompt).strip()

        # Check the input is an integer
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue

        # Enforce minimum and maximum if given
        if min_value is not None and value < min_value:
            print(f"Please enter a number at least {min_value}.")
            continue

        if max_value is not None and value > max_value:
            print(f"Please enter a number at most {max_value}.")
            continue

        return value


def choose_difficulty() -> tuple[int, int, int, str]:
    """
    Let the player choose a difficulty level.

    Returns:
        (low, high, max_attempts, label)
        where low/high define the secret number range,
        max_attempts is how many guesses are allowed,
        and label is the difficulty name.
    """
    print("\nChoose difficulty:")
    print("  1. Easy   (1–10, 6 attempts)")
    print("  2. Medium (1–50, 8 attempts)")
    print("  3. Hard   (1–100, 10 attempts)")

    choice = ask_int("Enter 1, 2 or 3: ", 1, 3)

    if choice == 1:
        return 1, 10, 6, "Easy"
    elif choice == 2:
        return 1, 50, 8, "Medium"
    else:
        return 1, 100, 10, "Hard"


def play_single_game() -> tuple[bool, int, str]:
    """
    Play one full round of the game.

    Returns:
        won (bool): True if the player guessed correctly, otherwise False.
        score (int): Points earned this round (0 if the player lost).
        difficulty_label (str): The difficulty level used.
    """
    low, high, max_attempts, label = choose_difficulty()
    secret = random.randint(low, high)
    attempts_used = 0

    print(f"\nI'm thinking of a number between {low} and {high}...")
    print(f"You are playing on {label} mode.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts_used < max_attempts:
        guess = ask_int(
            f"Attempt {attempts_used + 1}: your guess? ",
            min_value=low,
            max_value=high,
        )
        attempts_used += 1

        if guess == secret:
            print(f"🎉 Correct! The number was {secret}.")
            print(f"You guessed it in {attempts_used} attempt(s).\n")

            # Simple scoring: fewer attempts and larger ranges give higher scores
            base_range = high - low + 1
            score = base_range - attempts_used * 2
            if score < 1:
                score = 1
            return True, score, label

        # Give feedback
        if guess < secret:
            print("Too low.")
        else:
            print("Too high.")

        remaining = max_attempts - attempts_used
        if remaining:
            print(f"{remaining} attempt(s) remaining.\n")
        else:
            print(f"\nOut of attempts! The number was {secret}.")
            return False, 0, label


def ask_play_again() -> bool:
    """
    Ask the player whether they want to play another round.

    Returns:
        True if they want to play again, False otherwise.
    """
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")


def main() -> None:
    """
    Entry point for the Guess the Number game.

    Handles repeated rounds, basic statistics, and overall flow.
    """
    print("===================================")
    print("      Welcome to Guess the Number  ")
    print("===================================\n")
    print("Try to guess the secret number in as few attempts as possible.\n")

    total_games = 0
    total_score = 0
    best_score: int | None = None
    best_difficulty: str | None = None

    while True:
        won, score, difficulty_label = play_single_game()
        total_games += 1
        total_score += score

        if won:
            print(f"You earned {score} point(s) this round.")
            if best_score is None or score > best_score:
                best_score = score
                best_difficulty = difficulty_label
                print("New personal best score! 🎯")
        else:
            print("No points this round.")

        # Show simple statistics after each game
        print("\n--- Stats ---")
        print(f"Games played: {total_games}")
        print(f"Total score: {total_score}")
        if best_score is not None:
            print(f"Best round: {best_score} point(s) on {best_difficulty} mode")

        if not ask_play_again():
            print("\nThanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
