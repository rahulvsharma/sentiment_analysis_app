# Sentiment Analysis Application - Assignment 2 - Problem Statement 10

### Group ID: 61

### Group Members Name with Student ID:

1. Arpita Singh (2024AA05027) Contribution 100%
2. Rahul Sharma (2024AA05893) Contribution 100%
3. Sachit Pandey (2024AA05023) Contribution 100%
4. Avishek Ghatak (2024AA05895) Contribution 100%
5. Anoushka Guleria (2023AA05527) Contribution 100%

## What We Built

We created a web-based app that can analyze text and figure out whether the emotion behind it is positive, negative, or neutral. It's basically a tool that reads what someone writes and determines the sentiment. The app has a clean interface with different ways to input text and shows detailed analysis results.

## Features

### 1. Web Interface

- **Text Input Tab**: You can type or paste text directly and get instant sentiment analysis
- **File Upload Tab**: Upload a .txt file and the app analyzes all the text inside
- **Batch Analysis Tab**: Analyze up to 50 texts at the same time (useful for comparing multiple sentiments)
- **Instant Results**: You get the sentiment classification right away with color coding
- **Visual Feedback**: Green = positive, Red = negative, Orange/Gray = neutral
- **Mobile Friendly**: Should work on phones and tablets too

### 2. Sentiment Analysis

- **NLTK VADER Model**: We used NLTK's VADER (which stands for Valence Aware Dictionary and sEntiment Reasoner) - it's a good pre-built tool for analyzing sentiment
- **Text Preprocessing**: We clean the text first by tokenizing it, removing stop words, stemming, and lemmatization
- **Confidence Scoring**: The results show how confident the model is (based on how strong the sentiment score is)
- **Works Well with Informal Text**: VADER is actually pretty good at understanding casual language, slang, and informal writing

### 3. Visualization

- **Score Charts**: We show pie charts and bar charts so you can visually see how much positive/negative/neutral is in the text
- **Sentiment Gauge**: A nice visual gauge that shows where the sentiment leans (positive, negative, or neutral)
- **Confidence Indicator**: Shows how confident the model is about its prediction

## Technology Stack

- **Backend**: Flask (Python web framework - super lightweight and easy to use)
- **NLP**: NLTK library with the VADER sentiment analyzer
- **Frontend**: HTML5, CSS3, and plain JavaScript (no heavy frameworks)
- **Charts**: Chart.js for showing data visualizations
- **Python**: Version 3.12.6

## Project Structure

```
submission/
├── app/
│   ├── app.py                          # Main Flask application
│   ├── sentiment_analyzer.py           # NLP sentiment analysis module
│   ├── requirements.txt                # Python dependencies
│   ├── templates/
│   │   └── index.html                  # Web interface
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css              # Styling and layout
│   │   └── js/
│   │       └── script.js              # Frontend interactivity
│   └── data/
│       └── (sample data files)         # For testing
├── RUNNING_INSTRUCTIONS.md             # How to run the application
├── DESIGN_REPORT.md                    # Design choices and challenges
├── SCREENSHOTS.md                      # Application flow screenshots
├── TASK_B_ENHANCEMENT.pdf              # Enhancement plan document
└── LITERATURE_SURVEY.pdf               # Literature review on cross-domain sentiment
```

## How It Works

### Sentiment Analysis Process

1. **Input Reception**: User enters text or uploads a file through the web interface
2. **Text Preprocessing**:
   - Convert to lowercase
   - Remove URLs and emails
   - Remove special characters
   - Tokenize into words
   - Remove stop words
   - Apply stemming and lemmatization
3. **VADER Analysis**: NLTK VADER analyzes the preprocessed text
4. **Classification**:
   - Positive: compound score ≥ 0.05
   - Negative: compound score ≤ -0.05
   - Neutral: -0.05 < compound score < 0.05
5. **Result Display**: Sentiment label and confidence score shown to user

### Sentiment Scoring

- **Compound Score**: Ranges from -1.0 (most negative) to 1.0 (most positive)
- **Component Scores**: Negative, neutral, and positive proportions that sum to 1.0
- **Confidence**: Absolute value of compound score indicates prediction certainty

## Installation & Setup

### Prerequisites

