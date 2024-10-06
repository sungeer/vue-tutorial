from pathlib import Path

basedir = Path(__file__).resolve().parent.parent

KEY = '299095cc-1330-11e5-b06a-a45e60bec08b'
AUTH_KEY_NAME = 'auth-key'

error_log_file = basedir.joinpath('logs', 'error.log')
run_log_file = basedir.joinpath('logs', 'run.log')

cert_file_path = basedir.joinpath('cert', 'hostname')

test_mode = True

mode = 'agent'

plugins_dict = {
    'board': 'bee.plugins.board.BoardPlugin',
}

asset_api = 'http://127.0.0.1:5000/api/asset'
