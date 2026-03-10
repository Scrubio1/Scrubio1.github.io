#Create phrase guessing game where the player has to guess a phrase by guessing letters. The player has a limited number of guesses and the game should display the current state of the phrase after each guess.
import random   
def get_random_phrase():
    phrases = ["Administration for Community Living", "Beneficiary Contact", "State Health Insurance Assistance Program", "State Health Insurance Assistance Program Tracking and Reporting System", "Senior Medicare Patrol", "Medicare Fraud Hotline", "Medicare Fraud Prevention Tool", "Medicare Fraud Prevention Tool Training", "Medicare Fraud Prevention Tool User Guide", "Medicare Fraud Prevention Tool Video Tutorials"]
    return random.choice(phrases)
def display_phrase(phrase, guessed_letters):
    display = ""
    for letter in phrase:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()
def play_game():
    phrase = get_random_phrase()
    guessed_letters = set()
    attempts = 6
    print("Welcome to the Phrase Guessing Game!")
    while attempts > 0:
        print("\nPhrase: " + display_phrase(phrase, guessed_letters))
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        guessed_letters.add(guess)
        if guess in phrase:
            print("Good guess!")
        else:
            attempts -= 1
            print("Wrong guess! Attempts left: " + str(attempts))
        if all(letter in guessed_letters for letter in phrase):
            print("\nCongratulations! You've guessed the phrase: " + phrase)
            break
    else:
        print("\nGame Over! The phrase was: " + phrase)