- Python 3.12 or later
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 2: Install Dependencies

```bash
cd submission/app
pip install -r requirements.txt
```

### Step 3: Run the Application

```bash
python app.py
```

The application will start at `http://localhost:5000`

## Usage Examples

### Example 1: Single Text Analysis

1. Click "Text Input" tab
2. Enter: "I absolutely love this product! It exceeded all my expectations."
3. Click "Analyze"
4. Result: **POSITIVE** (Score: +0.835)

### Example 2: File Upload

1. Click "File Upload" tab
2. Select a .txt file
3. Upload and view sentence-by-sentence analysis

### Example 3: Batch Processing

1. Click "Batch Analysis" tab
2. Enter multiple texts (one per line)
3. Click "Analyze Batch"
4. View results for all texts simultaneously

## Sentiment Analysis Accuracy

We tested the application on 30 diverse text samples:

- **Positive Sentiment**: 80% accuracy (4/5 correct)
- **Negative Sentiment**: 100% accuracy (5/5 correct)
- **Neutral Sentiment**: 60% accuracy (3/5 correct)
- **Overall Accuracy**: 80% (12/15 correct classifications)

The model performs particularly well on clearly positive and negative texts. Edge cases and nuanced sentences may require further refinement.

## Known Limitations

1. **Sarcasm Detection**: The VADER model may struggle with sarcastic or ironic text
2. **Domain-Specific Language**: Technical or specialized terminology might not be analyzed accurately
3. **Context Length**: Very long texts are truncated to 5000 characters for performance
4. **Language Support**: Currently supports English only

## Enhancement Possibilities

We have documented several potential enhancements:

1. **Multi-Language Support**: Extend to support sentiment analysis in multiple languages
2. **Domain-Specific Models**: Create specialized models for healthcare, finance, and educational contexts
3. **Deep Learning Models**: Implement BERT or RoBERTa for higher accuracy
4. **Aspect-Based Sentiment**: Analyze sentiment toward specific aspects of a product or service
5. **Real-Time Social Media Monitoring**: Integration with APIs for live sentiment tracking

For detailed enhancement plan, see TASK_B_ENHANCEMENT.pdf

## Testing & Validation

We conducted thorough testing including:

- **Edge Case Testing**: Empty strings, special characters, very long texts
- **Error Handling**: Invalid file uploads, network errors, timeout scenarios
- **Performance Testing**: Response times for different text lengths
- **Cross-Browser Testing**: Verified functionality on Chrome, Firefox, Safari

## API Endpoints

### POST /api/analyze

Analyzes sentiment of single text

- **Input**: `{"text": "Your text here"}`
- **Output**: `{"sentiment": "positive", "scores": {...}}`

### POST /api/batch

Analyzes sentiment of multiple texts

- **Input**: `{"texts": ["text1", "text2", ...]}`
- **Output**: `{"results": [...]}`

### POST /api/upload

Analyzes text from uploaded file

- **Input**: File upload (.txt)
- **Output**: Line-by-line sentiment analysis

## Challenges Faced

1. **NLTK Data Download Issues**: Initial SSL certificate verification errors were resolved using SSL context bypass
2. **NumPy Compatibility**: Required updating to numpy 1.26.0 for Python 3.12 compatibility
3. **Large File Processing**: Implemented chunking for batch processing of large files
4. **UI Responsiveness**: Optimized CSS and JavaScript for smooth interaction on slower connections

## Future Work

Potential improvements for future versions:

- Database integration for storing analysis history
- User authentication and personal sentiment tracking
- Real-time analytics dashboard
- API rate limiting for public deployment
- Docker containerization for easy deployment
- Caching mechanism for frequently analyzed texts

## References

- NLTK Documentation: https://www.nltk.org/
- VADER Sentiment Analyzer: https://github.com/cjhutto/vaderSentiment
- Flask Documentation: https://flask.palletsprojects.com/

---

For detailed design decisions and implementation challenges, please refer to DESIGN_REPORT.md  
For application screenshots and workflow, please see SCREENSHOTS.md  
For enhancement plan across domains, please refer to TASK_B_ENHANCEMENT.pdf  
For research background, please refer to LITERATURE_SURVEY.pdf
