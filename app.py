from flask import Flask, render_template, request
import requests

app = Flask(__name__)

ENDPOINT_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyAcCFqcSUUsXNJYcBw0oPdlaLEitlxiyfc"

def generate_text(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "instances": [{"content": prompt}]
    }
    response = requests.post(ENDPOINT_URL, headers=headers, json=data)
    response_json = response.json()
    
    # Extract and return the generated text from the response
    generated_text = response_json['predictions'][0]['generated_text']
    return generated_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    generated_text = generate_text(prompt)
    return render_template('index.html', generated_text=generated_text)

if __name__ == '__main__':
    app.run(debug=True)
