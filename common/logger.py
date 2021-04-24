import logging
import os

log_path = os.path.join('/Users/baiwenkai/PycharmProjects/mihuiTestProject/mihuiapi_test_unittest'
                        '/mihui_test_unittest_porject/logging/' + 'log.log')
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler(log_path)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
