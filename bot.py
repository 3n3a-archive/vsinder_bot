from vsinderwrapper import API
import random
from time import sleep

class Main():

    def __init__(self):

        self.api = API(
            access_token = "your_access_token",
            cookie = "__cfduid=your_cookie",
            refresh_token = "your_refresh_token",
            ua = "VSinder/1.2.19 CFNetwork/1209 Darwin/20.2.0"
        )

        self.feed = self.api.feed()

    def like_all(self):

        for profile in self.feed['profiles']:
            rand_boolean = bool(random.getrandbits(1))

            response = self.api.view(Liked=rand_boolean, UserId=profile["id"])

            if response['match']:
                match_status = "MATCHED"
            else:
                match_status = "did NOT MATCH"

            if rand_boolean:
                like_status = "Liked"
            else:
                like_status = "Cancelled"
                
            print("{} {} and {}".format(like_status, profile["displayName"], match_status))

            sleep(random.randint(0, 20)/10)

    def message_matches(self):
        for match in self.api.matches(0)['matches']:
            if match['message'] == None: # could also be: match['read'] == False
                self.api.send_message(match['matchId'], match['userId'], "Hey there :)")
                print("Messaged {}".format(match["displayName"]))

def main():
    while True:
        print("Started Script!\nThis script is endless.. you can quit by hitting CTRL + C\n")
        a = Main()
        a.like_all()
        a.message_matches()
        sleep(random.randint(0, 6000)/10)

def test_messages():
    a = Main()
    a.message_matches()

if __name__ == "__main__":
    main()
