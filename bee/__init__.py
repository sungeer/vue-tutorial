import os
import sys

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)


def client():
    from bee import settings
    from bee.client import AutoAgent

    if settings.MODE == 'agent':
        cli = AutoAgent()
    else:
        raise Exception('No set mode.')
    cli.process()


if __name__ == '__main__':
    client()
