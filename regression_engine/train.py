import numpy as np
import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def generate_enterprise_housing_data():
    """Generates a clean synthetic corporate real estate matrix for training."""
    np.random.seed(42)
    n_samples = 1000
    
    rooms = np.random.randint(2, 6, n_samples)
    size_sqft = rooms * np.random.normal(400, 50, n_samples) + np.random.normal(500, 100, n_samples)
    # Location Grade: 1 = Suburban, 2 = Urban Tier-1, 3 = Premium Financial District
    location_grade = np.random.randint(1, 4, n_samples)
    
    # Target value calculation formula (Price in INR Lakhs) with normal distribution noise
    base_price_inr_lakhs = (rooms * 15) + (size_sqft * 0.05) + (location_grade * 30) + np.random.normal(0, 5, n_samples)
    
    df = pd.DataFrame({
        'rooms': rooms,
        'size_sqft': size_sqft,
        'location_grade': location_grade,
        'price_lakhs': base_price_inr_lakhs
    })
    
    # Ensure directory context is correct
    os.makedirs('regression_engine', exist_ok=True)
    df.to_csv('regression_engine/housing_data.csv', index=False)
    print("[DATA] Synthetic housing dataset compiled and saved to local disk.")

def train_valuation_engine():
    """Trains the Linear Regression model and exports the serialized artifact."""
    if not os.path.exists('regression_engine/housing_data.csv'):
        generate_enterprise_housing_data()
        
    df = pd.read_csv('regression_engine/housing_data.csv')
    
    # Feature matrix and Target vector isolation
    X = df[['rooms', 'size_sqft', 'location_grade']]
    y = df['price_lakhs']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Metrics Evaluation
    predictions = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)
    
    print("\n--- MODEL PERFORMANCE METRICS ---")
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f} Lakhs")
    print(f"Coefficient of Determination (R2 Score): {r2:.4f}")
    
    # Model Artifact Serialization
    with open('regression_engine/valuation_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("[ARTIFACT] Trained model object successfully compiled and exported.")

if __name__ == "__main__":
    train_valuation_engine()