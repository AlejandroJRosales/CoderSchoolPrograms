"""
A personal assitant that answers the users questions!
"""
import time


hour = int(time.strftime("%H"))

# say good morning if it is morning, afternoon if it is the afternoon, and
# night if it is the night
# remember this time is in army time
if 5 < hour < 12:
    print("Good morning!")
elif 12 <= hour < 20:
    print("Good afternoon!")
else:
    print("Hello, late is it not?")

# get the users name
# you can get the user name or hard code this variable if you want
user_name = input("Would you mind telling me you name?\n> ")
print(f"Welcome, {user_name}")

# run this part of the code till the user stops it
while True:
    # get the users query
    # we use .lower() function so that the user can type out Time or time
    # and the personal assitant will see it as the same thing. in short
    # so it is not case sensitive
    user_input = input(f"\nHow can I be of assitance {user_name}?\n> ").lower()

    # important to note we do not use == but instead "in" because
    # the in allows for the user to use a wider range of sentence then hard
    # coded sentences like "what is the time" and "tell me the time"

    # if the user asks for the time
    if "time" in user_input:
        # the hour will be military time
        # if you want it to be non-military time then uncomment the following
        # line of code
        # hour %= 12
        # we use '' for strftime here because it messes up the f-string if we
        # use " or /
        print(f"The current time is {time.strftime('%H:%M:%S')}")

    elif "dad joke" in user_input:
        answer = "nacho cheese"
        joke_input = input("What type of cheese isn't yours?\n> ").lower()
        if joke_input == answer:
            print("Exactly!")
        else:
            print(f"{answer}!")

# there we go, the ground work of the program, go ahead and add your own
# stuff now!

# maybe add in a timer
# maybe add in email sender
