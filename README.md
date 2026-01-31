# Fake News Detection Using Social Media Data
---

##  Problem Statement
The rapid growth of social media platforms has made it easy for misinformation and fake news to spread quickly. Manual fact-checking is time-consuming and not scalable. Therefore, there is a need for an automated system that can analyze news content and detect fake news efficiently.

---

## Project Objectives
- To analyze textual data from news articles
- To apply Natural Language Processing techniques for feature extraction
- To build a Machine Learning model to classify news as real or fake
- To deploy the trained model as a user-friendly web application

---

##  Technologies & Tools Used
- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn  
- **NLP Technique:** TF-IDF Vectorization  
- **Machine Learning Model:** Logistic Regression  
- **Web Framework:** Streamlit  
- **Model Serialization:** Pickle  

---

##  Dataset Information
- **Dataset Name:** ISOT Fake News Dataset  
- **Files Used:** `True.csv`, `Fake.csv`  
- The dataset contains labeled real and fake news articles.
- The dataset was used during model training and is **not included** in this repository.

---

##  Model Description
- Text data is cleaned and preprocessed
- TF-IDF is used to convert text into numerical features
- Logistic Regression is trained for binary classification
- The trained model achieves approximately **98% accuracy**

---

## How to Run the Project

### Step 1: Clone or Download the Repository
Download the repository or clone it using GitHub.

### Step 2: Install Required Dependencies

### Step 3: Run the Streamlit Application

### Step 3: Run the Streamlit Application

---

##  Application Features
- User-friendly interface
- Accepts custom news text as input
- Displays prediction: **Real News / Fake News**
- Shows confidence score for prediction

---

## Sample Predictions

**Example – Real News:**

---

## 📌 Limitations
- The model performs best on formal news-style text
- Informal or very short inputs may reduce accuracy
- Dataset bias toward professionally written articles

---

## 🔮 Future Enhancements
- Use of deep learning models such as BERT
- Multilingual fake news detection
- Integration with social media platforms
- Continuous model retraining with updated data

---

##  Author
**Sanjay P Nair**

---

## Project Category
TCS iON – Industry Oriented Machine Learning Project
