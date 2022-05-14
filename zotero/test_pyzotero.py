from pyzotero import zotero
import http.client
import re

f=open("account.txt","r")
lines=f.readlines()
print(len(lines))
library_id=lines[0].strip()
print(library_id)
library_type=lines[1].strip() # user/group
print(library_type)
api_key=lines[2].strip()
f.close()
zot = zotero.Zotero(library_id, library_type, api_key)

# http.client._is_legal_header_name = re.compile(r':|\A[^:\s][^:\r\n]*\Z').match
http.client._is_legal_header_name = re.compile(rb'[^\s][^:\r\n]*').fullmatch

# items = zot.top(limit=5)
# # we've retrieved the latest five top-level items in our library
# # we can print each item's item type and ID
# for item in items:
#     print('Item: %s | Key: %s' % (item['data']['itemType'], item['data']['key']))


c = zot.collections()
print(c[0])

# 发链接
collection = "DJP6HPWA"
# template = zot.item_template('book')
template = dict()
template['key'] = '1' # 没要求
template['version'] = 1
template["data"] = dict()
# template['data']["key"] = '19a4f01ad623aa7214f82347e3711f56'
# template['data']["version"] = 1
template["data"]["title"] = "333222111测试睡眠调控动力学机制研究 | 周日直播·神经动力学读书会直播"
template["data"]["url"] = 'http://mp.weixin.qq.com/s?__biz=MzIzMjQyNzQ5MA==&mid=2247616618&idx=3&sn=677bff75c6140b1513f1a2e4eca3c24a&chksm=e89652e7dfe1dbf184560de493a0477a352a146872c70626aca7356f34372ccc7ac7c8e04ea4#rd'
template["data"]["itemType"] = "webpage"
# template["data"]["title"] = "webpage"
template["data"]["collections"] = [collection]
# template["data"]["tags"][0]["tag"] = ["微信"]
# template["data"]["tag"] = ["微信"]
# template['creators'][0]['firstName'] = '集智俱乐部'
# template['creators'][0]['lastName'] = 'Cantsin'
# zot.addto_collection("DJP6HPWA", template)
zot.create_items([template])

# 发笔记
collection = "M3U87BG5"
# template = zot.item_template('book')
template = dict()
template['key'] = '1' # 没要求
template['version'] = 1
template["data"] = dict()
# template['data']["key"] = '19a4f01ad623aa7214f82347e3711f56'
# template['data']["version"] = 1
# template["data"]["title"] = "笔记333222111测试睡眠调控动力学机制研究 | 周日直播·神经动力学读书会直播"
template["data"]["note"] = "<p>abstractNote</p> <p>换行</p>"
template["data"]["note"] = "测试一下 <br/> <br/> 测试一下 <br/> <br/> <br/> 测试一下 <br/> <br/> <br/> <br/> <br/> 测试一下"
template["data"]["itemType"] = "note"
# template["data"]["title"] = "webpage"
template["data"]["collections"] = [collection]
# template["data"]["tags"] = ["微信"]
# template['creators'][0]['firstName'] = '集智俱乐部'
# template['creators'][0]['lastName'] = 'Cantsin'
# zot.addto_collection("DJP6HPWA", template)
zot.create_items([template])



itemID = "S6GI55DA"
# itemField = zot.item(itemID)
# print(itemField)
