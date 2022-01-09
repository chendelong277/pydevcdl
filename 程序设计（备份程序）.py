import os
import time
# 1.需要备份的文件被指定在一个路径中
source = ['/Users/chendelong/Desktop/pydevcdl/test4backup']
# 2.备份文件必须存储在一个路径中
target_dir = '/Users/chendelong/Desktop/pydevcdl/target4backup'

# 3.备份文件将被打包成zip文件
# 4.zip压缩文件的文件名由当前日期与时间构成
target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'
# 如果目标路径还不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
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

#编写程序时推荐的一种方式是遵循我们在编写备份脚本时所经历的步骤：
# 进行分析与设计；
# 开始实现一个简单版本；
# 测试并修复错误；
# 开始使用以确保工作状况皆如期望那般。
# 现在， 你可以添加任何你所希望拥有的功能，
# 并继续去重复这一“开始做—测试—使用”循环，
# 需要做 多少次就去做多少次。