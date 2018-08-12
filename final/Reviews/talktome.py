from google.cloud import texttospeech
from flask import current_app

def read_text(text):
    '''
    Takes in input text and converts it to a base 64 encoded audio string
    '''
    client = texttospeech.TextToSpeechClient()
    input = texttospeech.types.SynthesisInput(text=text)
    voice = current_app.config['VOICE']
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)
    response = client.synthsize_speech(input, voice, audio_config)

    return response.audiocontent

def choose_voice():
    pass
