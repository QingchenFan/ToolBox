from random import random

from psychopy import visual, core, event

# 创建一个窗口
win = visual.Window([800, 600], color="white")

# 创建一个文本提示
instruction_text = visual.TextStim(win, text="Find the target item and press the spacebar to continue.")

# 创建一个列表，包含目标项和干扰项
target_list = ['A', 'B', 'C', 'D', 'E']
distractor_list = ['F', 'G', 'H', 'I', 'J']
stimuli_list = target_list + distractor_list

# 将列表中的项随机排列
random.shuffle(stimuli_list)

# 创建一个文本刺激
stimulus_text = visual.TextStim(win)

# 显示每个刺激并记录参与者的反应时间
for stimulus in stimuli_list:
    # 在屏幕上显示刺激
    stimulus_text.setText(stimulus)
    stimulus_text.draw()
    win.flip()
    # 等待参与者按下空格键
    event.waitKeys(keyList=['space'])
    # 记录参与者的反应时间
    start_time = core.getTime()
    event.clearEvents()
    event.waitKeys(keyList=['space'])
    end_time = core.getTime()
    reaction_time = end_time - start_time
    # 在屏幕上显示反应时间
    reaction_time_text = visual.TextStim(win, text="Reaction time: %.3f seconds" % reaction_time)
    reaction_time_text.draw()
    win.flip()

# 输出实验结果
instruction_text.setText("Experiment finished!")
instruction_text.draw()
win.flip()
core.wait(2)
win.close()