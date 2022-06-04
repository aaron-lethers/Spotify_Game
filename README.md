# Spotify_Game
Working with ID-F22 to make a Spotify game! 

WHAT I WORKED ON:

6/3:
 - Took notes on OAUTH (under spotify header)
 - started fresh, wanted to to connect to spotify's api without external lib (spotipy)
 - following: https://developer.spotify.com/documentation/general/guides/authorization/code-flow/
 	- flow chart of everything we need to connect to spotify
 - moved app.py -> old_app.py and created a new app.py
 - able to get access tokens!!!!!!!!! woo hoo!!!!!!!
 - REQUEST ACCESS TOKEN IS DONE :D

6/2:
 - i found a nice python library called "spotipy" (get it haha) which helps us connect to the spotify api
 - thru the spotipy docs, i found a way to do oauth (i think this is just spotify giving access to us (our app) to use the "users" data)
 - hopefully you can get this set up, i wrote some stuff about setting up flask and downloading the spotipy lib
 - created an email for us and used this email to create a spotify account for us to share! 
 	- we needed to create a spotify dev account to use their api
 - updated the redirect links in the spotify dashboard
 - if you run this app, hopefully you will see 'GET TRACKS' and our liked tracks on spotify (there are none lol)
 - Was following: Jason Goodison's youtube tutorial on setting this whole thing up.... its pretty much the same
 	- ended on third video at around 5 minutes.. 
 	- i tried implementing this myself, but it was pretty rough, so decided to follow a tutorial
 - I know this isnt exactly what we had in mind, but hopefully we can spin this into something more unique and our own ie our spotify game
 - Lastly, I know this is really confusing and tough, im pretty lost too, but hopefully we can stick thru it and make something :) 
 BEST OF LUCK TO YOU! HOPE EVERYTHING GOES WELL

TODO and NEXT STEPS:

6/3:
 - finish setting up the authorization
 	- refresh tokens. <- 
 - make enviornment variables

6/2:
 - finish the tutorial
 - start pulling data that we actually need for this game: ie. artist views 
 - token will expire, somehow we will need to generate a new one

____________________________________________________________________________________________________________________________________

SETTING UP REPO:
 - https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository
 - Make sure to also create your own branch to work on! 
 	- I created a branch called "aaron" that I will push code to :) 
 - I will add you as a contributor once I get your GitHub ID 

FLASK:
 - https://code.visualstudio.com/docs/python/tutorial-flask
 - Create virtual env and install flask (Do this where you github repo is located on your computer :.../Spotify_Game):
 	- python3 -m venv .venv
 	- source .venv/bin/activate
 	- python3 -m pip install flask
 	- deactivate 	# deactivate venv
 - Running app:
 	- python3 app.py
 	- copy http link and paste into browser (http://127.0.0.1:5000)
 - Config:
 	- basically a dictionary where you can add app specific information
 	- https://flask.palletsprojects.com/en/2.1.x/config/
 - Session:
 	- https://flask.palletsprojects.com/en/2.1.x/api/#sessions
 	- A session makes it possible to remember information from one request to another
 	- dont think u have to install this... i just imported it
 	- this is different from Flask-Session (i think)
 - Request vs Requests:
 	- request is a flask lib that takes in form data from a client
 	- requests is to make HTTP requests to other sites, generally APIs

SPOTIFY API:
 - https://developer.spotify.com/documentation/web-api/reference/#/
 - created a new email for us:
 	- emailforspotifyapi@gmail.com 
 	- password12#$
 - used this email to register with Spotify and created a free account for us 
 	- created a spotify account with this email, password: password12#$
 - Our spotify developer dashboard:
 	- https://developer.spotify.com/dashboard/
 	- Where you can find out appID and secret ID
 - Spotify References: all the things you can get and do with the api: 
 	- https://developer.spotify.com/documentation/web-api/reference/#/
 - Updated Spotify Dashboard with our redirect links
 	- currently redirecting to 'home.html'
 	- you can see these if you click "edit settings" in our spotify dashboard (first gotta click our project "Spotify_game")
 - OAUTH2.0:
 	- Authorization vs authentication:
 		- Authentication: process of a user proving its owenership of a presented identity, generally by providing a username and password
 		- Authorization: process of letting a subject access resources after a successful authentication. 
 			- OAUTH -> authorization, deals with API calls. We are asking spotify for us to access their resources. 
 			- Metaphor: OAUTH is similar to a car's valet key. Given to a valet to temporarily drive and park the car. The valet does not own the car
 						but is allowed to use the car (resources) while given access. 
	- Framework, not a protocol
	- Uses HTTPS (HTTPS is a secure way to send data between a web server and a web browser)
	1. Authorization process requires valid client_id and client_secret (found on dashboard).
	2. Once authorization is granted, the authorization server (spotify) issues an access token. This is used to make API calls on behalf of the 	   user or application (our app!)
	- https://developer.spotify.com/documentation/general/guides/authorization/code-flow/ <- great doc, primarily followed this 

<---- NOT BEING USED ---->
SPOTIPY:
 - https://spotipy.readthedocs.io/en/2.19.0/#
 - python library for the spotify web api! 
 - To install (do this in your venv):
 	- pip install spotipy --upgrade
 - SpotifyOAuth: not quite sure what this object does, but i think it makes a connection to the spotify api


