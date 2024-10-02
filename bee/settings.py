import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

KEY = '299095cc-1330-11e5-b06a-a45e60bec08b'  # 用于API认证的KEY
AUTH_KEY_NAME = 'auth-key'  # 用于API认证的请求头

ERROR_LOG_FILE = os.path.join(BASEDIR, 'logs', 'error.log')
RUN_LOG_FILE = os.path.join(BASEDIR, 'logs', 'run.log')

CERT_FILE_PATH = os.path.join(BASEDIR, 'cert', 'hostname')  # Agent模式保存服务器唯一ID的文件

TEST_MODE = True

MODE = 'agent'

# 采集硬件数据的插件
PLUGINS_DICT = {
    'board': 'bee.plugins.board.BoardPlugin',
}

# 资产信息API
ASSET_API = 'http://127.0.0.1:8000/api/asset'

'''
POST时，返回值：{'code': xx, 'message': 'xx'}
 code:
    - 1000 成功;
    - 1001 接口授权失败;
    - 1002 数据库中资产不存在
'''
