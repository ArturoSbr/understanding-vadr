# Import libraries
from googleapiclient.discovery import build

# Function to scrape comments
def getComments(apiKey=None, videoId=None):
    
    # Build youtube instance
    youtube = build(serviceName='youtube', version='v3', developerKey=apiKey)

    # Build fields
    token = 'nextPageToken'
    author = 'items(snippet/topLevelComment/snippet/authorDisplayName)'
    comment = 'items(snippet/topLevelComment/snippet/textOriginal)'
    date = 'items(snippet/topLevelComment/snippet/publishedAt)'

    # Declare request
    req = youtube.commentThreads().list(
        part='snippet',
        moderationStatus='published',
        order='time',
        textFormat='plainText',
        videoId=videoId,
        fields=', '.join([token, author, comment, date]),
        prettyPrint=True,
        maxResults=50
    )

    # Send request
    res = req.execute()

    # Extract comments
    comments = res['items']

    # Store nextPageToken
    try:
        npt = res['nextPageToken']
    except:
        npt = None

    # Iterate through subsequent pages
    while npt is not None:
        # Buid another request
        req = youtube.commentThreads().list(
            part='snippet',
            moderationStatus='published',
            order='time',
            textFormat='plainText',
            videoId=videoId,
            fields=', '.join([token, author, comment, date]),
            prettyPrint=True,
            maxResults=15,
            pageToken=npt
        )

        # Send request
        res = req.execute()
        
        # Update nextPageToken
        try:
            npt = res['nextPageToken']
        except:
            npt = None

        # Add new comments
        comments = comments.append(res['items'])

    # Return response
    return comments

# Execute program
if __name__ == '__main__':
    main()