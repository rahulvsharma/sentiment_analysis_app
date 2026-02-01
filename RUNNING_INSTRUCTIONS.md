## Quick Start (Just want to run it quickly?)

### Group ID: 61

### Group Members Name with Student ID:

1. Arpita Singh (2024AA05027) Contribution 100%
2. Rahul Sharma (2024AA05893) Contribution 100%
3. Sachit Pandey (2024AA05023) Contribution 100%
4. Avishek Ghatak (2024AA05895) Contribution 100%
5. Anoushka Guleria (2023AA05527) Contribution 100%

### For macOS/Linux:

```bash
cd submission/app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

### For Windows:

```bash
cd submission/app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then go to **http://localhost:5001** in your browser and start analyzing sentiment!

---

### Prerequisites

**What you need:**

- Python 3.10 or newer (check with `python3 --version`)
- About 100MB of free space on your computer
- A web browser (Chrome, Firefox, Safari, Edge - any modern one)
- Internet connection (to download the NLP data from NLTK)

---

### Step 1: Create a Virtual Environment

A virtual environment is like a separate space on your computer for this project. It keeps this project's dependencies from messing with your system Python.

**macOS/Linux:**

```bash
cd /Users/rahul/Downloads/BITS/SEM3/NLPAPPS/Assignment2/submission/app
python3 -m venv venv
```

**Windows:**

```bash
cd path\to\Assignment2\submission\app
python -m venv venv
```

**Verify Creation:**

```bash
ls -la venv  # macOS/Linux
dir venv    # Windows
```

You should see: `bin/`, `include/`, `lib/`, `pyvenv.cfg`

---

### Step 2: Activate Virtual Environment

**macOS/Linux:**

```bash
source venv/bin/activate
```

You should see `(venv)` prefix in terminal.

**Windows Command Prompt:**

```bash
venv\Scripts\activate
```

**Windows PowerShell:**

```bash
venv\Scripts\Activate.ps1
```

**Verify Activation:**

```bash
which python  # macOS/Linux
where python  # Windows
```

Should point to: `/path/to/venv/bin/python`

---

### Step 3: Install Dependencies

With virtual environment activated, install required packages:

```bash
pip install -r requirements.txt
```

**What gets installed:**

- Flask 2.3.3 - Web framework
- nltk 3.8.1 - NLP library with VADER
- numpy 1.26.0 - Numerical computing
- Werkzeug 2.3.7 - WSGI utility library

**Verify Installation:**

```bash
pip list
```

You should see all 4 packages listed.

---

### Step 4: Run the Application

```bash
python3 app.py
```

**Expected Console Output:**

```
[nltk_data] Downloading package vader_lexicon...
[nltk_data]   Package vader_lexicon is already up-to-date!
[nltk_data] Downloading package punkt...
[nltk_data]   Package punkt is already up-to-date!
[nltk_data] Downloading package stopwords...
[nltk_data]   Package stopwords is already up-to-date!
[nltk_data] Downloading package wordnet...
[nltk_data]   Package wordnet is already up-to-date!
 * Serving Flask app 'app'
 * Debug mode: on
 * Restarting with reloader
 * Debugger is active!
 * Debugger PIN: 123-456-789
 * Running on http://localhost:5001
 * Press CTRL+C to quit
```

### Step 5: Access the Application

Open your web browser and navigate to:

**http://localhost:5001**

You should see the Sentiment Analysis Application interface.

---

## Troubleshooting

### Issue 1: "Command not found: python3"

**Solution:**

```bash
# Check if Python is installed
which python
python --version

# If not installed, install Python from python.org
# Then use 'python' instead of 'python3'
python -m venv venv
```

---

### Issue 2: "Port 5001 is already in use"

**Error Message:**

```
Address already in use
Port 5001 is in use by another program.
```

**Solutions:**

Option A: Kill process using port 5001

```bash
# macOS/Linux
lsof -i :5001
kill -9 <PID>

# Windows
netstat -ano | findstr :5001
taskkill /PID <PID> /F
```

Option B: Use different port
Edit `submission/app/app.py` line 282:

```python
# Change from:
app.run(debug=True, host='0.0.0.0', port=5001)

# To:
app.run(debug=True, host='0.0.0.0', port=5002)
```

