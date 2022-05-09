[在线JSON校验格式化工具（Be JSON）](https://www.bejson.com/)

git clone https://github.com/marty90/PyChromeDevTools.git
git clone https://github.com/eatcosmos/PyChromeDevTools.git

# 安装用到的现成的软件功能
pip3 isntall PyChromeDevTools
pip3 install Beautifulsoup4
pip3 install pyautogui
pip3 install Pillow

# 图形用户界面自动化

# pyautogui
import  pyautogui
wh  =  pyautogui.size()
for i in range(10):
  # Move mouse in a square     
  pyautogui.moveTo(100, 100, duration=0.25)
  pyautogui.moveTo(200, 100, duration=0.25)
  pyautogui.moveTo(200, 200, duration=0.25)
  pyautogui.moveTo(100, 200, duration=0.25)
for i in range(10)
  pyautogui.move(100, 0, duration=0.25)     # right
  pyautogui.move(0, 100, duration=0.25)     # down
  pyautogui.move(-100, 0, duration=0.25)    # left
  pyautogui.move(0, -100, duration=0.25)    # up
pyautogui.position()
pyautogui.click(10, 5, button='right') # Move mouse to (10, 5) and click.
pyautogui.mouseDown()
pyautogui.mouseUp()
pyautogui.rightClick()
pyautogui.middleClick()

pyautogui.doubleClick()

pyautogui.mouseInfo()