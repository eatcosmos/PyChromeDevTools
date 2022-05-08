import PyChromeDevTools
# chrome = PyChromeDevTools.ChromeInterface()
# chrome = PyChromeDevTools.ChromeInterface(host="1.1.1.1",port=1234)
chrome = PyChromeDevTools.ChromeInterface(host="127.0.0.1", port=9222)

# 启用域/Domains
chrome.Network.enable()
chrome.Page.enable()

# return_value, messages = chrome.Page.navigate(url="http://example.com/")
# print(return_value)
# print(messages)

# message=chrome.wait_message()
# matching_event,all_events=chrome.wait_event(event_name)

# messages=chrome.pop_messages()
# print(messages)

result, messages = chrome.Page.getResourceTree()
print(result)
# chrome.Page.getResourceContent()
