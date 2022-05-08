import PyChromeDevTools
import time

chrome = PyChromeDevTools.ChromeInterface()
chrome.Network.enable()
chrome.Page.enable()

start_time=time.time()
chrome.Page.navigate(url="http://www.baidu.com/")
chrome.wait_event("Page.loadEventFired", timeout=60)
end_time=time.time()

print ("Page Loading Time:", end_time-start_time)