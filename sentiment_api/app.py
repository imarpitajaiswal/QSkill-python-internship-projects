import os
import sys
from flask import Flask, request, jsonify
from textblob import TextBlob

# Initialize the Flask enterprise microservice application
app = Flask(__name__)

@app.route('/api/v1/sentiment', methods=['POST'])
def analyze_sentiment_endpoint():
    """
    RESTful endpoint processing corporate client text payloads 
    to output deterministic polarity and subjectivity matrix metrics.
    """
    # 1. Request Validation Layer
    payload = request.get_json(silent=True)
    
    if not payload or 'text' not in payload:
        return jsonify({
            "status": "error",
            "message": "Bad Request. Payload must contain a valid JSON object with a 'text' key."
        }), 400
        
    user_text = payload['text']
    
    if not isinstance(user_text, str) or not user_text.strip():
        return jsonify({
            "status": "error",
            "message": "Invalid input. The 'text' value must be a non-empty string."
        }), 422

    try:
        # 2. Algorithmic Processing Layer via TextBlob Engine
        blob = TextBlob(user_text)
        polarity = blob.sentiment.polarity        # Range: [-1.0 (Negative), 1.0 (Positive)]
        subjectivity = blob.sentiment.subjectivity  # Range: [0.0 (Objective), 1.0 (Subjective)]
        
        # 3. Dynamic Business Classification Rule Logic
        if polarity > 0.1:
            classification = "Positive"
        elif polarity < -0.1:
            classification = "Negative"
        else:
            classification = "Neutral"
            
        # 4. Standardized Corporate Response Structure
        return jsonify({
            "status": "success",
            "data": {
                "input_length": len(user_text),
                "classification": classification,
                "metrics": {
                    "polarity_score": round(polarity, 4),
                    "subjectivity_score": round(subjectivity, 4)
                }
            }
        }), 200

    except Exception as e:
        return jsonify({
            "status": "fail",
            "message": f"Internal Analytics Engine Failure: {str(e)}"
        }), 500

if __name__ == "__main__":
    # Deploying the internal server loop on port 5001 to isolate it from default ports
    print("[SYSTEM] Launching Automated Customer Feedback Triage REST API...")
    app.run(host="127.0.0.1", port=5001, debug=True)