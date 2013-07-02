import os
import requests
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def welcome():
  return render_template('welcome.html')

@app.route('/oauth/')
def oauth():
  code = request.args.get('code')
  client_id = 'YOUR_CLIENT_ID'
  client_secret = 'YOUR_CLIENT_SECRET'
  redirect_uri = 'YOUR_REDIRECT_URI'

  payload = {'client_id': client_id, 'client_secret': client_secret, 'redirect_uri': redirect_uri, 'code': code}
  r = requests.post("https://api-ssl.bitly.com/oauth/access_token", data=payload)

  data = {}
  pairs = r.text.split('&')
  for pair in pairs:
    k, v = pair.split('=')
    data[k] = v

  return render_template('oauth.html', login=data['login'], access_token=data['access_token'])

if __name__ == '__main__':
  app.run()
