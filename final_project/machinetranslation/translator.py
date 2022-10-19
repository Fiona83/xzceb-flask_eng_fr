"""
This module provides a translation service using IBM Watson API
"""
import os
#import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    """
    translate English text into French
    param: English text
    return: French textt
    """
    output = language_translator.translate(
        english_text, model_id='en-fr').get_result()
    return output['translations'][0]['translation']


def french_to_english(french_text):
    """
    translate French text into English
    param: French text
    return: English textt
    """
    output = language_translator.translate(
        french_text, model_id='fr-en').get_result()
    return output['translations'][0]['translation']
