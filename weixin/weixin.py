import PyChromeDevTools
import time
from bs4 import BeautifulSoup as BS
import json
# chrome = PyChromeDevTools.ChromeInterface()
# chrome = PyChromeDevTools.ChromeInterface(host="1.1.1.1",port=1234)
# return_value, messages = chrome.Page.navigate(url="http://example.com/")
# print(return_value)
# print(messages)
# message=chrome.wait_message()
# matching_event,all_events=chrome.wait_event(event_name)
# messages=chrome.pop_messages()
# print(messages)

chrome = PyChromeDevTools.ChromeInterface(host="127.0.0.1", port=9222)

# 处理数据
def deal_msg():
  # time.sleep(10) # 模拟耗时
  # 获取数据 链接、文本、图片
  # html = chrome.DOM.getOuterHTML(nodeId=3,backendNodeId=117) # 错误
  # html_json = chrome.DOM.getDocument(depth=-1)
  dom = chrome.DOM.getDocument(depth=-1) # -1表示什么？
  # print(dom[0]['result']['root']['nodeId']) # 1
  # print(dom[0]['result']['root']['backendNodeId']) # 115
  html = chrome.DOM.getOuterHTML(nodeId=dom[0]['result']['root']['nodeId']) # nodeId
  # print(type(html)) # tuple
  # print(type(html[0])) # dict
  html = html[0]['result']['outerHTML']
  # print(html) # 过长

  # dictObj = json.loads(jsObj)
  # jsObj = json.dumps(dictObj)
  # with open("tmp","w") as f:
  #   json.dump(html,f)

  # 把html写入文件
  # with open("tmp","w") as f:
    # f.write(html)
    # f.close()

  # """
  soup = BS(html, features="html.parser")
  ultag = soup.find('ul', {'class': 'msg-list'}) # 找<ul>
  litag = ultag.find_all('li')[-1] # 找新增的<li>
  # print(type(litags)) # bs4.element.ResultSet
  divtag = litag.find('div', {'class': 'msg-item__content'}) # 找消息，这个是肯定有的
  # 尝试找msg-appmsg
  contenttag = divtag.find('div', {'class': 'msg-appmsg'})
  if contenttag:
    article_url = contenttag.find('a', {'class' : 'msg-appmsg__content'})['href']
    article_title = contenttag.find('h4', {'class' : 'msg-appmsg__title'}).text
    article_desc = contenttag.find('p', {'class' : 'msg-appmsg__desc'}).text
    print(article_url+' '+article_title+' '+article_desc)
  else:
    # 尝试找msg-text
    contenttag = divtag.find('div', {'class': 'msg-text'})
    if contenttag:
      print(contenttag.text)
    else:
      # 尝试找msg-image
      contenttag = divtag.find('div', {'class': 'msg-image'})
      if contenttag:
        image_url = contenttag.find('img')['src']
        print(image_url)
      else:
        # 尝试找msg-file
        contenttag = divtag.find('div', {'class': 'msg-file__content'})
        if contenttag:
          file_title = contenttag.find('p', {'class' : 'msg-file__title'}).text
          file_desc = contenttag.find('p', {'class' : 'msg-file__desc'}).text
          print(file_title+' '+file_desc)
  # """
  # 发送数据，比如发送给zotero接口  

def test_PyChromeDevTools():
    # 初始化cdp（默认连接第一个tab页面）
    # chrome = PyChromeDevTools.ChromeInterface(host="127.0.0.1", port=9222) # 通过构造函数ChromeInterface创建对象即可完成接口对象初始化

    # 启用域/Domains
    chrome.Network.enable()
    chrome.Page.enable()
    chrome.Debugger.enable()
    chrome.Dom.enable()

    # 打印所有tab页面的url和标题
    for tab in chrome.tabs:
        # print(tab['url'], tab['title']) # dict
        pass

    # """
    result, messages = chrome.Page.getFrameTree() # 默认打开鼠标所在的tab
    print(f'指令ID: {result.get("id")}') # 1
    frameTree = result.get('result').get('frameTree')
    # 顶部frame
    frame_top = frameTree.get('frame')
    # id: AA0C0A47209B476D5429D83B9C173DE0, parentId: , url: https://filehelper.weixin.qq.com/
    print('id: {}, parentId: {}, url: {}'.format(
        frame_top.get('id', ''), frame_top.get('parentId', ''), frame_top.get('url', '')
    ))

    print('处理遗留阻塞信息...')
    chrome.Debugger.resume() # 相当于鼠标点击继续运行
    deal_msg()

    print('循环等待事件...')
    while 1:
      matching_event, all_events = chrome.wait_event("Debugger.paused", timeout=60) # 等待事件，立即返回
      if matching_event is None:
        # print(matching_event)
        pass # 如果没有等到事件，就进入下一个等待
        continue
      print('收到信息...')
      # Resume script execution
      chrome.Debugger.resume() # 相当于鼠标点击继续运行
      # 处理数据
      deal_msg()

test_PyChromeDevTools()
