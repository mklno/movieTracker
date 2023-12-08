import os
from dotenv import load_dotenv

load_dotenv()
import requests

url = "https://api.themoviedb.org/3/search/movie?query=Hana%20and%20Alice&include_adult=false&language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": os.environ.get("APITOKEN")
}

response = requests.get(url, headers=headers)

print(response.text)
