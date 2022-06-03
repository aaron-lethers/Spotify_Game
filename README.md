# Spotify_Game
Working with ID-F22 to make a Spotify game! 

WHAT I WORKED ON:
 - hey! so im gonna call it today, i made a little progress and i think i will call it here.
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

SPOTIPY:
 - https://spotipy.readthedocs.io/en/2.19.0/#
 - python library for the spotify web api! 
 - To install (do this in your venv):
 	- pip install spotipy --upgrade
 - SpotifyOAuth: not quite sure what this object does, but i think it makes a connection to the spotify api



NOTES:
 - its quite confusing and i dont understand it fully. found some tutorils, watched some vids, copied some code. 


