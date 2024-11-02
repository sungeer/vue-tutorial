import time
import hashlib
from pathlib import Path

import requests

from bee import settings, plugins
from bee.utils import tools
from bee.utils.log_util import logger


class AutoBase:

    def __init__(self):
        self.asset_api = settings.asset_api
        self.key = settings.auth_key
        self.key_name = settings.auth_key_name

    def auth_key(self):
        ha = hashlib.md5(self.key.encode('utf-8'))
        time_span = time.time()
        ha.update(bytes(f'{self.key}|{time_span}', encoding='utf-8'))
        encryption = ha.hexdigest()
        result = f'{encryption}|{time_span}'
        return {self.key_name: result}

    def get_asset(self):
        try:
            headers = {}
            headers.update(self.auth_key())
            response = requests.get(url=self.asset_api, headers=headers)
        except Exception as e:
            response = e
        return response.json()

    def post_asset(self, msg, callback=None):
        status = True
        try:
            headers = {}
            headers.update(self.auth_key())
            response = requests.post(url=self.asset_api, headers=headers, json=msg)
        except Exception as e:
            response = e
            status = False
        if callback:
            callback(status, response)

    def process(self):
        raise NotImplementedError('You must implement process method.')

    @staticmethod
    def callback(status, response):
        if not status:
            logger.log(str(response), False)
            return
        ret = tools.json_to_dict(response.text)
        if ret['code'] == 200:
            logger.log(ret['message'], True)
        else:
            logger.log(ret['message'], False)


class AutoAgent(AutoBase):

    def __init__(self):
        super().__init__()
        self.cert_file_path = settings.cert_file_path

    def load_local_cert(self):
        cert_file_path = Path(self.cert_file_path)
        if not cert_file_path.exists():
            return None
        with open(self.cert_file_path, mode='r') as f:
            data = f.read()
        if not data:
            return None
        cert = data.strip()
        return cert

    def write_local_cert(self, cert):
        cert_file_path = Path(self.cert_file_path)
        if not cert_file_path.exists():
            cert_file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.cert_file_path, mode='w') as f:
            f.write(cert)

    def process(self):
        server_info = plugins.get_server_info()
        if not server_info.status:
            return
        local_cert = self.load_local_cert()
        if local_cert:
            if local_cert == server_info.data['hostname']:
                pass
            else:
                server_info.data['hostname'] = local_cert
        else:
            self.write_local_cert(server_info.data['hostname'])
        server_json = tools.dict_to_json_ea(server_info.data)
        self.post_asset(server_json, self.callback)
