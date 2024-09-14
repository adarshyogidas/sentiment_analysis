# Install necessary library (uncomment if running locally)
# !pip install textblob

from textblob import TextBlob

# Sample data (can be replaced by reading a CSV or scraping data)
comments = [
    "I love the new features in this product!",
    "The service was terrible, I am not happy.",
    "I'm not sure if I like it or not.",
    "Absolutely fantastic! Best experience ever.",
    "This is the worst product I have ever used."
]

# Function to classify sentiment
def get_sentiment(comment):
    analysis = TextBlob(comment)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Apply sentiment analysis to the comments
for comment in comments:
    sentiment = get_sentiment(comment)
    print(f"Comment: {comment}")
    print(f"Sentiment: {sentiment}")
    print("-" * 50)
