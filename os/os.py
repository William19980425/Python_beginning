import os
from os.path import isfile, join,isdir

# 目标目录
targetDir = r'd:\A-professional\files'

# 所有的文件
print([f for f in os.listdir(targetDir) if isfile(join(targetDir, f))])

# 所有的目录
print([f for f in os.listdir(targetDir) if isdir(join(targetDir, f))])