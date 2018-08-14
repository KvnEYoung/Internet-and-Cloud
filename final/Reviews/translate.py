from google.cloud import translate
from flask import current_app
import six

def translate_text(text):
  translate_client = translate.Client()
  language = current_app.config['LANGUAGE']

  if isinstance(text, six.binary_type):
    text = text.decode('utf-8')

  result = translate_client.translate(text, target_language=language)
  return result['translatedText']

def translate_list(list):

	list = [translate_text(item) for item in list]
	return list
