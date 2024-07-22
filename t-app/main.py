from flask import Flask, request, render_template, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/speak', methods=['POST'])
def speak():
    text = request.form['text']
    tts = gTTS(text=text, lang='en')
    audio_path = "audio_files/output.mp3"
    tts.save(audio_path)
    return send_file(audio_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)




