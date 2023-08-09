from flask import Flask, render_template, request, jsonify
import pyttsx3


app = Flask(__name__, static_url_path='/text_to_speech_app/static')

def text_to_speech(text):
    engine = pyttsx3.init()
    # Set up the engine properties
    engine.setProperty("rate", 150)  # Speed of speech
    engine.setProperty("volume", 0.8)  # Volume level

    # Play the speech back to the user
    engine.say(text)
    engine.runAndWait()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_text_to_speech():
    try:
        text = request.form['text']
        text_to_speech(text)
        return "Speech played successfully"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
