import random
import nltk

from nltk.sentiment import SentimentIntensityAnalyzer

def get_sentiment(sentence):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(sentence)
    compound_score = sentiment_scores['compound']
    return compound_score

def bot_response(user_input):
    user_input = user_input.lower()

    if 'bye' in user_input:
        return "Goodbye! It was nice chatting with you."
    
    if 'why' in user_input:
        return "I'm sorry, I cannot answer that question."

    if 'how' in user_input:
        return "I'm doing well, thank you! How can I assist you today?"
    
    sentiment_score = get_sentiment(user_input)
    
    if sentiment_score >= 0.5:
        return "That sounds great!"
    elif sentiment_score <= -0.5:
        return "I'm sorry to hear that."
    else:
        responses = ["Interesting.", "Tell me more.", "I'm not sure, can you elaborate?"]
        return random.choice(responses)

def chat():
    print("Bot: Hello! How can I assist you today?")
    user_input = input("You: ")
    
    while user_input.lower() != 'bye':
        response = bot_response(user_input)
        print("Bot:", response)
        user_input = input("You: ")

    print("Bot: Goodbye! It was nice chatting with you.")

