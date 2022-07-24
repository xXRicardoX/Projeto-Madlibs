# # string concatenationn (aka how tto putt strings together)
# # suppose we want to create a string that says "subscribe to _____"
# youtuber = "ricardo f. de carvalho" # some string variable
#
# # a few ways tto do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjetive: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}!. It makes me so excited all the time because \n \"" \
          f"I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"




print(madlib)