from sklearn.svm import LinearSVC
import pickle
from preprocessing import preprocess_data

def train_model():
    # Preprocess data
    x_train, x_test, y_train, y_test = preprocess_data()

    # Train model
    model = LinearSVC()
    model.fit(x_train, y_train)

    # Save the trained model to a file
    with open('spamham_model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)

if __name__ == "__main__":
    train_model()
