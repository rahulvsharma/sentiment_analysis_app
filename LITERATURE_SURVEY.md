# Literature Survey: Cross-Domain Sentiment Analysis

### Group ID: 61

### Group Members Name with Student ID:

1. Arpita Singh (2024AA05027) Contribution 100%
2. Rahul Sharma (2024AA05893) Contribution 100%
3. Sachit Pandey (2024AA05023) Contribution 100%
4. Avishek Ghatak (2024AA05895) Contribution 100%
5. Anoushka Guleria (2023AA05527) Contribution 100%

---

## 1. Introduction & Background

### 1.1 What's Sentiment Analysis?

Sentiment analysis (also called opinion mining) is basically figuring out whether someone's opinion in text is positive, negative, or neutral. It's a big part of NLP because companies and researchers use it everywhere - from checking what people think about products, to monitoring social media, to market research (Pang & Lee, 2008).

### 1.2 The Cross-Domain Problem

Here's the tricky part: if you train a model on movie reviews, it might not work well on product reviews or restaurant reviews. The vocabularies and writing styles are different across domains. This problem is called "domain adaptation" or "cross-domain sentiment analysis" (Blitzer et al., 2007).

**Example:** A model trained on movie reviews may not perform well when analyzing product reviews, restaurant reviews, or healthcare feedback. The vocabularies, writing styles, and sentiment indicators differ significantly across domains.

### 1.3 Why Should We Care?

Cross-domain sentiment analysis is important for practical reasons:

- **Saves Money:** Instead of training a new model for every domain, you can reuse the same one
- **Works Everywhere:** One model can work for movies, products, restaurants, etc.
- **Knowledge Sharing:** What we learn from movie reviews can help with product reviews
- **Real Life:** Most real-world problems have data from different sources anyway

---

## 2. Literature Review

### 2.1 The Early Days

#### 2.1.1 Lexicon-Based Methods (Early 2000s)

**Important Papers:**

- Turney (2002): "Thumbs Up? Sentiment Classification using Machine Learning Techniques"
- Pang et al. (2002): "Sentiment Classification of Movie Reviews"

**How it works:** You have a dictionary of words (lexicon) that says whether each word is positive or negative. You count the words in a review and that tells you the sentiment.

**Good things:**

- You don't need training data
- You can see why the model made its decision
- Works okay across different domains

**Bad things:**

- Only works with words in the dictionary
- Doesn't understand domain-specific words
- Gets confused by sarcasm

**A real example:** VADER (Valence Aware Dictionary and sEntiment Reasoner) - Hutto & Gilbert (2014)

- Made specifically for social media
- Understands emojis and slang
- Still uses a dictionary but in a smarter way

---

#### 2.1.2 Machine Learning Approaches (Mid 2000s)

**Important Papers:**

- Pang et al. (2002): "Sentiment Classification of Movie Reviews" (Naive Bayes, SVM)
- Mullen & Collier (2004): "Sentiment Analysis using Support Vector Machines"

**How it works:** Instead of using a dictionary, you train algorithms (like Naive Bayes or SVM) on data where you already know if reviews are positive or negative.

**What features they used:**

- Bag of Words (BoW) - just counting words
- TF-IDF - weighing words by how common they are
- N-grams - sequences of words

**Good things:**

- Works better than just using a dictionary
- Can learn patterns that are specific to the domain

**Bad things:**

- You need lots of labeled data
- Works poorly when you switch to a different domain
- Sensitive to changes in the type of text

**Domain Performance:** Blitzer et al. (2007) demonstrated significant accuracy drop (10-40%) when applying models trained on one domain to another domain.

---

#### 2.1.3 Deep Learning Approaches (2014 onwards)

**Important Papers:**

- Kim et al. (2014): "Convolutional Neural Networks for Sentence Classification"
- Dos Santos & Gatti (2016): "Deep Learning for Sentiment Analysis: A Comparative Study"

**Different types of neural networks used:**

1. **CNNs (Convolutional Neural Networks)**
   - Train quickly
   - Can pick up local patterns in text
2. **RNNs/LSTMs (Recurrent Neural Networks)**
   - Good for sequences of words
   - Remember what happened earlier in the text
3. **Attention Mechanisms**
   - Focus on the important words
   - A bit easier to understand why it made a decision

**Good things:**

- Way more accurate than older machine learning methods
- Handles tricky patterns well
- Learns useful word representations that work across domains

**Bad things:**

