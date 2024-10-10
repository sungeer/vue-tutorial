from pathlib import Path

from loguru import logger as logging

from bee import settings


class Logger:

    def __init__(self):
        self.setup_log_file(settings.run_log_file, 'INFO', lambda record: record['level'].no < 40)
        self.setup_log_file(settings.error_log_file, 'ERROR')

    @staticmethod
    def setup_log_file(file_path, level, filter_func=None):
        log_file = Path(file_path)
        log_file.parent.mkdir(parents=True, exist_ok=True)

        logging.remove()

        logging.add(
            log_file,
            rotation='10MB',
            format='{time:YYYY-MM-DD HH:mm:ss} - {level} - {message}',
            encoding='utf-8',
            enqueue=True,
            level=level,
            diagnose=False,
            backtrace=False,
            colorize=False,
            filter=filter_func
        )

    @staticmethod
    def log(message, mode=True):
        if mode:
            logging.info(message)
        else:
            logging.error(message)


logger = Logger()
