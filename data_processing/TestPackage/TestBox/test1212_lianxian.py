import pygame
import random

# 初始化 Pygame
pygame.init()

# 定义窗口尺寸和颜色
window_size = (600, 600)
background_color = (255, 255, 255)

# 定义数字的参数
num_count = 5  # 数字数量

# 随机生成数字顺序
numbers = [str(i) for i in range(1, num_count + 1)]
random.shuffle(numbers)

# 创建窗口
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("数字连线游戏")

# 记录用户选择的数字顺序
selected_numbers = []

# 记录数字的位置
number_positions = []

# 生成数字的位置
def generate_number_positions():
    positions = []
    while len(positions) < num_count:
        x = random.randint(50, window_size[0] - 50)
        y = random.randint(50, window_size[1] - 50)
        new_position = (x, y)
        # 检查新的位置是否与已有位置重叠
        overlap = False
        for position in positions:
            if abs(position[0] - new_position[0]) <= 30 and abs(position[1] - new_position[1]) <= 30:
                overlap = True
                break
        if not overlap:
            positions.append(new_position)
    return positions

number_positions = generate_number_positions()

# 游戏主循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 获取鼠标点击位置
            mouse_pos = pygame.mouse.get_pos()
            if event.button == 1:  # 鼠标左键按下
                for i, position in enumerate(number_positions):
                    if abs(position[0] - mouse_pos[0]) <= 15 and abs(position[1] - mouse_pos[1]) <= 15:
                        number = numbers[i]
                        # 将鼠标点击的数字添加到选择列表中
                        selected_numbers.append(number)
                        # 重新生成数字位置，以实现数字重新排列
                        number_positions = generate_number_positions()
                        break
            elif event.button == 3:  # 鼠标右键按下
                if selected_numbers:
                    selected_numbers.pop()  # 取消上一步选择的数字

    # 绘制背景
    window.fill(background_color)

    # 绘制数字
    for i, position in enumerate(number_positions):
        rect = pygame.Rect(position[0] - 15, position[1] - 15, 30, 30)
        if numbers[i] in selected_numbers:
            pygame.draw.rect(window, (0, 255, 0), rect)  # 绘制被点击数字的绿色方块
        else:
            pygame.draw.rect(window, (0, 0, 0), rect, 1)  # 绘制数字的黑色边框
        font = pygame.font.Font(None, 24)
        text = font.render(numbers[i], True, (0, 0, 0))
        text_rect = text.get_rect(center=position)
        window.blit(text, text_rect)

    # 检查连线顺序
    if len(selected_numbers) == num_count:
        if selected_numbers == sorted(numbers):
            message = "Right"
        else:
            message = "Wrong"
        font = pygame.font.SysFont("宋体", 48)
        font = pygame.font.Font(None, 48)
        text = font.render(message, True, (255, 0, 0))
        text_rect = text.get_rect(center=(window_size[0] // 2, window_size[1] - 50))
        window.blit(text, text_rect)

    # 更新窗口显示
    pygame.display.flip()

# 退出游戏
pygame.quit()