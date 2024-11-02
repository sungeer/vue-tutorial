import traceback

from bee.settings import basedir
from bee.plugins.base import BasePlugin
from bee.utils.tools import BaseResponse


class BoardPlugin(BasePlugin):

    @staticmethod
    def parse(content):
        result = {}
        key_map = {
            'Manufacturer': 'manufacturer',
            'Product Name': 'model',
            'Serial Number': 'sn',
        }
        for item in content.split('\n'):
            row_data = item.strip().split(':')
            if len(row_data) == 2:
                key, value = row_data
                if key in key_map:
                    result[key_map[key]] = value.strip()
        return result

    def linux(self):
        response = BaseResponse()
        try:
            if self.test_mode:
                file_path = basedir.joinpath('files', 'board.out')
                with open(file_path, 'r') as file:
                    output = file.read()
            else:
                shell_command = 'sudo dmidecode -t1'
                output = self.exec_shell_cmd(shell_command)
            response.data = self.parse(output)
        except (Exception,):
            msg = f'{self.hostname} BoardPlugin Error: {traceback.format_exc()}'
            self.logger.log(msg, False)
            response.status = False
            response.error = msg
        return response
