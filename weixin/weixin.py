# PyChromeDevTools
import PyChromeDevTools
import time
from bs4 import BeautifulSoup as BS
import json
# pyzotero
from pyzotero import zotero
import http.client
import re

f=open("zotero/account.txt","r")
lines=f.readlines()
print(len(lines))
library_id=lines[0].strip()
print(library_id)
library_type=lines[1].strip() # user/group
print(library_type)
api_key=lines[2].strip()
f.close()
zot = zotero.Zotero(library_id, library_type, api_key)
http.client._is_legal_header_name = re.compile(rb'[^\s][^:\r\n]*').fullmatch

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
# 获取微信tab对象
# 打印所有tab页面的url和标题
idx = 0
for tab in chrome.tabs:
  # print(tab['url'], tab['title'])
  if tab['url'] == "https://filehelper.weixin.qq.com/":
    print(tab['title'])
    break
  idx = idx + 1
chrome = PyChromeDevTools.ChromeInterface(host="127.0.0.1", port=9222, tab=idx)
li_cnt_befor, li_cnt_after = 0, 0 # 初始化全局变量

# 获取li个数
def get_li_cnt():
  dom = chrome.DOM.getDocument(depth=-1) # -1表示什么？
  html = chrome.DOM.getOuterHTML(nodeId=dom[0]['result']['root']['nodeId']) # nodeId
  html = html[0]['result']['outerHTML']
  soup = BS(html, features="html.parser")
  try:
    ultag = soup.find('ul', {'class': 'msg-list'}) # 找<ul>
    litags = ultag.find_all('li') # 找新增的<li>
    li_cnt = len(litags)
  except:
    li_cnt = 0
  # print('有 '+str(li_cnt)+' 个li...')
  return li_cnt

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
  litags = ultag.find_all('li') # 找新增的<li>
  li_cnt_befor = len(litags) # 更新 li_cnt_befor
  # print(type(litags)) # bs4.element.ResultSet
  divtag = litags[-1].find('div', {'class': 'msg-item__content'}) # 找消息，这个是肯定有的
  # 尝试找msg-appmsg
  contenttag = divtag.find('div', {'class': 'msg-appmsg'})
  if contenttag:
    article_url = contenttag.find('a', {'class' : 'msg-appmsg__content'})['href']
    article_title = contenttag.find('h4', {'class' : 'msg-appmsg__title'}).text
    article_desc = contenttag.find('p', {'class' : 'msg-appmsg__desc'}).text
    print('收到文章消息...')
    print(article_url+' '+article_title+' '+article_desc)
    # 发链接
    collection = "DJP6HPWA" # 稍后读
    item = dict()
    item['key'] = '1' # 没要求
    item['version'] = 1
    item["data"] = dict()
    item["data"]["title"] = article_title
    item["data"]["url"] = article_url
    item["data"]["itemType"] = "webpage"
    item["data"]["collections"] = [collection]
    zot.create_items([item])
  else:
    # 尝试找msg-text
    contenttag = divtag.find('div', {'class': 'msg-text'})
    if contenttag:
      print('收到文本消息...')
      # msg_text = ''.join(contenttag.find('br').next_siblings)
      msg_text = ' '.join([str(n) for n in contenttag.contents]) # bs4.element.Tag
      print(msg_text)
      # 发笔记
      collection = "M3U87BG5" # 卡片笔记
      item = dict()
      item['key'] = '1' # 没要求
      item['version'] = 1
      item["data"] = dict()
      item["data"]["note"] = msg_text
      item["data"]["itemType"] = "note"
      item["data"]["collections"] = [collection]
      zot.create_items([item])
    else:
      # 尝试找msg-image
      contenttag = divtag.find('div', {'class': 'msg-image'})
      if contenttag:
        image_url = contenttag.find('img')['src']
        print('收到图片消息...')
        print(image_url)
      else:
        # 尝试找msg-file
        contenttag = divtag.find('div', {'class': 'msg-file__content'})
        if contenttag:
          file_title = contenttag.find('p', {'class' : 'msg-file__title'}).text
          file_desc = contenttag.find('p', {'class' : 'msg-file__desc'}).text
          print('收到文件消息...')
          print(file_title+' '+file_desc)
  # """
  # 发送数据，比如发送给zotero接口  

def test_PyChromeDevTools():
    chrome = PyChromeDevTools.ChromeInterface(host="127.0.0.1", port=9222)
    # 获取微信tab对象
    # 打印所有tab页面的url和标题
    idx = 0
    for tab in chrome.tabs:
      # print(tab['url'], tab['title'])
      if tab['url'] == "https://filehelper.weixin.qq.com/":
        print(tab['title'])
        break
      idx = idx + 1
    chrome = PyChromeDevTools.ChromeInterface(host="127.0.0.1", port=9222, tab=idx)
    li_cnt_befor, li_cnt_after = 0, 0 # 初始化全局变量

    # 启用域/Domains
    chrome.Network.enable()
    chrome.Page.enable()
    chrome.Debugger.enable()
    chrome.Dom.enable()
    chrome.DOMDebugger.enable()

    dom = chrome.DOM.getDocument(depth=-1) # -1表示什么？
    chrome.DOMDebugger.setDOMBreakpoint(nodeId=4, type="subtree-modified")
    # chrome.DOMDebugger.setEventListenerBreakpoint(eventName="subtree-modified", targetName="*")

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

    # 处理遗留阻塞信息...
    li_cnt_befor = get_li_cnt()
    chrome.Debugger.resume() # 相当于鼠标点击继续运行
    li_cnt_after = get_li_cnt()
    if li_cnt_after > li_cnt_befor:
      li_cnt_befor = li_cnt_after # 更新 li_cnt_befor
      print('处理遗留阻塞信息...')
      try:
        deal_msg()
      except:
        pass

    
    print('循环等待事件...')
    li_cnt_befor
    while 1:
      matching_event, all_events = chrome.wait_event("Debugger.paused", timeout=1) # 等待事件，立即返回
      if matching_event is None:
        # 处理遗留阻塞信息...
        # li_cnt_befor = get_li_cnt()
        chrome.Debugger.resume() # 相当于鼠标点击继续运行
        try:
          li_cnt_after = get_li_cnt()
        except:
          # 说明网页出现问题了，重启weixin.py
          print('微信文件传输助手网页版正在重启...')
          main()
        if li_cnt_after > li_cnt_befor:
          li_cnt_befor = li_cnt_after
          print('处理遗留阻塞信息...')
          try:
            deal_msg()
          except:
            pass
        continue
      
      # print('触发DOM 断点...') # 说明 li 肯定增加了
      chrome.Debugger.resume() # Resume script execution 相当于鼠标点击继续运行
      # 处理数据
      try:
        li_cnt_after = get_li_cnt()
      except:
        # 说明网页出现问题了，重启weixin.py
        print('微信文件传输助手网页版正在重启...')
        main()
      if li_cnt_after > li_cnt_befor:
        li_cnt_befor = li_cnt_after
        print('处理遗留阻塞信息...')
        try:
          deal_msg()
        except:
          pass
      
      """
      li_cnt_befor = get_li_cnt()
      chrome.Debugger.resume() # 相当于鼠标点击继续运行
      li_cnt_after = get_li_cnt()
      if li_cnt_after > li_cnt_befor: # 说明有新信息
        deal_msg()
      time.sleep(2)
      """
def main():      
  test_PyChromeDevTools()

if __name__ == "__main__":
  main()