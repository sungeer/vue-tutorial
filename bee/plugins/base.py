import subprocess

from bee import settings
from bee.utils.logs import logger


class BasePlugin:

    def __init__(self, hostname=''):
        self.logger = logger
        self.test_mode = settings.test_mode
        self.mode_list = ['agent']
        self.mode = getattr(settings, 'MODE', 'agent')
        self.hostname = hostname

    @staticmethod
    def agent(cmd):
        output = subprocess.getoutput(cmd)
        return output

    def exec_shell_cmd(self, cmd):
        if self.mode not in self.mode_list:
            raise ValueError(f'Invalid mode: {self.mode}.')
        func = getattr(self, self.mode)
        output = func(cmd)
        return output

    def execute(self):
        return self.linux()

    def linux(self):
        raise NotImplementedError('You must implement the linux method.')
