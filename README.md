# Amazon Food Reviews Sentiment Analysis Web App

This project is part of my personal journey to demonstrate my skills in **Web Scraping**, **NLP**, and **Machine Learning** by building a working sentiment analysis model that can classify Amazon food reviews into **Positive**, **Neutral**, or **Negative** sentiments.

## My Goal

My goal with this project was to:

- Learn & understand real-world machine learning workflows
- Practice handling imbalanced datasets
- Build an end-to-end Streamlit web app
- Push the complete code to GitHub
- And finally, deploy it online

## What I Did

- I used a **public dataset of Amazon food reviews** from Hugging Face.
- Performed data preprocessing, handled class imbalance, and applied machine learning.
- Trained a **Logistic Regression model** using **TF-IDF vectorization**.
- Evaluated performance using accuracy and **ROC curve analysis**.
- Handled class imbalance using **resampling techniques** to improve model generalization.
- Saved the trained model and vectorizer using `joblib`.
- Developed a simple yet effective **Streamlit UI** to allow live prediction testing.
- Added a clean UI where users can input a review and get instant predictions.

## Live App

🔗 [Click here to try the app] - https://amazonfoodreviewsgit-paxrpq6qihb3ptolp7cmd9.streamlit.app/ 


##  Dataset

- The dataset used in this project is the **Amazon Food Reviews** dataset available on [Hugging Face](https://huggingface.co/datasets/amazon_polarity).
- It contains thousands of food product reviews with sentiment labels (positive/negative).
https://huggingface.co/datasets/jhan21/amazon-food-reviews-dataset

## Tech Stack

- **Python** (Pandas, Scikit-learn, NumPy)
- **Streamlit** for interactive UI
- **Joblib** for saving/loading models
- **Jupyter Notebook** in VS Code for development
