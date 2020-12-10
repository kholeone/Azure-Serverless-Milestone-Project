import logging
import requests
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    letterstring = requests.get('http://localhost:7071/api/service-two').text

    nostring = requests.get('http://localhost:7071/api/service-three').text

    username = ""
    for i in range(5):
        username += letterstring[i]
        username += nostring[i]


