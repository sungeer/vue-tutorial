import logging
from pathlib import Path

from bee import settings


class Logger:

    def __init__(self):
        self.run_log_file = Path(settings.run_log_file)
        self.error_log_file = Path(settings.error_log_file)

        self.run_logger = self._initialize_logger(self.run_log_file, 'run_log', logging.INFO)
        self.error_logger = self._initialize_logger(self.error_log_file, 'error_log', logging.ERROR)

    @staticmethod
    def _check_path_exist(log_file):
        log_path = log_file.parent
        log_path.mkdir(parents=True, exist_ok=True)

    def _initialize_logger(self, log_file, logger_name, level):
        self._check_path_exist(log_file)
        handler = logging.FileHandler(log_file, 'a', encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
        handler.setFormatter(formatter)

        logger = logging.getLogger(logger_name)  # 获取日志记录器
        logger.setLevel(level)
        logger.addHandler(handler)
        logger.propagate = False  # 防止日志重复

        return logger

    def log(self, message, mode=True):
        if mode:
            self.run_logger.info(message)
        else:
            self.error_logger.error(message)


logger = Logger()
