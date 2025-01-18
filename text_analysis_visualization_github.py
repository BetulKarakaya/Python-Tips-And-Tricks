import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
import string

# Ensure nltk resources are downloaded
nltk.download('stopwords')
nltk.download('vader_lexicon')

def preprocess_text(text):
    """
    Preprocess the input text by removing punctuation, converting to lowercase,
    and filtering out stopwords.
    """
    stop_words = set(stopwords.words('english'))
    translator = str.maketrans('', '', string.punctuation)
    
    # Remove punctuation and convert to lowercase
    clean_text = text.translate(translator).lower()
    
    # Remove stopwords
    words = [word for word in clean_text.split() if word not in stop_words]
    return words

def generate_wordcloud(word_freq):
    """
    Generate and display a word cloud from word frequencies.
    """
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud", fontsize=16)
    plt.show()

def plot_word_frequencies(word_freq):
    """
    Plot the top 10 most common words and their frequencies.
    """
    most_common = word_freq.most_common(10)
    words, counts = zip(*most_common)

    plt.figure(figsize=(8, 6))
    plt.bar(words, counts, color='skyblue')
    plt.title("Top 10 Most Common Words", fontsize=16)
    plt.xlabel("Words", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def analyze_sentiment(text):
    """
    Analyze the sentiment of the input text and display the results.
    """
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)

    labels = ['Positive', 'Neutral', 'Negative']
    sizes = [sentiment['pos'], sentiment['neu'], sentiment['neg']]
    colors = ['pink', 'yellow', 'lightgreen']

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    plt.title("Sentiment Analysis", fontsize=16)
    plt.show()

def main():
    print("Welcome to the Text Analysis and Visualization Program!")


    text = (
        "Text analysis, or text mining, extracts meaningful insights from unstructured data like emails, social media, and articles. "
        "Common applications include sentiment analysis to gauge emotions in customer feedback and topic modeling to identify themes in large datasets."
        "Techniques such as tokenization, stemming, and lemmatization are often used to process text. Advanced tools like natural language processing (NLP) and machine learning enable deeper pattern recognition and classification."
        "In the era of big data, text analysis helps organizations make informed decisions by uncovering valuable insights hidden in text."
    )

    print("\nOriginal Text:\n", text)

    # Preprocess text
    words = preprocess_text(text)

    # Analyze word frequencies
    word_freq = Counter(words)

    # Generate visualizations
    generate_wordcloud(word_freq)
    plot_word_frequencies(word_freq)

    # Sentiment analysis
    print("\nPerforming Sentiment Analysis...")
    analyze_sentiment(text)
    print("Analysis complete! Thank you for using the program.")

if __name__ == "__main__":
    main()
