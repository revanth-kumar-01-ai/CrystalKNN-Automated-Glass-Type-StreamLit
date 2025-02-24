import warnings
import pickle

warnings.filterwarnings('ignore')

def Model(df):
    try: 
        with open('./models/glass_AI_model.pkl', 'rb') as model_file:
            model = pickle.load(model_file)
    except Exception as e:
        print(f"Error loading data or model: {e}")
        model = None

    if model is None:
        print("Model is not loaded. Evaluation cannot proceed.")
        return None
    
    try:
        # Test predictions
        pred = model.predict(df)
        
        return pred[0]
    except Exception as e:
        print(f"Error during evaluation: {e}")
        return None