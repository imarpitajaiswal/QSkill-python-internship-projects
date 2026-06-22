import pickle
import pandas as pd  # Changed from numpy to pandas
import os
import sys

def execute_inference(rooms: int, size_sqft: float, location_grade: int):
    """Loads the exported serialization parameters to run an isolated prediction request."""
    model_path = 'regression_engine/valuation_model.pkl'
    
    if not os.path.exists(model_path):
        print(f"[ERROR] Serialization artifact not found at {model_path}. Execute train.py first.")
        sys.exit(1)
        
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
        
    # FIX: Use a Pandas DataFrame with exact feature names to prevent validation warnings
    input_data = pd.DataFrame([[rooms, size_sqft, location_grade]], 
                              columns=['rooms', 'size_sqft', 'location_grade'])
    
    predicted_price = model.predict(input_data)[0]
    
    print("\n--- OPERATIONAL REAL-TIME VALUATION ---")
    print(f"Parameters Provided -> Rooms: {rooms} | Size: {size_sqft} sqft | Location Grade: {location_grade}")
    print(f"Estimated Market Asset Value: {predicted_price:.2f} Lakhs INR")

if __name__ == "__main__":
    # Input simulation: A premium 4-room, 1850 sqft corporate facility located in a Grade 3 zone
    execute_inference(rooms=4, size_sqft=1850.0, location_grade=3)