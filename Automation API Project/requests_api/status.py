import requests
import requests_api

def get_status():
    return requests.get('https://simple-books-api.glitch.me/status')