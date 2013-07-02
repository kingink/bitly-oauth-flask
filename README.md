# Bitly Oauth Python (Flask) Example


## Setup on bitly

Go to http://bitly.com/a/oauth_apps and follow the steps to register a new application.

Make sure to use your Client ID and Client Secret in index.html.erb and welcome_controller.rb.


## The files
This example is modeled after [bitly-oauth-rails](https://github.com/kingink/bitly-oauth-rails)

[templates/welcome.html](https://github.com/kingink/bitly-oauth-flask/blob/sanitize/templates/welcome.html) - Simple link that starts the authentication process.  This will take the user to a bitly login page.

[bitly_oauth.py](https://github.com/kingink/bitly-oauth-flask/blob/sanitize/bitly_oauth.py) - This is were the meat is.  After the user logs in they will be redirected back here for more of the oauth process and to get the user access token.

[templates/oauth.html](https://github.com/kingink/bitly-oauth-flask/blob/sanitize/templates/oauth.html) - Access_token and Login will show on this page.


##Links

[bitly Developer Website](http://dev.bitly.com/)

[More on bitly Authentication](http://dev.bitly.com/authentication.html)
