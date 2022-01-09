import os
import time
# 1.需要备份的文件被指定在一个路径中
source = ['/Users/chendelong/Desktop/pydevcdl/test4backup']
# 2.备份文件必须存储在一个路径中
target_dir = '/Users/chendelong/Desktop/pydevcdl/target4backup'
# 如果目标路径还不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 3.备份文件将被压缩成zip格式
# 4.将当前日期作为主备份路径下的子路径名称
today = target_dir + os.sep + time.strftime('%Y%m%d')
# 将当前时间作为zip文件的文件名
now = time.strftime('%H%M%S')
target = today + os.sep + now + '.zip'

# 如果子路径不存在则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)
    

# 5.使用 zip 命令将文件打包成 zip 格式
zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))
# 运行备份

print('zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('successful backup to ', target)
else:
    print('backup failed')