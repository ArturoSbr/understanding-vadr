# Libraries
import os
from dotenv import load_dotenv

# Load api key from .env
load_dotenv()
key = os.getenv('API_KEY')

# Test
if key is not None:
    print('\nWOW it worked!!')
# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python


# import googleapiclient.discovery

# def main():
#     # Disable OAuthlib's HTTPS verification when running locally.
#     # *DO NOT* leave this option enabled in production.
#     os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

#     api_service_name = "youtube"
#     api_version = "v3"
#     key = 

#     youtube = googleapiclient.discovery.build(
#         api_service_name, api_version, developerKey = DEVELOPER_KEY)

#     request = youtube.commentThreads().list(
#         part="snippet",
#         moderationStatus="published",
#         order="time",
#         textFormat="plainText",
#         videoId="ASzOzrB-a9E",
#         fields="nextPageToken, items(snippet/topLevelComment/snippet)",
#         prettyPrint=True
#     )
#     response = request.execute()

#     print(response)

# if __name__ == "__main__":
#     main()