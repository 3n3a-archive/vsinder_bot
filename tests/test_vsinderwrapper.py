from vsinderwrapper import API
import vcr

@vcr.use_cassette('tests/vcr_cassettes/me-info.yml')
def test_me_info():
    """Tests an API call to get the users info"""

    api_instance = API(
        access_token = "your_access_token",
        cookie = "__cfduid=your_cookie",
        refresh_token = "your_refresh_token",
        ua = "VSinder/1.2.19 CFNetwork/1209 Darwin/20.2.0"
    )
    response = api_instance.me()

    assert isinstance(response, dict)
    assert response['user']['id'] == "your_use_id"

@vcr.use_cassette('tests/vcr_cassettes/feed-users.yml')
def test_feed_users():
    """Tests the API call to get the Feed of users"""

    api_instance = API(
        access_token = "your_access_token",
        cookie = "__cfduid=your_cookie",
        refresh_token = "your_refresh_token",
        ua = "VSinder/1.2.19 CFNetwork/1209 Darwin/20.2.0"
    )
    response = api_instance.feed()

    print(response['profiles'][0]['id'])

    assert isinstance(response, dict)
    assert response['profiles'][0]['age'] >= 1

@vcr.use_cassette('tests/vcr_cassettes/like-users.yml')
def test_like_users():
    """Tests the API call to like a user"""

    api_instance = API(
        access_token = "your_access_token",
        cookie = "__cfduid=your_cookie",
        refresh_token = "your_refresh_token",
        ua = "VSinder/1.2.19 CFNetwork/1209 Darwin/20.2.0"
    )
    response = api_instance.view(Liked=True, UserId="a_user_id")

    assert isinstance(response, dict)
    assert response['ok'] == True

@vcr.use_cassette('tests/vcr_cassettes/matches.yml')
def test_matches():
    """Tests the API call to get the matches"""

    api_instance = API(
        access_token = "your_access_token",
        cookie = "__cfduid=your_cookie",
        refresh_token = "your_refresh_token",
        ua = "VSinder/1.2.19 CFNetwork/1209 Darwin/20.2.0"
    )
    response = api_instance.matches(0)

    assert isinstance(response, dict)