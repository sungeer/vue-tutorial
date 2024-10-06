import traceback

from bee.plugins.base import BasePlugin
from bee.utils.tools import BaseResponse


class ServerPlugin(BasePlugin):

    def os_platform(self):
        if self.test_mode:
            output = 'linux'
        else:
            output = self.exec_shell_cmd('uname')
        return output.strip()

    def os_version(self):
        if self.test_mode:
            output = 'CentOS release 6.6 (Final)\nKernel'
        else:
            output = self.exec_shell_cmd('cat /etc/issue')
        result = output.strip().split('\n')[0]
        return result

    def os_hostname(self):
        if self.test_mode:
            output = 'xyz.com'
        else:
            output = self.exec_shell_cmd('hostname')
        return output.strip()

    def linux(self):
        response = BaseResponse()
        try:
            ret = {
                'os_platform': self.os_platform(),
                'os_version': self.os_version(),
                'hostname': self.os_hostname(),
            }
            response.data = ret
        except (Exception,):
            msg = f'{self.hostname} BasicPlugin Error: {traceback.format_exc()}'
            self.logger.log(msg, False)
            response.status = False
            response.error = msg
        return response
