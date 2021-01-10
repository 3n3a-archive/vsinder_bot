from .session import SESSION as s

class API(object):
    "The Instance for the VSINDER API"
    
    def __init__(self, access_token, refresh_token, cookie, ua):
        """This initalizes the requests session from .session and adds these headers needed for auth"""
        headers = {
            'access-token': access_token,
            'refresh-token': refresh_token,
            'User-Agent': ua,
            'Cookie': cookie
        }
        self.session = s(headers)

    def me(self):
        """This Endpoint returns Info on the User itself."""
        url = "https://api.vsinder.com/me"
        response = self.session.get(url)
        return response.json()

    def feed(self):
        """This Endpoint returns the feed which is expected to be swiped through by the user"""
        url = "https://api.vsinder.com/feed"
        response = self.session.get(url)
        return response.json()

    def view(self, Liked, UserId):
        """This Endpoint "swipes" on a given UserID"""
        url = "https://api.vsinder.com/view"
        response = self.session.post(url, {"liked": Liked, "userId": UserId})
        return response.json()

    def matches(self, page):
        """This Endpoint returns the feed which is expected to be swiped through by the user"""
        url = "https://api.vsinder.com/matches/{}".format(str(page))
        response = self.session.get(url)
        return response.json()

    def send_message(self, match_id, rec_id, text):
        """This Endpoint sends messages to a given user on the app"""
        url = "https://api.vsinder.com/message"
        return self.session.post(url, {"matchId": match_id, "recipientId": rec_id, "text": text})

    def get_messages(self, id):
        """This Endpoint returns the DM Messages from an ID, IDK what ID tho"""
        url = "https://api.vsinder.com/messages/{}".format(str(id))
        response = self.session.get(url)
        return response.json()
