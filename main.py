import spotipy
import pprint
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="a5bfac740a424406bc4e29abe95f0274",
        client_secret="23ade15d2bcb4b58ab1fe403be325b81",
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
# print(user_id)
user = sp.current_user()
# print(user)
fav_song = input("Hey Lynne! Which is your Fav song now?")
artist = input("By?")
result = sp.search(q=f"track:{fav_song} artist:{artist}", type="track")
pprint.pprint(result)
songs_uri_list = []
try:
    uri = result["tracks"]["items"][0]["uri"]
    songs_uri_list.append(uri)
    print(songs_uri_list)
    playlist_name = "All Time Favs"
    # # Create a playlist
    playlist = sp.user_playlist_create(user_id, name=playlist_name, public=False)
    id = playlist["id"]
    # Add items to the playlist
    sp.playlist_add_items(playlist_id="168R1BGIOhJq043l6E6PN7", items=songs_uri_list)

except IndexError:
    print("Song not in Spotify🥺")






