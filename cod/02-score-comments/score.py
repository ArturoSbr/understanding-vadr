# Libraries
import json
import pandas as pd
import langid
from vaderSentiment import vaderSentiment

# Load model
m = vaderSentiment.SentimentIntensityAnalyzer()

# Load data
d = json.load(open('dat/bf2042.json', 'r'))

# Initialize empty list
l = []

# Iterate through nested dictionaries
for comment in d:
    # Extract comment
    comment = comment.get('snippet').get('topLevelComment').get('snippet')
    text = comment.get('textOriginal')

    # Check if comment is english
    lang = langid.classify(text)[0]
    
    # Skip non-english texts
    if lang != 'en':
        continue
    
    # Score text and fetch negative score
    score = m.polarity_scores(text).get('neg')

    # Append to list
    l.append(list(comment.values()) + [score])

# Data to dataframe
df = pd.DataFrame(data=l, columns=['comment','author','date','score'])

# Export dataframe
df.to_csv('dat/scored_comments.csv', index=False)