- Need really big datasets to train
- You can't easily see why it made a decision
- Takes a lot of computing power

---

### 2.2 Solving the Cross-Domain Problem

#### 2.2.1 Smart Feature Learning (Domain Adaptation)

**The Study:** Blitzer et al. (2007) - "Biographies, Bollywood, Boom-boxes and Blenders: Domain Adaptation for Sentiment Classification"

**The Problem:** When you use a model trained on one type of review (say, electronics) on another type (like books), accuracy drops by 12-18%.

**Their Solution:** Find words that appear in reviews from all different types, and use those to learn features that work everywhere.

**What they found:**

- By using this method, they cut the performance drop from 12-18% to just 2-4%
- This showed that models CAN learn to work across different domains

---

#### 2.2.2 Using Adversarial Training

**The Study:** Glorot et al. (2011) - "Domain-Adversarial Training of Neural Networks"

**The Idea:** Train two networks at the same time:

- One network tries to learn sentiment
- Another network tries to guess which domain the text came from

Because of this "fight", the sentiment network learns features that work no matter what domain you're in.

**Results:** They got 80-85% accuracy across multiple domains - a big improvement!

**Problem:** This only works if you have examples from all the domains during training

---

#### 2.2.3 Pre-trained Language Models (The Game Changer)

**The Big Discovery:** Radford et al. (2018) - "Language Models are Unsupervised Multitask Learners" (GPT)

**What Changed:** They showed that when you train a model on TONS of text from the internet first, it learns general language understanding that works great across different domains.

**The Follow-Ups:**

- BERT (Devlin et al., 2019): Even better at understanding context
- RoBERTa (Liu et al., 2019): Improved version of BERT

**Why it works:**

1. Training on massive amounts of text teaches general patterns
2. When you fine-tune on your specific data, it adapts
3. The word meanings learned capture relationships that transfer

**Real numbers:** Fine-tuned BERT gets over 90% accuracy on sentiment across totally different domains, sometimes with as few as 100-200 labeled examples.

---

### 2.3 How Sentiment Analysis Works Differently in Different Domains

#### 2.3.1 Healthcare Reviews

**The Challenge:** Medical texts have specialized words that normal people don't use.

**Study:** Denecke (2008) - "Using SentiWordNet for Multilingual Sentiment Analysis"

**Domain-Specific Words:**

- Positive: "effective", "improved", "recovered", "healing"
- Negative: "adverse", "complications", "severe", "infection"
- Tricky: "aggressive" treatment (positive), but "aggressive" cancer (negative)

**Solutions:**

1. Use medical-specific dictionaries (like UMLS - Unified Medical Language System)
2. Train word embeddings on medical papers and articles
3. Combine general sentiment models with medical-specific models

**Results:** Domain-specific models get 85-90% accuracy vs. 70-75% for general models.

---

#### 2.3.2 Financial/Stock Market Sentiment

**Study:** Tetlock (2007) - "Giving Content to Investor Sentiment: The Role of Media in the Stock Market"

**The Tricky Part:** Same words mean different things in finance

- "Bullish" = good (positive)
- "Bearish" = bad (negative)
- "Volatile" = risky (depends on context)

**Financial Sentiment Words:**

- General negative: "bad", "poor", "fail"
- Finance specific: "loss", "bankruptcy", "dilution"
- Context matters: "down 5%" is bad in a bull market but could be good in a bear market

**What They Found:** If financial news is really pessimistic, stock prices are 15.3% more likely to go down next month.

---

#### 2.3.3 Social Media (Twitter, Instagram, etc.)

**Study:** Rosenthal et al. (2017) - "SemEval-2017 Task 4: Sentiment Analysis in Twitter"

**Why It's Hard:**

- People use slang and abbreviations
- Sarcasm is everywhere ("Oh great, another meeting")
- Emojis and hashtags
- Language changes super fast

**Solutions:**

- Special tools for breaking up Twitter text
- Use pre-trained embeddings trained on Twitter data
- Add sarcasm detection
- Handle emojis properly

**Key Finding:** VADER (which we use in this project!) was made specifically for social media and beats general models by 10-15% on Twitter data.

---

### 2.4 Fancier Techniques

#### 2.4.1 Aspect-Based Sentiment (Sentiment About Specific Things)

**What is it:** Sometimes you want to know sentiment about specific parts of something.

**Example:** "The food was delicious but the service was terrible"

- Food = Positive
- Service = Negative ✗

