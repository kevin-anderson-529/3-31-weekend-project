# Spotify Access Token
import requests
import base64

client_id = '6733de16c17d451a9be1b236a3533f08'
client_secret = 'dfbc05a30d0148ef890cd36f673ffdc0'

auth_url = 'https://accounts.spotify.com/api/token'
auth_headers = {
    'Authorization': f'Basic {base64.b64encode((client_id + ":" + client_secret).encode()).decode()}',
    'Content-Type': 'application/x-www-form-urlencoded'
}
auth_data = {
    'grant_type': 'client_credentials'
}
response = requests.post(auth_url, headers=auth_headers, data=auth_data)
response_data = response.json()
access_token = response_data['access_token']

print(f"Your access token is: {access_token}")