Then access: http://localhost:5002

---

### Issue 3: "SSL: CERTIFICATE_VERIFY_FAILED"

**Error Message:**

```
SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed
```

**This error is already handled in the code**, but if you see it:

```bash
# For macOS, run this:
/Applications/Python\ 3.12/Install\ Certificates.command

# For Windows, run:
python -m pip install --upgrade certifi
```

---

### Issue 4: "ModuleNotFoundError: No module named 'flask'"

**Solution:**
Make sure virtual environment is activated:

```bash
# Verify activation - should see (venv) prefix
echo $VIRTUAL_ENV  # macOS/Linux
echo %VIRTUAL_ENV%  # Windows

# If not activated, activate it:
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows

# Then install dependencies again:
pip install -r requirements.txt
```

---

### Issue 5: Application runs but won't respond

**Possible causes:**

- Firewall blocking port 5001
- Port still locked from previous session

**Solution:**

```bash
# Try port 5002
# Edit app.py and change port to 5002
python3 app.py
# Access: http://localhost:5002
```

---

## Using the Application

### Tab 1: Text Input Analysis

1. Click "Text Input" tab
2. Enter or paste text (up to 5000 characters)
3. Click "Analyze"
4. View results:
   - Sentiment classification (Positive/Negative/Neutral)
   - Confidence score
   - Component scores (positive %, negative %, neutral %)
   - Processed text (after preprocessing)

**Examples to Try:**

Positive:

```
I absolutely love this product! It exceeded my expectations and works perfectly.
```

Negative:

```
This is the worst purchase I've made. Total waste of money and it broke immediately.
```

Neutral:

```
The weather today is cloudy with occasional rain.
```

---

### Tab 2: File Upload

1. Click "File Upload" tab
2. Click "Choose File" or drag & drop .txt file
3. File is analyzed line-by-line
4. View results table with:
   - Line number
   - Text
   - Sentiment classification
   - Confidence score

**File Requirements:**

- Format: Plain text (.txt)
- Size: Less than 1MB
- Encoding: UTF-8 (standard text files)

**Sample File Format:**

```
This movie was absolutely amazing!
I hated every minute of it.
It was okay, nothing special.
The acting was incredible.
Worst film I've ever seen.
```

---

### Tab 3: Batch Analysis

1. Click "Batch Analysis" tab
2. Enter multiple texts (one per line)
3. Click "Analyze Batch"
4. View results table with all texts analyzed

**Limits:**

- Maximum 50 texts per batch
- Maximum 5000 characters per text

**Example:**

```
Great product, would definitely recommend!
Terrible experience, would not buy again
The item works as advertised
This is the best purchase I've made
Absolutely disappointed with this
```

---

## API Endpoints (For Developers)

If accessing via API directly:

### 1. Analyze Single Text

**Endpoint:** `POST /api/analyze`

**Request:**

```bash
curl -X POST http://localhost:5001/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this product!"}'
```

**Response:**

```json
{
  "success": true,
  "sentiment": "positive",
  "scores": {
    "positive": 0.64,
    "negative": 0.0,
    "neutral": 0.36,
    "compound": 0.8713
  },
  "confidence": 0.87,
  "processed_text": "love product"
}
```

---

### 2. Batch Analysis

**Endpoint:** `POST /api/batch`

**Request:**

```bash
curl -X POST http://localhost:5001/api/batch \
  -H "Content-Type: application/json" \
  -d '{"texts": ["I love it!", "I hate it!"]}'
```

**Response:**

```json
{
  "success": true,
  "results": [
    {
      "text": "I love it!",
      "sentiment": "positive",
      "confidence": 0.82
    },
    {
      "text": "I hate it!",
      "sentiment": "negative",
      "confidence": 0.79
    }
  ]
}
```

---

### 3. File Upload

**Endpoint:** `POST /api/upload`

**Request:**

```bash
curl -X POST http://localhost:5001/api/upload \
  -F "file=@sample.txt"
```

**Response:**

```json
{
  "success": true,
  "results": [
    { "line": 1, "text": "Great!", "sentiment": "positive" },
    { "line": 2, "text": "Terrible!", "sentiment": "negative" }
  ]
}
```

---

### 4. Health Check

**Endpoint:** `GET /api/health`

