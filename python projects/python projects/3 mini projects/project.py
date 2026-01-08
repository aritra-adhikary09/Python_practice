# fake news project
# pending task is to modify it with verious features.
import random
subjects = ["suisei",
           "miko",
           "matsuri",
           "marin",
           "mio",
           "azki"]

actions = ["wakaranai",
           "uta ga tokui baso",
           "nandemo dekichau",
           "dekinai",
           "takai tokoro",
           "in desuka?"
           ]
places = ["tokyo",
            "osaka",
            "kyoto",
            "narita",
            "saitama",
            "hakone",]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)

    headline = f" BREAKING NEWS: {subject} {action} {place}"

    print("\n" + headline)

    user = input("Do you want another news? (yes/no): ").strip().lower()
    
    if user == "no":
        break

print("Thanks for using this website. have fun making fake news!")
   
