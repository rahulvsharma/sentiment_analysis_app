"""
Sentiment Analysis Web Application
==================================
A Flask-based web application that performs sentiment analysis on user-provided text.
Uses NLTK's VADER sentiment analyzer for accurate sentiment detection.

"""

from flask import Flask, render_template, request, jsonify
from sentiment_analyzer import SentimentAnalyzer
import os
from werkzeug.utils import secure_filename

# Initialize Flask application
app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

# Create upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Initialize sentiment analyzer
sentiment_analyzer = SentimentAnalyzer()


def allowed_file(filename):
    """Check if file is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')


@app.route('/api/analyze', methods=['POST'])
def analyze():
    """
    Analyze sentiment of provided text
    
    Expected JSON:
    {
        "text": "user text to analyze"
    }
    
    Returns:
    {
        "sentiment": "positive/negative/neutral",
        "scores": {
            "positive": float,
            "negative": float,
            "neutral": float,
            "compound": float
        },
        "success": bool,
        "message": str
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({
                'success': False,
                'message': 'No text provided'
            }), 400
        
        text = data['text'].strip()
        
        if not text:
            return jsonify({
                'success': False,
                'message': 'Text cannot be empty'
            }), 400
        
        if len(text) > 5000:
            return jsonify({
                'success': False,
                'message': 'Text is too long. Maximum 5000 characters allowed'
            }), 400
        
        # Analyze sentiment
        result = sentiment_analyzer.analyze(text)
        
        return jsonify({
            'success': True,
            'sentiment': result['sentiment'],
            'scores': result['scores'],
            'processed_text': result['processed_text'],
            'message': 'Analysis completed successfully'
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error during analysis: {str(e)}'
        }), 500


@app.route('/api/upload', methods=['POST'])
def upload_file():
    """
    Handle file upload and analyze sentiment
    
    Expected: multipart/form-data with 'file' field
    
    Returns:
    {
        "success": bool,
        "sentiment": str,
        "scores": dict,
        "text": str,
        "message": str
    }
    """
    try:
        if 'file' not in request.files:
            return jsonify({
                'success': False,
                'message': 'No file part in the request'
            }), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({
                'success': False,
                'message': 'No file selected'
            }), 400
        
        if not allowed_file(file.filename):
            return jsonify({
                'success': False,
                'message': 'Only .txt files are allowed'
            }), 400
        
        # Read file content
        content = file.read().decode('utf-8', errors='ignore')
        
        if not content.strip():
            return jsonify({
                'success': False,
                'message': 'File is empty'
            }), 400
        
        if len(content) > 5000:
            return jsonify({
                'success': False,
                'message': 'File content is too long. Maximum 5000 characters allowed'
            }), 400
        
        # Analyze sentiment
        result = sentiment_analyzer.analyze(content)
        
        return jsonify({
            'success': True,
            'sentiment': result['sentiment'],
            'scores': result['scores'],
            'text': content[:200] + '...' if len(content) > 200 else content,
            'full_text': content,
            'processed_text': result['processed_text'],
            'message': 'File analyzed successfully'
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error processing file: {str(e)}'
        }), 500


@app.route('/api/batch', methods=['POST'])
def batch_analyze():
    """
    Analyze multiple texts at once
    
    Expected JSON:
    {
        "texts": ["text1", "text2", ...]
    }
    
    Returns:
    {
        "success": bool,
        "results": [
            {
                "text": str,
                "sentiment": str,
                "scores": dict
            },
            ...
        ]
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'texts' not in data:
            return jsonify({
                'success': False,
                'message': 'No texts provided'
            }), 400
        
        texts = data['texts']
        
        if not isinstance(texts, list):
            return jsonify({
                'success': False,
                'message': 'Texts must be a list'
            }), 400
        
        if len(texts) > 50:
            return jsonify({
                'success': False,
                'message': 'Maximum 50 texts can be analyzed at once'
            }), 400
        
        results = []
        compound_scores = []
        for text in texts:
            text = text.strip()
            if text:
                result = sentiment_analyzer.analyze(text)
                results.append({
                    'text': text,
                    'sentiment': result['sentiment'],
                    'scores': result['scores']
                })
                compound_scores.append(result['scores']['compound'])
        
        # Calculate average compound score
        avg_compound = sum(compound_scores) / len(compound_scores) if compound_scores else 0
        
        return jsonify({
            'success': True,
            'results': results,
            'count': len(results),
            'average_compound_score': avg_compound
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error during batch analysis: {str(e)}'
        }), 500


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Sentiment Analysis API'
    }), 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'success': False,
        'message': 'Endpoint not found'
    }), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({
        'success': False,
        'message': 'Internal server error'
    }), 500


if __name__ == '__main__':
    # Run the Flask application
    # Use debug=True for development, debug=False for production
    app.run(debug=True, host='0.0.0.0', port=5001)
