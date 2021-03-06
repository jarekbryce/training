import random, easygui

secret = random.randint(1, 99)
guess = 0
tries = 0

easygui.msgbox("""AHOY!  I'm the dread Pirate Roberts, and I have a secret!
It is a number from 1 to 99.  I'll give you 5 tries to guess it.""")

while guess != secret and tries < 5:
    guess = easygui.integerbox("What's yer guess, matey?")
    if not guess: break
    if guess < secret:
        easygui.msgbox(str(guess) + " is too low, ye scurvy dog!")
    elif guess > secret:
        easygui.msgbox(str(guess) + " is too high, landlubber!")
    tries = tries + 1

if guess == secret:
    easygui.msgbox("Avast! Ye got it! Found my number you did!")
else:
    easygui.msgbox("You be out of guesses. Better luck next time!")