**Study:** Pontiki et al. (2016) - "SemEval-2016 Task 5: Aspect-Based Sentiment Analysis"

**How to do it:**

1. Find the aspects (food, service)
2. Figure out the sentiment for each aspect

**One cool approach:** Use attention mechanisms (basically telling the model which words matter for which aspects)

**How well does it work:** Best systems get 75-80% accuracy.

**Real use case:** Restaurants - extract sentiment about food, service, ambiance, price separately

---

#### 2.4.2 Emotion Detection (Beyond Just Positive/Negative)

**The Idea:** Instead of just saying "this is positive", detect specific emotions: happy, angry, sad, scared, surprised, disgusted

**Study:** Demszky et al. (2020) - "GoEmotions: A Dataset of Fine-Grained Emotions"

**The Basics:**

- Each sentence can have multiple emotions
- Emotions have intensity (a little angry vs. really angry)
- Emotions change throughout longer texts

**Real Applications:** Customer service chatbots - know not just if someone's upset, but WHY they're upset (confused, frustrated, angry)

---

#### 2.4.3 Using Video, Audio, AND Text Together (Multimodal)

**What is it:** Not just analyzing the words, but also tone of voice, facial expressions, etc.

**Study:** Zadeh et al. (2017) - "Multimodal Language Analysis in the Wild: CMU-MOSEI Dataset and Interpretable Dynamic Fusion Graph"

**Why it helps:**

- Words: "This is fine" (what you say)
- Tone: Sarcastic voice (how you say it)
- Face: Angry expression (your feelings)

**How to combine them:**

1. Early fusion: Combine everything before analyzing
2. Late fusion: Analyze each separately, then combine results
3. Hybrid: Mix them at different stages

**Challenge:** Making sure video/audio/text are aligned (when someone speaks, their mouth moves at the same time)

**Real use:** Analyzing movie reviews with video clips, YouTube sentiment analysis

---

### 2.5 The Latest Stuff (2020-2024)

#### 2.5.1 Using BERT and Transformers

**What's BERT:** A pre-trained model that already understands language before you teach it sentiment

**How to use:** Train it on your data (even with just 100-200 examples) and it works great

**Good things:**

- Understands context really well
- Learns word meanings that transfer across domains
- Gets 90%+ accuracy

**Not so good:**

- Needs a GPU (slow on regular computers)
- Hard to understand why it made a decision
- Needs some training on your specific data

**How good:** On standard benchmarks, gets 94%+ accuracy

---

#### 2.5.2 Just Asking the Model (Few-Shot Learning)

**The Discovery:** Brown et al. (2020) - "Language Models are Few-Shot Learners" (GPT-3)

**The Trick:** You don't train the model, you just ask it correctly. Show it a couple examples and it figures out the rest.

**Example:**

```
Here's a positive review: "Great product, would recommend!"
Here's a negative review: "The worst purchase ever."
Here's a neutral review: "It works okay."
Now classify this: "Amazing experience, highly satisfied!"
```

The model says: "Positive"

**Why it's cool:**

- No training needed
- Works for many languages
- Super flexible

**The catch:** You need access to big models like GPT-3 (costs money or computing power)

---

#### 2.5.3 Training Models That Work on Anything

**Study:** Wang et al. (2021) - "Domain Generalization: A Survey"

**The Question:** Can we train a model that works on domains we've never even seen?

**Methods:**

1. Data augmentation - create fake variations of your data
2. Meta-learning - teach the model how to learn
3. Self-supervised learning - learn from unlabeled data first

**Results:** Models trained this way stay above 85% accuracy even on totally new domains

---

## 3. What We've Learned From All This

### 3.1 How Things Changed Over Time

| Years     | Method             | Accuracy | Works Cross-Domain | Easy to Understand |
| --------- | ------------------ | -------- | ------------------ | ------------------ |
| 2000-2005 | Dictionary/Lexicon | 70-75%   | Kinda              | Yes                |
| 2005-2012 | Machine Learning   | 80-85%   | Nope (bad)         | Somewhat           |
| 2012-2018 | Deep Learning      | 85-90%   | A little bit       | Not really         |
| 2018-2024 | Pre-trained Models | 90-95%   | Really well        | Not much           |
| 2024+     | Large Language Mod | 90-98%   | Amazingly          | A bit better       |

**Key Trend:** We get better accuracy AND better cross-domain performance over time!

### 3.2 Why Some Methods Work Better Across Domains

