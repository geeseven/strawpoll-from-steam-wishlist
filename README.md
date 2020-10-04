# strawpoll-from-steam-wishlist

Create a [Straw Poll][0] with games from a Steam user's wishlist via a cli script or a [Flask][1] web application.  If the wishlist has between 2 and 30 items, a poll will get created.  If not, an error message is displayed. The Straw Poll title and Steam user are configured by `poll_title` and `steam_user` in each file.

## CLI
```console
$ python make-poll-cli.py
['Rust', 'Oxygen Not Included', 'Warhammer: Vermintide 2', 'Legends of Aria', 'Age of Wonders: Planetfall', 'Project Winter', 'Total War: THREE KINGDOMS', 'Cliff Empire', 'Metal Wolf Chaos XD']
https://www.strawpoll.me/18827739
```

## Flask

```console
$ env FLASK_APP=make-poll-flask.py flask run
 * Serving Flask app "make-poll-flask.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [04/Oct/2020 16:35:58] "GET / HTTP/1.1" 200 -
```

```console
$ curl http://127.0.0.1:5000/ 
<title>poll maker</title>ERROR! There is currently 71 games on your wishlist.  Strawpoll only supports between 2 and 30.
```

[0]: https://www.strawpoll.me/
[1]: https://palletsprojects.com/p/flask/
