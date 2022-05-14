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
pip3 install pyzotero
<!-- pip3 install pyautogui -->
<!-- pip3 install Pillow -->
# 通过vscode运行weixin.py
终端就会打印消息了



## bug 处理远程桌面连接问题
query session # 查看回话

>\>rdp-tcp#11        Administrator             1  运行中

tscon rdp-tcp#11 /dest:console # **rdp-tcp#11**换成上面查到的，意思就是把**rdp-tcp#11**交给新会话，名字是**console**

tscon console /dest:rdp-tcp#11

## 参考资料
- [如何关闭远程桌面后仍处于可交互状态\_weixin\_30736301的博客\-CSDN博客](https://blog.csdn.net/weixin_30736301/article/details/95383609)
  - [tscon \| Microsoft Docs](https://docs.microsoft.com/zh-cn/windows-server/administration/windows-commands/tscon)
  - [Windows系统软件自动化程序不能在mstsc远程断开的时候正常运行的解决方案\_John\_Doe\.的博客\-CSDN博客](https://blog.csdn.net/sinat_34149445/article/details/115314120)
- [Python JSON \| 菜鸟教程](https://www.runoob.com/python/python-json.html)