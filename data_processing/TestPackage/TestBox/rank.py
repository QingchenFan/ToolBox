import random


names = ["金悦宁", "王昌硕", "蔡雨洋", "何毓文", "扈原源","樊青晨","祝铭","吴依涵"]

# 随机打乱姓名列表
random.shuffle(names)


for name in names:
    print(name)