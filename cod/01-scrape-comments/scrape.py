# Libraries
import os
import json
from dotenv import load_dotenv
from comments import getComments

# Load api key from .env
load_dotenv()
key = os.getenv('API_KEY')

# Get 5K comments from BF2042 trailer
c = getComments(apiKey=key, videoId='ASzOzrB-a9E', limit=5000)

# Export file
json.dump(c, open('dat/bf2042.json', 'w'))