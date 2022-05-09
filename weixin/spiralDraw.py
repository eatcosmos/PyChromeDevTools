from turtle import distance
import pyautogui, time

time.sleep(5)
pyautogui.click() # spiralDraw.py将控制鼠标，单击画图程序获得焦点

distance = 300
change = 20

while distance > 0:
  pyautogui.drag(distance, 0, duration=0.2)
  distance = distance - change
  pyautogui.drag(0, distance, duration=0.2)
  pyautogui.drag(-distance, 0, duration=0.2)
  distance = distance - change
  pyautogui.drag(0, -distance, duration=0.2)

b = pyautogui.locateOnScreen('icon__download.png')
b
# 激活微信窗口

# 点击下载图标
pyautogui.click(b[0], b[1], button='left')