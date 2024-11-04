# 彩票双色球号码随机生成（红色球号码区由1-33号码中的6个号码组成，蓝色球号码区由1-16号码中的1个号码组成）。
import random

# 定义双色球的两种颜色球和红球的范围
red_range = range(1, 34)

# 生成七个随机的红球号码和一个蓝球号码
red_ball = random.sample(red_range, 6)
blue_ball = random.randint(1, 16)

# 输出中奖号码
print(f'双色球中奖号码为：\n红球：{red_ball}\n蓝球：{blue_ball}')

