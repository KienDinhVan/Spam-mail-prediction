import pickle

def prediction():
    # Load vectorizer, label encoder, and trained model
    with open('tfidf_vectorizer.pkl', 'rb') as tfidf_file:
        tfidf = pickle.load(tfidf_file)

    with open('spamham_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    with open('label_encoder.pkl', 'rb') as encod_file:
        encod = pickle.load(encod_file)

    # Input the email text
    mail = input('Your received mail: ')
    text = [mail]

    # Transform input using vectorizer
    vec_text = tfidf.transform(text)

    # Predict using the model
    y_pred = model.predict(vec_text)

    # Map prediction to category
    if y_pred[0] == 0:
        print('Ham')
    else:
        print('Spam')

if __name__ == "__main__":
    prediction()