1. **Bigger training datasets** = learns more general patterns
2. **Similar tasks** = transfer better than completely different domains
3. **Good quality labeled data** = gets you there faster
4. **Overlapping words** = movie reviews → product reviews is easier than tech → healthcare

### 3.3 How to Pick the Right Approach

**If you want maximum accuracy (90%+):**

- Use BERT or similar pre-trained models
- Get 100-200 labeled examples
- Fine-tune on your specific domain

**If you need it to be fast:**

- Use VADER or DistilBERT
- Cache results so you don't recalculate
- Accept maybe 5-10% lower accuracy for 10x faster speed

**If you need to understand WHY it made a choice:**

- Use attention mechanisms (show important words)
- Combine with lexicon approaches
- Use LIME/SHAP tools to explain

**If you need it to work on domains you haven't seen:**

- Start with pre-trained models
- Use multiple models and combine them
- Mix general + domain-specific approaches

---

## 4. Sentiment Analysis in Real Domains

### 4.1 Healthcare/Medical Reviews

**Why it's hard:**

- Doctors use special medical words (UMLS has over 1 MILLION concepts!)
- "Aggressive" treatment is good, but "aggressive" cancer is bad
- You gotta be careful - wrong results could affect patient care
- Privacy rules are strict - can't share patient data

**How to solve it:**

1. Use medical word embeddings (trained on medical papers, not just Twitter)
2. Combine with medical-specific word lists
3. Always use a confidence threshold - if not sure, flag it
4. Have doctors check the results

**Good papers:** Denecke (2008), Lohr et al. (2018), Shim et al. (2021)

---

### 4.2 Finance/Stock Market Sentiment

**Why it's hard:**

- Words change meaning based on market conditions
- "Down 5%" is bad in a bull market but could be good in a bear market
- Timing matters - sentiment today predicts stock prices tomorrow
- Laws restrict what you can do with financial info

**How to solve it:**

1. Include market context (bull vs bear market)
2. Track sentiment over time (is it getting better or worse?)
3. Check if sentiment matches actual stock movements
4. Combine with other market indicators

**Real finding:** Tetlock showed that very negative financial news predicts stock drops 15% more often next month.

---

### 4.3 Student Feedback/Education

**Why it's hard:**

- Students give praise but also constructive criticism (both are useful)
- Different feedback is useful for different people (teachers vs. admin)
- Feedback changes over time (students like courses better as they progress)
- You want actionable insights, not just "good" or "bad"

**How to solve it:**

1. Analyze sentiment for different aspects (teaching, difficulty, materials, pace)
2. Categorize feedback (praise, suggestion, complaint)
3. Track changes over time
4. Summarize differently for teachers vs. administration

**References:** Cheung & Lee (2012), Rasamoelina et al. (2020)

---

## 5. Problems Nobody Has Solved Yet

### 5.1 The Hard Stuff

1. **Sarcasm** 😏
   - "Oh great, another meeting" (sounds positive but is negative)
   - Needs world knowledge - you gotta understand context
   - Best systems only get 65-70% accuracy

2. **Working Across Languages**
   - Transfer works great in English
   - But teaching an English model to understand Chinese is hard
   - Current best: 75-80% (vs. 90%+ for single language)

3. **Language Keeps Changing**
   - New slang pops up constantly
   - Models get worse over time if you don't update them
   - Need systems that learn continuously

4. **Privacy**
   - Healthcare and financial data is sensitive
   - Can't share real patient/customer data
   - New "federated learning" methods are trying to solve this

### 5.2 New Opportunities

1. **Combining Video, Audio, AND Text**
   - Much more complete understanding
   - Can see sarcasm (tone of voice)
   - Still pretty new and challenging

2. **Making Models Explainable**
   - "Why did you think this was positive?"
   - Attention visualizations help
   - Tools like LIME/SHAP are getting better

3. **Learning Without Labels**
   - Training without needing humans to label data
   - Self-supervised learning promising
   - Zero-shot learning (work on new domains with no training data)

4. **Using Knowledge Graphs**
   - Connect concepts together
   - Understand deeper meaning
   - Early results look promising

---

## 6. Real-World Money and Applications

### 6.1 Industries Using This (and Making Money)

