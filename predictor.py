import pickle
import pandas as pd

# Load model
with open('./models/recommendation_model.pkl', 'rb') as f:
    model = pickle.load(f)

print("✅ Model loaded successfully!")

def prepare_features(title, tags, upload_hour):
    title_length = len(str(title))
    num_tags = len(str(tags).split('|')) if tags else 0
    features = pd.DataFrame({
        'title_length': [title_length],
        'num_tags': [num_tags],
        'upload_hour': [upload_hour]
    })
    return features

def predict_trending(title, tags, upload_hour):
    features = prepare_features(title, tags, upload_hour)
    probability = model.predict_proba(features)[0][1]
    prediction = model.predict(features)[0]
    print(f"Prediction: {'Trending' if prediction == 1 else 'Not Trending'} (Probability: {probability:.4f})")
    return prediction, probability

if __name__ == "__main__":
    title = "Amazing travel vlog | Exploring Bali"
    tags = "travel|vlog|bali|adventure"
    upload_hour = 15
    predict_trending(title, tags, upload_hour)
