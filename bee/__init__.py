import sys
from pathlib import Path

basedir = Path(__file__).resolve().parent.parent
sys.path.append(str(basedir))


def run():
    from bee import settings
    from bee.autos import AutoAgent

    if settings.mode == 'agent':
        client = AutoAgent()
    else:
        raise Exception('No set mode.')
    client.process()


if __name__ == '__main__':
    run()
