#!usr/bin/python3
# coding=utf-8
#导入bs4下的美丽汤
from bs4 import BeautifulSoup
#导入se
import lxml
from selenium import webdriver
# 继承父类为unittest.TestCase
class Douyu_Spider(object):
    # 初始化方法
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.num = 0
        # 自定义的测试方法（必须以test开头）
    def Douyu(self):
        self.driver.get("https://www.douyu.com/directory/all")
        while True:
            #返回网页渲染后的源代码
            html = self.driver.page_source
            # print 112
            #利用BeautifulSoup进行处理,共分两步
            soup = BeautifulSoup(html,"lxml")
            all_node = soup.find("div", {"id": "live-list-content"})
            # print all_node
            #一页的房间列表
            room_list = all_node.find_all("h3", {"class": "ellipsis"})
            # print room_list
            #一页主播的名字
            name_list = all_node.find_all("span", {"class": "dy-name ellipsis fl"})
            #一页观众人数
            people_list = all_node.find_all("span", {"class": "dy-num fr"})
            # print people_list[1].get_text()
            #利用zip一一对应,然后遍历
            # print 11
            for room, name , people in zip(room_list, name_list, people_list):
                #获取标签里的文本值,然后去掉空白
                # print 1
                print u"房间名: " + room.get_text().strip()
                print u"主播名: " + name.get_text().strip()
                print u"观众人数: " + people.get_text().strip()
                print "\n\n"
                #主播数+1
                self.num += 1
                #在最后一页时,下一页为灰色,可以查找字符串shark-pager-disable-next,找不到则返回真值,这时候有下一页
            if html.find("shark-pager-disable-next") != -1:
                print "总共有主播人数: %d"%self.num
                break
                #模拟点击
            self.driver.find_element_by_class_name("shark-pager-next").click()

    def close(self):
        self.driver.quit()
if __name__ == "__main__":
    douyu_spider = Douyu_Spider()
    douyu_spider.Douyu()
    douyu_spider.close()