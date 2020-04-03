import requests
import json
import logging
import csv
import sys

if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO

from polysdk.models.maskeddata import MaskedData
from polysdk.models.unmaskeddata import UnmaskedData


class PolyClient:
    __base_url = "https://v1.polymerapp.io:4560"
    __mask_api_url = __base_url + "/v1/pub/mask"
    __unmask_api_url = __base_url + "/v1/pub/unmask"

    __api_token = ""
    __api_headers = {
        'Content-Type': 'application/json',
        'Public-Token': ''
    }

    @staticmethod
    def __validate_args(data, key):
        return data is not '' and key is not ''

    def __init__(self, api_token):
        if api_token is '' or len(api_token) != 32:
            exception_msg = "api_token is empty or invalid."
            logging.exception(exception_msg)
            raise Exception(exception_msg)

        self.__api_token = api_token
        self.__api_headers['Public-Token'] = self.__api_token

    def mask_data(self, data, key):
        if not self.__validate_args(data, key):
            raise Exception("data or key is empty.")

        payload = {
            'key': key,
            'text': data
        }

        r = requests.post(self.__mask_api_url, data=json.dumps(payload), headers=self.__api_headers)

        try:
            logging.info('Status code: ' + str(r.status_code))
            logging.info('Response body: ' + str(r.json()))
            response_body = r.json()

            data = MaskedData(text=response_body['text'])

            return data
        except Exception:
            logging.exception('Error: ' + r.text)
            raise Exception(r.text)

    def unmask_data(self, data, key):
        if not self.__validate_args(data, key):
            raise Exception("data or key is empty.")

        payload = {
            'key': key,
            'text': data
        }

        r = requests.post(self.__unmask_api_url, data=json.dumps(payload), headers=self.__api_headers)

        try:
            logging.info('Status code: ' + str(r.status_code))
            logging.info('Response body: ' + str(r.json()))
            response_body = r.json()

            data = UnmaskedData(text=response_body['text'])

            return data
        except Exception:
            logging.exception('Error: ' + r.text)
            raise Exception(r.text)