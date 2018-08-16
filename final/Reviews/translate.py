from google.cloud import translate
from flask import current_app
import html.parser as htmlparser
import six

def translate_text(text, lang):
  """ 
  Takes in input text and utilizes Google's Translate API to convert 
  it to the selected language. 
  """
  translate_client = translate.Client() 
  language = lang

  if isinstance(text, six.binary_type):
    text = text.decode('utf-8')

  # Initialize parser to convert special characters back to their original form after 
  # Google translation API has finished translating the text.
  parser = htmlparser.HTMLParser()
  result = translate_client.translate(text, target_language=language)

  return parser.unescape(result['translatedText'])

def translate_list(list, language):
  """ 
  Takes in a list of text and iterates through it to convert the list to the 
  selected language with Google's Translate API in the translate_text function. 
  """
  list = [translate_text(item, language) for item in list]
  return list
