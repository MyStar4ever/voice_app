from flask import Flask, request, jsonify
from transcribe import transcribe_audio
import sounddevice as sd
import numpy as np
import wave

app = Flask(__name__)

@app.route("/record_session", methods=["POST"])
def record_session():
    duration = int(request.json.get("duration", 5))
    fs = 16000
    recording = sd.rec(int(duration*fs), samplerate=fs, channels=1)
    sd.wait()
    # сохраняем в WAV
    filename = "temp.wav"
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes((recording*32767).astype(np.int16).tobytes())
    text = transcribe_audio(filename)
    return jsonify({"text": text})

if __name__ == "__main__":
    app.run(debug=True)
