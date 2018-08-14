from google.cloud import translate
from flask import current_app
import html.parser as htmlparser
import six

def translate_text(text):
  '''Takes in input text and converts it to the selected language'''
  translate_client = translate.Client() 
  language = current_app.config['LANGUAGE']
  parser = htmlparser.HTMLParser()

  if isinstance(text, six.binary_type):
    text = text.decode('utf-8')

  result = translate_client.translate(text, target_language=language)
 
  return parser.unescape(result['translatedText'])

def translate_list(list):
  '''Takes in list text and converts it to the selected language'''
  list = [translate_text(item) for item in list]
  return list
