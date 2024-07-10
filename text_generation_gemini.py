!pip install -U -q google-generativeai
# import necessary modules.
import google.generativeai as genai
import json
import base64
import pathlib
import pprint
import requests
import mimetypes
from IPython.display import Markdown
# setting API key
from kaggle_secrets import UserSecretsClient

def define_model():

    GOOGLE_API_KEY = UserSecretsClient().get_secret("GOOGLE_API_KEY")

    # Configure the client library by providing your API key.
    genai.configure(api_key=GOOGLE_API_KEY)

    model = 'gemini-1.0-pro' # @param {isTemplate: true}
    contents_b64 = 'W3sicm9sZSI6InVzZXIiLCJwYXJ0cyI6ImdldCBtZSBhIG1vdGl2YXRpb25hbCBxdW90ZSJ9LHsicm9sZSI6Im1vZGVsIiwicGFydHMiOiJcIlRoZSBvbmx5IHBlcnNvbiB5b3UgYXJlIGRlc3RpbmVkIHRvIGJlY29tZSBpcyB0aGUgcGVyc29uIHlvdSBkZWNpZGUgdG8gYmUuXCIgLSBSYWxwaCBXYWxkbyBFbWVyc29uIn1d' # @param {isTemplate: true}
    generation_config_b64 = 'eyJ0ZW1wZXJhdHVyZSI6MC41LCJ0b3BfcCI6MSwidG9wX2siOjEsIm1heF9vdXRwdXRfdG9rZW5zIjoyMDQ4LCJzdG9wX3NlcXVlbmNlcyI6W119' # @param {isTemplate: true}
    safety_settings_b64 = 'W3siY2F0ZWdvcnkiOiJIQVJNX0NBVEVHT1JZX0hBUkFTU01FTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfSEFURV9TUEVFQ0giLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfU0VYVUFMTFlfRVhQTElDSVQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfREFOR0VST1VTX0NPTlRFTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn1d' # @param {isTemplate: true}
    user_input_b64 = '' # @param {isTemplate: true}

    contents = json.loads(base64.b64decode(contents_b64))
    generation_config = json.loads(base64.b64decode(generation_config_b64))
    safety_settings = json.loads(base64.b64decode(safety_settings_b64))
    user_input = base64.b64decode(user_input_b64).decode()
    stream = False

    generation_config['temperature'] = 0.8
    
    return (model, contents)


def generate(user_input, model, contents, stream=False):

    # Call the model and print the response.
    gemini = genai.GenerativeModel(model_name=model)

    chat = gemini.start_chat(history=contents)

    response = chat.send_message(
        user_input,
        stream=stream)

    display(Markdown(response.text))


# define model first
dialogue_engine, contents = define_model()

# define the prompt (the context) to generate the text
user_input = "Students are having problems in understanding the concepts in the lecture, assume yoursefl as a friend talking directly to the studetna and give some adivse in very short sentence, not in bullet point form only in onse sentence"

# generating the text for 10 iterations
for i in range(10):
    print ("I have a useful suggestion to you!\n")
    generate(user_input, dialogue_engine, contents)


