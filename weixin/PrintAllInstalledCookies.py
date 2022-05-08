import PyChromeDevTools
import time

chrome = PyChromeDevTools.ChromeInterface()
chrome.Network.enable()
chrome.Page.enable()

chrome.Page.navigate(url="http://www.baidu.com/")
chrome.wait_event("Page.frameStoppedLoading", timeout=60) # 等待加载完成，其实0.2s就加载完成了

#Wait last objects to load
time.sleep(5)

cookies,messages = chrome.Network.getCookies() # 这个cookies可以理解为一个等级表，比如你去借书，图书馆就有你的信息，然后这个cookies是一个json格式的数据
for cookie in cookies["result"]["cookies"]:
    print ("Cookie:")
    print ("\tDomain:", cookie["domain"])
    print ("\tKey:", cookie["name"])
    print ("\tValue:", cookie["value"])
    print ("\n")