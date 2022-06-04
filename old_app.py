from flask import Flask, request, render_template, redirect, flash, session, url_for
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import time

app = Flask(__name__)

# found on spotify dashboard
client_id = '64323a9307734d05b0a1a3176db9a688'		# unique id for our app
client_secret = '9c507901fae7407dbacd4a9409d19ab8' 	# this is our super secret key
scope = "user-library-read"							# what information i can get from spotify

# config
app.secret_key='secret_key'

def create_oauth():
	return SpotifyOAuth(
		scope=scope, 
		client_id=client_id, 
		client_secret=client_secret, 
		redirect_uri=url_for('redirect_page', _external=True))

def get_token():
	token_info = session['token']			# remember we saved this token as session['token'] (its under the redirect_page func)
	if not token_info:						# token_info can expire, we will need a new one
		raise "exception"

	now = int(time.time())
	is_expired = token_info['expires_at'] - now
	if is_expired < 60:
		sp = create_oauth()
		token_info = sp.refresh_access_token(token_info['refresh_token'])
	return token_info

# every time we launch this app we will need to get oauth from spotify, and this will redirect us to "redirect_page"
@app.route('/')
def oauth():
	sp = create_oauth()						# creating a new spotify oauth
	auth_url = sp.get_authorize_url()		# redirect url
	print("AUTH_URL: ", auth_url)
	return redirect(auth_url)

# where spotify will redirect our user after oauth
@app.route('/redirect_page')			
def redirect_page():
	sp = create_oauth()
	session.clear()							# added some notes on session in the README
	code = request.args.get('code')			# getting special "code" from spotify oauth
	# print("CODE: ", code)
	token_info = sp.get_access_token(code)	# some spotipy func
	session['token'] = token_info			# saving token info in session
	# print("TOKEN_INFO: ", token_info)
	return redirect(url_for('get_tracks'))

@app.route('/get_tracks')
def get_tracks():
	liked_songs = []
	try:
		token_info = get_token()
	except:
		print("user not logged in")
		return redirect(url_for('oauth'))
		
	sp = spotipy.Spotify(auth=token_info['access_token'])
	results = sp.current_user_saved_tracks(limit=50, offset=0)
	for item in results['items']:
		track = item['track']

		artist = track['artists'][0]['name']
		song = track['name']

		liked_songs.append({'artist':artist, 'song':song})

	return render_template('get_tracks.html', liked_songs=liked_songs)

if __name__ == '__main__':
	app.run(debug=True)