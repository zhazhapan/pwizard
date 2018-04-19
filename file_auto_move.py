import json
import os
import shutil
from datetime import datetime

# 加载配置文件
config = json.load(open('file_movable_config.json', 'r'))

# 目标文件夹
path = config['destinationDir']

if config['enableFormat']:
    path = path + os.sep + datetime.now().strftime(config['newFolderFormat'])

# 检测目标文件夹是否存在，不存在则创建
if not os.path.exists(path):
    os.makedirs(path)

# 列出源文件夹下所有文件，对符合规则的文件进行移动
files = [f for f in os.listdir(config['sourceDir'])]
for file in files:
    if config['fileFilter'] in file:
        shutil.move(config['sourceDir'] + os.sep + file, path)

print('move done.')
