from flask import Flask, render_template, request, jsonify
import requests  

app_FRONT = Flask(__name__)

FASTAPI_BACKEND_URL = "http://127.0.0.1:8000/rag-chroma/invoke"  # Make sure to add /invoke

@app_FRONT.route('/')
def index():
    return render_template('index5.html')  # Just render the form on the index route

@app_FRONT.route('/ask', methods=['POST'])
def ask():
    # print(request.json)  # Add this to log the incoming JSON payload
    question_text = request.json.get('question')
    if not question_text:
        return jsonify({"error": "Please enter a question."}), 400

    # Construct the payload with the "input" key as expected by the backend
    payload = {"input": question_text}

    # Make the POST request to the backend server
    response = requests.post(
        FASTAPI_BACKEND_URL,
        json=payload,
        headers={"Content-Type": "application/json"}
    )

    # Check if the call to the backend was successful and return the appropriate response
    if response.status_code == 200:
        data = response.json()
        # Extract the "output" from the backend response. Adjust this key if the backend uses a different key.
        return jsonify({"answer": data.get("output", "No answer found")})
    else:
        # If the backend response indicates an error, log it and send an error message to the frontend
        print(f"Backend API error: {response.status_code}")
        print(f"Response content: {response.content}")
        return jsonify({"error": "Error getting an answer from the backend API."}), 500


if __name__ == '__main__':
    app_FRONT.run(host='0.0.0.0', port=5000, debug=True)
    # app_FRONT.run(debug=True)
