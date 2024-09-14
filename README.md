Sentiment Analysis using TextBlob

Objective:
To classify a list of comments into Positive, Negative, or Neutral based on their sentiment using TextBlob.

Implementation:

Libraries Used:

textblob: For sentiment analysis.
Steps:

Define Comments:
A sample list of comments is used for sentiment analysis.

Sentiment Classification:
The get_sentiment function analyzes the polarity of each comment. Positive, neutral, or negative labels are assigned based on polarity values.

Design Choices:

TextBlob was chosen for its simplicity and ease of use in extracting sentiment without needing deep learning models.
The polarity threshold is intuitive, where polarity > 0 is positive, polarity = 0 is neutral, and polarity < 0 is negative.
Challenges Faced:

TextBlob’s sentiment analyzer works well for English text, but for more complex text or non-English, performance can be limited.
