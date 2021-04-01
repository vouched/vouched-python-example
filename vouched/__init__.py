from dotenv import load_dotenv
from pathlib import Path
import os
 
load_dotenv()
 
# retrieving keys and adding them to the project
# from the .env file through their key names
API_KEY = os.getenv("API_KEY")
appId = os.getenv("appId")

# api url
API_URL = 'https://verify.vouched.id/api'

config = dict(
  API_KEY=API_KEY,
  API_URL=API_URL
)



