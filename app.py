from flask import Flask, request, render_template, redirect, flash, session, url_for
import base64
import json
import requests

app = Flask(__name__)

"""
ENVIORNMENT VARS:
# found on spotify dashboard

scope = "user-library-read"							# what information i can get from spotify
state = 'je73hcyejwkdjen6'							# random 16 char str (i just typed 16 random letters)
url = 'https://accounts.spotify.com/authorize?'
"""
state = 'je73hcyejwkdjen6'
redirect_uri = 'http://127.0.0.1:5000/redirect_page'
client_id = '64323a9307734d05b0a1a3176db9a688'		# unique id for our app
client_secret = '9c507901fae7407dbacd4a9409d19ab8' 	# this is our super secret key

"""
Request authorization from user to access data
Requires: response_type, client_id, scope, redirect_uri, state

"""
@app.route('/')
def req_auth():
	url = 'https://accounts.spotify.com/authorize?'

	auth_info = [
		'response_type=code',
		'client_id=64323a9307734d05b0a1a3176db9a688',
		'scope=user-library-read',
		'redirect_uri=' + redirect_uri,
		'state=' + state
	]

	query = url + '&'.join(auth_info)
	# print("QUERY: ", query)
	resp = requests.get(url=query)
	print('RESP: ', resp)

	return redirect(query)

"""
Request access and refresh tokens
Requires: client_id, client_secret, grant_type, code, redirect_uri

"""
@app.route('/redirect_page')
def redirect_page():
	code = request.args.get('code')
	print('CODE: ', code)
	res_state = request.args.get('state')
	print('STATE: ', state)

	if res_state != state:
		# flash message
		return redirect(url_for('req_auth'))
	else:
		if not code:
			error = request.args.get('error')
			print("User did not accept access: ", error)
			# implement flash message
			return redirect(url_for('req_auth'))

	userpass = client_id + ':' + client_secret
	encoded = 'Basic ' + base64.b64encode(userpass.encode('utf-8')).decode('utf-8')
	url = 'https://accounts.spotify.com/api/token'
	data = {
		'code': code,
		'redirect_uri': redirect_uri,
		'grant_type': 'authorization_code'
	}
	headers = {
		'Authorization': encoded
	}

	resp = requests.post(url=url, data=data, headers=headers).json()
	# print(resp)

	return render_template('redirect_page.html')

if __name__ == '__main__':
	app.run(debug=True)