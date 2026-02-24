# This program is a number guessing game
# Computer picks a random number between 1 and 100
# User gets 7 attempts to guess it

import random  # used to generate random number

best_score = None  # to store minimum attempts used

while True:  # game loop for play again

    secret_number = random.randint(1, 100)
    attempts_left = 7
    attempts_used = 0

    print("\n=== Number Guessing Game ===")
    print("Guess a number between 1 and 100")

    while attempts_left > 0:
        user_guess = int(input("Enter your guess: "))
        attempts_used += 1
        attempts_left -= 1

        # checking guess
        if user_guess == secret_number:
            print("🎉 Correct! You guessed the number.")
            print("Attempts used:", attempts_used)

            # updating best score
            if best_score is None or attempts_used < best_score:
                best_score = attempts_used
                print("⭐ New best score!")

            break

        elif user_guess > secret_number:
            print("Too high!")

        else:
            print("Too low!")

        # hint if close within 5
        if abs(user_guess - secret_number) <= 5:
            print("🔥 Very close!")

        print("Attempts remaining:", attempts_left)

    else:
        # runs if loop ends without break
        print("❌ You lost! The number was:", secret_number)

    # showing best score if exists
    if best_score is not None:
        print("Best score (minimum attempts):", best_score)

    # asking to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing 👋")
        break