import whisper
import re

model = whisper.load_model("small")  # или medium

def clean_text(text):
    text = re.sub(r'\b(эээ|мм+)\b', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\s+([.,!?])', r'\1', text)
    text = '. '.join([s.strip().capitalize() for s in text.split('. ')])
    return text

def transcribe_audio(audio_file):
    result = model.transcribe(audio_file)
    text = clean_text(result['text'])
    return text
