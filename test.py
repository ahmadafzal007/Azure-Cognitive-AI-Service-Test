import json
import os 
from pprint import pprint
import requests
from dotenv import load_dotenv

'''
This sample makes a call to the Computer Vision API with a URL image query to analyze an image,
and then returns user input parameter data like category, description, and color.
API: https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/587f2c6a154055056008f200
'''

# Load environment variables from .env file
load_dotenv()

# Retrieve your Computer Vision subscription key and endpoint from environment variables
subscription_key = os.getenv('COMPUTER_VISION_SUBSCRIPTION_KEY')
endpoint = os.getenv('COMPUTER_VISION_ENDPOINT') + "/vision/v2.1/analyze"

# Check if the environment variables are loaded correctly
if not subscription_key or not endpoint:
    raise ValueError("Missing environment variables for subscription key or endpoint.")

# Request headers.
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

# Request parameters. All of them are optional.
params = {
    'visualFeatures': 'Categories,Description,Color',
    'language': 'en',
}

# Any image with objects will work.
body = {'url': 'https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/objects.jpg'}

# Call the API.
try:
    response = requests.post(endpoint, headers=headers, params=params, json=body)
    response.raise_for_status()

    print("\nHeaders:\n")
    print(response.headers)

    print("\nJSON Response:\n")
    pprint(response.json())
except Exception as ex:
    print(f"An error occurred: {ex}")
