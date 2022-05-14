# 借助云服务器，收藏微信文章、文本到zotero文件夹
## 视频

## 文档
https://github.com/eatcosmos/PyChromeDevTools/blob/master/weixin/README.md

## 配置云服务器
### 购买云服务器
腾讯云
这里选择购买腾讯云的轻量应用服务器，也可以选择百度智能云，百度的价格更低而且不限制流量。
腾讯轻量应用服务器新用户购买地址：https://cloud.tencent.com/act/pro/lighthouse2021
选择 2核2G4M300G 新用户 58元/年，安装宝塔windows server2012。
百度云
https://cloud.baidu.com/campaign/202204BCCpromotion/index.html?track=46c1e408c32daf0de9066b676a74e0ba4d507901fcc72fd3#person
选择 轻量应用服务器1核2G4M不限流量 新用户 39元/每年 也安装windows server2012

建议先腾讯云的这个，省事些，因为下面的步骤是参考的腾讯轻量应用服务器，安装的宝塔windows server2012。
#### 配置云服务器
修改密码
## 远程桌面连接到云服务器
在本地电脑用远程桌面工具登录，windows电脑就搜 mstsc
用ip/域名 用户名 密码 登录
选择一个合适的分辨率 1440*900
### 下载、安装、配置软件
### 配置google chrome
下载google chrome http://baoku.360.cn/soft/show/appid/104384025
注意点右下角的那个安全下载，不要点中间的安全下载，否则会下载360.
#### 配置chrome启动参数
桌面Google Chrome快捷方式，右键选择属性，在目标一栏，最后空一格，输入下面的参数：
 --remote-debugging-port=9222 --enable-benchmarking --enable-net-benchmarking
关闭浏览器，然后通过桌面的那个快捷方式启动浏览器。
#### 登录微信文件传输助手网页版
https://filehelper.weixin.qq.com/
扫描登录
#### 设置网页变动断点
微信文件传输助手网页版的网页上面，右键，选择弹出菜单最下面的 检查，打开网页调试工具窗口
在文件传输助手页面随便发送一个消息给 文件传输助手，便于网页生成消息结构
在调试工具Elements窗口搜 "msg-list"，然后选中 <ul>标签右键，选择里面的的Break On里面的Subtree Modification，意思就是有消息的的话，网页就会暂停。
### 配置git
用于下载代码
下载git https://github.com/git-for-windows/git/releases/download/v2.36.1.windows.1/Git-2.36.1-64-bit.exe，下载太慢还是从360下载吧 http://baoku.360.cn/soft/show/appid/104716994，注意点击右下角的那个安全下载。
#### 下载代码
腾讯云的任务栏的powershell默认就是管理员权限，就打开那个
git clone https://github.com/eatcosmos/PyChromeDevTools.git
git clone git@github.com:eatcosmos/PyChromeDevTools.git
git clone https://gitee.com/eatcosmos/PyChromeDevTools.git
不知道为什么git clone下载不了？
https://github.com/eatcosmos/PyChromeDevTools/archive/refs/heads/master.zip
就解压到下载路径下吧 C:\Users\Administrator\Downloads\PyChromeDevTools-master
### 配置vscode
用于编辑代码

### 配置python
因为腾讯云这个的宝塔版本已经自带了一个python3.8，C:\Program Files\python，这里就不装了。
安装需要的python库，在powershell里面就可以了。
在 C:\Users\Administrator\Downloads\PyChromeDevTools-master\weixin 文件管理器的路径栏，输入cmd，就在当前路径下打开cmd了。
pip3 install PyChromeDevTools
pip3 install Beautifulsoup4
pip3 install pyzotero
pip3 install pyautogui

### 配置zotero账户信息
在C:\Users\Administrator\Downloads\PyChromeDevTools-master\zotero下建立新建一个txt文件 account_zotero.txt，里面每行对应一个参数，类似下面的：
1712345
user
r1uAMPw50SDEjTCNcaUsJ8qk
ABCDEFG3
MCDS7BG5

上面的 1712345 是你的zotero用户ID，到 https://www.zotero.org/settings/keys 搜，有一行
Your userID for use in API calls is 1234567，这里的1234567就是用户ID。
上面的 user 表示的是东西存档zotero的 我的文库，而不是群组。
上面的 r1uAMPw50SDEjTCNcaUsJ8qk 表示zotero的apikey，也是到 https://www.zotero.org/settings/keys 生成，上面有一个 Create new private key 按钮，就点击了生成下，不要泄露，泄露了重新删了生成下。
上面的 ABCDEFG3 是保存文章zotero的文件夹的ID，可以在zotero的网页版的url那里找，比如https://www.zotero.org/eatcosmos/collections/ABCDEFG3
上面的 MCDS7BG5 是保存文本/卡片的文件夹的ID，可以在zotero的网页版的url那里找，比如 https://www.zotero.org/eatcosmos/collections/M3U87BG5
保存 C:\Users\Administrator\Downloads\PyChromeDevTools-master\zotero\account_zotero.txt
### 运行程序
在文件管理器进入到 C:\Users\Administrator\Downloads\PyChromeDevTools-master\weixin 目录
然后在文件路径栏输入cmd，弹出cmd黑窗口，在这里运行python脚本
输入 python weixin.py
注意：cmd窗口不要退出，防止脚本在后台不动了。

## 退出远程桌面连接
退出远程桌面连接不要直接点击 远程桌面连接 的x号。
而是点击 C:\Users\Administrator\Downloads\PyChromeDevTools-master\weixin\tscon.bat
这个会把 远程桌面连接 赋值给默认的console对象，这样就表示这个会话一直有对象在连接。

## bug
1. zotero收到的延时长
2. 不稳定
3. 微信可能时间长了会退出登录，到时候重新登录下，然后再运行下python脚本

## 视频教程

## 代码仓库

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
--remote-debugging-port=9222 --enable-benchmarking --enable-net-benchmarking
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