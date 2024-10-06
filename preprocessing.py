import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
import pickle

def preprocess_data(input_file='spamham.csv'):
    # Load dataset
    data = pd.read_csv(input_file)
    
    # Encode target labels
    encod = LabelEncoder()
    encod.fit(['spam', 'ham'])
    data['Category'] = encod.transform(data['Category'])
    
    # Split features and target
    x = data['Message']
    y = data['Category']
    
    # Vectorize features using Tfidf
    tfidf = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
    x = tfidf.fit_transform(x)
    
    # Split dataset
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=4)

    # Save vectorizer and encoder to files
    with open('tfidf_vectorizer.pkl', 'wb') as tfidf_file:
        pickle.dump(tfidf, tfidf_file)
    with open('label_encoder.pkl', 'wb') as encod_file:
        pickle.dump(encod, encod_file)

    return x_train, x_test, y_train, y_test

if __name__ == "__main__":
    preprocess_data()
