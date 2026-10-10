#greet.py
import time

class userGreeter:
    def __init__(self):
        user_file = open("user_profile","r")
        profile = {}
        for x in user_file:
            profile[x.partition(':')[0]] = x.partition(':')[2].strip()
        self.fname = profile["firstName"]
        self.sname = profile["sureName"]
        self.age = profile["age"]
        self.gender = profile["gender"]
        user_file.close()
    def greetings(self):
        if time.localtime().tm_hour < 3:
            print("Are you a night owl",end="")
        elif time.localtime().tm_hour < 6:
            print("The Early Riser",end="")
        elif time.localtime().tm_hour < 12:
            print("Good morning",end="")
        elif time.localtime().tm_hour < 16:
            print("Good afternoon",end="")
        else:
            print("Night",end="")
        print(f", {self.fname}")

user = userGreeter()
user.greetings()

