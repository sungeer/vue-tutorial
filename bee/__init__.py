import os
import sys

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)


def run():
    from bee import settings
    from bee.autos import AutoAgent

    if settings.MODE == 'agent':
        client = AutoAgent()
    else:
        raise Exception('No set mode.')
    client.process()


if __name__ == '__main__':
    run()