| Industry         | Market Value | What They Use It For                          | Why It Matters              |
| ---------------- | ------------ | --------------------------------------------- | --------------------------- |
| **Healthcare**   | $15 Billion  | Patient reviews, drug feedback, clinical data | Better patient outcomes     |
| **Finance**      | $20 Billion  | Market news analysis, trading signals         | Direct money impact         |
| **E-commerce**   | $50B+        | Product reviews, customer feedback            | More sales                  |
| **Social Media** | $30B+        | Brand reputation, trending topics             | Advertising dollars         |
| **Customer Svc** | $10 Billion  | Chatbot responses, support ticket routing     | Lower costs, happier people |

### 6.2 Tools You Can Actually Use

**Paid Services (Easy but Costs Money):**

- Amazon Comprehend - 85% accuracy
- Google Cloud NLP - 90% accuracy
- Microsoft Azure - 88% accuracy
- IBM Watson - 87% accuracy

**Free/Open Source (DIY):**

- VADER (what we use!) - 80-82% accuracy, super fast
- Hugging Face - 90%+ with some setup
- TextBlob - 75-78%, very basic
- Stanford CoreNLP - 80-85%
- spaCy - 82-85%

---

## 7. Wrapping Up

### 7.1 The Big Takeaways

1. **Things Got Better Over Time**
   - From simple word lists → Machine Learning → Deep Learning → Pre-trained Models
   - Each generation is more accurate AND works better across different domains

2. **Pre-trained Models Changed Everything**
   - Before: If you switched domains, accuracy dropped 15-40%
   - Now: Only drops 2-5%
   - You can train on just 100-200 examples and get great results

3. **Domain Still Matters**
   - General models are good, but domain-specific ones are better
   - Healthcare needs medical knowledge
   - Finance needs market knowledge
   - Combining both approaches works best

4. **Real Trade-offs**
   - **Speed vs. Accuracy:** BERT gets 95% accuracy but takes 200ms. VADER gets 80% in 2ms.
   - **Understandability vs. Power:** Lexicon methods are easy to explain but less accurate. Deep learning is powerful but mysterious.
   - **Cost vs. Quality:** Paid APIs are best but expensive. Open-source is free but needs more work.

### 7.2 Advice for This Assignment & Beyond

**For this assignment:**

- VADER (what we used) is perfect - it's proven, fast, and built for this task
- Add domain-specific word lists if you want to boost accuracy
- Combine multiple approaches for best results

**If you're deploying to production:**

- Use fine-tuned BERT for 90%+ accuracy
- Cache results to make it faster
- Monitor and retrain as language changes

**For research (future projects):**

- Multimodal analysis (video + audio + text)
- Better sarcasm detection
- Privacy-preserving methods
- Real-time learning and adaptation

---

## 8. References

### Core Sentiment Analysis Papers

- Pang, B., & Lee, L. (2008). "Opinion Mining and Sentiment Analysis". Foundations and Trends in Information Retrieval, 2(1-2), 1-135.
- Hutto, C. J., & Gilbert, E. (2014). "VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text". ICWSM.

### Cross-Domain Sentiment Analysis

- Blitzer, J., Daumé III, H., & Pereira, F. (2007). "Biographies, Bollywood, Boom-boxes and Blenders: Domain Adaptation for Sentiment Classification". ACL.
- Glorot, X., Bordes, A., & Bengio, Y. (2011). "Domain-Adversarial Training of Neural Networks". JMLR.

### Deep Learning & Transfer Learning

- Kim, Y. (2014). "Convolutional Neural Networks for Sentence Classification". EMNLP.
- Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2019). "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding". NAACL.
- Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., & Sutskever, I. (2019). "Language Models are Unsupervised Multitask Learners". OpenAI.

### Domain-Specific Applications

- Denecke, K. (2008). "Using SentiWordNet for Multilingual Sentiment Analysis". ICDE.
- Tetlock, P. C. (2007). "Giving Content to Investor Sentiment: The Role of Media in the Stock Market". Journal of Finance, 62(3).
- Pontiki, M., Grangier, D., Papageorgiou, Z. (2016). "SemEval-2016 Task 5: Aspect Based Sentiment Analysis". SemEval@ACL.

### Advanced Topics

- Zadeh, A., Liang, P. P., Poria, S., Cambria, E., & Morency, L. P. (2018). "Multimodal Language Analysis in the Wild: CMU-MOSEI Dataset and Interpretable Dynamic Fusion Graph". ACL.
- Demszky, D., Movshovitz-Attias, D., Chang, J., Eisner, J., Ravi, S., & Szpektor, I. (2020). "GoEmotions: A Dataset of Fine-Grained Emotions". ACL.

---
