import requests
import json
import logging

from polysdk.models.maskeddata import MaskedData
from polysdk.models.unmaskeddata import UnmaskedData


class PolyClient:
    __base_url = "https://v1.polymerapp.io:4560"
    __mask_api_url = __base_url + "/v1/pub/mask"
    __unmask_api_url = __base_url + "/v1/pub/unmask"
    __mask_files_api_url = __base_url + "/v1/pub/mask/files"
    __unmask_files_api_url = __base_url + "/v1/pub/unmask/files"

    __api_token = ""
    __api_headers = {
        'Content-Type': 'application/json',
        'Public-Token': ''
    }

    @staticmethod
    def __validate_args(text, key):
        return text is not '' and key is not ''

    @staticmethod
    def __validate_file_args(file_path, key):
        return file_path is not '' and key is not ''

    def __init__(self, api_token):
        if api_token is '' or len(api_token) != 32:
            exception_msg = "api_token is empty or invalid."
            logging.exception(exception_msg)
            raise Exception(exception_msg)

        self.__api_token = api_token
        self.__api_headers['Public-Token'] = self.__api_token

    def mask_text(self, text, key):
        if not self.__validate_args(text, key):
            raise Exception("text or key is empty.")

        payload = {
            'text': text,
            'key': key
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

    def unmask_text(self, text, key):
        if not self.__validate_args(text, key):
            raise Exception("text or key is empty.")

        payload = {
            'text': text,
            'key': key
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

    def mask_text_file(self, file_path, key):
        if not self.__validate_file_args(file_path, key):
            raise Exception("file_path or key is empty.")

        with open(file_path) as file:
            text = file.read()
            masked_data = self.mask_text(text=text, key=key)
            return masked_data

    def unmask_text_file(self, file_path, key):
        if not self.__validate_file_args(file_path, key):
            raise Exception("file_path or key is empty.")

        with open(file_path) as file:
            text = file.read()
            unmasked_data = self.unmask_text(text=text, key=key)
            return unmasked_data

    def mask_csv_file(self, file_path, key, selected_columns=None):
        if selected_columns is None:
            selected_columns = []
        if not self.__validate_file_args(file_path, key):
            raise Exception("file_path or key is empty.")

        api_url = self.__mask_files_api_url
        files = {
            'source': open(file_path, 'rb')
        }

        custom_headers = {
            **self.__api_headers
        }
        custom_headers.pop('Content-Type')

        custom_data = {
            'password': key,
            'selected_columns': ','.join(selected_columns) if selected_columns is not [] else ''
        }

        r = requests.post(api_url, files=files, data=custom_data, headers=custom_headers)

        try:
            logging.info('Status code: ' + str(r.status_code))
            logging.info('Response body: ' + str(r.json()))
            response_body = r.json()

            data = MaskedData(text=response_body)
            return data
        except Exception:
            logging.exception('Error: ' + r.text)
            raise Exception(r.text)

    def unmask_csv_file(self, file_path, key):
        if not self.__validate_file_args(file_path, key):
            raise Exception("file_path or key is empty.")

        api_url = self.__unmask_files_api_url
        files = {
            'source': open(file_path, 'rb')
        }

        custom_headers = {
            **self.__api_headers
        }
        custom_headers.pop('Content-Type')

        custom_data = {
            'password': key
        }

        r = requests.post(api_url, files=files, data=custom_data, headers=custom_headers)

        try:
            logging.info('Status code: ' + str(r.status_code))
            logging.info('Response body: ' + str(r.json()))
            response_body = r.json()

            data = MaskedData(text=response_body)
            return data
        except Exception:
            logging.exception('Error: ' + r.text)
            raise Exception(r.text)
