from flask import Flask
import requests

app = Flask(__name__)


@app.route('/search/<token>/<q>')
def do_search(token, q):
    url = 'https://api.spotify.com/v1/search'
    params = {'q': q, 'type': 'track,artist', 'limit': 15}
    return request_spotify(url, params, token)


@app.route('/artist_top/<token>/<artist_id>')
def get_artist_top(token, artist_id):
    url = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks'
    params = {'country': 'BR'}
    return request_spotify(url, params, token)


@app.route('/related_artists/<token>/<artist_id>')
def get_related_artists(token, artist_id):
    url = f'https://api.spotify.com/v1/artists/{artist_id}/related-artists'
    return request_spotify(url, {}, token)


@app.route('/get_artist/<token>/<artist_id>')
def get_artist(token, artist_id):
    url = f'https://api.spotify.com/v1/artists/{artist_id}'
    return request_spotify(url, {}, token)


@app.route('/get_user/<token>')
def get_user(token):
    url = 'https://api.spotify.com/v1/me'
    return request_spotify(url, {}, token)


def request_spotify(url, params, token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, params=params, headers=headers)
    return response.json()


"""
if __name__ == "__main__":
    app.run(debug=True)
"""
