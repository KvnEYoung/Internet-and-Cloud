from google.cloud import texttospeech
from google.cloud import storage
from flask import current_app

def read_text(text):
    '''
    Takes in input text and converts it to a base 64 encoded audio string
    '''
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('lund-young-510')
    client = texttospeech.TextToSpeechClient()
    input = texttospeech.types.SynthesisInput(text=text)
    voice = texttospeech.types.VoiceSelectionParams(language_code='en-US', ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)
    audio_config = texttospeech.types.AudioConfig(audio_encoding=texttospeech.enums.AudioEncoding.MP3)
    response = client.synthesize_speech(input, voice, audio_config)

    return str(response.audio_content)

def choose_voice():
    pass
