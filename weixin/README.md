# 安装软件
1. 安装chrome https://baoku.360.cn/soft/show/appid/104384025
2. 安装python https://www.python.org/downloads/
3. 安装vscode https://code.visualstudio.com/Download#
<!-- 4. 安装git https://git-scm.com/ -->

# 下载代码/软件
<!-- git clone https://github.com/marty90/PyChromeDevTools.git -->
git clone https://github.com/eatcosmos/PyChromeDevTools.git
或者直接下载 https://github.com/eatcosmos/PyChromeDevTools/archive/refs/heads/master.zip



# 配置chrome启动参数
 "https://filehelper.weixin.qq.com/" --remote-debugging-port=9222 --enable-benchmarking --enable-net-benchmarking
通过桌面快捷方式打开chrome
# 扫描登录文件传输助手网页版
https://filehelper.weixin.qq.com/
http://127.0.0.1:9222/json/new?https://filehelper.weixin.qq.com 新开Tab打开指定地址
http://127.0.0.1:9222/json 查看已经打开的Tab列表
http://127.0.0.1:9222/json/activate/3180EF356AB532ED6425DC232E489E1A 切换到目标Tab
ul.msg-list

# 配置vscode
1. 安装python扩展
2. 为python扩展选择之前安装的python程序

# 安装用到的现成的python软件包
pip3 install PyChromeDevTools
pip3 install Beautifulsoup4
<!-- pip3 install pyautogui -->
<!-- pip3 install Pillow -->
# 通过vscode运行weixin.py
终端就会打印消息了


# 链接
- [在线JSON校验格式化工具（Be JSON）](https://www.bejson.com/)
- 
# 图形用户界面自动化，用不到
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