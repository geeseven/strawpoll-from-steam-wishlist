import json
import requests

steam_user = "ezekiel_iii"
poll_title = "What game is next?"

# Steam uses pageanation for larger wishlists.  Each page contains 99 items.
# Hard coding only page 0 is 'ok' as strawpoll only support 30 items in a single poll.
# Here are a few different URL formats that could be used.
# https://store.steampowered.com/wishlist/profiles/76561197974046543/wishlistdata/?p=0
# https://store.steampowered.com/wishlist/id/royalgamer06/wishlistdata/?p=0
# https://store.steampowered.com/wishlist/id/ezekiel_iii/wishlistdata/?p=0

url = "https://store.steampowered.com/wishlist/id/{}/wishlistdata/?p=0".format(steam_user)


def get_wishlist(url):
    # Check to make there is not networking errors connecting to Steam
    try:
        req = requests.get(url, allow_redirects=False, timeout=(3.05, 27))
    except requests.exceptions.RequestException as e:
        return("ERROR! Could not connect to Steam, some sort of networking issue. Raw error message:\n\n{}".format(e))
    else:
        # Check to make sure we got valid json.  This will also catch non 200 replies.
        try:
            wishlist_json = req.json()
        except json.decoder.JSONDecodeError as e:
            return("ERROR! Steam did not provide valid data. Raw json error message:\n\n{}".format(e))
    return(wishlist_json)


def wishlist_games(wishlist):
    # Strawpoll only supports between 2 and 30 items.  Check to make sure the wishlist has the correct range of games.
    if 2 <= len(wishlist) <= 30:
        games = []
        for value in wishlist.items():
            games.append(value[1]['name'])
        return(games)
    else:
        return("ERROR! There is currently {} games on your wishlist.  Strawpoll only supports between 2 and 30.".format(len(wishlist)))


def make_poll(games):
    # Strawpoll API info https://github.com/strawpoll/strawpoll/wiki/API
    poll_info = {"title": poll_title, "options": games, "multi": "false"}
    try:
        poll = requests.post("https://www.strawpoll.me/api/v2/polls",
                             headers={"Content-Type": "application/json"},
                             json=poll_info,
                             timeout=(3.05, 27))
    except requests.exceptions.RequestException as e:
        return("ERROR! Could not connect to Srawpoll, some sort of networking issue. Raw error message:\n\n{}".format(e))
    else:
        # Check to make sure we got valid json.  This will also catch non 200 replies.
        try:
            poll_reply = poll.json()
        except json.decoder.JSONDecodeError as e:
            return("ERROR! Connected to Strawpoll, but could not create poll. Raw json error:\n\n{}".format(e))
    return(poll_reply)


wish_list = get_wishlist(url)
# get_wishlist() error returns str if not dict or empty list
if (type(wish_list)) is not str:
    game_list = wishlist_games(wish_list)
    # wishlist_games() error returns str if not list
    if type(game_list) is list:
        poll = make_poll(game_list)
        if type(poll) is not str:
            # print created poll
            print("https://www.strawpoll.me/" + str(poll["id"]))
        else:
            # print error creating poll
            print(poll)
    # print game list error
    else:
        print(game_list)
# print Steam error
else:
    print(wish_list)
# maybe keep a log all polls created