**Request:**

```bash
curl http://localhost:5001/api/health
```

**Response:**

```json
{
  "status": "healthy",
  "message": "Application is running"
}
```

---

## Performance Benchmarks

**Measured on:**

- MacBook Pro (M1 Pro, 16GB RAM)
- Python 3.12.6
- Flask with debug mode

| Operation                   | Time  | Notes                  |
| --------------------------- | ----- | ---------------------- |
| Single text analysis        | 87ms  | Standard text          |
| Very long text (5000 chars) | 95ms  | At size limit          |
| Batch 5 texts               | 425ms | Average time           |
| File upload 50 lines        | 1.2s  | Including file parsing |
| Page load                   | 340ms | Initial page load      |

**Optimization Tips:**

- Batch process when analyzing multiple texts
- Disable browser extensions that may slow page load
- Use modern browser (Chrome/Firefox recommended)

---

## File Structure

```
submission/app/
├── app.py                          # Flask application (main entry point)
├── sentiment_analyzer.py           # NLP sentiment analysis module
├── requirements.txt                # Python dependencies
├── templates/
│   └── index.html                  # Web interface
├── static/
│   ├── css/
│   │   └── style.css              # Styling
│   └── js/
│       └── script.js              # Frontend logic
├── data/                           # Sample data (optional)
└── screenshots/                    # Application screenshots
```

---

## Environment Variables (Optional)

Create `.env` file for configuration:

```bash
# Debug mode (True/False)
FLASK_DEBUG=True

# Port (default 5001)
FLASK_PORT=5001

# Max file size (in bytes, default 1MB)
MAX_FILE_SIZE=1048576

# Max characters per text (default 5000)
MAX_CHARS=5000
```

Load in app.py:

```python
import os
from dotenv import load_dotenv

load_dotenv()
DEBUG = os.getenv('FLASK_DEBUG', 'True') == 'True'
PORT = int(os.getenv('FLASK_PORT', 5001))
```

---

## Stopping the Application

**To stop the running application:**

Press `CTRL+C` in the terminal where it's running.

**Expected Output:**

```
^C
Traceback (most recent call last):
  ...
KeyboardInterrupt
```

The application will shut down gracefully.

---

## Production Deployment (Advanced)

For deployment beyond local testing:

```bash
# Install production server
pip install gunicorn

# Run with gunicorn
gunicorn --workers 4 --bind 0.0.0.0:5000 app:app

# Or with environment variables
export FLASK_ENV=production
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## Testing the Application

### Manual Testing Steps

1. **Positive Sentiment Test**
   - Input: "I absolutely love this! Best product ever!"
   - Expected: Sentiment = Positive, Confidence > 0.80

2. **Negative Sentiment Test**
   - Input: "Worst experience, absolutely terrible!"
   - Expected: Sentiment = Negative, Confidence > 0.75

3. **Neutral Sentiment Test**
   - Input: "The weather is cloudy today."
   - Expected: Sentiment = Neutral, Confidence varies

4. **Edge Case - Empty Input**
   - Input: "" (empty)
   - Expected: Error message

5. **Edge Case - Special Characters**
   - Input: "😊 Great!"
   - Expected: Successfully analyzed, special chars handled

6. **File Upload Test**
   - Upload sample.txt with 5 lines
   - Expected: All 5 lines analyzed correctly

---

## Support & Troubleshooting

**Common Issues Quick Reference:**

| Issue            | Solution                                      |
| ---------------- | --------------------------------------------- |
| Port in use      | Change port in app.py (line 282)              |
| Module not found | Activate virtual environment, run pip install |
| SSL error        | Already handled, try restarting app           |
| App won't start  | Check for syntax errors in app.py             |
| Slow performance | Try batch processing, check browser cache     |

**For Additional Help:**

- Check Flask documentation: https://flask.palletsprojects.com/
- Check NLTK documentation: https://www.nltk.org/
- Review error messages in terminal carefully

---

## Next Steps

1.  Run the application
2.  Test all three tabs
3.  Try sample texts in examples
4.  Experiment with file uploads
5.  Check API endpoints (for developers)
6.  Review Design Report for implementation details
7.  Read Task B Enhancement Plan for future improvements
8.  Check Literature Survey for research background

---
