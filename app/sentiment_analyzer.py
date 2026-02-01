"""
Sentiment Analyzer Module
=========================
This module handles NLP preprocessing and sentiment analysis using VADER sentiment analyzer.
Provides comprehensive text preprocessing including tokenization, stemming, and lemmatization.

"""

import nltk
import ssl
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import re
from typing import Dict, List, Tuple
import string

# Handle SSL certificate verification issues
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Download required NLTK data
try:
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

try:
    nltk.data.find('punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('wordnet')
except LookupError:
    nltk.download('wordnet')

try:
    nltk.data.find('averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger')


class SentimentAnalyzer:
    """
    Sentiment Analysis class using VADER (Valence Aware Dictionary and sEntiment Reasoner)
    
    VADER is specifically optimized for social media text and works well with:
    - Emoticons
    - Slang
    - Informal language
    - Multi-word expressions
    """
    
    def __init__(self):
        """Initialize the sentiment analyzer with NLTK tools"""
        self.sia = SentimentIntensityAnalyzer()
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        
    def preprocess_text(self, text: str) -> Tuple[str, List[str], List[str]]:
        """
        Preprocess the input text for sentiment analysis
        
        Steps:
        1. Lowercase conversion
        2. URL removal
        3. Special character handling
        4. Tokenization
        5. Stopword removal
        6. Stemming and Lemmatization
        
        Args:
            text (str): Raw input text
            
        Returns:
            Tuple containing:
            - processed_text (str): Cleaned and processed text
            - tokens (List[str]): Tokens after preprocessing
            - lemmatized_tokens (List[str]): Lemmatized tokens
        """
        # 1. Convert to lowercase
        text = text.lower()
        
        # 2. Remove URLs
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        
        # 3. Remove email addresses
        text = re.sub(r'\S+@\S+', '', text)
        
        # 4. Remove special characters but keep important punctuation
        text = re.sub(r'[^\w\s.!?,-]', '', text)
        
        # 5. Handle multiple spaces
        text = re.sub(r'\s+', ' ', text).strip()
        
        # 6. Tokenization
        tokens = word_tokenize(text)
        
        # 7. Remove stopwords (optional - keeping for context preservation)
        filtered_tokens = [token for token in tokens if token not in self.stop_words]
        
        # 8. Stemming
        stemmed_tokens = [self.stemmer.stem(token) for token in filtered_tokens]
        
        # 9. Lemmatization
        lemmatized_tokens = [self.lemmatizer.lemmatize(token) for token in filtered_tokens]
        
        processed_text = ' '.join(lemmatized_tokens)
        
        return processed_text, stemmed_tokens, lemmatized_tokens
    
    def analyze(self, text: str) -> Dict:
        """
        Analyze sentiment of the given text
        
        Uses VADER sentiment analyzer which returns:
        - positive: proportion of text that is positive
        - negative: proportion of text that is negative
        - neutral: proportion of text that is neutral
        - compound: normalized composite sentiment score (-1 to 1)
        
        Classification:
        - compound >= 0.05: POSITIVE
        - compound <= -0.05: NEGATIVE
        - -0.05 < compound < 0.05: NEUTRAL
        
        Args:
            text (str): Input text to analyze
            
        Returns:
            Dict containing:
            - sentiment: str ('positive', 'negative', or 'neutral')
            - scores: dict with sentiment probabilities
            - processed_text: str with preprocessed text
            - confidence: float indicating confidence level
        """
        if not text or not text.strip():
            return {
                'sentiment': 'neutral',
                'scores': {
                    'positive': 0.0,
                    'negative': 0.0,
                    'neutral': 1.0,
                    'compound': 0.0
                },
                'processed_text': '',
                'confidence': 0.0
            }
        
        # Get VADER sentiment scores
        scores = self.sia.polarity_scores(text)
        
        # Determine sentiment based on compound score
        compound = scores['compound']
        
        if compound >= 0.05:
            sentiment = 'positive'
            confidence = scores['pos']
        elif compound <= -0.05:
            sentiment = 'negative'
            confidence = scores['neg']
        else:
            sentiment = 'neutral'
            confidence = scores['neu']
        
        # Preprocess the text
        processed_text, _, _ = self.preprocess_text(text)
        
        return {
            'sentiment': sentiment,
            'scores': {
                'positive': round(scores['pos'], 4),
                'negative': round(scores['neg'], 4),
                'neutral': round(scores['neu'], 4),
                'compound': round(scores['compound'], 4)
            },
            'processed_text': processed_text,
            'confidence': round(confidence, 4)
        }
    
    def analyze_sentences(self, text: str) -> List[Dict]:
        """
        Analyze sentiment of individual sentences
        
        Useful for understanding which parts of the text are positive/negative
        
        Args:
            text (str): Input text containing multiple sentences
            
        Returns:
            List of dictionaries containing sentence-level sentiment analysis
        """
        sentences = sent_tokenize(text)
        results = []
        
        for sentence in sentences:
            if sentence.strip():
                result = self.analyze(sentence)
                results.append({
                    'sentence': sentence,
                    'sentiment': result['sentiment'],
                    'scores': result['scores']
                })
        
        return results
    
    def get_key_sentiments(self, text: str) -> Dict:
        """
        Extract key sentiment indicators from text
        
        Identifies words/phrases that strongly influence sentiment
        
        Args:
            text (str): Input text
            
        Returns:
            Dict with keywords and their sentiment contributions
        """
        _, stemmed, lemmatized = self.preprocess_text(text)
        
        positive_words = []
        negative_words = []
        
        positive_indicators = {
            'good', 'great', 'excellent', 'amazing', 'love', 'wonderful',
            'fantastic', 'brilliant', 'happy', 'perfect', 'best'
        }
        
        negative_indicators = {
            'bad', 'terrible', 'awful', 'hate', 'horrible', 'worst',
            'ugly', 'sad', 'poor', 'worst', 'annoying'
        }
        
        for word in lemmatized:
            if word in positive_indicators:
                positive_words.append(word)
            elif word in negative_indicators:
                negative_words.append(word)
        
        return {
            'positive_indicators': list(set(positive_words)),
            'negative_indicators': list(set(negative_words)),
            'key_positive_count': len(set(positive_words)),
            'key_negative_count': len(set(negative_words))
        }
    
    def compare_sentiments(self, texts: List[str]) -> Dict:
        """
        Compare sentiment across multiple texts
        
        Args:
            texts (List[str]): List of texts to compare
            
        Returns:
            Dict with comparative analysis
        """
        results = []
        total_compound = 0
        
        for text in texts:
            result = self.analyze(text)
            results.append(result)
            total_compound += result['scores']['compound']
        
        avg_compound = total_compound / len(texts) if texts else 0
        
        return {
            'results': results,
            'average_compound_score': round(avg_compound, 4),
            'total_texts': len(texts),
            'positive_count': sum(1 for r in results if r['sentiment'] == 'positive'),
            'negative_count': sum(1 for r in results if r['sentiment'] == 'negative'),
            'neutral_count': sum(1 for r in results if r['sentiment'] == 'neutral')
        }
