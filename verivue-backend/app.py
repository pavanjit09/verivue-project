from flask import Flask, request, jsonify
import speech_recognition as sr
from transformers import pipeline
import moviepy.editor as mp

app = Flask(__name__)

summarizer = pipeline("summarization")
fact_checker = pipeline("text-classification", model="microsoft/deberta-v3-base")

@app.route('/factcheck', methods=['POST'])
def factcheck():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    video = request.files['file']
    video.save('uploaded_video.mp4')

    # Extract audio from video
    clip = mp.VideoFileClip('uploaded_video.mp4')
    clip.audio.write_audiofile('audio.wav')

    # Transcribe audio
    recognizer = sr.Recognizer()
    with sr.AudioFile('audio.wav') as source:
        audio_data = recognizer.record(source)
        transcript = recognizer.recognize_google(audio_data)

    # Summarize text
    summary = summarizer(transcript, max_length=100, min_length=30, do_sample=False)

    # Fact-checking
    claims = summary[0]['summary_text'].split('. ')
    fact_results = [{"claim": claim, "result": fact_checker(claim)} for claim in claims]

    return jsonify({"summary": summary[0]['summary_text'], "fact_checks": fact_results})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
