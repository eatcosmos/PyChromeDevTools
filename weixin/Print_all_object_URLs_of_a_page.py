import PyChromeDevTools

# 初始化
chrome = PyChromeDevTools.ChromeInterface() # 创建对象
chrome.Network.enable()
chrome.Page.enable()

chrome.Page.navigate(url="https://github.com/marty90/PyChromeDevTools") # 访问网页
event,messages=chrome.wait_event("Page.frameStoppedLoading", timeout=60) # 等待加载完成

print(messages) # 东西非常多，都是访问这个网页发生的事情

for m in messages:
    if "method" in m and m["method"] == "Network.responseReceived": # json
        try:
            url=m["params"]["response"]["url"]
            print (url)
        except:
            pass