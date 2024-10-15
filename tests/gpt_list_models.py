import google.generativeai as genai
import pprint


for model in genai.list_models():
    pprint.pprint(model)
